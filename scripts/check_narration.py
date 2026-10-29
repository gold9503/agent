"""나레이션 발음 점검: 합성된 음성을 음성 인식으로 다시 받아 적어 대본과 비교한다.

글자 오류율(CER)이 높은 문장은 TTS가 잘못 읽었을 가능성이 크므로 표기를 바꿔야 한다.
사용법: python check_narration.py <에피소드 폴더>
"""
import json
import sys
from pathlib import Path

import numpy as np
import sherpa_onnx
import soundfile as sf

ASR_DIR = Path("/opt/choigo-models/sherpa-onnx-zipformer-korean-2024-06-24")
CER_WARN = 0.25


def cer(ref, hyp):
    ref, hyp = ref.replace(" ", ""), hyp.replace(" ", "")
    d = np.arange(len(hyp) + 1)
    for i, r in enumerate(ref, 1):
        prev, d[0] = d[0], i
        for j, h in enumerate(hyp, 1):
            prev, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, prev + (r != h))
    return d[-1] / max(len(ref), 1)


def strip_punct(s):
    return "".join(c for c in s if c.isalnum() or c.isspace())


DIGITS = "영일이삼사오육칠팔구"


def read_number(n):
    """정수를 한자어 수사로 읽는다 (1694 → 천육백구십사). 인식기가 숫자로 받아 적은 것을 대본 표기와 맞추기 위함."""
    if n == 0:
        return "영"
    out = ""
    for unit, name in ((10000, "만"), (1000, "천"), (100, "백"), (10, "십"), (1, "")):
        d, n = divmod(n, unit)
        if d:
            out += ("" if d == 1 and name else DIGITS[d]) + name
    return out


def normalize_numbers(s):
    import re
    return re.sub(r"\d+", lambda m: read_number(int(m.group())), s)


def main():
    ep = Path(sys.argv[1])
    sb = json.loads((ep / "03_storyboard.json").read_text(encoding="utf-8"))
    timings = {t["id"]: t for t in json.loads((ep / "assets/audio/timings.json").read_text(encoding="utf-8"))}
    rec = sherpa_onnx.OfflineRecognizer.from_transducer(
        encoder=str(ASR_DIR / "encoder-epoch-99-avg-1.int8.onnx"),
        decoder=str(ASR_DIR / "decoder-epoch-99-avg-1.onnx"),
        joiner=str(ASR_DIR / "joiner-epoch-99-avg-1.int8.onnx"),
        tokens=str(ASR_DIR / "tokens.txt"), num_threads=4)
    rows, worst = [], []
    for sc in sb["scenes"]:
        audio, sr = sf.read(ep / f"assets/audio/scene_{sc['id']:02d}.wav", dtype="float32")
        for n, t in zip(sc["narration"], timings[sc["id"]]["sentences"]):
            seg = audio[int(t["start"] * sr): int(t["end"] * sr)]
            st = rec.create_stream()
            st.accept_waveform(sr, seg)
            rec.decode_stream(st)
            hyp = st.result.text
            e = cer(strip_punct(n["say"]), strip_punct(normalize_numbers(hyp)))
            rows.append(e)
            if e >= CER_WARN:
                worst.append((sc["id"], e, n["say"], hyp))
    print(f"문장 {len(rows)}개, 평균 CER {np.mean(rows):.3f}")
    for sid, e, ref, hyp in sorted(worst, key=lambda x: -x[1]):
        print(f"[장면 {sid:02d}] CER {e:.2f}\n  대본: {ref}\n  인식: {hyp}")


if __name__ == "__main__":
    main()
