"""「최고의 공부」 공통 영상 스타일 (Manim).

모든 에피소드의 visuals.py는 이 모듈의 ChoigoScene을 상속한다.
- 장면 길이와 문장 타이밍은 assets/audio/timings.json에서 읽어 나레이션과 맞춘다.
- 화면 아래쪽(y < -2.5)은 자막 자리이므로 비워둔다.
"""
import json
import os
from pathlib import Path

from manim import *  # noqa: F401,F403

# ── 색상 ────────────────────────────────────────────────
BG = "#15171C"
INK = "#EDEAE3"       # 기본 글자
MUTED = "#8A8F98"     # 보조 글자
GOLD = "#E8B44C"      # 핵심 강조
TEAL = "#4FB3BF"      # 보조 강조
CORAL = "#E86A5C"     # 경고, 오해
CLAY = "#B07A4F"      # 역사 소품

SANS = "Noto Sans CJK KR"
SERIF = "Noto Serif CJK KR"

SAFE_BOTTOM = -2.5    # 이 아래는 자막 영역

config.background_color = BG
config.frame_rate = 30
config.pixel_width = 1920
config.pixel_height = 1080

TexTemplateLibrary.default.add_to_preamble(r"\usepackage{amsmath}")


def T(text, size=36, color=INK, font=SANS, weight=NORMAL, **kw):
    """한글 텍스트."""
    return Text(text, font=font, font_size=size, color=color, weight=weight, **kw)


def M(*tex, size=56, color=INK, **kw):
    """수식."""
    return MathTex(*tex, font_size=size, color=color, **kw)


def chapter_card(number, title):
    """구간 제목: '② 시대 속으로'."""
    num = T(number, size=40, color=GOLD, font=SERIF, weight=BOLD)
    ttl = T(title, size=64, font=SERIF, weight=BOLD)
    grp = VGroup(num, ttl).arrange(RIGHT, buff=0.35)
    line = Line(LEFT, RIGHT, color=GOLD, stroke_width=2).set_width(grp.width + 0.6)
    line.next_to(grp, DOWN, buff=0.25)
    return VGroup(grp, line)


class ChoigoScene(MovingCameraScene):
    """나레이션 타이밍에 맞춰 장면을 만드는 기본 클래스.

    하위 클래스는 SCENE_ID와 build()를 정의한다.
    build() 안에서 self.at(i)로 i번째 문장이 시작될 때까지 기다린다.
    """

    SCENE_ID = None
    ZOOM_PER_SEC = 0.0015   # 느린 줌인(Ken Burns)
    CAMERA_DRIFT = True

    def setup(self):
        super().setup()
        ep = Path(os.environ["CHOIGO_EPISODE"])
        timings = json.loads((ep / "assets/audio/timings.json").read_text(encoding="utf-8"))
        info = next(t for t in timings if t["id"] == self.SCENE_ID)
        self.scene_len = info["duration"]
        self.sents = info["sentences"]

    def until(self, t):
        if t - self.time > 1 / 30:
            self.wait(t - self.time)

    def at(self, i, offset=0.0):
        """i번째 문장 시작(+offset)까지 기다린다."""
        self.until(self.sents[i]["start"] + offset)

    def construct(self):
        if self.CAMERA_DRIFT:
            frame = self.camera.frame
            frame.add_updater(lambda m, dt: m.scale(1 - self.ZOOM_PER_SEC * dt))
            self.add(frame)
        self.build()
        self.until(self.scene_len)
        print(f"[choigo] S{self.SCENE_ID:02d} rendered {self.time:.2f}s / narration {self.scene_len:.2f}s")

    def build(self):
        raise NotImplementedError

    # ── 자주 쓰는 연출 ──────────────────────────────────
    def show_chapter(self, number, title, hold=1.2):
        card = chapter_card(number, title)
        self.play(FadeIn(card[0], shift=UP * 0.2), Create(card[1]), run_time=0.8)
        self.wait(hold)
        self.play(FadeOut(card), run_time=0.5)
