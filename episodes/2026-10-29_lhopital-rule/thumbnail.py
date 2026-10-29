"""유튜브 썸네일(1280×720): 0/0 + 두 곡선(장면 5) + 큰 제목.

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

overlay = EP / "assets/render/S05/videos/visuals/1080p30/S05.mov"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "color=c=0x15171C:s=1920x1080", "-sseof", "-0.3",
                "-i", str(overlay), "-filter_complex", "[0][1]overlay=format=auto", "-frames:v", "1", str(BG)], check=True)

graph = Image.open(BG).convert("RGB").crop((80, 160, 1150, 1000)).resize((590, 464))
im = Image.new("RGB", (1280, 720), "#15171C")
im.paste(graph, (0, 200))
d = ImageDraw.Draw(im)
d.text((60, 40), "0/0", font=ImageFont.truetype(SERIF, 150, index=KR), fill="#E8B44C")
d.text((330, 95), "= ?", font=ImageFont.truetype(SERIF, 96, index=KR), fill="#EDEAE3")
d.text((660, 190), "로피탈의 정리", font=ImageFont.truetype(SERIF, 92, index=KR), fill="#E8B44C")
d.text((664, 330), "주인은 따로 있었다", font=ImageFont.truetype(SANS, 58, index=KR), fill="#EDEAE3")
d.rectangle((664, 430, 1220, 436), fill="#E8B44C")
d.text((664, 460), "0/0은 빠르기 대결이다", font=ImageFont.truetype(SANS, 36, index=KR), fill="#8A8F98")
d.text((664, 620), "최고의 공부", font=ImageFont.truetype(SERIF, 40, index=KR), fill="#E8B44C")
im.save(EP / "output/thumbnail.png")
