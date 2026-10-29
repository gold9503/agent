"""장면 구성표의 나레이션을 문장 단위로 음성 합성하고, 장면별 음성 파일과 자막 타이밍을 만든다.

엔진:
  elevenlabs  ElevenLabs (기본, 공개용). 음성 생성은 ElevenLabs 커넥터로 제작팀이 장면마다 한 번씩 하고,
          assets/audio/elevenlabs/scene_XX.mp3 로 저장해 둔다 (장면별 원고: --prompts 로 출력).
          이 스크립트는 그 파일을 읽어 문장 사이의 쉼을 찾아 자막 타이밍을 만든다.
  clova   네이버 클라우드 CLOVA Voice Premium (예비)
          환경 변수 NCP_CLOVA_CLIENT_ID, NCP_CLOVA_CLIENT_SECRET 필요
          화자는 CHOIGO_CLOVA_SPEAKER (기본 nminsang, 차분한 남성)
  mimic3  무료 오프라인 음성 (비공개 테스트용, 발음 오류율 약 30%)

출력:
  assets/audio/scene_XX.wav   장면별 나레이션
  assets/audio/timings.json   장면 길이와 문장별 시작/끝 시각(장면 기준, 초)
  assets/audio/cache/         문장별 합성 결과 캐시 (같은 문장은 다시 요청하지 않아 비용 절약)

화자 비교 샘플:  python tts.py --samples <출력 폴더>
"""
import argparse
import hashlib
import json
import os
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np
import soundfile as sf

SR = 48000
SENTENCE_GAP = 0.35   # 문장 사이 쉼(초)
SCENE_LEAD = 0.4      # 장면 시작 후 첫 문장까지
SCENE_TAIL = 0.8      # 마지막 문장 후 장면 끝까지

CLOVA_URL = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"
CLOVA_SAMPLE_SPEAKERS = ["nminsang", "njinho", "nsinu", "nkyuwon", "nwontak", "nkitae"]
MIMIC3_DIR = Path("/opt/choigo-models/vits-mimic3-ko_KO-kss_low")


class ClovaTTS:
    """CLOVA Voice Premium. speed/pitch는 −5~5 (speed는 음수일수록 빠름)."""

    def __init__(self, speaker, speed=0, pitch=0):
        self.id = os.environ.get("NCP_CLOVA_CLIENT_ID")
        self.secret = os.environ.get("NCP_CLOVA_CLIENT_SECRET")
        if not (self.id and self.secret):
            raise SystemExit("NCP_CLOVA_CLIENT_ID / NCP_CLOVA_CLIENT_SECRET 환경 변수가 없습니다. 기술지원팀 설정 필요.")
        self.speaker, self.speed, self.pitch = speaker, speed, pitch
        self.key = f"clova-{speaker}-{speed}-{pitch}"

    def mp3(self, text):
        body = urllib.parse.urlencode({"speaker": self.speaker, "text": text, "volume": 0, "speed": self.speed,
                                       "pitch": self.pitch, "format": "mp3"}).encode()
        req = urllib.request.Request(CLOVA_URL, data=body, method="POST", headers={
            "X-NCP-APIGW-API-KEY-ID": self.id, "X-NCP-APIGW-API-KEY": self.secret,
            "Content-Type": "application/x-www-form-urlencoded"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"CLOVA {e.code}: {e.read().decode(errors='replace')}") from None

    def synth(self, text, cache):
        path = cache / f"{hashlib.sha1((self.key + text).encode()).hexdigest()}.mp3"
        if not path.exists():
            path.write_bytes(self.mp3(text))
        return decode(path)


class Mimic3TTS:
    def __init__(self, speed=0.9):
        import sherpa_onnx
        self.tts = sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(
            model=sherpa_onnx.OfflineTtsModelConfig(
                vits=sherpa_onnx.OfflineTtsVitsModelConfig(
                    model=str(MIMIC3_DIR / "ko_KO-kss_low.onnx"), tokens=str(MIMIC3_DIR / "tokens.txt"),
                    data_dir=str(MIMIC3_DIR / "espeak-ng-data"),
                    noise_scale=0.333,     # 기본값(0.667)보다 낮추면 발음이 또렷해진다
                    noise_scale_w=0.5),
                num_threads=4)))
        self.speed = speed

    def synth(self, text, cache):
        a = self.tts.generate(text, sid=0, speed=self.speed)
        x = np.array(a.samples, dtype=np.float32)
        return resample(x, a.sample_rate)


