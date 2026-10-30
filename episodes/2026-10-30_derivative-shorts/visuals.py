"""미분 숏츠 (세로 1080×1920). 화면 좌표: 가로 ±4.5, 세로 ±8 (1단위 = 120px).

그림은 SAFE_TOP(4.3) 아래, SAFE_BOTTOM(-3.1) 위, SAFE_RIGHT(3.6) 왼쪽에만 둔다.
헤드라인, AI 표시, 자막은 assemble.py가 입힌다.
"""
import numpy as np

from choigo_style import *

ORANGE = "#F08A3C"
YELLOW = "#F2D04B"
ROAD = "#5A5F66"
CX = -0.35          # 그림 영역 가운데 (오른쪽 버튼 자리를 피해 살짝 왼쪽)

# 이번 편의 '휘어진 길': 간 거리 f(t) = 0.4t + 0.6t² (점점 빨라짐, t는 0~1. 장면 10 예시와 같은 방향)
def f(t):
    return 0.4 * t + 0.6 * t * t


def df(t):
    return 0.4 + 1.2 * t


def big(text, size=120, color=INK):
    return T(text, size=size, color=color, weight=BOLD)


def flash(scene, run_time=0.45):
    """카메라 섬광: 화면 전체가 하얗게 번쩍였다가 사라진다."""
    w = Rectangle(width=config.frame_width + 1, height=config.frame_height + 1, stroke_width=0,
                  fill_color=WHITE, fill_opacity=0.85)
    scene.add(w)
    scene.play(FadeOut(w), run_time=run_time)


def red_x(mob, width=14):
    return VGroup(Line(mob.get_corner(UL), mob.get_corner(DR)), Line(mob.get_corner(UR), mob.get_corner(DL))) \
        .set_stroke(CORAL, width)


def stopwatch(radius=0.55):
    face = Circle(radius=radius, color=INK, stroke_width=6)
    knob = Rectangle(width=0.22, height=0.14, stroke_width=0, fill_color=INK, fill_opacity=1).next_to(face, UP, buff=0.02)
    hand = Line(ORIGIN, UP * radius * 0.8, color=YELLOW, stroke_width=6)
    return VGroup(face, knob, hand)


class RoadGraph(VGroup):
    """시간-거리 그래프를 '휘어진 길'로 그린다."""

    def __init__(self, width=6.6, height=5.4, center=(CX, 0.4, 0), **kw):
        super().__init__(**kw)
        self.ax = Axes(x_range=[0, 1.05, 1], y_range=[0, 1.1, 1], x_length=width, y_length=height,
                       tips=True, axis_config={"color": INK, "stroke_width": 4, "include_ticks": False})
        self.ax.move_to(center)
        self.road = self.ax.plot(f, x_range=[0, 1], color=ROAD, stroke_width=34)
        self.edge = self.ax.plot(f, x_range=[0, 1], color=GREY_B, stroke_width=40).set_z_index(-1)
        self.lane = DashedVMobject(self.ax.plot(f, x_range=[0, 1], color=WHITE, stroke_width=4), num_dashes=26)
        self.xl = T("시간", size=30, color=MUTED).next_to(self.ax.x_axis.get_end(), DOWN, buff=0.15).shift(LEFT * 0.3)
        self.yl = T("간 거리", size=30, color=MUTED).next_to(self.ax.y_axis.get_end(), RIGHT, buff=0.15)
        self.add(self.ax, self.edge, self.road, self.lane, self.xl, self.yl)

    def p(self, t):
        return self.ax.c2p(t, f(t))

    def chord(self, t1, t2, extend=0.6, color=ORANGE, width=8):
        a, b = np.array(self.p(t1)), np.array(self.p(t2))
        d = (b - a) / np.linalg.norm(b - a)
        return Line(a - d * extend, b + d * extend, color=color, stroke_width=width)

    def tangent(self, t, half=1.6, color=ORANGE, width=8):
        a = np.array(self.p(t))
        d = np.array(self.ax.c2p(1, df(t))) - np.array(self.ax.c2p(0, 0))
        d = d / np.linalg.norm(d)
        return Line(a - d * half, a + d * half, color=color, stroke_width=width)


def graph_plate(g):
    return plate(VGroup(), opacity=0.5)[0].become(
        RoundedRectangle(corner_radius=0.2, width=g.width + 0.6, height=g.height + 0.6, stroke_width=0,
                         fill_color=BLACK, fill_opacity=0.5).move_to(g))


