"""렌더링된 장면, 나레이션, 배경음악, 자막을 합쳐 최종 영상을 만든다.

입력:  assets/render/videos/visuals/1080p30/SXX.mp4, assets/audio/scene_XX.wav, assets/audio/timings.json
출력:  output/final.mp4, output/subtitles.srt
"""
import argparse
import json
import math
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

HERE = Path(__file__).resolve().parent
SUB_MAX_LINE = 24          # 자막 한 줄 최대 글자 수
SUB_MAX_LINES = 2
BGM_GAIN_DB = -24          # 나레이션 대비 배경음악 크기
SUB_STYLE = ("FontName=Noto Sans CJK KR,FontSize=17,Bold=1,PrimaryColour=&H00F0F0F0,"
             "OutlineColour=&H00000000,BackColour=&H90000000,BorderStyle=4,Outline=1,Shadow=0,"
             "MarginV=12,Alignment=2")


def run(cmd):
    subprocess.run(cmd, check=True)


def probe_duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                         check=True, capture_output=True, text=True).stdout
    return float(out.strip())


def split_balanced(words, parts):
    """어절 목록을 글자 수가 비슷한 parts개 묶음으로 나눈다."""
    total = sum(len(w) for w in words) + len(words) - 1
    groups, cur, acc = [], [], 0
    for i, w in enumerate(words):
        cur.append(w)
        acc += len(w) + 1
        left = len(words) - i - 1
        if len(groups) < parts - 1 and left > 0 and acc >= total * (len(groups) + 1) / parts:
            groups.append(cur)
            cur = []
    groups.append(cur)
    return [g for g in groups if g]


def cues_for(sentence, offset):
    """긴 문장은 여러 자막으로 고르게 나누고, 글자 수 비율로 시간을 나눈다."""
    words = sentence["text"].split()
    n_chars = len(sentence["text"])
    n_cues = math.ceil(n_chars / (SUB_MAX_LINE * SUB_MAX_LINES))
    t = offset + sentence["start"]
    span = sentence["end"] - sentence["start"]
    cues = []
    for g in split_balanced(words, n_cues):
        text = " ".join(g)
        lines = split_balanced(g, 2) if len(text) > SUB_MAX_LINE else [g]
        d = span * len(text) / n_chars
        cues.append((t, t + d, "\n".join(" ".join(l) for l in lines)))
        t += d
    return cues


def srt_time(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode")
    args = ap.parse_args()
    ep = Path(args.episode).resolve()
    out = ep / "output"
    work = ep / "assets/build"
    out.mkdir(exist_ok=True)
    work.mkdir(parents=True, exist_ok=True)

    timings = json.loads((ep / "assets/audio/timings.json").read_text(encoding="utf-8"))

    # 1) 장면 영상 길이에 맞춰 나레이션을 이어 붙이고 자막 시각을 계산
    narration, cues, offset, sr = [], [], 0.0, None
    concat_list = []
    for sc in timings:
        name = f"S{sc['id']:02d}"
        vid = ep / f"assets/render/{name}/videos/visuals/1080p30/{name}.mp4"
        wav = ep / f"assets/audio/scene_{sc['id']:02d}.wav"
        if not vid.exists() or vid.stat().st_mtime < wav.stat().st_mtime:
            sys.exit(f"{name}: 장면 영상이 없거나 나레이션보다 오래되었습니다. render_scenes.sh를 다시 실행하세요.")
        vdur = probe_duration(vid)
        audio, sr = sf.read(wav, dtype="float32")
        n = int(round(vdur * sr))
        audio = np.pad(audio, (0, max(0, n - len(audio))))[:n]
        narration.append(audio)
        for s in sc["sentences"]:
            cues += cues_for(s, offset)
        concat_list.append(f"file '{vid}'")
        offset += vdur
    sf.write(work / "narration.wav", np.concatenate(narration), sr)
    (work / "concat.txt").write_text("\n".join(concat_list) + "\n")

    srt = out / "subtitles.srt"
    srt.write_text("".join(f"{i}\n{srt_time(a)} --> {srt_time(b)}\n{t}\n\n" for i, (a, b, t) in enumerate(cues, 1)),
                   encoding="utf-8")

    # 2) 배경음악
    run([sys.executable, str(HERE / "bgm.py"),
         str(work / "bgm.wav"), f"{offset:.2f}"])

    # 3) 영상 이어 붙이기
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(work / "concat.txt"),
         "-c", "copy", str(work / "video.mp4")])

    # 4) 소리 섞기 + 자막 입히기 + 음량 정규화(-14 LUFS)
    gain = 10 ** (BGM_GAIN_DB / 20)
    filt = (f"[2:a]volume={gain:.4f}[bgm];"
            f"[1:a]aformat=channel_layouts=stereo[nar];"
            f"[nar][bgm]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a];"
            f"[0:v]subtitles={srt}:force_style='{SUB_STYLE}'[v]")
    run(["ffmpeg", "-y", "-v", "error", "-i", str(work / "video.mp4"), "-i", str(work / "narration.wav"),
         "-i", str(work / "bgm.wav"), "-filter_complex", filt, "-map", "[v]", "-map", "[a]",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", str(out / "final.mp4")])
    print(f"final.mp4: {probe_duration(out / 'final.mp4'):.1f}s, {len(cues)} subtitle cues")


if __name__ == "__main__":
    main()