class ElevenLabsFiles:
    """커넥터로 미리 만든 장면별 mp3를 읽는다. 문장 경계는 쉼(무음) 구간으로 찾는다."""

    def __init__(self, ep):
        self.dir = ep / "assets/audio/elevenlabs"

    def scene(self, sc):
        path = self.dir / f"scene_{sc['id']:02d}.mp3"
        if not path.exists():
            raise SystemExit(f"{path} 가 없습니다. ElevenLabs로 장면 {sc['id']} 나레이션을 먼저 생성하세요 (tts.py --prompts).")
        x = trim_silence(decode(path))
        return x, split_sentences(x, sc["narration"])


def split_sentences(x, narration, min_gap=0.18):
    """무음 구간 중 가장 긴 것들을 문장 경계로 쓴다. 부족하면 글자 수 비율로 나눈다."""
    n = len(narration)
    win = int(0.02 * SR)
    env = np.sqrt(np.convolve(x ** 2, np.ones(win) / win, mode="same"))
    quiet = env < max(0.01, 0.06 * np.percentile(env, 95))
    gaps, i = [], 0
    while i < len(quiet):
        if quiet[i]:
            j = i
            while j < len(quiet) and quiet[j]:
                j += 1
            if (j - i) / SR >= min_gap and i > 0 and j < len(quiet):
                gaps.append((j - i, i, j))
            i = j
        else:
            i += 1
    # 글자 수 비율로 예상한 경계에 가장 가까운 긴 쉼을 고른다
    lens = np.array([len(m["say"]) for m in narration], dtype=float)
    expected = np.cumsum(lens)[:-1] / lens.sum() * len(x)
    bounds, used = [], set()
    for e in expected:
        cands = [g for g in gaps if g[1] not in used]
        if cands:
            g = min(cands, key=lambda g: abs((g[1] + g[2]) / 2 - e) - 0.5 * g[0])
            if abs((g[1] + g[2]) / 2 - e) < 0.25 * len(x):
                used.add(g[1])
                bounds.append((g[1], g[2]))
                continue
        bounds.append((int(e), int(e)))
    bounds.sort()
    starts = [0] + [b[1] for b in bounds]
    ends = [b[0] for b in bounds] + [len(x)]
    return [(a / SR, b / SR) for a, b in zip(starts, ends)]


def decode(path):
    """mp3 → 48kHz 모노 float32."""
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                         check=True, capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def resample(x, sr):
    if sr == SR:
        return x
    t = np.arange(int(len(x) * SR / sr)) * sr / SR
    return np.interp(t, np.arange(len(x)), x).astype(np.float32)


def trim_silence(x, thresh=0.01):
    idx = np.where(np.abs(x) > thresh)[0]
    if len(idx) == 0:
        return x
    pad = int(0.05 * SR)
    return x[max(idx[0] - pad, 0): idx[-1] + pad]


def make_engine(args):
    if args.engine == "clova":
        return ClovaTTS(args.speaker, args.clova_speed, args.clova_pitch)
    return Mimic3TTS()


