"""베르누이의 원리 편 장면 (Manim). 장면 번호는 03_storyboard.json의 id와 같다.

모든 장면은 AI 실사 영상 위에 겹쳐지는 투명 레이어다.
핵심 비유 '세 주머니 지갑'의 색: 파랑 = 미는 주머니(압력), 주황 = 달리는 주머니(움직임), 회색 = 높이 주머니.
"""
from choigo_style import *  # noqa: F401,F403

P_BLUE = "#4FA3E0"     # 압력
K_ORANGE = "#F08A3C"   # 움직임의 에너지
H_GRAY = "#A7ADB5"     # 높이의 에너지


# ── 공용 부품: 세 주머니 지갑 ──────────────────────────────────
class Wallet(VGroup):
    """세 주머니 막대 + 총액 막대. values = (압력, 움직임, 높이), 합은 total."""

    def __init__(self, values=(5, 1, 2), total=8, height=2.4, width=0.42, labels=True, title=None, **kw):
        super().__init__(**kw)
        self.unit = height / total
        cols = [(P_BLUE, "미는"), (K_ORANGE, "달리는"), (H_GRAY, "높이")]
        self.bars = VGroup()
        for (c, name), v in zip(cols, values):
            bar = Rectangle(width=width, height=max(v * self.unit, 0.02), stroke_width=0, fill_color=c, fill_opacity=0.95)
            self.bars.add(bar)
        self.bars.arrange(RIGHT, buff=0.12, aligned_edge=DOWN)
        frame = RoundedRectangle(corner_radius=0.15, width=self.bars.width + 0.5, height=height + 0.5,
                                 stroke_color=INK, stroke_width=2, fill_color=BLACK, fill_opacity=0.55)
        frame.move_to(self.bars.get_bottom() + UP * height / 2)
        self.bars.align_to(frame, DOWN).shift(UP * 0.25)
        self.total_line = DashedLine(frame.get_left() + RIGHT * 0.1, frame.get_right() + LEFT * 0.1,
                                     color=GOLD, stroke_width=2).move_to(
            [frame.get_center()[0], self.bars.get_bottom()[1] + height, 0])
        self.add(frame, self.bars, self.total_line)
        if labels:
            self.labels = VGroup(*[T(n, size=14, color=c) for c, n in cols]).arrange(RIGHT, buff=0.1)
            self.labels.next_to(frame, DOWN, buff=0.08)
            self.add(self.labels)
        if title:
            self.add(T(title, size=22, color=INK).next_to(frame, UP, buff=0.1))

    def bars_for(self, values):
        """막대 높이를 values로 바꾼 사본 (Transform용)."""
        new = self.bars.copy()
        for bar, v in zip(new, values):
            bar.stretch_to_fit_height(max(v * self.unit, 0.02), about_edge=DOWN)
        return new


AI_GENERAL = "AI로 만든 영상"
AI_EXPERIMENT = "AI로 만든 영상 · 실제 실험 촬영 아님"
AI_HISTORY = "AI로 만든 재현 영상"


def ai_badge(text=AI_GENERAL):
    """법무 1차 지적 6: AI 클립이 보이는 동안 우측 상단에 고정, 반투명 바탕 위."""
    return plate(T(text, size=26, color=INK), opacity=0.6, buff=0.12).to_corner(UR, buff=0.25)


def flow_arrow(start, end, color=K_ORANGE, width=8):
    return Arrow(start, end, color=color, stroke_width=width, buff=0, max_tip_length_to_length_ratio=0.15)


def push_arrow(start, end, color=P_BLUE, width=10):
    return Arrow(start, end, color=color, stroke_width=width, buff=0, max_tip_length_to_length_ratio=0.3)


# ── ① 오프닝 질문 ──────────────────────────────────────────
class S01(ChoigoScene):
    SCENE_ID = 1
    CAMERA_DRIFT = False   # 실사 영상의 흔들림만으로 충분

    def build(self):
        self.add(ai_badge(AI_EXPERIMENT))
        self.at(3)
        wind = VGroup(*[Arrow(UP * 2.6 + RIGHT * dx, UP * 0.2 + RIGHT * dx, color=WHITE, stroke_width=6,
                              buff=0).set_opacity(0.55) for dx in (-0.25, 0.25)])
        q = VGroup(T("?", size=110, color=GOLD, weight=BOLD).move_to(LEFT * 3.6 + UP * 0.6),
                   T("?", size=110, color=GOLD, weight=BOLD).move_to(RIGHT * 3.6 + UP * 0.6))
        self.play(GrowArrow(wind[0]), GrowArrow(wind[1]), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(x, scale=1.6) for x in q], lag_ratio=0.3), run_time=0.8)
        line = plate(T("바람이 밀었는데, 왜 다가올까?", size=40, weight=BOLD)).move_to(DOWN * 1.7)
        self.play(FadeIn(line, shift=UP * 0.2), run_time=0.6)
        self.until(self.scene_len - 1.3)
        title = plate(T("베르누이의 원리", size=72, font=SERIF, weight=BOLD, color=GOLD), opacity=0.7, buff=0.4)
        self.play(FadeOut(VGroup(wind, q, line)), FadeIn(title, scale=0.95), run_time=0.5)


