"""유튜브 썸네일(1280×720): 완성된 정사각형 그림(장면 13) + 큰 제목.

사용법 (에피소드 폴더에서): python thumbnail.py
"""
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

EP = Path(__file__).resolve().parent
BG = EP / "assets/build/thumb_bg.png"
SANS = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
KR = 1  # .ttc 안의 한국어(KR) 글꼴 번호

subprocess.run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.3", "-i",
                str(EP / "assets/render/S13/videos/visuals/1080p30/S13.mp4"), "-frames:v", "1", str(BG)], check=True)

fig = Image.open(BG).convert("RGB").crop((60, 0, 1000, 1010)).resize((622, 668))
im = Image.new("RGB", (1280, 720), "#15171C")
im.paste(fig, (20, 26))
d = ImageDraw.Draw(im)
d.text((680, 150), "근의 공식", font=ImageFont.truetype(SERIF, 120, index=KR), fill="#E8B44C")
d.text((684, 320), "외우지 마세요", font=ImageFont.truetype(SANS, 72, index=KR), fill="#EDEAE3")
d.rectangle((684, 440, 1240, 446), fill="#E8B44C")
d.text((684, 470), "1200년 전 바그다드의 정사각형", font=ImageFont.truetype(SANS, 36, index=KR), fill="#8A8F98")
d.text((684, 620), "최고의 공부", font=ImageFont.truetype(SERIF, 40, index=KR), fill="#E8B44C")
im.save(EP / "output/thumbnail.png")
