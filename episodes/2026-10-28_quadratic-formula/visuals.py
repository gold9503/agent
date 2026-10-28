"""근의 공식 편 장면 (Manim). 장면 번호는 03_storyboard.json의 id와 같다."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from choigo_style import *  # noqa: E402,F401,F403

# ── 알 콰리즈미의 정사각형 (x = 3 비율 그대로) ─────────────────
U = 0.62                   # 수 1의 길이
S = 3 * U                  # x
W = 2.5 * U                # 조각 폭 2.5
C = np.array([-3.0, 0.35, 0])
RIGHT_PANEL = np.array([3.6, 0.6, 0])


def x_square():
    sq = Square(S, color=TEAL, fill_color=TEAL, fill_opacity=0.25, stroke_width=4).move_to(C)
    lab = M("x^2", size=60, color=INK).move_to(C)
    top = M("x", size=44, color=TEAL).next_to(sq, UP, buff=0.15)
    left = M("x", size=44, color=TEAL).next_to(sq, LEFT, buff=0.15)
    return sq, lab, VGroup(top, left)


def side_pieces():
    """네 변에 붙는 x × 2.5 직사각형 (위, 아래, 왼쪽, 오른쪽)."""
    style = dict(color=GOLD, fill_color=GOLD, fill_opacity=0.22, stroke_width=3)
    top = Rectangle(width=S, height=W, **style).move_to(C + UP * (S + W) / 2)
    bot = Rectangle(width=S, height=W, **style).move_to(C + DOWN * (S + W) / 2)
    lft = Rectangle(width=W, height=S, **style).move_to(C + LEFT * (S + W) / 2)
    rgt = Rectangle(width=W, height=S, **style).move_to(C + RIGHT * (S + W) / 2)
    return VGroup(top, bot, lft, rgt)


def corners(filled=True):
    d = (S + W) / 2
    sqs = VGroup(*[
        Square(W, color=CORAL, stroke_width=3,
               fill_color=CORAL, fill_opacity=0.45 if filled else 0).move_to(C + d * (sx * RIGHT + sy * UP))
        for sx, sy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]
    ])
    return sqs


def full_figure():
    sq, lab, xl = x_square()
    return VGroup(sq, lab, side_pieces(), corners())


# ── ① 오프닝 질문 ──────────────────────────────────────────
class S01(ChoigoScene):
    SCENE_ID = 1

    def build(self):
        f = M(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", size=96, color=GOLD)
        self.play(Write(f), run_time=3.2)
        self.at(1)
        echoes = VGroup(*[
            M(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", size=s, color=MUTED).set_opacity(o).move_to(p)
            for s, o, p in [(40, .25, [-4.6, 2.6, 0]), (34, .2, [4.4, 2.3, 0]), (44, .18, [-4.2, -1.9, 0]),
                            (30, .22, [4.8, -1.6, 0]), (28, .15, [0.2, 3.1, 0])]
        ])
        self.play(LaggedStart(*[FadeIn(e, scale=1.2) for e in echoes], lag_ratio=0.3), run_time=2.5)
        tag = T("외우는 주문?", size=40, color=INK).next_to(f, DOWN, buff=0.6)
        self.play(FadeIn(tag, shift=UP * 0.2))


class S02(ChoigoScene):
    SCENE_ID = 2

    def build(self):
        f = M(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", size=96, color=GOLD)
        self.add(f)
        q = T("?", size=200, color=INK, font=SERIF, weight=BOLD).move_to(RIGHT * 4.6 + UP * 0.4)
        self.play(f.animate.shift(LEFT * 1.2).set_opacity(0.5), FadeIn(q, scale=0.5), run_time=1.0)
        self.at(1)
        self.play(FadeOut(f), FadeOut(q), run_time=0.6)
        t1 = T("근의 공식은", size=56, font=SERIF, color=MUTED)
        t2 = T("누가, 왜 만들었을까?", size=84, font=SERIF, weight=BOLD)
        g = VGroup(t1, t2).arrange(DOWN, buff=0.4).shift(UP * 0.5)
        brand = T("최고의 공부", size=28, color=GOLD, font=SERIF).to_edge(UP, buff=0.5)
        self.play(FadeIn(t1, shift=UP * 0.2), FadeIn(t2, shift=UP * 0.2), FadeIn(brand), run_time=0.8)


# ── ② 시대 속으로 ──────────────────────────────────────────
class S03(ChoigoScene):
    SCENE_ID = 3

    def build(self):
        card = chapter_card("②", "시대 속으로").shift(UP * 1.6)
        self.play(FadeIn(card[0], shift=UP * 0.2), Create(card[1]), run_time=0.8)
        year = Integer(2026, group_with_commas=False, font_size=120, color=GOLD)
        unit = T("년", size=60, color=GOLD, font=SERIF)
        pre = T("서기", size=44, color=MUTED, font=SERIF)
        row = VGroup(pre, year, unit).arrange(RIGHT, buff=0.3, aligned_edge=DOWN).shift(DOWN * 0.4)
        unit.add_updater(lambda m: m.next_to(year, RIGHT, buff=0.15, aligned_edge=DOWN))
        self.add(row)
        self.play(ChangeDecimalToValue(year, 820), run_time=2.2, rate_func=rate_functions.ease_in_out_cubic)
        about = T("경", size=60, color=GOLD, font=SERIF).next_to(unit, RIGHT, buff=0.1, aligned_edge=DOWN)
        self.play(FadeIn(about))
        self.at(1)
        city = T("바그다드", size=72, font=SERIF, weight=BOLD).next_to(row, DOWN, buff=0.6)
        self.play(FadeIn(city, shift=UP * 0.3))


class S04(ChoigoScene):
    SCENE_ID = 4

    def build(self):
        pts = {"그리스": np.array([-5.0, 1.6, 0]), "바그다드": np.array([0.2, 0.3, 0]), "인도": np.array([4.9, -1.2, 0])}
        dots, labels = VGroup(), VGroup()
        for name, p in pts.items():
            big = name == "바그다드"
            d = Dot(p, radius=0.16 if big else 0.11, color=GOLD if big else TEAL)
            halo = Circle(radius=0.38, color=GOLD, stroke_width=2).move_to(p) if big else VMobject()
            dots.add(VGroup(halo, d))
            labels.add(T(name, size=40 if big else 34, color=INK if big else MUTED).next_to(d, DOWN, buff=0.25))
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.2),
                  LaggedStart(*[FadeIn(l) for l in labels], lag_ratio=0.2), run_time=1.6)
        big = T("세계에서 가장 큰 도시 가운데 하나", size=30, color=MUTED).next_to(dots[1], UP, buff=0.6)
        self.play(FadeIn(big, shift=UP * 0.2))
        self.at(1)
        # 지혜의 집 (돔 지붕)
        base = Rectangle(width=1.4, height=0.7, color=GOLD, stroke_width=3).next_to(dots[1], UP, buff=0.55)
        dome = Arc(radius=0.7, start_angle=0, angle=PI, color=GOLD, stroke_width=3).next_to(base, UP, buff=0)
        house = VGroup(base, dome)
        name = T("지혜의 집", size=36, color=GOLD, weight=BOLD).next_to(house, UP, buff=0.2)
        self.play(FadeOut(big), Create(house), FadeIn(name), run_time=1.2)
        self.at(1, 2.2)
        arrows, books = VGroup(), VGroup()
        for src in ("그리스", "인도"):
            a = CurvedArrow(pts[src] + (RIGHT if src == "그리스" else LEFT) * 0.3,
                            pts["바그다드"] + (LEFT if src == "그리스" else RIGHT) * 0.4,
                            angle=-PI / 5 if src == "그리스" else -PI / 5, color=TEAL, stroke_width=3)
            arrows.add(a)
            for k in range(3):
                b = Rectangle(width=0.26, height=0.34, color=INK, fill_color=INK, fill_opacity=0.8, stroke_width=1)
                books.add(b.move_to(a.point_from_proportion(0.25 + 0.25 * k)))
        self.play(Create(arrows), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(b, scale=0.3) for b in books], lag_ratio=0.15), run_time=1.5)
        tr = T("그리스어 · 산스크리트어 → 아랍어", size=30, color=MUTED).move_to(DOWN * 2.2)
        self.play(FadeIn(tr))


class S05(ChoigoScene):
    SCENE_ID = 5

    def build(self):
        name = T("알 콰리즈미", size=80, font=SERIF, weight=BOLD)
        life = T("780년경 ~ 850년경 · 바그다드", size=32, color=MUTED)
        card = VGroup(name, life).arrange(DOWN, buff=0.35)
        self.play(Write(name), run_time=1.4)
        self.play(FadeIn(life, shift=UP * 0.2))
        self.at(1)
        self.play(card.animate.scale(0.7).to_edge(UP, buff=0.6))
        self.at(2)
        # 유산 나누기: 셋으로 나뉜 원
        pie = VGroup(*[AnnularSector(inner_radius=0, outer_radius=0.85, angle=TAU / 3, start_angle=k * TAU / 3,
                                     color=c, fill_opacity=0.55, stroke_width=2, stroke_color=BG)
                       for k, c in enumerate([GOLD, TEAL, CLAY])])
        # 땅 넓이: 격자 사각형
        land = VGroup(Rectangle(width=1.9, height=1.4, color=TEAL, stroke_width=3),
                      *[Line([-0.95 + 0.475 * i, -0.7, 0], [-0.95 + 0.475 * i, 0.7, 0], color=TEAL,
                             stroke_width=1, stroke_opacity=0.5) for i in range(1, 4)],
                      *[Line([-0.95, -0.7 + 0.467 * j, 0], [0.95, -0.7 + 0.467 * j, 0], color=TEAL,
                             stroke_width=1, stroke_opacity=0.5) for j in range(1, 3)])
        # 거래: 저울
        beam = Line(LEFT, RIGHT, color=GOLD, stroke_width=4)
        post = Line(DOWN * 0.9, ORIGIN, color=GOLD, stroke_width=4)
        pans = VGroup(*[Arc(radius=0.32, start_angle=PI, angle=PI, color=GOLD, stroke_width=3)
                        .move_to(beam.get_end() * s + DOWN * 0.45) for s in (1, -1)])
        strings = VGroup(*[Line(beam.get_end() * s, beam.get_end() * s + DOWN * 0.3, color=GOLD, stroke_width=2)
                           for s in (1, -1)])
        scale_icon = VGroup(beam, post, pans, strings)
        icons = VGroup(pie, land, scale_icon).arrange(RIGHT, buff=1.9).shift(DOWN * 0.6)
        caps = VGroup(*[T(s, size=34).next_to(i, DOWN, buff=0.35)
                        for s, i in zip(["유산 나누기", "땅 넓이 재기", "거래 계산"], icons)])
        self.play(LaggedStart(*[AnimationGroup(FadeIn(i, scale=0.6), FadeIn(c)) for i, c in zip(icons, caps)],
                              lag_ratio=0.45), run_time=2.6)


class S06(ChoigoScene):
    SCENE_ID = 6

    def build(self):
        land = Rectangle(width=3 * U * 1.1, height=13 * U * 0.42, color=TEAL, fill_color=TEAL,
                         fill_opacity=0.15, stroke_width=3).move_to(LEFT * 3.6 + UP * 0.4)
        w = M("x", size=44, color=TEAL).next_to(land, DOWN, buff=0.15)
        h = M("x + 10", size=44, color=TEAL).next_to(land, LEFT, buff=0.15)
        area = T("넓이 39", size=36).move_to(land)
        self.play(Create(land), FadeIn(w), FadeIn(h), run_time=1.2)
        self.play(FadeIn(area))
        e1 = M("x", "(", "x + 10", ")", "=", "39", size=72).move_to(RIGHT * 2.6 + UP * 1.0)
        self.play(Write(e1), run_time=1.4)
        e2 = M("x^2", "+", "10x", "=", "39", size=80).move_to(RIGHT * 2.6 + DOWN * 0.3)
        e2[0].set_color(CORAL)
        self.play(TransformFromCopy(e1, e2), run_time=1.4)
        self.play(Indicate(e2[0], color=CORAL, scale_factor=1.4), run_time=1.2)
        self.at(1)
        lab = T("이차방정식", size=56, color=GOLD, font=SERIF, weight=BOLD).next_to(e2, DOWN, buff=0.7)
        sub = T("가장 높은 차수가 2인 방정식", size=28, color=MUTED).next_to(lab, DOWN, buff=0.2)
        self.play(FadeIn(lab, shift=UP * 0.2), FadeIn(sub))


def timeline():
    line = Line(LEFT * 6.2, RIGHT * 6.2, color=MUTED, stroke_width=3).shift(DOWN * 0.3)
    xs = {"bc": -4.4, "628": 0.0, "820": 4.4}
    ticks = VGroup(*[Line(UP * 0.18, DOWN * 0.18, color=MUTED, stroke_width=3).move_to([x, -0.3, 0])
                     for x in xs.values()])
    return line, xs, ticks


def clay_tablet():
    tab = RoundedRectangle(corner_radius=0.18, width=1.5, height=1.9, color=CLAY,
                           fill_color=CLAY, fill_opacity=0.55, stroke_width=3)
    wedges = VGroup()
    rng = np.random.default_rng(7)
    for r in range(5):
        for c in range(4):
            if rng.random() < 0.8:
                t = Triangle(color="#5B3A22", fill_color="#5B3A22", fill_opacity=1, stroke_width=0).scale(0.07)
                t.rotate(PI / 2 * rng.integers(0, 4))
                wedges.add(t.move_to(tab.get_corner(UL) + np.array([0.3 + 0.3 * c, -0.32 - 0.31 * r, 0])))
    return VGroup(tab, wedges)


class S07(ChoigoScene):
    SCENE_ID = 7

    def build(self):
        line, xs, ticks = timeline()
        self.play(Create(line), FadeIn(ticks), run_time=1.0)
        y0 = T("기원전 1800년경", size=30, color=GOLD).next_to(ticks[0], DOWN, buff=0.3)
        n0 = T("바빌로니아 점토판", size=30).next_to(y0, DOWN, buff=0.15)
        tab = clay_tablet().next_to(ticks[0], UP, buff=0.4)
        self.play(FadeIn(tab, shift=DOWN * 0.3), FadeIn(y0), FadeIn(n0), run_time=1.2)
        self.at(1)
        steps = VGroup(*[T(s, size=24, color=INK) for s in ["① 반으로 나눈다", "② 제곱한다", "③ 더한다", "④ 제곱근을 구한다"]])
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.12).next_to(tab, RIGHT, buff=0.35)
        tag = T("문제별 '계산 순서'", size=26, color=MUTED).next_to(steps, UP, buff=0.2, aligned_edge=LEFT)
        self.play(FadeIn(tag), LaggedStart(*[FadeIn(s, shift=RIGHT * 0.2) for s in steps], lag_ratio=0.3), run_time=2.0)
        self.at(2)
        self.play(FadeOut(steps), FadeOut(tag), run_time=0.5)
        y1 = T("628년", size=30, color=GOLD).next_to(ticks[1], DOWN, buff=0.3)
        n1 = T("인도 · 브라마굽타", size=30).next_to(y1, DOWN, buff=0.15)
        verse = VGroup(*[Line(LEFT * 0.7, RIGHT * (0.7 - 0.25 * (k % 2)), color=INK, stroke_width=3)
                         for k in range(4)]).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        frame = SurroundingRectangle(verse, color=TEAL, buff=0.25, corner_radius=0.1)
        rule = VGroup(frame, verse).next_to(ticks[1], UP, buff=0.4)
        cap = T("말로 쓴 규칙", size=26, color=TEAL).next_to(rule, UP, buff=0.15)
        self.play(FadeIn(rule, shift=DOWN * 0.3), FadeIn(cap), FadeIn(y1), FadeIn(n1), run_time=1.2)
        self.wait(1.5)
        y2 = T("820년경", size=30, color=GOLD).next_to(ticks[2], DOWN, buff=0.3)
        n2 = T("바그다드 · 알 콰리즈미", size=30).next_to(y2, DOWN, buff=0.15)
        self.play(FadeIn(VGroup(y2, n2), shift=UP * 0.2), Flash(ticks[2], color=GOLD), run_time=1.0)


class S08(ChoigoScene):
    SCENE_ID = 8

    def build(self):
        line, xs, ticks = timeline()
        y2 = T("820년경", size=30, color=GOLD).next_to(ticks[2], DOWN, buff=0.3)
        n2 = T("바그다드 · 알 콰리즈미", size=30).next_to(y2, DOWN, buff=0.15)
        self.add(line, ticks, y2, n2)
        self.play(VGroup(line, ticks).animate.set_opacity(0.3), run_time=0.8)
        self.at(1)
        a = T("이 문제는 이렇게 푼다", size=40, color=MUTED).move_to(UP * 2.2 + LEFT * 2.6)
        arrow = Arrow(LEFT, RIGHT, color=GOLD).next_to(a, RIGHT, buff=0.3)
        b = T("왜?", size=110, color=GOLD, font=SERIF, weight=BOLD).next_to(arrow, RIGHT, buff=0.4)
        self.play(FadeIn(a), run_time=0.6)
        self.play(GrowArrow(arrow), FadeIn(b, scale=1.5), run_time=1.0)
        pic = T("→ 그림으로 보여주기", size=36).next_to(VGroup(a, b), DOWN, buff=0.5)
        self.play(FadeIn(pic, shift=UP * 0.2))


# ── ③ 개념의 탄생 ──────────────────────────────────────────
class S09(ChoigoScene):
    SCENE_ID = 9

    def build(self):
        self.show_chapter("③", "개념의 탄생", hold=1.0)
        self.at(1)
        words = T("어떤 수의 제곱에, 그 수의 10배를 더했더니 39가 되었다.", size=40, font=SERIF).shift(UP * 1.0)
        self.play(AddTextLetterByLetter(words), run_time=2.6)
        self.at(2)
        q = T("그 수는 무엇인가?", size=44, font=SERIF, color=GOLD).next_to(words, DOWN, buff=0.4)
        self.play(FadeIn(q, shift=UP * 0.2))
        eq = M("x^2", "+", "10x", "=", "39", size=96).shift(DOWN * 1.3)
        self.play(Write(eq), run_time=1.5)
        note = T("오늘날의 기호로 쓰면", size=26, color=MUTED).next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(note))


class S10(ChoigoScene):
    SCENE_ID = 10

    def build(self):
        words = T("어떤 수의 제곱에, 그 수의 10배를 더했더니 39", size=36, font=SERIF).shift(UP * 1.0)
        nox = VGroup(M("x", size=72, color=MUTED), T("기호 없음", size=32, color=MUTED)).arrange(RIGHT, buff=0.4)
        nox.next_to(words, DOWN, buff=0.7)
        cross = Cross(nox[0], stroke_color=CORAL, stroke_width=6)
        self.play(FadeIn(nox), Create(cross), run_time=1.0)
        self.at(1)
        self.play(FadeIn(words, shift=UP * 0.2), run_time=1.0)
        self.at(2)
        self.play(FadeOut(VGroup(words, nox, cross)), run_time=0.6)
        self.at(3)
        sq, lab, xl = x_square()
        self.play(Create(sq), run_time=1.4)
        self.play(FadeIn(xl), run_time=0.6)
        self.at(3, 2.6)
        self.play(Write(lab))
        eq = M("x^2", "+", "10x", "=", "39", size=60).move_to(RIGHT_PANEL + UP * 1.8)
        self.play(FadeIn(eq))
        self.play(Indicate(eq[0], color=TEAL))


class S11(ChoigoScene):
    SCENE_ID = 11

    def build(self):
        sq, lab, xl = x_square()
        eq = M("x^2", "+", "10x", "=", "39", size=60).move_to(RIGHT_PANEL + UP * 1.8)
        self.add(sq, lab, xl, eq)
        self.play(Indicate(eq[2], color=GOLD))
        # 10x 직사각형: 높이 x, 길이 10 (오른쪽 패널에 축소해서)
        k = 0.42
        big = Rectangle(width=10 * U * k, height=S * k, color=GOLD, fill_color=GOLD, fill_opacity=0.22,
                        stroke_width=3).move_to(RIGHT_PANEL + DOWN * 0.1)
        bl = M("10", size=36, color=GOLD).next_to(big, DOWN, buff=0.12)
        hl = M("x", size=36, color=GOLD).next_to(big, LEFT, buff=0.12)
        self.play(TransformFromCopy(eq[2], big), FadeIn(bl), FadeIn(hl), run_time=1.4)
        self.at(1)
        cuts = VGroup(*[DashedLine(big.get_corner(DL) + RIGHT * big.width * i / 4,
                                   big.get_corner(UL) + RIGHT * big.width * i / 4, color=INK)
                        for i in (1, 2, 3)])
        self.play(Create(cuts), run_time=0.8)
        pieces_src = VGroup(*[Rectangle(width=big.width / 4, height=big.height, color=GOLD, fill_color=GOLD,
                                        fill_opacity=0.22, stroke_width=3)
                              .move_to(big.get_left() + RIGHT * big.width * (i + 0.5) / 4) for i in range(4)])
        self.add(pieces_src)
        self.remove(big, cuts)
        targets = side_pieces()
        self.play(FadeOut(bl), FadeOut(hl), FadeOut(xl),
                  LaggedStart(*[ReplacementTransform(p, t) for p, t in zip(pieces_src, targets)], lag_ratio=0.25),
                  run_time=2.6)
        self.at(2)
        labs = VGroup(
            M("2.5", size=34, color=GOLD).move_to(targets[0]),
            M("2.5", size=34, color=GOLD).move_to(targets[1]),
            M("2.5", size=34, color=GOLD).move_to(targets[2]).rotate(PI / 2),
            M("2.5", size=34, color=GOLD).move_to(targets[3]).rotate(PI / 2),
        )
        self.play(LaggedStart(*[FadeIn(l) for l in labs], lag_ratio=0.2), run_time=1.0)
        note = M(r"10 \div 4 = 2.5", size=48, color=GOLD).move_to(RIGHT_PANEL + DOWN * 0.1)
        self.play(FadeIn(note, shift=UP * 0.2))


class S12(ChoigoScene):
    SCENE_ID = 12

    def build(self):
        sq, lab, xl = x_square()
        pieces = side_pieces()
        eq = M("x^2", "+", "10x", "=", "39", size=60).move_to(RIGHT_PANEL + UP * 1.8)
        self.add(sq, lab, pieces, eq)
        empty = corners(filled=False)
        for e in empty:
            e.set_stroke(CORAL, opacity=0.9).set_style(stroke_width=3)
        dashed = VGroup(*[DashedVMobject(e, num_dashes=16) for e in empty])
        self.play(Create(dashed), run_time=1.0)
        self.play(*[Indicate(d, color=CORAL, scale_factor=1.15) for d in dashed], run_time=1.2)
        self.at(1)
        filled = corners(filled=True)
        self.play(LaggedStart(*[FadeIn(f, scale=0.6) for f in filled], lag_ratio=0.25), FadeOut(dashed), run_time=1.6)
        cl = VGroup(*[M("2.5^2", size=26, color=INK).move_to(f) for f in filled])
        self.play(FadeIn(cl))
        calc = M(r"4 \times 2.5^2", "=", "25", size=60).move_to(RIGHT_PANEL + DOWN * 0.1)
        calc[2].set_color(CORAL)
        self.play(Write(calc), run_time=1.4)


class S13(ChoigoScene):
    SCENE_ID = 13

    def build(self):
        fig = full_figure()
        eq = M("x^2", "+", "10x", "=", "39", size=60).move_to(RIGHT_PANEL + UP * 1.8)
        self.add(fig, eq)
        outline = Square(S + 2 * W, color=GOLD, stroke_width=7).move_to(C)
        self.play(Create(outline), run_time=1.4)
        self.at(1)
        e2 = M("39", "+", "25", "=", "64", size=72).move_to(RIGHT_PANEL + UP * 0.5)
        e2[2].set_color(CORAL)
        e2[4].set_color(GOLD)
        self.play(Write(e2), run_time=1.4)
        area = M("64", size=96, color=GOLD).move_to(C)
        self.play(FadeOut(fig[1]), FadeIn(area), fig[0].animate.set_fill(opacity=0.1),
                  fig[2].animate.set_fill(opacity=0.08), fig[3].animate.set_fill(opacity=0.15))
        self.at(2)
        e3 = VGroup(T("한 변", size=40), M(r"= \sqrt{64} = 8", size=60)).arrange(RIGHT, buff=0.2)
        e3.move_to(RIGHT_PANEL + DOWN * 0.7)
        brace = Brace(outline, LEFT, color=GOLD, buff=0.08)
        b8 = M("8", size=44, color=GOLD).next_to(brace, LEFT, buff=0.08)
        self.play(FadeIn(e3), GrowFromCenter(brace), FadeIn(b8), run_time=1.2)
        self.at(3)
        top = outline.get_top() + UP * 0.12
        x0 = outline.get_left()[0]
        segs = VGroup(
            BraceBetweenPoints([x0, top[1], 0], [x0 + W, top[1], 0], UP, color=CORAL),
            BraceBetweenPoints([x0 + W, top[1], 0], [x0 + W + S, top[1], 0], UP, color=TEAL),
            BraceBetweenPoints([x0 + W + S, top[1], 0], [x0 + 2 * W + S, top[1], 0], UP, color=CORAL),
        )
        sl = VGroup(M("2.5", size=32, color=CORAL), M("x", size=36, color=TEAL), M("2.5", size=32, color=CORAL))
        for l, s in zip(sl, segs):
            l.next_to(s, UP, buff=0.05)
        self.play(FadeIn(segs), FadeIn(sl), run_time=1.0)
        e4 = M("2.5", "+", "x", "+", "2.5", "=", "8", size=56).move_to(RIGHT_PANEL + DOWN * 1.8)
        self.play(Write(e4), run_time=1.2)
        e5 = M("x", "=", "8 - 5", "=", "3", size=72, color=GOLD).move_to(e4)
        self.play(ReplacementTransform(e4, e5), run_time=1.0)
        self.play(Circumscribe(e5, color=GOLD), run_time=1.0)


class S14(ChoigoScene):
    SCENE_ID = 14

    def build(self):
        fig = full_figure()
        self.add(fig)
        self.play(fig.animate.scale(0.6).move_to(LEFT * 4.6 + UP * 0.4), run_time=1.0)
        self.play(*[Indicate(c, color=CORAL) for c in fig[3]], run_time=1.2)
        self.at(1)
        name = T("완전제곱식", size=56, color=GOLD, font=SERIF, weight=BOLD).next_to(fig, DOWN, buff=0.35)
        self.play(FadeIn(name, shift=UP * 0.2))
        self.at(2)
        arrow = Arrow(LEFT * 0.9, RIGHT * 0.9, color=GOLD, stroke_width=6).move_to(LEFT * 0.9 + UP * 0.4)
        allq = T("모든 이차방정식에 적용", size=26, color=MUTED).next_to(arrow, UP, buff=0.2)
        f = M(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", size=64, color=GOLD).move_to(RIGHT * 3.3 + UP * 0.4)
        self.play(GrowArrow(arrow), FadeIn(allq), run_time=0.8)
        self.play(Write(f), run_time=2.0)
        cap = T("근의 공식", size=44, font=SERIF, weight=BOLD).next_to(f, DOWN, buff=0.4)
        self.play(FadeIn(cap))


# ── ④ 진짜 쉬운 설명 ───────────────────────────────────────
class S15(ChoigoScene):
    SCENE_ID = 15

    def build(self):
        self.show_chapter("④", "진짜 쉬운 설명", hold=0.6)
        self.at(1)
        e1 = M("x^2", "+", "10x", "=", "39", size=84).shift(UP * 1.3)
        e1[0].set_color(TEAL)
        e1[2].set_color(GOLD)
        self.play(Write(e1), run_time=1.2)
        mix = T("두 종류가 섞여 있다", size=30, color=MUTED).next_to(e1, UP, buff=0.3)
        self.play(FadeIn(mix), Wiggle(e1[0]), Wiggle(e1[2]), run_time=1.4)
        self.at(2)
        e2 = M("x^2", "+", "10x", "+", "25", "=", "64", size=84).move_to(e1)
        e2[0].set_color(TEAL)
        e2[2].set_color(GOLD)
        e2[4].set_color(CORAL)
        self.play(FadeOut(mix), TransformMatchingTex(e1, e2), run_time=1.2)
        e3 = M("(x + 5)^2", "=", "64", size=96).shift(DOWN * 0.3)
        b = SurroundingRectangle(e3[0], color=GOLD, buff=0.15)
        self.play(TransformFromCopy(e2, e3), run_time=1.4)
        lump = T("한 덩어리", size=32, color=GOLD).next_to(b, DOWN, buff=0.2)
        self.play(Create(b), FadeIn(lump))
        self.at(3)
        e4 = M(r"x + 5 = \pm 8", size=72).shift(DOWN * 2.0)
        self.play(FadeOut(lump), Write(e4), run_time=1.2)


class S16(ChoigoScene):
    SCENE_ID = 16

    def build(self):
        tag = T("흔한 오해", size=40, color=CORAL, font=SERIF, weight=BOLD).to_edge(UP, buff=0.7)
        self.play(FadeIn(tag, shift=DOWN * 0.2))
        self.at(1)
        claim = T("근의 공식은 인수분해가 안 될 때만 쓰는 공식?", size=40).shift(UP * 1.4)
        self.play(FadeIn(claim, shift=UP * 0.2), run_time=0.8)
        self.at(2)
        cross = Cross(claim, stroke_color=CORAL, stroke_width=6)
        self.play(Create(cross), run_time=0.6)
        self.play(VGroup(claim, cross).animate.set_opacity(0.35))
        # 열쇠
        head = Circle(radius=0.45, color=GOLD, stroke_width=6)
        hole = Circle(radius=0.14, color=GOLD, stroke_width=4).move_to(head)
        shaft = Line(head.get_right(), head.get_right() + RIGHT * 1.6, color=GOLD, stroke_width=8)
        teeth = VGroup(*[Line(shaft.get_end() + LEFT * d, shaft.get_end() + LEFT * d + DOWN * 0.3,
                              color=GOLD, stroke_width=8) for d in (0.05, 0.4)])
        key = VGroup(head, hole, shaft, teeth)
        k_cap = VGroup(T("근의 공식", size=40, weight=BOLD, color=GOLD), T("모든 이차방정식을 여는 만능 열쇠", size=30))
        k_cap.arrange(DOWN, buff=0.15)
        # 지름길
        path = ArcBetweenPoints(LEFT * 1.1, RIGHT * 1.1, angle=-PI / 2, color=MUTED, stroke_width=4)
        path = DashedVMobject(path, num_dashes=12)
        short = Arrow(LEFT * 1.1, RIGHT * 1.1, color=TEAL, stroke_width=6, buff=0)
        cut = VGroup(path, short)
        s_cap = VGroup(T("인수분해", size=40, weight=BOLD, color=TEAL), T("운이 좋을 때 쓰는 지름길", size=30))
        s_cap.arrange(DOWN, buff=0.15)
        left = VGroup(key, k_cap).arrange(DOWN, buff=0.4).move_to(LEFT * 3.3 + DOWN * 0.9)
        right = VGroup(cut, s_cap).arrange(DOWN, buff=0.4).move_to(RIGHT * 3.3 + DOWN * 0.9)
        self.play(FadeIn(key, shift=RIGHT * 0.3), FadeIn(k_cap), run_time=1.0)
        self.at(2, 4.6)
        self.play(Create(path), GrowArrow(short), FadeIn(s_cap), run_time=1.0)


# ── ⑤ 공식 풀어보기 ────────────────────────────────────────
SPLIT = [r"x =", r"-\frac{b}{2a}", r"\pm", r"\frac{\sqrt{b^2 - 4ac}}{2a}"]


class S17(ChoigoScene):
    SCENE_ID = 17

    def build(self):
        self.show_chapter("⑤", "공식 풀어보기", hold=0.6)
        f = M(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", size=84, color=INK).shift(UP * 1.6)
        self.play(Write(f), run_time=1.4)
        fs = M(*SPLIT, size=84).move_to(f)
        self.play(TransformMatchingShapes(f, fs), run_time=1.2)
        self.at(1)
        box = SurroundingRectangle(fs[1], color=GOLD, buff=0.12)
        self.play(Create(box), fs[1].animate.set_color(GOLD))
        mini = full_figure().scale(0.38).move_to(LEFT * 4.3 + DOWN * 1.2)
        self.play(FadeIn(mini), run_time=0.6)
        calc = M("2.5", "+", "2.5", "=", "5", size=60).move_to(RIGHT * 1.2 + DOWN * 0.9)
        calc[0].set_color(CORAL)
        calc[2].set_color(CORAL)
        calc[4].set_color(GOLD)
        self.play(Write(calc), run_time=1.2)
        self.at(2)
        half = M(r"= 10 \div 2", size=52, color=MUTED).next_to(calc, RIGHT, buff=0.3)
        self.play(FadeIn(half, shift=LEFT * 0.2))
        self.at(2, 2.4)
        minus = VGroup(T("큰 변", size=36), M("- 5 = x", size=56)).arrange(RIGHT, buff=0.2)
        minus.next_to(calc, DOWN, buff=0.45).align_to(calc, LEFT)
        self.play(FadeIn(minus, shift=UP * 0.2))


class S18(ChoigoScene):
    SCENE_ID = 18

    def build(self):
        fs = M(*SPLIT, size=84).shift(UP * 1.9)
        self.add(fs)
        box = SurroundingRectangle(fs[3][0:9], color=TEAL, buff=0.1)
        self.play(Create(box), fs[3].animate.set_color(TEAL), run_time=0.8)
        lab = T("완성한 정사각형의 넓이를 결정", size=32, color=TEAL).next_to(fs, DOWN, buff=0.3)
        self.play(FadeIn(lab))
        cases = VGroup()
        for sym, shape, txt, col in [
            ("> 0", Square(1.0, color=GOLD, fill_opacity=0.3), "해 2개", GOLD),
            ("= 0", Dot(radius=0.1, color=GOLD), "해 1개", GOLD),
            ("< 0", VGroup(DashedVMobject(Square(1.0, color=CORAL)), Cross(Square(1.0), stroke_color=CORAL, stroke_width=5)),
             "그릴 수 없음", CORAL),
        ]:
            head = M("b^2 - 4ac", sym, size=40, color=col)
            box_ = VGroup(head, shape.copy().set_height(1.0) if not isinstance(shape, Dot) else shape,
                          T(txt, size=28, color=col)).arrange(DOWN, buff=0.3)
            cases.add(box_)
        cases.arrange(RIGHT, buff=1.6).shift(DOWN * 1.35)
        self.play(LaggedStart(*[FadeIn(c[0]) for c in cases[:2]], *[FadeIn(c[1:]) for c in cases[:2]],
                              lag_ratio=0.2), run_time=1.6)
        self.at(1)
        self.play(FadeIn(cases[2][0]), Create(cases[2][1]), run_time=1.0)
        self.at(2)
        self.play(FadeIn(cases[2][2]), Indicate(cases[2], color=CORAL))


class S19(ChoigoScene):
    SCENE_ID = 19

    def build(self):
        head = T("알 콰리즈미의 문제로 확인", size=36, color=MUTED).to_edge(UP, buff=0.6)
        self.play(FadeIn(head))
        self.at(1)
        l1 = M("x^2 + 10x - 39 = 0", size=64)
        l2 = M("a = 1,", r"\quad b = 10,", r"\quad c = -39", size=52, color=TEAL)
        lines = VGroup(l1, l2).arrange(DOWN, buff=0.45).shift(UP * 1.1)
        self.play(Write(l1), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.2) for p in l2], lag_ratio=0.5), run_time=1.6)
        self.at(2)
        l3 = M("b^2 - 4ac", "=", "100 + 156", "=", "256", size=60).next_to(l2, DOWN, buff=0.55)
        l3[4].set_color(GOLD)
        self.play(Write(l3), run_time=2.0)
        self.at(3)
        l4 = M(r"\sqrt{256} = 16", size=64, color=GOLD).next_to(l3, DOWN, buff=0.45)
        self.play(Write(l4), run_time=1.0)


class S20(ChoigoScene):
    SCENE_ID = 20

    def build(self):
        top = M(r"x = \frac{-10 \pm 16}{2}", size=72).shift(UP * 2.0)
        self.play(Write(top), run_time=1.2)
        r1 = M(r"\frac{-10 + 16}{2} = 3", size=64, color=GOLD).move_to(LEFT * 3.2 + DOWN * 0.1)
        self.play(TransformFromCopy(top, r1), run_time=1.0)
        self.at(1)
        r2 = M(r"\frac{-10 - 16}{2} = -13", size=64).move_to(RIGHT * 3.2 + DOWN * 0.1)
        self.play(TransformFromCopy(top, r2), run_time=1.0)
        self.at(2)
        mini = full_figure().scale(0.3).next_to(r1, DOWN, buff=0.3)
        self.play(FadeIn(mini), Circumscribe(r1, color=GOLD), run_time=1.2)
        self.at(3)
        self.play(r2.animate.set_opacity(0.35), run_time=0.6)
        neg = T("음수 길이는 없다", size=30, color=CORAL).next_to(r2, DOWN, buff=0.4)
        self.play(FadeIn(neg))


# ── ⑥ 오늘의 한 줄 ─────────────────────────────────────────
class S21(ChoigoScene):
    SCENE_ID = 21

    def build(self):
        fig = full_figure().scale(0.55).move_to(UP * 1.2)
        fig.set_opacity(0.85)
        tag = T("오늘의 한 줄", size=34, color=GOLD, font=SERIF).to_edge(UP, buff=0.4)
        self.play(FadeIn(tag), FadeIn(fig), run_time=1.0)
        self.at(1)
        l1 = T("근의 공식은 외우는 주문이 아니라", size=38, font=SERIF)
        l2 = T("정사각형을 완성하는 이야기", size=50, font=SERIF, weight=BOLD, color=GOLD)
        g = VGroup(l1, l2).arrange(DOWN, buff=0.3).next_to(fig, DOWN, buff=0.45)
        self.play(FadeIn(l1, shift=UP * 0.2), run_time=0.8)
        self.wait(1.8)
        self.play(Write(l2), run_time=1.6)


class S22(ChoigoScene):
    SCENE_ID = 22
    CAMERA_DRIFT = False

    def build(self):
        rows = VGroup()
        for src, dst, ko in [("al-jabr", "algebra", "대수학"), ("Algoritmi", "algorithm", "알고리즘")]:
            a = T(src, size=44, color=MUTED, font=SERIF)
            arr = Arrow(LEFT * 0.6, RIGHT * 0.6, color=GOLD)
            b = T(dst, size=52, color=GOLD, font=SERIF, weight=BOLD)
            c = T(f"({ko})", size=34)
            rows.add(VGroup(a, arr, b, c).arrange(RIGHT, buff=0.3))
        rows.arrange(DOWN, buff=0.5, aligned_edge=LEFT).shift(UP * 0.5)
        self.play(FadeIn(rows[0][0]), run_time=0.5)
        self.play(GrowArrow(rows[0][1]), FadeIn(rows[0][2:]), run_time=1.0)
        self.wait(2.0)
        self.play(FadeIn(rows[1][0]), run_time=0.5)
        self.play(GrowArrow(rows[1][1]), FadeIn(rows[1][2:]), run_time=1.0)
        self.at(1)
        self.play(FadeOut(rows), run_time=0.6)
        nxt = T("다음 편", size=34, color=MUTED, font=SERIF).shift(UP * 2.4)
        title = T("이차함수", size=72, font=SERIF, weight=BOLD).next_to(nxt, DOWN, buff=0.25)
        ax = Axes(x_range=[-3, 3], y_range=[-1, 5], x_length=4.2, y_length=2.6,
                  axis_config={"color": MUTED, "stroke_width": 2, "include_ticks": False}).shift(DOWN * 1.0)
        par = ax.plot(lambda x: x ** 2 * 0.5, x_range=[-2.9, 2.9], color=GOLD, stroke_width=5)
        self.play(FadeIn(nxt), FadeIn(title, shift=UP * 0.2), Create(ax), run_time=1.0)
        self.play(Create(par), run_time=1.6)
        self.at(2)
        self.play(FadeOut(VGroup(nxt, title, ax, par)), run_time=0.6)
        logo = T("최고의 공부", size=96, font=SERIF, weight=BOLD, color=GOLD)
        sub = T("하루에 개념 하나", size=36, color=MUTED).next_to(logo, DOWN, buff=0.35)
        self.play(FadeIn(logo, scale=0.9), FadeIn(sub), run_time=1.0)
