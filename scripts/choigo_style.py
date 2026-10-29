"""「최고의 공부」 공통 영상 스타일 (Manim).

모든 에피소드의 visuals.py는 이 모듈의 ChoigoScene을 상속한다.
- 장면 길이와 문장 타이밍은 assets/audio/timings.json에서 읽어 나레이션과 맞춘다.
- 화면 아래쪽(y < -2.5)은 자막 자리이므로 비워둔다.
- 장면은 투명 배경으로 렌더링된다. 배경(실사 영상/사진 또는 기본 배경색)은 assemble.py가 아래에 깐다.
  장면 구성표에서 visual.background로 지정한 소재가 배경이 되고, 출처 표시(AI 재현 표시 포함)는 자동으로 붙는다.
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


def plate(mob, opacity=0.55, buff=0.3):
    """실사 배경 위에서 글자가 잘 보이도록 뒤에 반투명 판을 깐다."""
    bg = RoundedRectangle(corner_radius=0.12, width=mob.width + 2 * buff, height=mob.height + 2 * buff,
                          stroke_width=0, fill_color=BLACK, fill_opacity=opacity).move_to(mob)
    return VGroup(bg, mob)


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
        self.ep = ep
        sb = json.loads((ep / "03_storyboard.json").read_text(encoding="utf-8"))
        self.storyboard_scene = next(s for s in sb["scenes"] if s["id"] == self.SCENE_ID)
        src = ep / "assets/sources.json"
        self.sources = {a["id"]: a for a in json.loads(src.read_text(encoding="utf-8"))["assets"]} \
            if src.exists() else {}

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
        bg = self.storyboard_scene["visual"].get("background")
        if bg:
            self.background_label(bg["media"])
        self.build()
        self.until(self.scene_len)
        print(f"[choigo] S{self.SCENE_ID:02d} rendered {self.time:.2f}s / narration {self.scene_len:.2f}s")

    def build(self):
        raise NotImplementedError

    # ── 실사 소재 ──────────────────────────────────────
    def media_file(self, mid):
        files = sorted((self.ep / "assets/media").glob(f"{mid}.*"))
        if not files:
            raise FileNotFoundError(f"소재 없음: assets/media/{mid}.* (fetch_media.py 확인)")
        return files[0]

    def media_label(self, mid):
        info = self.sources.get(mid, {})
        if info.get("ai"):
            return "AI로 만든 재현 영상" if info.get("type") == "video" else "AI로 만든 재현 이미지"
        return info.get("credit") or info.get("author") or ""

    def background_label(self, mid):
        """배경 소재의 출처(또는 AI 재현 표시)를 오른쪽 위에 작게 단다."""
        text = self.media_label(mid)
        if text:
            lab = T(text[:40], size=18, color=INK).set_opacity(0.75).to_corner(UR, buff=0.3)
            self.add(lab)

    def photo(self, mid, height=None, full=False, label=True):
        """사진(박물관 자료, AI 이미지)을 화면에 놓는다. full=True면 화면을 가득 채운다."""
        img = ImageMobject(str(self.media_file(mid)))
        if full:
            img.scale(max(config.frame_width / img.width, config.frame_height / img.height))
        elif height:
            img.set_height(height)
        grp = Group(img)
        if label and self.media_label(mid):
            cap = T(self.media_label(mid)[:40], size=18, color=INK).set_opacity(0.8)
            cap.next_to(img, DOWN, buff=0.1, aligned_edge=RIGHT) if not full else cap.to_corner(UR, buff=0.3)
            grp.add(cap)
        return grp

    def photo_or(self, mid, fallback, height):
        """사진이 있으면 사진을, 아직 없으면 직접 그린 대체 그림을 같은 크기로 쓴다."""
        if sorted((self.ep / "assets/media").glob(f"{mid}.*")):
            return self.photo(mid, height=height)
        return fallback.set_height(height)

    # ── 자주 쓰는 연출 ──────────────────────────────────
    def show_chapter(self, number, title, hold=1.2):
        card = chapter_card(number, title)
        self.play(FadeIn(card[0], shift=UP * 0.2), Create(card[1]), run_time=0.8)
        self.wait(hold)
        self.play(FadeOut(card), run_time=0.5)