# ── ② 시대 속으로 ──────────────────────────────────────────
class S02(ChoigoScene):
    SCENE_ID = 2

    def build(self):
        self.add(ai_badge(AI_HISTORY))
        self.show_chapter("②", "시대 속으로", hold=0.3)
        card = plate(VGroup(T("다니엘 베르누이", size=56, font=SERIF, weight=BOLD),
                            T("1700~1782 · 바젤에서 활동", size=28)).arrange(DOWN, buff=0.15), buff=0.4).move_to(UP * 1.4)
        self.play(FadeIn(card, shift=UP * 0.2), run_time=0.8)
        self.at(1)
        dad = VGroup(T("요한 베르누이", size=34, weight=BOLD), T("아버지", size=24, color=MUTED)).arrange(DOWN, buff=0.08)
        son = VGroup(T("다니엘", size=34, weight=BOLD, color=GOLD), T("아들", size=24, color=MUTED)).arrange(DOWN, buff=0.08)
        tree = VGroup(dad, Arrow(UP * 0.4, DOWN * 0.4, color=INK), son).arrange(DOWN, buff=0.15)
        tag = T("로피탈의 숨은 스승", size=22, color=CORAL).next_to(dad, RIGHT, buff=0.3)
        box = plate(VGroup(tree, tag), buff=0.35).move_to(DOWN * 0.9)
        self.play(FadeIn(box[0]), FadeIn(dad, shift=DOWN * 0.2), run_time=0.6)
        self.play(GrowArrow(tree[1]), FadeIn(son, shift=DOWN * 0.2), FadeIn(tag, shift=LEFT * 0.2), run_time=0.8)


class S03(ChoigoScene):
    SCENE_ID = 3

    def build(self):
        self.add(ai_badge(AI_HISTORY + " · 전해지는 이야기"))
        year = plate(VGroup(T("1734", size=56, color=GOLD, weight=BOLD),
                            T("파리 왕립 과학 아카데미 대상", size=30)).arrange(RIGHT, buff=0.35)).move_to(UP * 2.3)
        self.play(FadeIn(year, shift=DOWN * 0.2), run_time=0.7)
        beam = Line(LEFT * 1.8, RIGHT * 1.8, color=GOLD, stroke_width=6)
        post = Line(DOWN * 1.1, ORIGIN, color=GOLD, stroke_width=6).next_to(beam, DOWN, buff=0)
        left = T("아버지", size=32).next_to(beam.get_left(), UP, buff=0.2)
        right = T("아들", size=32).next_to(beam.get_right(), UP, buff=0.2)
        eq = T("공동 수상", size=26, color=GOLD).next_to(post, DOWN, buff=0.15)
        scale_ = VGroup(beam, post, left, right, eq).move_to(DOWN * 0.1)
        bg = plate(scale_, buff=0.3)[0]
        self.play(FadeIn(bg), Create(beam), Create(post), FadeIn(left), FadeIn(right), FadeIn(eq), run_time=1.0)
        self.at(1)
        self.play(Rotate(VGroup(beam, left, right), angle=-0.12), run_time=0.8)
        crack = VGroup(Line(UP * 0.5 + LEFT * 0.1, DOWN * 0.1 + RIGHT * 0.1, color=CORAL, stroke_width=6),
                       Line(DOWN * 0.1 + RIGHT * 0.1, DOWN * 0.6 + LEFT * 0.15, color=CORAL, stroke_width=6)).move_to(beam)
        self.play(Create(crack), run_time=0.4)
        self.play(FadeOut(VGroup(scale_, bg, crack), shift=DOWN * 0.3), run_time=0.8)
        note = plate(T("…라고 전해집니다", size=28, color=MUTED)).move_to(DOWN * 1.6)
        self.play(FadeIn(note))