def samples(args):
    """여러 남성 화자로 같은 문장을 만들어 비교용 파일을 만든다."""
    out = Path(args.samples)
    out.mkdir(parents=True, exist_ok=True)
    text = "시간을 천이백 년 전으로 돌려보겠습니다. 장소는 바그다드입니다. 근의 공식은 외우는 주문이 아니라, 정사각형을 완성하는 이야기입니다."
    for spk in CLOVA_SAMPLE_SPEAKERS:
        try:
            x = ClovaTTS(spk, args.clova_speed, args.clova_pitch).synth(text, out)
            sf.write(out / f"sample_{spk}.wav", x, SR)
            print(f"ok {spk}")
        except RuntimeError as e:
            print(f"skip {spk}: {e}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode", nargs="?")
    ap.add_argument("--engine", choices=["elevenlabs", "clova", "mimic3"],
                    default=os.environ.get("CHOIGO_TTS_ENGINE", "elevenlabs"))
    ap.add_argument("--prompts", action="store_true", help="ElevenLabs에 넣을 장면별 원고를 출력하고 끝낸다")
    ap.add_argument("--speaker", default=os.environ.get("CHOIGO_CLOVA_SPEAKER", "nminsang"))
    ap.add_argument("--clova-speed", type=int, default=0)
    ap.add_argument("--clova-pitch", type=int, default=0)
    ap.add_argument("--samples", help="화자 비교 샘플을 만들 폴더")
    args = ap.parse_args()
    if args.samples:
        return samples(args)

    ep = Path(args.episode)
    sb = json.loads((ep / "03_storyboard.json").read_text(encoding="utf-8"))
    out = ep / "assets" / "audio"
    cache = out / "cache"
    cache.mkdir(parents=True, exist_ok=True)

    if args.prompts:
        prompts = {f"scene_{sc['id']:02d}": " ".join(n["say"] for n in sc["narration"]) for sc in sb["scenes"]}
        print(json.dumps(prompts, ensure_ascii=False, indent=1))
        return

    if args.engine == "elevenlabs":
        eleven = ElevenLabsFiles(ep)
        timings = []
        for sc in sb["scenes"]:
            x, spans = eleven.scene(sc)
            audio = np.concatenate([np.zeros(int(SCENE_LEAD * SR), dtype=np.float32), x,
                                    np.zeros(int(SCENE_TAIL * SR), dtype=np.float32)])
            sents = [{"start": round(SCENE_LEAD + a, 3), "end": round(SCENE_LEAD + b, 3), "text": n.get("sub", n["say"])}
                     for (a, b), n in zip(spans, sc["narration"])]
            sf.write(out / f"scene_{sc['id']:02d}.wav", audio, SR)
            timings.append({"id": sc["id"], "duration": round(len(audio) / SR, 3), "sentences": sents})
            print(f"scene {sc['id']:02d}: {len(audio) / SR:5.1f}s")
        (out / "timings.json").write_text(json.dumps(timings, ensure_ascii=False, indent=1), encoding="utf-8")
        (out / "engine.txt").write_text(f"elevenlabs {os.environ.get('CHOIGO_ELEVEN_VOICE', '')}\n")
        print(f"total: {sum(s['duration'] for s in timings):.1f}s (elevenlabs)")
        return

    tts = make_engine(args)
    timings = []
    for sc in sb["scenes"]:
        chunks, sents, t = [], [], SCENE_LEAD
        for n in sc["narration"]:
            x = trim_silence(tts.synth(n["say"], cache))
            dur = len(x) / SR
            sents.append({"start": round(t, 3), "end": round(t + dur, 3), "text": n.get("sub", n["say"])})
            chunks += [x, np.zeros(int(SENTENCE_GAP * SR), dtype=np.float32)]
            t += dur + SENTENCE_GAP
        audio = np.concatenate([np.zeros(int(SCENE_LEAD * SR), dtype=np.float32)] + chunks[:-1]
                               + [np.zeros(int(SCENE_TAIL * SR), dtype=np.float32)])
        sf.write(out / f"scene_{sc['id']:02d}.wav", audio, SR)
        timings.append({"id": sc["id"], "duration": round(len(audio) / SR, 3), "sentences": sents})
        print(f"scene {sc['id']:02d}: {len(audio) / SR:5.1f}s")

    (out / "timings.json").write_text(json.dumps(timings, ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "engine.txt").write_text(f"{args.engine} {args.speaker if args.engine == 'clova' else ''}\n")
    print(f"total: {sum(s['duration'] for s in timings):.1f}s ({args.engine})")


if __name__ == "__main__":
    main()