# ── ① 훅 ─────────────────────────────────────────────────
class S01(ChoigoScene):
    SCENE_ID = 1
    CAMERA_DRIFT = False
    FLASH = 2.6     # 배경 영상(5.0초부터)에서 차가 지나며 섬광이 터지는 시각

    def build(self):
        q1 = big("0÷0", 190)
        q2 = big("= 과속?", 110, ORANGE)
        VGroup(q1, q2).arrange(DOWN, buff=0.25).move_to([CX, 0.9, 0])
        self.play(FadeIn(q1, scale=1.8), run_time=0.25)      # 첫 프레임부터 질문
        self.play(q1.animate.scale(1.05), run_time=self.FLASH - 0.3, rate_func=there_and_back)
        flash(self, 0.3)
        self.play(FadeIn(q2, shift=LEFT * 0.4, scale=1.3), run_time=0.25)


# ── ② 문제 세우기 ─────────────────────────────────────────
class S02(ChoigoScene):
    SCENE_ID = 2

    def build(self):
        eq = VGroup(T("속도", size=72, weight=BOLD), T("=", size=72), T("거리", size=72, weight=BOLD, color=TEAL),
                    T("÷", size=72), T("시간", size=72, weight=BOLD, color=YELLOW)).arrange(RIGHT, buff=0.25)
        eq.move_to([CX, 1.6, 0])
        bg = plate(eq, opacity=0.5, buff=0.35)[0]
        self.play(FadeIn(bg), LaggedStart(*[Write(m) for m in eq], lag_ratio=0.25), run_time=1.3)
        self.at(1)
        self.play(self.camera.frame.animate.scale(0.92).move_to([CX, 1.0, 0]), run_time=0.3)
        sw = stopwatch(0.75).move_to([CX - 1.6, -1.0, 0])
        tape = VGroup(Line(LEFT * 1.2, RIGHT * 1.2, color=TEAL, stroke_width=10),
                      *[Line(UP * 0.15, DOWN * 0.15, color=TEAL, stroke_width=6).shift(RIGHT * x) for x in (-1.2, 1.2)])
        tape.move_to([CX + 1.6, -1.0, 0])
        self.play(FadeIn(sw), FadeIn(tape), run_time=0.4)
        z_t = T("0초", size=56, color=YELLOW, weight=BOLD).next_to(sw, DOWN, buff=0.2)
        z_d = T("0m", size=56, color=TEAL, weight=BOLD).next_to(tape, DOWN, buff=0.4)
        self.play(tape.animate.stretch(0.02, 0), FadeIn(z_t), FadeIn(z_d), run_time=0.8)
        self.play(Transform(eq[2], T("0m", size=72, weight=BOLD, color=TEAL).move_to(eq[2])),
                  Transform(eq[4], T("0초", size=72, weight=BOLD, color=YELLOW).move_to(eq[4])), run_time=0.5)


class S03(ChoigoScene):
    SCENE_ID = 3
    CAMERA_DRIFT = False

    def build(self):
        q = T("?", size=420, color=GOLD, weight=BOLD).set_opacity(0.35).move_to([CX, 0.6, 0])
        zz = big("0 ÷ 0", 170).move_to([CX, 0.6, 0])
        self.add(zz)
        self.play(FadeIn(q, scale=0.4), run_time=0.6)
        crack = VMobject(stroke_color=CORAL, stroke_width=8).set_points_as_corners(
            [[CX - 0.2, 1.5, 0], [CX + 0.15, 0.9, 0], [CX - 0.25, 0.4, 0], [CX + 0.2, -0.3, 0]])
        self.play(Create(crack), Wiggle(zz, scale_value=1.05, rotation_angle=0.04), run_time=0.7)
        self.until(self.scene_len - 0.45)
        self.play(self.camera.frame.animate.scale(0.55).move_to([-2.5, 0.6, 0]), run_time=0.4)


# ── ③ 카메라의 비밀 ───────────────────────────────────────
def no_device_note():
    return plate(T("실제 단속 장비 촬영 아님", size=30, color=INK), opacity=0.6, buff=0.12).move_to([CX, 3.95, 0])