class S04(ChoigoScene):
    SCENE_ID = 4

    def build(self):
        self.add(ai_badge(AI_HISTORY))
        line = Line(LEFT * 5.6, RIGHT * 5.6, color=INK, stroke_width=3).shift(DOWN * 0.2)
        x1738 = 0.0
        d = Dot([x1738, -0.2, 0], color=GOLD, radius=0.12)
        c = plate(VGroup(T("1738", size=40, weight=BOLD, color=GOLD), T("다니엘 『유체역학』", size=30)).arrange(DOWN, buff=0.1))
        c.next_to(d, UP, buff=0.35)
        self.play(Create(line), FadeIn(d, scale=2), FadeIn(c, shift=DOWN * 0.2), run_time=1.0)
        self.at(1)
        dad_book = plate(VGroup(T("아버지 『수력학』", size=28, weight=BOLD), T("실제 출간은 그 뒤", size=22, color=MUTED))
                         .arrange(DOWN, buff=0.08)).move_to([4.0, -1.4, 0])
        printed = plate(VGroup(T("책에 적힌 연도", size=22, color=MUTED), T("'1732'", size=34, color=CORAL, weight=BOLD))
                        .arrange(DOWN, buff=0.06)).move_to([-4.0, -1.4, 0])
        self.play(FadeIn(dad_book, shift=LEFT * 0.2), run_time=0.6)
        arc = CurvedArrow(dad_book.get_top() + UP * 0.05, printed.get_top() + UP * 0.05, angle=PI / 3, color=CORAL)
        arc = DashedVMobject(arc, num_dashes=30)
        self.play(Create(arc), run_time=1.0)
        self.play(FadeIn(printed, scale=1.2), FadeIn(T("?", size=56, color=CORAL, weight=BOLD).next_to(printed, RIGHT, buff=0.2)))


# ── ③ 개념의 탄생 ──────────────────────────────────────────
class S05(ChoigoScene):
    SCENE_ID = 5

    def build(self):
        self.add(ai_badge(AI_HISTORY))
        self.show_chapter("③", "개념의 탄생", hold=0.3)
        lab = plate(T("압력 = 물이 벽을 미는 세기", size=32, color=P_BLUE, weight=BOLD)).to_corner(UL, buff=0.5)
        self.play(FadeIn(lab, shift=RIGHT * 0.2))
        self.at(1)
        # 확인된 실험만: 물통 + 굵기가 일정한 관 + 유리관 하나 (영상 위 투시도)
        tank = Rectangle(width=1.6, height=3.0, stroke_color=INK, stroke_width=3).move_to(LEFT * 4.6 + DOWN * 0.2)
        tank_w = Rectangle(width=1.5, height=2.5, stroke_width=0, fill_color=P_BLUE, fill_opacity=0.5).align_to(tank, DOWN).shift(UP * 0.05)
        pipe = Rectangle(width=7.4, height=0.5, stroke_color=INK, stroke_width=3).next_to(tank, RIGHT, buff=0).align_to(tank, DOWN)
        tube = Rectangle(width=0.3, height=2.6, stroke_color=INK, stroke_width=3).next_to(pipe, UP, buff=0).shift(RIGHT * 0.3)
        sch = VGroup(tank, tank_w, pipe, tube)
        bg = plate(sch, opacity=0.45, buff=0.3)[0]
        self.play(FadeIn(bg), Create(tank), FadeIn(tank_w), Create(pipe), Create(tube), run_time=1.0)
        hole = Circle(radius=0.3, color=WHITE, stroke_width=4).move_to(tube.get_bottom())
        self.play(Create(hole), run_time=0.5)
        self.at(2)
        full = tank_w.get_top()[1] - pipe.get_top()[1]
        col = Rectangle(width=0.26, height=full, stroke_width=0, fill_color=P_BLUE, fill_opacity=0.9)
        col.align_to(tube, DOWN).move_to(tube, coor_mask=[1, 0, 0])
        up = push_arrow(tube.get_bottom() + RIGHT * 0.6, tube.get_bottom() + RIGHT * 0.6 + UP * 1.6)
        self.play(GrowFromEdge(col, DOWN), GrowArrow(up), run_time=1.0)
        self.at(3)
        base = DashedLine([tank.get_left()[0], tank_w.get_top()[1], 0], [tube.get_right()[0] + 1.2, tank_w.get_top()[1], 0],
                          color=GOLD, stroke_width=3)
        base_lab = T("물통 수면", size=22, color=GOLD).next_to(base, RIGHT, buff=0.1)
        flow = flow_arrow(pipe.get_left() + RIGHT * 0.4, pipe.get_right() + LEFT * 0.4)
        self.play(Create(base), FadeIn(base_lab), GrowArrow(flow), run_time=0.8)
        self.play(col.animate.stretch_to_fit_height(full * 0.55, about_edge=DOWN), run_time=1.0)
        mark = T("↓ ?", size=48, color=CORAL, weight=BOLD).next_to(tube, RIGHT, buff=0.3).shift(UP * 0.3)
        self.play(FadeIn(mark, scale=1.3))


