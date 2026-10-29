"""유튜브 썸네일(1280×720): 서로 붙는 종이 두 장(장면 1의 AI 영상 마지막 장면) + 큰 질문.

사용법 (에피소드 폴더에서): python thumbnail.py
"""
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

EP = Path(__file__).resolve().parent
BG = EP / "assets/build/thumb_bg.png"
SANS = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
KR = 1  # .ttc 안의 한국어(KR) 글꼴 번호
GOLD, INK, BG_COLOR = "#E8B44C", "#EDEAE3", "#15171C"

# 종이 아래쪽이 안쪽으로 모인 순간 (AI 영상 7초 무렵)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "7.0", "-i", str(EP / "assets/media/paper_sheets_blow.mp4"),
                "-frames:v", "1", str(BG)], check=True)

photo = Image.open(BG).convert("RGB").crop((520, 0, 1400, 1080)).resize((587, 720))
photo = ImageEnhance.Brightness(photo).enhance(0.85)
im = Image.new("RGB", (1280, 720), BG_COLOR)
im.paste(photo, (0, 0))
d = ImageDraw.Draw(im)
# 종이가 모이는 방향 화살표 두 개
for x0, x1 in ((90, 230), (497, 357)):
    d.line((x0, 470, x1, 470), fill=GOLD, width=14)
    tip = 1 if x1 > x0 else -1
    d.polygon([(x1 + tip * 34, 470), (x1, 448), (x1, 492)], fill=GOLD)
d.rounded_rectangle((14, 14, 420, 58), radius=8, fill=(0, 0, 0))
d.text((26, 18), "AI 이미지 · 실제 실험 사진 아님", font=ImageFont.truetype(SANS, 26, index=KR), fill=INK)

d.text((640, 120), "왜 붙을까?", font=ImageFont.truetype(SANS, 112, index=KR), fill=GOLD)
d.text((644, 285), "숨을 불었는데 종이가 다가온다", font=ImageFont.truetype(SANS, 36, index=KR), fill=INK)
d.rectangle((644, 360, 1220, 366), fill=GOLD)
d.text((644, 400), "베르누이의 원리", font=ImageFont.truetype(SERIF, 72, index=KR), fill=INK)
d.text((644, 620), "최고의 공부", font=ImageFont.truetype(SERIF, 40, index=KR), fill=GOLD)
im.save(EP / "output/thumbnail.png")