class S04(ChoigoScene):
    SCENE_ID = 4

    def build(self):
        # 실사 바닥 영상(움직임)은 분위기로 어둡게 깔고, 원리는 위에서 내려다본 차로 도식으로 보여준다
        self.add(no_device_note())
        lane = Rectangle(width=3.0, height=6.4, stroke_color=INK, stroke_width=4, fill_color=BLACK, fill_opacity=0.55)
        lane.move_to([CX, 0.4, 0])
        sy = (-0.9, 1.7)                                     # 센서 1(아래) → 센서 2(위), 차는 아래에서 위로
        boxes = VGroup(*[RoundedRectangle(corner_radius=0.06, width=2.6, height=0.5, stroke_color=YELLOW, stroke_width=5,
                                          fill_color=YELLOW, fill_opacity=0.35).move_to([CX, y, 0]) for y in sy])
        labs = VGroup(*[T(f"센서 {k + 1}", size=30, color=INK, weight=BOLD).move_to(b) for k, b in enumerate(boxes)])
        self.play(FadeIn(lane), run_time=0.4)
        for b, l in zip(boxes, labs):
            self.play(FadeIn(b, scale=1.1), FadeIn(l), run_time=0.45)
        gap = DoubleArrow([CX - 2.0, sy[0], 0], [CX - 2.0, sy[1], 0], color=YELLOW, buff=0, stroke_width=6)
        gl = T("짧은\n거리", size=30, color=YELLOW, weight=BOLD).next_to(gap, LEFT, buff=0.12)
        self.play(GrowFromCenter(gap), FadeIn(gl), run_time=0.4)
        self.at(1)
        car = RoundedRectangle(corner_radius=0.18, width=1.1, height=1.7, stroke_width=0, fill_color=ORANGE,
                               fill_opacity=0.95).move_to([CX, -2.4, 0])
        sw = stopwatch(0.6).move_to([CX + 2.35, 0.4, 0])
        self.play(FadeIn(car), FadeIn(sw), run_time=0.2)
        front = car.height / 2
        self.play(car.animate.move_to([CX, sy[0] - front, 0]), run_time=0.4, rate_func=linear)
        self.play(car.animate.move_to([CX, sy[1] - front, 0]), Indicate(boxes[0], color=WHITE),
                  Rotate(sw[2], angle=-1.4 * PI, about_point=sw[0].get_center()), run_time=0.9, rate_func=linear)
        self.play(car.animate.move_to([CX, 3.2, 0]), Indicate(boxes[1], color=WHITE), run_time=0.4, rate_func=linear)


class S05(ChoigoScene):
    SCENE_ID = 5

    def build(self):
        self.add(no_device_note())
        top = T("아주 짧은 거리", size=58, color=TEAL, weight=BOLD)
        bot = T("아주 짧은 시간", size=58, color=YELLOW, weight=BOLD)
        bar = Line(LEFT * 2.6, RIGHT * 2.6, color=INK, stroke_width=6)
        frac = VGroup(top, bar, bot).arrange(DOWN, buff=0.3).move_to([CX, 1.2, 0])
        bg = plate(frac, opacity=0.5, buff=0.35)[0]
        self.play(FadeIn(bg), FadeIn(top, shift=DOWN * 0.2), Create(bar), FadeIn(bot, shift=UP * 0.2), run_time=0.9)
        self.at(1)
        zz = T("0 ÷ 0", size=64, weight=BOLD).move_to([CX, -1.2, 0])
        self.play(FadeIn(zz), run_time=0.3)
        self.play(Create(red_x(zz)), run_time=0.4)
        tags = VGroup(T("≈0", size=40, color=ORANGE, weight=BOLD).next_to(top, RIGHT, buff=0.2),
                      T("≈0", size=40, color=ORANGE, weight=BOLD).next_to(bot, RIGHT, buff=0.2))
        note = plate(T("정확히는: 아주 짧은 구간의 평균 속도", size=30, color=INK), buff=0.12).move_to([CX, -2.5, 0])
        self.play(FadeIn(tags, scale=1.4), FadeIn(note), run_time=0.5)


# ── ④ 휘어진 길 ──────────────────────────────────────────
class S06(ChoigoScene):
    SCENE_ID = 6

    def build(self):
        self.wait(0.6)   # 드론 실사가 먼저 화면을 채운다
        g = RoadGraph()
        bg = graph_plate(g)
        self.play(FadeIn(bg), Create(g.ax), FadeIn(g.xl), FadeIn(g.yl), run_time=0.6)
        car = Dot(g.p(0), radius=0.16, color=ORANGE)
        t = ValueTracker(0)
        car.add_updater(lambda m: m.move_to(g.p(t.get_value())))
        self.add(car)
        self.play(Create(g.edge), Create(g.road), Create(g.lane), t.animate.set_value(1), run_time=2.0, rate_func=linear)