class S06(ChoigoScene):
    SCENE_ID = 6

    def build(self):
        self.add(ai_badge(AI_GENERAL))
        drop = VGroup(Circle(radius=0.45, color=TEAL, fill_color=TEAL, fill_opacity=0.6, stroke_width=3),
                      Triangle(color=TEAL, fill_color=TEAL, fill_opacity=0.6, stroke_width=0).scale(0.33).shift(UP * 0.48))
        drop.move_to(LEFT * 5.0 + UP * 1.2)
        purse = RoundedRectangle(corner_radius=0.08, width=0.6, height=0.42, color=GOLD, fill_color=GOLD,
                                 fill_opacity=0.9, stroke_width=0).next_to(drop, RIGHT, buff=-0.05).shift(DOWN * 0.25)
        hero = VGroup(drop, purse)
        self.play(FadeIn(hero, shift=RIGHT * 0.5), run_time=0.8)
        self.play(hero.animate.shift(RIGHT * 1.2), run_time=1.0, rate_func=linear)
        self.at(1)
        lock = plate(T("총액 = 일정", size=34, color=GOLD, weight=BOLD)).next_to(hero, UP, buff=0.3)
        self.play(FadeIn(lock, scale=1.2))
        self.at(2)
        w = Wallet(values=(5, 1, 2), total=8, height=2.6).move_to(RIGHT * 3.4 + UP * 0.2)
        self.play(FadeIn(w[0]), FadeIn(w.total_line), run_time=0.5)
        for bar, lab in zip(w.bars, w.labels):
            self.play(GrowFromEdge(bar, DOWN), FadeIn(lab), run_time=0.45)
        self.at(3)
        # 법무 1차 지적 2: 동전 이동은 '닫힌 관' 안에서만 (열린 개울은 분위기 배경)
        tube = VMobject(stroke_color=WHITE, stroke_width=4).set_points_as_corners(
            [[-6.2, 0.4, 0], [-2.6, 0.4, 0], [-1.6, 0.85, 0], [0.6, 0.85, 0]])
        tube2 = VMobject(stroke_color=WHITE, stroke_width=4).set_points_as_corners(
            [[-6.2, 2.0, 0], [-2.6, 2.0, 0], [-1.6, 1.55, 0], [0.6, 1.55, 0]])
        tlab = T("닫힌 관", size=22, color=INK).next_to(tube2, UP, buff=0.1).shift(LEFT * 2.5)
        self.play(FadeOut(lock), Create(tube), Create(tube2), FadeIn(tlab), run_time=0.6)
        self.play(hero.animate.move_to([-0.6, 1.2, 0]).scale(0.75), run_time=1.4, rate_func=rate_functions.ease_in_quad)
        coin = Circle(radius=0.12, color=GOLD, fill_color=GOLD, fill_opacity=1).move_to(w.bars[0].get_top())
        self.play(FadeIn(coin), run_time=0.2)
        self.play(coin.animate.move_to(w.bars[1].get_top()), Transform(w.bars, w.bars_for((2, 4, 2))), run_time=1.2)
        self.play(FadeOut(coin), Indicate(w.total_line, color=GOLD), run_time=0.6)


class S07(ChoigoScene):
    SCENE_ID = 7

    def build(self):
        # 법무 2차 지적 2-1: 개울 배경 위라도 압력 이야기는 '닫힌 관' 도식 안에서만 한다
        self.add(ai_badge(AI_GENERAL))
        lab = plate(T("닫힌 관(벤투리관) 그림", size=26, color=INK)).to_corner(UL, buff=0.4)
        y0, wide, thin = -1.45, 0.55, 0.22          # 관 중심 높이, 넓은 곳·좁은 곳 반폭
        xs = [-5.2, -1.6, -0.8, 0.8, 1.6, 5.2]
        half = [wide, wide, thin, thin, wide, wide]
        up_pts = [[x, y0 + h, 0] for x, h in zip(xs, half)]
        dn_pts = [[x, y0 - h, 0] for x, h in zip(xs, half)]
        top = VMobject(stroke_color=WHITE, stroke_width=4).set_points_as_corners(up_pts)
        bot = VMobject(stroke_color=WHITE, stroke_width=4).set_points_as_corners(dn_pts)
        water = Polygon(*up_pts, *dn_pts[::-1], stroke_width=0, fill_color=P_BLUE, fill_opacity=0.35)
        tube_h = 2.7
        t_wide = Rectangle(width=0.3, height=tube_h, stroke_color=INK, stroke_width=3)
        t_wide.move_to([-3.4, y0 + wide + tube_h / 2, 0])
        t_thin = Rectangle(width=0.3, height=tube_h, stroke_color=INK, stroke_width=3)
        t_thin.move_to([0.0, y0 + thin + tube_h / 2, 0])
        level = y0 + wide + tube_h * 0.8               # 흐르기 전 두 물기둥 높이
        def column(tube, base_y):
            c = Rectangle(width=0.26, height=level - base_y, stroke_width=0, fill_color=P_BLUE, fill_opacity=0.9)
            return c.move_to([tube.get_center()[0], (level + base_y) / 2, 0])
        c_wide, c_thin = column(t_wide, y0 + wide), column(t_thin, y0 + thin)
        sch = VGroup(top, bot, water, t_wide, t_thin)
        bg = plate(sch, opacity=0.5, buff=0.3)[0]
        self.play(FadeIn(lab), FadeIn(bg), Create(top), Create(bot), FadeIn(water),
                  Create(t_wide), Create(t_thin), FadeIn(c_wide), FadeIn(c_thin), run_time=0.9)
        flow = flow_arrow([xs[0] + 0.3, y0, 0], [xs[5] - 0.3, y0, 0], width=6)
        self.play(GrowArrow(flow), run_time=0.5)
        fast = T("빨라짐", size=24, color=K_ORANGE, weight=BOLD).next_to([0, y0 - thin, 0], DOWN, buff=0.12)
        self.play(FadeIn(fast), run_time=0.3)
        drop_to = (level - (y0 + thin)) * 0.45
        surf = Line(LEFT * 0.35, RIGHT * 0.35, color=WHITE, stroke_width=6).move_to([0, level, 0])
        self.add(surf)
        self.play(c_thin.animate.stretch_to_fit_height(drop_to, about_edge=DOWN),
                  surf.animate.move_to([0, y0 + thin + drop_to, 0]),
                  run_time=1.0, rate_func=rate_functions.ease_in_cubic)
        word = plate(T("쑥!", size=48, color=GOLD, weight=BOLD)).next_to(surf, RIGHT, buff=0.35)
        self.play(FadeIn(word, scale=1.5), run_time=0.3)
        self.at(1)
        w_wide = Wallet(values=(5, 1, 2), total=8, height=1.5, width=0.28, labels=False, title="넓은 곳")
        w_wide.next_to(t_wide, LEFT, buff=0.35).align_to(t_wide, UP)
        w_thin = Wallet(values=(5, 1, 2), total=8, height=1.5, width=0.28, labels=False, title="좁은 곳")
        w_thin.next_to(t_thin, RIGHT, buff=1.0).align_to(w_wide, UP)
        self.play(FadeIn(w_wide), FadeIn(w_thin), FadeOut(word), run_time=0.5)
        self.play(Transform(w_thin.bars, w_thin.bars_for((2, 4, 2))), run_time=0.8)
        same = DashedLine(w_wide.total_line.get_right(), w_thin.total_line.get_left(), color=GOLD, stroke_width=2)
        self.play(Create(same), FadeIn(plate(T("총액은 같다", size=24, color=GOLD)).next_to(w_thin, RIGHT, buff=0.2)),
                  run_time=0.6)


