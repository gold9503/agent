"""본편에서 장면 몇 개를 골라 세로(9:16) 숏폼과 정사각형(1:1) SNS 영상을 만든다.

본편 합성(assemble.py)이 끝난 뒤에 실행한다. 장면은 자막 없는 합성본(assets/build/scenes/SXX.mp4)을 쓰고,
화면 비율에 맞춰 자막과 제목을 새로 입힌다.
  - 위아래 빈자리는 같은 장면을 흐리게 깔아 채운다 (원본 16:9 화면과 AI 표시는 그대로 보인다)
  - 장면 사이 쉬는 시간은 줄인다 (숏폼은 호흡이 빨라야 한다)

설정: 03_storyboard.json → "shorts": {"scenes": [1, 5, ...], "headline": ["첫 줄", "둘째 줄"], "end": "마지막 안내 문구",
      "cards": [{"scene": 5, "text": "인물 이름 카드", "dur": 4}]}  (cards는 선택)
출력: output/shorts_vertical.mp4 (유튜브 숏츠, 인스타그램 릴스, 틱톡)
      output/shorts_square.mp4 (인스타그램·페이스북 피드, X)
사용법: python make_shorts.py <에피소드 폴더> [--format vertical|square|all]
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

from assemble import BGM_GAIN_DB, HERE, cues_for, probe_duration, run

SCENE_TAIL = 0.3   # 숏폼에서 장면 끝 문장 뒤에 남기는 여유(초)
END_CARD = 2.5     # 마지막 안내 문구를 띄우는 시간(초)
AI_SIZE = 36       # 숏폼 AI 표시 글자 크기(px). 법무 기준 28px 이상, 세로 화면 가독성 위해 36

# ASS 색상은 &HBBGGRR 순서
INK, GOLD, MUTED = "&H00E3EAED", "&H004CB4E8", "&H00988F8A"

LAYOUTS = {
    # 화면 크기, 원본 영상을 놓을 y, 자막 한 줄 글자 수, 글자 크기, 각 요소의 위치(위에서부터 px)
    "vertical": dict(w=1080, h=1920, video_y=560, max_line=16, sub_size=58, sub_y=1245,
                     head_size=80, head_y=200, brand_size=40, brand_y=115, end_y=1510, end_size=42,
                     ai_y=420, ai_text=r"실사 화면은 AI로 만든 영상입니다\N실제 실험·역사 촬영 아님"),
    # 세로 숏츠 전용 에피소드(assemble.py): 화면 전체가 영상, Manim 그림은 y 450~1330px 안
    "native": dict(w=1080, h=1920, video_y=0, max_line=16, sub_size=60, sub_y=1375,
                   head_size=76, head_y=150, brand_size=34, brand_y=70, end_y=1540, end_size=44,
                   ai_y=360, ai_text="AI로 만든 영상 · 실제 촬영 아님"),
    "square": dict(w=1080, h=1080, video_y=170, max_line=22, sub_size=44, sub_y=810,
                   head_size=54, head_y=48, brand_size=28, brand_y=1020, end_y=1020, end_size=30,
                   ai_y=935, ai_text="AI로 만든 영상 · 실제 실험·역사 촬영 아님"),
}


def ass_time(t):
    cs = int(round(t * 100))
    h, cs = divmod(cs, 360_000)
    m, cs = divmod(cs, 6_000)
    s, cs = divmod(cs, 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


def write_ass(path, L, cues, headline, brand, end_text, total, cards=()):
    """cards: [(시작, 끝, 문구)] 동안은 헤드라인 자리에 이름 카드 등을 대신 띄운다."""
    def style(name, size, color, bold, outline, box=False):
        border = 3 if box else 1
        back = "&H99000000" if box else "&H00000000"
        return (f"Style: {name},Noto Sans CJK KR,{size},{color},{color},&H00000000,{back},{bold},0,0,0,"
                f"100,100,0,0,{border},{outline},0,8,60,60,0,1")

    def ev(start, end, st, y, text):
        return f"Dialogue: 0,{ass_time(start)},{ass_time(end)},{st},,0,0,{y},,{text}"

    lines = ["[Script Info]", "ScriptType: v4.00+", f"PlayResX: {L['w']}", f"PlayResY: {L['h']}",
             "WrapStyle: 2", "", "[V4+ Styles]",
             "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, "
             "Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
             "Alignment, MarginL, MarginR, MarginV, Encoding",
             style("Head", L["head_size"], INK, -1, 4),
             style("Brand", L["brand_size"], INK, 0, 3),
             style("Sub", L["sub_size"], INK, -1, 10, box=True),
             style("End", L["end_size"], GOLD, -1, 3),
             style("AI", AI_SIZE, INK, 0, 8, box=True),
             "", "[Events]",
             "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    # 헤드라인은 카드가 뜨는 동안만 비운다
    spans, t0 = [], 0.0
    for a, b, _ in sorted(cards):
        spans.append((t0, a))
        t0 = b
    spans.append((t0, total))
    for a, b, text in cards:
        lines.append(ev(a, b, "Head", L["head_y"], text))
    # 법무 2차 지적 2-2: 축소된 원본 배지와 별도로, 숏폼 화면 자체에 AI 표시를 크게 고정
    lines.append(ev(0, total, "AI", L["ai_y"], L["ai_text"]))
    if L["h"] > L["w"]:   # 세로: 제목 두 줄, 둘째 줄 강조
        head = headline[0] + r"\N" + rf"{{\c{GOLD}}}" + headline[1]
        lines += [ev(a, b, "Head", L["head_y"], head) for a, b in spans if b > a]
        lines.append(ev(0, total, "Brand", L["brand_y"], brand))
        if end_text:
            lines.append(ev(total - END_CARD, total, "End", L["end_y"], end_text))
    else:                 # 정사각형: 제목 한 줄, 아래 줄은 브랜드 → 마지막에 안내 문구
        head = headline[0] + " " + rf"{{\c{GOLD}}}" + headline[1]
        lines += [ev(a, b, "Head", L["head_y"], head) for a, b in spans if b > a]
        lines.append(ev(0, total - (END_CARD if end_text else 0), "Brand", L["brand_y"], brand))
        if end_text:
            lines.append(ev(total - END_CARD, total, "End", L["end_y"], end_text))
    for a, b, text in cues:
        lines.append(ev(a, b, "Sub", L["sub_y"], text.replace("\n", r"\N")))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build(ep, fmt, cfg, timings, title):
    L = LAYOUTS[fmt]
    work = ep / "assets/build/shorts"
    work.mkdir(parents=True, exist_ok=True)
    by_id = {t["id"]: t for t in timings}

    # 1) 장면별 사용 길이: 마지막 장면은 끝까지, 나머지는 마지막 문장 + 여유
    clips, audio, cues, offset, sr = [], [], [], 0.0, None
    starts = {}
    for i, sid in enumerate(cfg["scenes"]):
        t = by_id[sid]
        starts[sid] = offset
        vid = ep / f"assets/build/scenes/S{sid:02d}.mp4"
        if not vid.exists():
            sys.exit(f"{vid}가 없습니다. 본편(assemble.py)을 먼저 만드세요.")
        last = i == len(cfg["scenes"]) - 1
        dur = probe_duration(vid) if last else min(t["sentences"][-1]["end"] + SCENE_TAIL, probe_duration(vid))
        a, sr = sf.read(ep / f"assets/audio/scene_{sid:02d}.wav", dtype="float32")
        n = int(round(dur * sr))
        audio.append(np.pad(a, (0, max(0, n - len(a))))[:n])
        for s in t["sentences"]:
            cues += cues_for(s, offset, max_line=L["max_line"])
        clips.append((vid, dur))
        offset += dur
    total = offset
    if total > 60:
        print(f"주의: {fmt} 길이 {total:.1f}초 (60초 초과). 유튜브 숏츠는 3분까지 되지만 60초 이하가 좋다.")
    sf.write(work / "narration.wav", np.concatenate(audio), sr)
    run([sys.executable, str(HERE / "bgm.py"), str(work / "bgm.wav"), f"{total:.2f}"])

    ass = work / f"{fmt}.ass"
    cards = []
    for c in cfg.get("cards", []):   # {"scene": 5, "text": "...", "dur": 4}: 그 장면 시작부터 dur초
        a = starts[c["scene"]] + 0.3
        cards.append((a, a + c.get("dur", 4.0), c["text"]))
    write_ass(ass, L, cues, cfg["headline"], f"최고의 공부 · {title}", cfg["end"], total, cards)

    # 2) 장면 이어 붙이기 → 흐린 배경 + 원본 16:9 + 글자
    inputs, chains = [], []
    for k, (vid, dur) in enumerate(clips):
        inputs += ["-t", f"{dur:.3f}", "-i", str(vid)]
        chains.append(f"[{k}:v]setpts=PTS-STARTPTS,fps=30[c{k}]")
    n = len(clips)
    w, h = L["w"], L["h"]
    filt = (";".join(chains) + ";" + "".join(f"[c{k}]" for k in range(n)) + f"concat=n={n}:v=1:a=0[cat];"
            f"[cat]split[a][b];"
            f"[a]scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},boxblur=28:2,"
            f"eq=brightness=-0.18:saturation=0.8[bg];"
            f"[b]scale={w}:-2[fg];"
            f"[bg][fg]overlay=0:{L['video_y']},ass={ass}[v];"
            f"[{n}:a]aformat=channel_layouts=stereo[nar];[{n + 1}:a]volume={10 ** (BGM_GAIN_DB / 20):.4f}[bgm];"
            f"[nar][bgm]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[aout]")
    dest = ep / f"output/shorts_{fmt}.mp4"
    run(["ffmpeg", "-y", "-v", "error", *inputs, "-i", str(work / "narration.wav"), "-i", str(work / "bgm.wav"),
         "-filter_complex", filt, "-map", "[v]", "-map", "[aout]", "-t", f"{total:.3f}",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", str(dest)])
    print(f"{dest.name}: {probe_duration(dest):.1f}s, {w}x{h}, 장면 {cfg['scenes']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode")
    ap.add_argument("--format", default="all", choices=["vertical", "square", "all"])
    args = ap.parse_args()
    ep = Path(args.episode).resolve()
    sb = json.loads((ep / "03_storyboard.json").read_text(encoding="utf-8"))
    if "shorts" not in sb:
        sys.exit('03_storyboard.json에 "shorts" 설정이 없습니다 (scenes, headline, end).')
    timings = json.loads((ep / "assets/audio/timings.json").read_text(encoding="utf-8"))
    title = sb.get("concept") or sb["title"].split(":")[0]
    for fmt in (["vertical", "square"] if args.format == "all" else [args.format]):
        build(ep, fmt, sb["shorts"], timings, title)


if __name__ == "__main__":
    main()