class S07(ChoigoScene):
    SCENE_ID = 7

    def build(self):
        g = RoadGraph()
        self.add(graph_plate(g), g)
        t1, t2 = ValueTracker(0.42), ValueTracker(0.62)
        d1 = always_redraw(lambda: Dot(g.p(t1.get_value()), radius=0.15, color=YELLOW))
        d2 = always_redraw(lambda: Dot(g.p(t2.get_value()), radius=0.15, color=YELLOW))
        l1 = plate(T("센서 1", size=28, color=YELLOW, weight=BOLD), buff=0.08).next_to(g.p(0.42), DR, buff=0.1)
        l2 = plate(T("센서 2", size=28, color=YELLOW, weight=BOLD), buff=0.08).next_to(g.p(0.62), UL, buff=0.1)
        self.play(FadeIn(d1, scale=2), FadeIn(l1), run_time=0.4)
        self.play(FadeIn(d2, scale=2), FadeIn(l2), run_time=0.4)
        self.at(1)
        sec = always_redraw(lambda: g.chord(t1.get_value(), t2.get_value()))
        self.play(FadeOut(l1), FadeOut(l2), Create(sec), run_time=0.5)
        tag = plate(T("느림", size=44, color=TEAL, weight=BOLD), buff=0.12).move_to([CX + 0.4, -1.4, 0])
        self.play(t1.animate.set_value(0.05), t2.animate.set_value(0.25), FadeIn(tag), run_time=0.8)
        self.wait(0.5)
        tag2 = plate(T("빠름", size=44, color=ORANGE, weight=BOLD), buff=0.12).move_to([CX - 1.4, 2.6, 0])
        self.play(t1.animate.set_value(0.72), t2.animate.set_value(0.92), FadeOut(tag), FadeIn(tag2), run_time=0.8)


# ── ⑤ 아하 ───────────────────────────────────────────────
class S08(ChoigoScene):
    SCENE_ID = 8
    CAMERA_DRIFT = False

    def build(self):
        # 위쪽 절반은 드론 실사(길이 펴지는 장면)가 보이도록 비워 두고, 아래쪽에 돋보기
        c = np.array([CX, -1.0, 0])
        R = 1.85
        lens = Circle(radius=R, color=INK, stroke_width=8).move_to(c)
        glass = Circle(radius=R, stroke_width=0, fill_color=BLACK, fill_opacity=0.65).move_to(c)
        handle = Line(c + np.array([R * 0.72, -R * 0.72, 0]), c + np.array([R * 1.25, -R * 1.2, 0]),
                      color=INK, stroke_width=16)
        k = 1.1                     # 돋보기 안 곡선 기울기 (화면 단위)
        bend = -1.1                 # 배율 1일 때 휘어짐 (아래로 볼록)

        def local_road(mag):
            curve = FunctionGraph(lambda u: k * u - bend * u * u / mag, x_range=[-R * 0.62, R * 0.62])
            curve.shift(c)
            road = curve.copy().set_stroke(ROAD, 30)
            edge = curve.copy().set_stroke(GREY_B, 36)
            lane = DashedVMobject(curve.copy().set_stroke(WHITE, 4), num_dashes=12)
            pts = VGroup(Dot(curve.point_from_proportion(0.38), radius=0.13, color=YELLOW),
                         Dot(curve.point_from_proportion(0.62), radius=0.13, color=YELLOW))
            return VGroup(edge, road, lane, pts)

        cur = local_road(1)
        mag = plate(T("×1", size=34, color=GOLD, weight=BOLD), buff=0.1).next_to(lens, UP, buff=0.12)
        self.play(FadeIn(glass), Create(lens), Create(handle), FadeIn(cur), FadeIn(mag), run_time=0.6)
        for m in (2, 10, 100):
            new = local_road(m)
            new[3][0].move_to(interpolate(new[3][0].get_center(), c, 0.5 - 0.5 / m ** 0.3))
            new[3][1].move_to(interpolate(new[3][1].get_center(), c, 0.5 - 0.5 / m ** 0.3))
            self.play(Transform(cur, new), Transform(mag, plate(T(f"×{m}", size=34, color=GOLD, weight=BOLD), buff=0.1)
                                                    .next_to(lens, UP, buff=0.12)), run_time=0.7)
        self.at(1, 0.6)
        straight = Line(c + np.array([-R * 0.62, -k * R * 0.62, 0]), c + np.array([R * 0.62, k * R * 0.62, 0]),
                        color=WHITE, stroke_width=10)
        self.play(Create(straight), run_time=0.3)
        flash(self, 0.4)
        word = plate(T("거의 직선", size=60, color=GOLD, weight=BOLD), buff=0.15).move_to(c + np.array([-1.7, 1.25, 0]))
        note = T("매끄러운 곡선일 때", size=24, color=MUTED).next_to(lens, DOWN, buff=0.12).shift(LEFT * 0.6)
        self.play(FadeIn(word, scale=1.4), FadeIn(note), run_time=0.4)