class S08(ChoigoScene):
    SCENE_ID = 8

    def build(self):
        self.add(ai_badge(AI_EXPERIMENT))
        # 종이 두 장 (영상 위 도식)
        left = Line(UP * 2.4, DOWN * 1.2, color=WHITE, stroke_width=5).shift(LEFT * 0.7)
        right = Line(UP * 2.4, DOWN * 1.2, color=WHITE, stroke_width=5).shift(RIGHT * 0.7)
        bg = plate(VGroup(left, right), opacity=0.35, buff=1.6)[0]
        self.play(FadeIn(bg), Create(left), Create(right), run_time=0.6)
        fast = flow_arrow(UP * 2.2, DOWN * 0.9, width=10)
        inside = push_arrow(LEFT * 0.2 + UP * 0.6, LEFT * 0.55 + UP * 0.6, width=4)
        inside2 = push_arrow(RIGHT * 0.2 + UP * 0.6, RIGHT * 0.55 + UP * 0.6, width=4)
        self.play(GrowArrow(fast), GrowArrow(inside), GrowArrow(inside2), run_time=0.8)
        self.at(1)
        out_l = push_arrow(LEFT * 2.6 + UP * 0.6, LEFT * 0.9 + UP * 0.6, width=14)
        out_r = push_arrow(RIGHT * 2.6 + UP * 0.6, RIGHT * 0.9 + UP * 0.6, width=14)
        l_in = plate(T("좁은 틈에서 빨라진 공기 → 덜 민다", size=24, color=K_ORANGE)).move_to(DOWN * 1.65)
        l_out = plate(T("바깥: 보통 공기 압력(대기압) 그대로", size=24, color=P_BLUE)).move_to(LEFT * 3.9 + UP * 1.6)
        note = T("정확히는 종이의 휘어짐, 공기가 종이 면을 따라 흐르는 효과도 함께 작용", size=18, color=MUTED)
        note.next_to(ai_badge(), DOWN, buff=0.15).align_to(ai_badge(), RIGHT)
        self.play(GrowArrow(out_l), GrowArrow(out_r), FadeIn(l_in), FadeIn(l_out), FadeIn(note), run_time=1.0)
        self.play(left.animate.shift(RIGHT * 0.3), right.animate.shift(LEFT * 0.3), run_time=0.8)
        self.at(2)
        title = plate(VGroup(T("베르누이의 원리", size=64, font=SERIF, weight=BOLD, color=GOLD),
                             T("흐름이 빨라지면, 압력이 낮아진다", size=34)).arrange(DOWN, buff=0.2), opacity=0.75, buff=0.45)
        self.play(FadeOut(VGroup(left, right, fast, inside, inside2, out_l, out_r, l_in, l_out, bg, note)),
                  FadeIn(title, scale=0.95), run_time=0.7)


