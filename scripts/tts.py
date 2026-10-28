"""장면 구성표의 나레이션을 문장 단위로 음성 합성하고, 장면별 음성 파일과 자막 타이밍을 만든다.

출력:
  assets/audio/scene_XX.wav   장면별 나레이션
  assets/audio/timings.json   장면 길이와 문장별 시작/끝 시각(장면 기준, 초)
"""
import argparse
import json
from pathlib import Path

import numpy as np
import sherpa_onnx
import soundfile as sf

MODEL_DIR = Path("/opt/choigo-models/vits-mimic3-ko_KO-kss_low")
SENTENCE_GAP = 0.35   # 문장 사이 쉼(초)
SCENE_LEAD = 0.4      # 장면 시작 후 첫 문장까지
SCENE_TAIL = 0.8      # 마지막 문장 후 장면 끝까지


def load_tts():
    cfg = sherpa_onnx.OfflineTtsConfig(
        model=sherpa_onnx.OfflineTtsModelConfig(
            vits=sherpa_onnx.OfflineTtsVitsModelConfig(
                model=str(MODEL_DIR / "ko_KO-kss_low.onnx"),
                tokens=str(MODEL_DIR / "tokens.txt"),
                data_dir=str(MODEL_DIR / "espeak-ng-data"),
                noise_scale=0.333,     # 기본값(0.667)보다 낮추면 발음이 또렷해진다 (check_narration.py로 확인)
                noise_scale_w=0.5,
            ),
            num_threads=4,
        )
    )
    return sherpa_onnx.OfflineTts(cfg)


def trim_silence(x, sr, thresh=0.01):
    idx = np.where(np.abs(x) > thresh)[0]
    if len(idx) == 0:
        return x
    pad = int(0.05 * sr)
    return x[max(idx[0] - pad, 0): idx[-1] + pad]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode")
    ap.add_argument("--speed", type=float, default=0.9)
    args = ap.parse_args()

    ep = Path(args.episode)
    sb = json.loads((ep / "03_storyboard.json").read_text(encoding="utf-8"))
    out = ep / "assets" / "audio"
    out.mkdir(parents=True, exist_ok=True)

    tts = load_tts()
    timings = []
    for sc in sb["scenes"]:
        sr = None
        chunks, sents, t = [], [], SCENE_LEAD
        for n in sc["narration"]:
            a = tts.generate(n["say"], sid=0, speed=args.speed)
            sr = a.sample_rate
            x = trim_silence(np.array(a.samples, dtype=np.float32), sr)
            dur = len(x) / sr
            sents.append({"start": round(t, 3), "end": round(t + dur, 3), "text": n.get("sub", n["say"])})
            chunks += [x, np.zeros(int(SENTENCE_GAP * sr), dtype=np.float32)]
            t += dur + SENTENCE_GAP
        audio = np.concatenate([np.zeros(int(SCENE_LEAD * sr), dtype=np.float32)] + chunks[:-1]
                               + [np.zeros(int(SCENE_TAIL * sr), dtype=np.float32)])
        sf.write(out / f"scene_{sc['id']:02d}.wav", audio, sr)
        timings.append({"id": sc["id"], "duration": round(len(audio) / sr, 3), "sentences": sents})
        print(f"scene {sc['id']:02d}: {len(audio) / sr:5.1f}s")

    (out / "timings.json").write_text(json.dumps(timings, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"total: {sum(s['duration'] for s in timings):.1f}s")


if __name__ == "__main__":
    main()