class S09(ChoigoScene):
    SCENE_ID = 9

    def build(self):
        g = RoadGraph()
        bg = graph_plate(g)
        t = ValueTracker(0.35)
        dot = always_redraw(lambda: Dot(g.p(t.get_value()), radius=0.16, color=YELLOW))
        tan = always_redraw(lambda: g.tangent(t.get_value()))
        self.play(FadeIn(bg), FadeIn(g), run_time=0.4)
        self.play(FadeIn(dot, scale=2), Create(tan), run_time=0.5)
        lab = plate(T("순간 속도", size=40, color=ORANGE, weight=BOLD), buff=0.12).move_to([CX + 1.2, -0.9, 0])
        self.play(FadeIn(lab, shift=UP * 0.2), run_time=0.4)
        self.at(1)
        head = plate(T("기울기 = 미분", size=76, color=GOLD, weight=BOLD), opacity=0.7, buff=0.25).move_to([CX, 3.5, 0])
        self.play(FadeIn(head, shift=DOWN * 0.3), FadeOut(lab), run_time=0.5)
        self.play(t.animate.set_value(0.05), run_time=0.5)
        self.play(t.animate.set_value(0.95), run_time=1.0)


# ── ⑥ 오해 깨기 ──────────────────────────────────────────
class S10(ChoigoScene):
    SCENE_ID = 10

    def build(self):
        d0 = big("÷ 0", 200).move_to([CX, 1.0, 0])
        self.play(FadeIn(d0, scale=1.3), run_time=0.3)
        x0 = red_x(d0, 18)
        self.play(Create(x0), run_time=0.3)
        self.at(1)
        self.play(FadeOut(d0), FadeOut(x0), run_time=0.25)
        head = T("거리 ÷ 시간", size=56, weight=BOLD).move_to([CX, 3.4, 0])
        self.play(FadeIn(head), run_time=0.25)
        steps = [(1, "61"), (0.1, "60.1"), (0.01, "60.01"), (0.001, "60.001")]
        y_bar, y_val = 1.2, -0.4
        bar = Rectangle(width=5.4, height=0.5, stroke_width=0, fill_color=YELLOW, fill_opacity=0.9)
        bar.move_to([CX, y_bar, 0])
        cap = T("시간 간격  1", size=36, color=YELLOW).next_to(bar, UP, buff=0.15)
        val = T("61", size=110, color=ORANGE, weight=BOLD).move_to([CX, y_val, 0])
        self.play(FadeIn(bar), FadeIn(cap), FadeIn(val), run_time=0.2)
        for dt, v in steps[1:]:
            w = max(5.4 * (dt ** 0.35), 0.06)
            self.play(bar.animate.stretch_to_fit_width(w), Transform(cap, T(f"시간 간격  {dt}", size=36, color=YELLOW)
                                                                       .next_to(bar, UP, buff=0.15)),
                      Transform(val, T(v, size=110, color=ORANGE, weight=BOLD).move_to([CX, y_val, 0])), run_time=0.32)
        goal = T("→ 60", size=80, color=GOLD, weight=BOLD).next_to(val, DOWN, buff=0.3)
        sym = M(r"\Delta t \to 0", size=56, color=MUTED).next_to(goal, DOWN, buff=0.3)
        ex = T("예시 숫자", size=24, color=MUTED).move_to([CX + 2.6, 4.0, 0])
        self.play(FadeIn(goal, shift=LEFT * 0.3), FadeIn(sym), FadeIn(ex), run_time=0.35)


# ── ⑦ 마지막 한 방 ───────────────────────────────────────
class S11(ChoigoScene):
    SCENE_ID = 11
    CAMERA_DRIFT = False

    def build(self):
        zz = big("0÷0", 170).move_to([CX, 1.0, 0])
        self.play(FadeIn(zz, scale=1.3), run_time=0.3)
        xz = red_x(zz, 16)
        self.play(Create(xz), run_time=0.4)
        self.at(1)
        self.play(FadeOut(zz), FadeOut(xz), run_time=0.2)
        flash(self, 0.35)
        msg = VGroup(T("0에 다가가면", size=72, weight=BOLD), T("→ 잡힌다", size=96, color=ORANGE, weight=BOLD)) \
            .arrange(DOWN, buff=0.25).move_to([CX, 1.0, 0])
        self.play(FadeIn(msg, scale=1.2), run_time=0.4)
        self.at(2)
        logo = VGroup(T("최고의 공부", size=110, font=SERIF, color=GOLD, weight=BOLD),
                      T("하루에 개념 하나", size=40)).arrange(DOWN, buff=0.25).move_to([CX, 1.0, 0])
        self.play(FadeOut(msg), FadeIn(logo, scale=0.9), run_time=0.4)