# ── ④ 진짜 쉬운 설명 ───────────────────────────────────────
def airfoil(scale=1.0):
    pts = [[-2.2, 0, 0], [-1.6, 0.42, 0], [-0.4, 0.62, 0], [1.0, 0.38, 0], [2.3, 0, 0],
           [1.0, -0.08, 0], [-0.4, -0.12, 0], [-1.6, -0.12, 0], [-2.2, 0, 0]]
    w = VMobject(color=INK, stroke_width=4, fill_color=GREY_D, fill_opacity=0.5).set_points_smoothly(pts)
    return w.scale(scale)


class S09(ChoigoScene):
    SCENE_ID = 9

    def build(self):
        self.add(ai_badge(AI_GENERAL))
        self.show_chapter("④", "진짜 쉬운 설명", hold=0.3)
        self.at(1)
        wing = airfoil(1.2).move_to(UP * 0.3)
        head = plate(T("흔한 설명: 같은 시간 도착설", size=32, weight=BOLD)).move_to(UP * 2.5)
        bg = plate(wing, opacity=0.4, buff=0.9)[0]
        self.play(FadeIn(bg), FadeIn(head), Create(wing), run_time=0.8)
        top_path = ArcBetweenPoints(wing.get_left(), wing.get_right(), angle=-0.9)
        bot_path = ArcBetweenPoints(wing.get_left(), wing.get_right(), angle=0.25)
        top = DashedVMobject(top_path, num_dashes=24).set_color(K_ORANGE)
        bot = DashedVMobject(bot_path, num_dashes=24).set_color(P_BLUE)
        d1, d2 = Dot(wing.get_left(), color=K_ORANGE), Dot(wing.get_left(), color=P_BLUE)
        self.play(Create(top), Create(bot), FadeIn(d1), FadeIn(d2), run_time=0.6)
        self.play(MoveAlongPath(d1, top_path), MoveAlongPath(d2, bot_path), run_time=2.2, rate_func=linear)
        meet = T("동시에 만난다?", size=26, color=INK).next_to(wing.get_right(), RIGHT, buff=0.15)
        self.play(FadeIn(meet))
        self.at(2, 1.2)
        stamp = VGroup(Line(UL, DR), Line(UR, DL)).set_color(CORAL).set_stroke(width=14).scale(1.2).move_to(wing)
        self.play(GrowFromCenter(stamp), run_time=0.4)
        no = plate(T("틀렸습니다", size=44, color=CORAL, weight=BOLD)).move_to(DOWN * 1.6)
        self.play(FadeIn(no, scale=1.3), run_time=0.4)


class S10(ChoigoScene):
    SCENE_ID = 10

    def build(self):
        self.add(ai_badge(AI_GENERAL))
        cap = T("흐름 그림: H. 바빈스키(케임브리지대) 연기 펄스 실험을 바탕으로 그린 애니메이션", size=20, color=INK)
        cap.set_opacity(0.85).next_to(ai_badge(), DOWN, buff=0.12).align_to(ai_badge(), RIGHT)
        self.add(cap)
        wing = airfoil(1.2).move_to(UP * 0.2)
        bg = plate(wing, opacity=0.35, buff=1.0)[0]
        self.play(FadeIn(bg), Create(wing), run_time=0.6)
        top = ArcBetweenPoints(wing.get_left() + UP * 0.05, wing.get_right() + RIGHT * 1.6 + DOWN * 0.4, angle=-0.9)
        bot = ArcBetweenPoints(wing.get_left() + DOWN * 0.05, wing.get_right() + RIGHT * 1.6 + DOWN * 0.4, angle=0.2)
        d1, d2 = Dot(color=K_ORANGE, radius=0.12), Dot(color=P_BLUE, radius=0.12)
        t1, t2 = ValueTracker(0), ValueTracker(0)
        d1.add_updater(lambda m: m.move_to(top.point_from_proportion(t1.get_value())))
        d2.add_updater(lambda m: m.move_to(bot.point_from_proportion(t2.get_value())))
        self.add(d1, d2)
        self.play(t1.animate.set_value(1.0), t2.animate.set_value(0.6), run_time=2.0, rate_func=linear)
        first = plate(T("위쪽이 먼저 도착", size=30, color=K_ORANGE, weight=BOLD)).next_to(d1, UP, buff=0.3)
        self.play(FadeIn(first, scale=1.2))
        self.at(1)
        down = push_arrow(wing.get_right() + RIGHT * 0.3 + UP * 0.2, wing.get_right() + RIGHT * 1.2 + DOWN * 1.4, color=WHITE, width=12)
        upf = push_arrow(wing.get_center() + DOWN * 0.1, wing.get_center() + UP * 1.6, color=GOLD, width=12)
        self.play(GrowArrow(down), run_time=0.6)
        self.play(GrowArrow(upf), FadeIn(T("반작용", size=26, color=GOLD).next_to(upf, LEFT, buff=0.15)), run_time=0.6)
        self.at(2)
        n = plate(VGroup(T("뉴턴", size=30, weight=BOLD), T("공기를 아래로", size=24)).arrange(DOWN, buff=0.08)).move_to(LEFT * 4.3 + DOWN * 1.6)
        b = plate(VGroup(T("베르누이", size=30, weight=BOLD), T("날개 위 압력 ↓", size=24, color=P_BLUE)).arrange(DOWN, buff=0.08)).move_to(RIGHT * 4.3 + DOWN * 1.6)
        rib = plate(T("같은 흐름의 두 얼굴", size=28, color=GOLD)).move_to(DOWN * 1.6)
        self.play(FadeIn(n, shift=RIGHT * 0.2), FadeIn(b, shift=LEFT * 0.2), run_time=0.6)
        self.play(FadeIn(rib, scale=1.2), run_time=0.5)


# ── ⑤ 공식 풀어보기 ────────────────────────────────────────
class S11(ChoigoScene):
    SCENE_ID = 11

    def build(self):
        self.show_chapter("⑤", "공식 풀어보기", hold=0.3)
        w = Wallet(values=(5, 1, 2), total=8, height=1.8, width=0.45, labels=False).move_to(LEFT * 5.2 + UP * 1.7)
        self.play(FadeIn(w, shift=RIGHT * 0.5), run_time=0.6)
        self.at(1)
        eq = M("P", "+", r"\tfrac{1}{2}\rho v^2", "+", r"\rho g h", "=", r"\text{const}", size=72).move_to(DOWN * 0.3)
        eq[0].set_color(P_BLUE)
        eq[2].set_color(K_ORANGE)
        eq[4].set_color(H_GRAY)
        eq[6].set_color(GOLD)
        names = VGroup(T("압력", size=24, color=P_BLUE).next_to(eq[0], DOWN, buff=0.25),
                       T("움직임의 에너지", size=24, color=K_ORANGE).next_to(eq[2], DOWN, buff=0.25),
                       T("높이의 에너지", size=24, color=H_GRAY).next_to(eq[4], DOWN, buff=0.25),
                       T("일정", size=24, color=GOLD).next_to(eq[6], DOWN, buff=0.25))
        bg = plate(VGroup(eq, names), opacity=0.6, buff=0.35)[0]
        self.play(FadeIn(bg), run_time=0.3)
        for k, nm in zip((0, 2, 4, 6), names):
            self.play(Write(eq[k]), FadeIn(nm), *( [Write(eq[k - 1])] if k else []), run_time=0.55)
        hint = T("ρ 밀도 · v 속력 · g 중력 가속도 · h 높이", size=22, color=MUTED).next_to(bg, DOWN, buff=0.15)
        memo = plate(T("속력 2배 → 4배", size=22, color=K_ORANGE)).next_to(eq[2], UP, buff=0.35)
        self.play(FadeIn(hint), FadeIn(memo), run_time=0.5)
        self.at(2)
        cond = plate(T("조건: 마찰 없음 · 같은 흐름선 · 흐름이 일정 · 밀도 일정(물, 느린 공기)", size=24, color=GOLD)).move_to(DOWN * 2.05)
        self.play(FadeOut(hint), FadeIn(cond, shift=UP * 0.2))


class S12(ChoigoScene):
    SCENE_ID = 12

    def build(self):
        s1 = plate(VGroup(T("넓은 곳", size=26), M(r"v = 1\,\mathrm{m/s}", size=44),
                          T("→  단면 넓이 ½ →", size=26, color=MUTED),
                          T("좁은 곳", size=26), M(r"v = 2\,\mathrm{m/s}", size=44, color=K_ORANGE))
                   .arrange(RIGHT, buff=0.3)).move_to(UP * 2.6)
        self.play(FadeIn(s1, shift=DOWN * 0.2), run_time=0.7)
        self.at(1)
        s2 = plate(VGroup(M(r"\tfrac12 \times 1000 \times 1^2 = 500", size=38),
                          M(r"\;\to\;", size=38),
                          M(r"\tfrac12 \times 1000 \times 2^2 = 2000\ \mathrm{J/m^3}", size=38, color=K_ORANGE)).arrange(RIGHT, buff=0.15))
        s2.move_to(UP * 1.4)
        rho = T("물의 밀도 ρ = 1000 · 움직임의 에너지(물 1m³당)", size=20, color=MUTED).next_to(s2, DOWN, buff=0.08)
        self.play(FadeIn(s2), FadeIn(rho), run_time=0.8)
        w = Wallet(values=(5, 0.5, 0), total=5.5, height=1.9, width=0.38, labels=False).move_to(LEFT * 4.6 + DOWN * 0.6)
        self.play(FadeIn(w), run_time=0.4)
        self.at(2)
        coin = Circle(radius=0.12, color=GOLD, fill_color=GOLD, fill_opacity=1).move_to(w.bars[0].get_top())
        self.play(FadeIn(coin), run_time=0.2)
        self.play(coin.animate.move_to(w.bars[1].get_top()), Transform(w.bars, w.bars_for((3.5, 2.0, 0))), run_time=1.0)
        s3 = plate(VGroup(M(r"P", size=48, color=P_BLUE), M(r"1500\,\mathrm{Pa}\ \downarrow", size=48)).arrange(RIGHT, buff=0.2))
        s3.move_to(DOWN * 0.3)
        pa = T("Pa(파스칼) = 압력의 단위 · J/m³와 같다", size=20, color=MUTED).next_to(s3, DOWN, buff=0.08)
        self.play(FadeOut(coin), FadeIn(s3, scale=1.2), FadeIn(pa), run_time=0.6)
        self.at(3)
        t1 = Rectangle(width=0.35, height=1.8, stroke_color=INK, stroke_width=3)
        t2 = t1.copy()
        tubes = VGroup(t1, t2).arrange(RIGHT, buff=0.8).move_to(RIGHT * 4.6 + DOWN * 0.5)
        f1 = Rectangle(width=0.3, height=1.5, stroke_width=0, fill_color=P_BLUE, fill_opacity=0.9).align_to(t1, DOWN).move_to(t1, coor_mask=[1, 0, 0])
        f2 = Rectangle(width=0.3, height=0.9, stroke_width=0, fill_color=P_BLUE, fill_opacity=0.9).align_to(t2, DOWN).move_to(t2, coor_mask=[1, 0, 0])
        br = BraceBetweenPoints(f1.get_top() + RIGHT * 0.8, [f1.get_top()[0] + 0.8, f2.get_top()[1], 0], RIGHT, color=GOLD)
        lab = T("약 15cm", size=24, color=GOLD, weight=BOLD).next_to(br, RIGHT, buff=0.08)
        chk = M(r"h = \frac{1500}{1000 \times 9.8} \approx 0.15\,\mathrm{m}", size=30).next_to(tubes, DOWN, buff=0.25)
        bg = plate(VGroup(tubes, br, lab, chk), opacity=0.55, buff=0.25)[0]
        self.play(FadeIn(bg), Create(tubes), GrowFromEdge(f1, DOWN), GrowFromEdge(f2, DOWN), run_time=0.8)
        self.play(GrowFromCenter(br), FadeIn(lab), FadeIn(chk), run_time=0.6)


# ── ⑥ 오늘의 한 줄 ─────────────────────────────────────────
class S13(ChoigoScene):
    SCENE_ID = 13

    def build(self):
        self.add(ai_badge(AI_GENERAL))
        tag = T("오늘의 한 줄", size=30, color=GOLD, font=SERIF).to_edge(UP, buff=0.5)
        card = plate(T("빨라진 공기는, 덜 민다", size=56, font=SERIF, weight=BOLD, color=GOLD), opacity=0.65, buff=0.4)
        card.move_to(UP * 1.6)
        self.play(FadeIn(tag), FadeIn(card, scale=0.95), run_time=0.8)
        self.at(1)
        circ = Circle(radius=0.9, color=WHITE, stroke_width=3).move_to(RIGHT * 4.8 + DOWN * 0.3)
        sheets = VGroup(ArcBetweenPoints(UP * 0.6 + LEFT * 0.25, DOWN * 0.6 + LEFT * 0.05, angle=0.4),
                        ArcBetweenPoints(UP * 0.6 + RIGHT * 0.25, DOWN * 0.6 + RIGHT * 0.05, angle=-0.4)).set_color(WHITE)
        sheets.set_stroke(width=4).move_to(circ)
        mini_lab = T("실제 실험 촬영 아님", size=16, color=INK).next_to(circ, DOWN, buff=0.08)
        mini = VGroup(Circle(radius=0.9, stroke_width=0, fill_color=BLACK, fill_opacity=0.6).move_to(circ), circ, sheets, mini_lab)
        self.play(FadeIn(mini, scale=0.8), run_time=0.5)
        self.wait(1.8)
        self.play(FadeOut(mini, scale=0.8), run_time=0.4)
        self.at(2)
        nxt = plate(VGroup(T("다음 편", size=24, color=MUTED), T("연속 방정식", size=48, font=SERIF, weight=BOLD),
                           T("좁은 곳에서 물은 왜 빨라질까?", size=28)).arrange(DOWN, buff=0.12), buff=0.35).move_to(DOWN * 0.6)
        self.play(FadeIn(nxt, shift=UP * 0.2), run_time=0.6)
        self.at(3)
        self.play(FadeOut(VGroup(nxt, card, tag)), run_time=0.4)
        logo = plate(VGroup(T("최고의 공부", size=88, font=SERIF, weight=BOLD, color=GOLD),
                            T("하루에 개념 하나", size=32)).arrange(DOWN, buff=0.25), opacity=0.6, buff=0.45)
        self.play(FadeIn(logo, scale=0.9), run_time=0.7)
