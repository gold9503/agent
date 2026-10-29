"""로피탈의 정리 편 장면 (Manim). 장면 번호는 03_storyboard.json의 id와 같다."""
from choigo_style import *  # noqa: F401,F403

BLUE = TEAL        # 분자 f
ORANGE = "#E8954C"  # 분모 g
PAPER = "#E9DFC8"
INKBROWN = "#3B2A1A"

# 장면 5·6에서 쓰는 두 함수: a에서 함께 0이 되고, 기울기 비가 3 : 1
A = 1.0


def f(x):
    return 1.5 * (x - A) + 0.35 * (x - A) ** 2


def g(x):
    return 0.5 * (x - A) - 0.25 * (x - A) ** 2


def title_page():
    """『무한소 해석』 초판(1696) 속표지 문구를 직접 조판한 대체 그림."""
    page = Rectangle(width=3.0, height=4.2, stroke_color=CLAY, stroke_width=3, fill_color=PAPER, fill_opacity=1)
    serif = "Noto Serif CJK KR"
    lines = VGroup(
        Text("ANALYSE", font=serif, weight=BOLD, color=INKBROWN, font_size=30),
        Text("DES", font=serif, color=INKBROWN, font_size=20),
        Text("INFINIMENT PETITS,", font=serif, weight=BOLD, color=INKBROWN, font_size=19),
        Text("Pour l'intelligence des", font=serif, color=INKBROWN, font_size=16),
        Text("lignes courbes.", font=serif, color=INKBROWN, font_size=16),
        Line(LEFT * 0.8, RIGHT * 0.8, color=INKBROWN, stroke_width=2),
        Text("A PARIS,", font=serif, color=INKBROWN, font_size=18),
        Text("M. DC. XCVI.", font=serif, weight=BOLD, color=INKBROWN, font_size=20),
    ).arrange(DOWN, buff=0.17).move_to(page)
    return VGroup(page, lines)


def name_card(name, years):
    return VGroup(T(name, size=48, font=SERIF, weight=BOLD), T(years, size=26, color=INK)).arrange(DOWN, buff=0.15)


# ── ① 오프닝 질문 ──────────────────────────────────────────
class S01(ChoigoScene):
    SCENE_ID = 1

    def build(self):
        frac = M(r"\frac{0}{0}", size=160, color=GOLD)
        q = M("= \\, ?", size=120, color=INK).next_to(frac, RIGHT, buff=0.4)
        grp = VGroup(frac, q).move_to(UP * 0.4)
        self.play(Write(frac), run_time=1.6)
        self.at(1)
        self.play(FadeIn(q, shift=LEFT * 0.2))
        self.at(2)
        spell = plate(T("“위아래를 따로 미분하라”", size=40, color=INK)).next_to(grp, DOWN, buff=0.6)
        self.play(FadeIn(spell, shift=UP * 0.2))
        self.at(3)
        name = T("로피탈의 정리", size=72, font=SERIF, weight=BOLD, color=GOLD)
        self.play(FadeOut(VGroup(grp, spell)), FadeIn(name, scale=0.95), run_time=0.8)
        self.at(4)
        owner = T("의 주인은?", size=56, font=SERIF)
        target = VGroup(name.copy(), owner).arrange(RIGHT, buff=0.12, aligned_edge=DOWN).move_to(ORIGIN)
        self.play(name.animate.move_to(target[0]), FadeIn(owner, shift=LEFT * 0.2), run_time=0.8)


# ── ② 시대 속으로 ──────────────────────────────────────────
class S02(ChoigoScene):
    SCENE_ID = 2

    def build(self):
        self.show_chapter("②", "시대 속으로", hold=0.4)
        year = plate(VGroup(T("1696년", size=64, font=SERIF, weight=BOLD, color=GOLD),
                            T("파리", size=40, font=SERIF)).arrange(RIGHT, buff=0.4, aligned_edge=DOWN))
        year.move_to(UP * 2.6)
        self.play(FadeIn(year, shift=DOWN * 0.2), run_time=0.6)
        self.at(1)
        book = self.photo_or("analyse_title", title_page(), height=4.2).move_to(LEFT * 3.2 + DOWN * 0.3)
        cap = T("1715년 판 속표지" if self.sources.get("analyse_title") else "1696년 초판 속표지 문구 재현",
                size=20, color=INK).next_to(book, DOWN, buff=0.12)
        info = VGroup(T("『무한소 해석』", size=48, font=SERIF, weight=BOLD, color=GOLD),
                      T("미분을 다룬 최초의 교과서", size=32),
                      T("로피탈 후작 (1661~1704)", size=28, color=INK)).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        info_p = plate(info, buff=0.4).move_to(RIGHT * 2.8 + DOWN * 0.2)
        self.play(FadeIn(book, shift=UP * 0.3), FadeIn(cap), run_time=1.0)
        self.play(FadeIn(info_p, shift=LEFT * 0.2), run_time=0.8)
        self.at(2)
        hidden = T("숨은 스승?", size=44, font=SERIF, weight=BOLD, color=CORAL).next_to(info_p, DOWN, buff=0.35)
        self.play(FadeIn(hidden, scale=1.2))


class S03(ChoigoScene):
    SCENE_ID = 3

    def build(self):
        card_p = plate(name_card("요한 베르누이", "1667~1748 · 스위스 바젤"), buff=0.4)
        if sorted((self.ep / "assets/media").glob("bernoulli_portrait.*")):
            portrait = self.photo("bernoulli_portrait", height=3.6).move_to(LEFT * 4.2 + UP * 0.6)
            card_p.move_to(RIGHT * 1.0 + UP * 1.6)
            self.play(FadeIn(portrait), run_time=0.8)
        else:
            card_p.move_to(UP * 1.6)
        self.play(FadeIn(card_p, shift=UP * 0.2), run_time=0.8)
        self.at(1)
        date = plate(T("1694년 3월 · 로피탈의 편지", size=36, color=GOLD)).next_to(card_p, DOWN, buff=0.5)
        self.play(FadeIn(date, shift=UP * 0.2))
        self.at(2)
        deal = VGroup(T("해마다 300리브르", size=40, weight=BOLD, color=GOLD),
                      Arrow(LEFT * 0.7, RIGHT * 0.7, color=INK),
                      T("새 발견은 로피탈에게만", size=40, weight=BOLD)).arrange(RIGHT, buff=0.35)
        deal_p = plate(VGroup(T("편지 요지", size=22, color=MUTED), deal).arrange(DOWN, buff=0.2), buff=0.35)
        deal_p.next_to(date, DOWN, buff=0.4)
        self.play(FadeIn(deal_p[0]), FadeIn(deal_p[1][0]), FadeIn(deal[0]), run_time=0.6)
        self.play(GrowArrow(deal[1]), FadeIn(deal[2], shift=LEFT * 0.2), run_time=0.8)


class S04(ChoigoScene):
    SCENE_ID = 4

    def build(self):
        line = Line(LEFT * 5.8, RIGHT * 5.8, color=INK, stroke_width=3).shift(UP * 0.3)
        xs = [-4.2, 0.0, 4.2]
        ticks = VGroup(*[Dot([x, 0.3, 0], radius=0.1, color=GOLD) for x in xs])
        labels = [("1694. 3", "계약 제안"), ("1694. 7", "베르누이의 편지\n0/0을 푸는 방법"), ("1696", "『무한소 해석』 출간")]
        cards = VGroup(*[
            plate(VGroup(T(d, size=32, color=GOLD, weight=BOLD), T(t, size=26, line_spacing=0.9)).arrange(DOWN, buff=0.12),
                  buff=0.25).next_to(tk, DOWN, buff=0.35)
            for (d, t), tk in zip(labels, ticks)])
        self.play(Create(line), FadeIn(ticks[0]), FadeIn(cards[0]), run_time=0.8)
        self.play(FadeIn(ticks[1]), FadeIn(cards[1], shift=UP * 0.2), Flash(ticks[1], color=GOLD), run_time=1.0)
        self.at(1)
        self.play(FadeIn(ticks[2]), FadeIn(cards[2], shift=UP * 0.2), run_time=0.8)
        arrow = CurvedArrow(ticks[1].get_center() + UP * 0.2, ticks[2].get_center() + UP * 0.2,
                            angle=-PI / 3, color=GOLD)
        name = plate(T("‘로피탈의 정리’로 불리게 됨", size=30, color=GOLD)).next_to(arrow, UP, buff=0.15)
        self.play(Create(arrow), FadeIn(name), run_time=1.0)
        self.at(2)
        note = plate(T("머리말: 베르누이의 도움을 밝힘", size=28)).move_to(UP * 2.9 + LEFT * 3.2)
        self.play(FadeIn(note, shift=DOWN * 0.2))


# ── ③ 개념의 탄생 ──────────────────────────────────────────
def axes():
    ax = Axes(x_range=[-0.2, 2.4, 1], y_range=[-1.2, 1.6, 1], x_length=7.0, y_length=4.6,
              axis_config={"color": MUTED, "stroke_width": 2, "include_ticks": False}).shift(LEFT * 2.6 + DOWN * 0.1)
    return ax


class S05(ChoigoScene):
    SCENE_ID = 5

    def build(self):
        self.show_chapter("③", "개념의 탄생", hold=0.4)
        ax = axes()
        cf = ax.plot(f, x_range=[0.3, 1.9], color=BLUE, stroke_width=5)
        cg = ax.plot(g, x_range=[-0.1, 2.3], color=ORANGE, stroke_width=5)
        lf = M("f(x)", size=40, color=BLUE).next_to(ax.c2p(1.9, f(1.9)), RIGHT, buff=0.1)
        lg = M("g(x)", size=40, color=ORANGE).next_to(ax.c2p(-0.1, g(-0.1)), UP, buff=0.15)
        self.play(Create(ax), run_time=0.6)
        self.play(Create(cf), Create(cg), FadeIn(lf), FadeIn(lg), run_time=1.4)
        self.at(1)
        pa = ax.c2p(A, 0)
        dot = Dot(pa, color=GOLD, radius=0.09)
        la = M("a", size=40, color=GOLD).next_to(dot, DOWN + LEFT, buff=0.1)
        both = M("f(a) = 0,", r"\ g(a) = 0", size=40).move_to(RIGHT * 4.0 + UP * 2.2)
        both[0].set_color(BLUE)
        both[1].set_color(ORANGE)
        self.play(FadeIn(dot, scale=2), FadeIn(la), Write(both), run_time=1.0)
        self.at(2)
        lens = Circle(radius=0.55, color=GOLD, stroke_width=3).move_to(pa)
        big = Circle(radius=1.6, color=GOLD, stroke_width=3).move_to(RIGHT * 4.3 + DOWN * 0.2)
        link = Line(lens.get_right(), big.get_left(), color=GOLD, stroke_width=2)
        s = 1.35
        tf = Line(big.get_center() + s * np.array([-1, -1.5 / 1.6, 0]) * 0.75,
                  big.get_center() + s * np.array([1, 1.5 / 1.6, 0]) * 0.75, color=BLUE, stroke_width=5)
        tg = Line(big.get_center() + s * np.array([-1, -0.5 / 1.6, 0]) * 0.95,
                  big.get_center() + s * np.array([1, 0.5 / 1.6, 0]) * 0.95, color=ORANGE, stroke_width=5)
        straight = T("거의 직선", size=30, color=GOLD).next_to(big, DOWN, buff=0.15)
        self.play(Create(lens), Create(link), Create(big), run_time=0.8)
        self.play(Create(tf), Create(tg), FadeIn(straight), run_time=1.0)


class S06(ChoigoScene):
    SCENE_ID = 6

    def build(self):
        l1 = M(r"f(x) \approx", r"f'(a)", r"\,(x-a)", size=56)
        l2 = M(r"g(x) \approx", r"g'(a)", r"\,(x-a)", size=56)
        for l, c in ((l1, BLUE), (l2, ORANGE)):
            l[1].set_color(c)
        rows = VGroup(l1, l2).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(UP * 2.0)
        hint = T("높이 = 기울기 × 떨어진 거리", size=28, color=MUTED).next_to(rows, UP, buff=0.3)
        self.play(FadeIn(hint), Write(l1), run_time=1.2)
        self.play(Write(l2), run_time=1.0)
        self.at(1)
        ratio = M(r"\frac{f(x)}{g(x)} \approx", r"\frac{f'(a)\,(x-a)}{g'(a)\,(x-a)}", size=60).move_to(DOWN * 0.3)
        self.play(Write(ratio), run_time=1.4)
        crosses = VGroup(*[Line(DL * 0.18, UR * 0.18, color=CORAL, stroke_width=6).move_to(ratio[1].get_center() + v)
                           for v in (RIGHT * 0.62 + UP * 0.38, RIGHT * 0.62 + DOWN * 0.42)])
        self.play(Create(crosses), run_time=0.6)
        final = M(r"\frac{f(x)}{g(x)} \approx", r"\frac{f'(a)}{g'(a)}", size=72).move_to(DOWN * 0.3)
        final[1].set_color(GOLD)
        self.play(FadeOut(crosses), TransformMatchingShapes(ratio, final), run_time=1.0)
        self.at(2)
        lab = plate(T("0/0의 정체 = 0으로 다가가는 빠르기의 비", size=34, color=GOLD)).next_to(final, DOWN, buff=0.5)
        self.play(FadeIn(lab, shift=UP * 0.2))
        self.at(3)
        d = T("빠르기 = 도함수", size=40, weight=BOLD, color=GOLD)
        box = SurroundingRectangle(final[1], color=GOLD, buff=0.15)
        d.next_to(box, RIGHT, buff=0.4)
        self.play(Create(box), FadeIn(d, shift=LEFT * 0.2))
        fine = T("직관적 설명 · 엄밀한 증명은 코시의 평균값 정리", size=22, color=MUTED).to_corner(UL, buff=0.4)
        self.play(FadeIn(fine))


# ── ④ 진짜 쉬운 설명 ───────────────────────────────────────
def tracks():
    finish_x = 4.5
    t1 = Line([-5.5, 1.0, 0], [finish_x, 1.0, 0], color=MUTED, stroke_width=2)
    t2 = Line([-5.5, -0.6, 0], [finish_x, -0.6, 0], color=MUTED, stroke_width=2)
    finish = DashedLine([finish_x, 1.8, 0], [finish_x, -1.4, 0], color=INK)
    flag = T("결승선", size=26).next_to(finish, DOWN, buff=0.1)
    return VGroup(t1, t2, finish, flag), finish_x


class S07(ChoigoScene):
    SCENE_ID = 7

    def build(self):
        self.show_chapter("④", "진짜 쉬운 설명", hold=0.4)
        tr, fx = tracks()
        r1 = Dot([-5.0, 1.0, 0], radius=0.18, color=BLUE)       # 3배 먼 곳에서 3배 빠르게
        r2 = Dot([fx - (fx + 5.0) / 3, -0.6, 0], radius=0.18, color=ORANGE)
        l1 = T("분자", size=26, color=BLUE).next_to(r1, UP, buff=0.15)
        l2 = T("분모", size=26, color=ORANGE).next_to(r2, UP, buff=0.15)
        self.play(FadeIn(tr), FadeIn(r1), FadeIn(r2), FadeIn(l1), FadeIn(l2), run_time=0.8)
        l1.add_updater(lambda m: m.next_to(r1, UP, buff=0.15))
        l2.add_updater(lambda m: m.next_to(r2, UP, buff=0.15))
        # 결승 직전까지 달린다 (남은 거리 비 3 : 1 유지)
        stop = 0.88
        self.play(r1.animate.set_x(-5.0 + (fx + 5.0) * stop), r2.animate.set_x(r2.get_x() + (fx - r2.get_x()) * stop),
                  run_time=2.4, rate_func=linear)
        self.at(1)
        g1 = Line(r1.get_center(), [fx, 1.0, 0], color=BLUE, stroke_width=10)
        g2 = Line(r2.get_center(), [fx, -0.6, 0], color=ORANGE, stroke_width=10)
        rem = plate(T("남은 거리 → 둘 다 0으로", size=30)).move_to(DOWN * 2.0)
        self.play(Create(g1), Create(g2), FadeIn(rem), run_time=0.8)
        self.at(2)
        ratio = plate(VGroup(T("남은 거리의 비", size=30), M("3 : 1", size=48, color=GOLD),
                             T("=  속도의 비", size=30, color=GOLD)).arrange(RIGHT, buff=0.3)).move_to(DOWN * 2.0)
        self.play(FadeOut(rem), FadeIn(ratio, shift=UP * 0.2), run_time=0.8)
        self.play(r1.animate.set_x(fx), r2.animate.set_x(fx), FadeOut(g1), FadeOut(g2), run_time=0.8, rate_func=linear)
        self.play(Flash([fx, 0.2, 0], color=GOLD), run_time=0.6)


class S08(ChoigoScene):
    SCENE_ID = 8

    def build(self):
        tag = T("흔한 실수", size=44, color=CORAL, font=SERIF, weight=BOLD).to_edge(UP, buff=0.6)
        self.play(FadeIn(tag, shift=DOWN * 0.2))
        self.at(1)
        warn = T("0/0 꼴이 아닌데 위아래를 미분하기", size=34).next_to(tag, DOWN, buff=0.3)
        self.play(FadeIn(warn))
        self.at(2)
        lim = M(r"\lim_{x \to 0} \frac{x+1}{x+2}", size=64).move_to(LEFT * 3.4 + DOWN * 0.1)
        right = M(r"= \frac{1}{2}", size=64, color=TEAL).next_to(lim, RIGHT, buff=0.3)
        ok = T("0/0 아님 → 로피탈 사용 불가", size=26, color=TEAL).next_to(VGroup(lim, right), DOWN, buff=0.2)
        okmark = tick(Square(0.4).next_to(right, RIGHT, buff=0.2)).set_color(TEAL)
        self.play(Write(lim), run_time=1.0)
        self.play(FadeIn(right), Create(okmark), FadeIn(ok), run_time=0.8)
        self.at(3)
        wrong = M(r"\frac{(x+1)'}{(x+2)'} = \frac{1}{1} = 1", size=56).move_to(RIGHT * 3.4 + DOWN * 0.1)
        cross = Cross(wrong, stroke_color=CORAL, stroke_width=7)
        self.play(Write(wrong), run_time=1.0)
        self.play(Create(cross), run_time=0.5)
        rule = plate(T("먼저 대입해 보기: 0/0 또는 ∞/∞ 인가?", size=30, color=GOLD)).move_to(DOWN * 2.15)
        self.play(FadeIn(rule, shift=UP * 0.2))


# ── ⑤ 공식 풀어보기 ────────────────────────────────────────
def checklist():
    rows = VGroup(
        VGroup(T("①", size=36, color=GOLD), M(r"\frac{0}{0}", size=48), T("또는", size=34),
               M(r"\frac{\infty}{\infty}", size=48), T("꼴", size=34)),
        VGroup(T("②", size=36, color=GOLD), M("a", size=48), T("근처에서 미분 가능,", size=34),
               M(r"g'(x) \neq 0", size=48)),
        VGroup(T("③", size=36, color=GOLD), M(r"\lim \frac{f'(x)}{g'(x)}", size=48), T("가 존재", size=34)),
    )
    for r in rows:
        r.arrange(RIGHT, buff=0.22)
    rows.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
    boxes = VGroup(*[Square(0.4, color=GOLD, stroke_width=3).next_to(r, LEFT, buff=0.3) for r in rows])
    return rows, boxes


def tick(box):
    return VMobject(color=GOLD, stroke_width=6).set_points_as_corners(
        [box.get_center() + v for v in (LEFT * 0.14, DOWN * 0.13 + RIGHT * 0.01, UP * 0.18 + RIGHT * 0.2)])


THEOREM = r"\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}"


class S09(ChoigoScene):
    SCENE_ID = 9

    def build(self):
        self.show_chapter("⑤", "공식 풀어보기", hold=0.4)
        rows, boxes = checklist()
        grp = VGroup(boxes, rows).move_to(UP * 1.3)
        self.at(1)
        self.play(Create(boxes[0]), Write(rows[0]), run_time=1.0)
        self.at(2)
        self.play(Create(boxes[1]), Write(rows[1]), run_time=1.2)
        self.at(3)
        self.play(Create(boxes[2]), Write(rows[2]), run_time=1.0)
        self.play(*[Create(tick(b)) for b in boxes], run_time=0.6)
        thm = M(THEOREM, size=60, color=GOLD).next_to(grp, DOWN, buff=0.6)
        self.play(Write(thm), run_time=1.6)


class S10(ChoigoScene):
    SCENE_ID = 10

    def build(self):
        head = T("예제", size=36, color=GOLD, font=SERIF, weight=BOLD).to_edge(UP, buff=0.6)
        ex = M(r"\lim_{x \to 1} \frac{x^3 - 1}{x - 1}", size=84).move_to(UP * 0.8)
        self.play(FadeIn(head), Write(ex), run_time=1.6)
        self.at(1)
        sub = M(r"\frac{1^3 - 1}{1 - 1} = \frac{0}{0}", size=64).next_to(ex, DOWN, buff=0.6)
        self.play(Write(sub), run_time=1.2)
        ok = T("① 조건 통과", size=34, color=GOLD).next_to(sub, RIGHT, buff=0.6)
        self.play(FadeIn(ok, shift=LEFT * 0.2))


class S11(ChoigoScene):
    SCENE_ID = 11

    def build(self):
        ex = M(r"\lim_{x \to 1}", r"\frac{x^3 - 1}{x - 1}", size=72).move_to(UP * 2.0 + LEFT * 2.0)
        self.add(ex)
        d = M(r"= \lim_{x \to 1} \frac{3x^2}{1}", size=72).next_to(ex, RIGHT, buff=0.3)
        num = Arrow(ex[1].get_top() + UP * 0.05, d.get_top() + UP * 0.05 + LEFT * 0.4, color=BLUE, path_arc=-1.2)
        self.play(Create(num), Write(d), run_time=1.4)
        res = M(r"= \frac{3 \cdot 1^2}{1} = 3", size=72, color=GOLD).move_to(UP * 0.5)
        self.play(Write(res), run_time=1.2)
        check = plate(VGroup(T("검산", size=24, color=MUTED),
                             M(r"\frac{(x-1)(x^2+x+1)}{x-1} \to 1+1+1 = 3", size=36)).arrange(RIGHT, buff=0.3))
        check.move_to(DOWN * 1.2)
        self.play(FadeIn(check))
        self.at(1)
        conds = plate(T("② g′(x) = 1 ≠ 0  ✓   ③ 극한 3 존재  ✓", size=26, color=GOLD)).to_corner(UL, buff=0.4)
        self.play(FadeIn(conds, shift=DOWN * 0.2))
        mini = plate(T("분자가 분모보다 3배 빠르게 0으로", size=34, color=GOLD)).move_to(DOWN * 2.15)
        self.play(FadeIn(mini, shift=UP * 0.2))


# ── ⑥ 오늘의 한 줄 ─────────────────────────────────────────
class S12(ChoigoScene):
    SCENE_ID = 12

    def build(self):
        tag = T("오늘의 한 줄", size=34, color=GOLD, font=SERIF).to_edge(UP, buff=0.5)
        self.play(FadeIn(tag))
        self.at(1)
        l1 = T("0/0은 빠르기 대결", size=60, font=SERIF, weight=BOLD, color=GOLD)
        l2 = T("승부는 기울기(도함수)로 가린다", size=40, font=SERIF)
        card = plate(VGroup(l1, l2).arrange(DOWN, buff=0.3), buff=0.45).move_to(UP * 0.8)
        self.play(FadeIn(card[0]), Write(l1), run_time=1.2)
        self.play(FadeIn(l2, shift=UP * 0.2))
        self.at(2)
        warn = plate(T("쓰기 전에: 0/0? ∞/∞?", size=34, color=CORAL)).next_to(card, DOWN, buff=0.4)
        self.play(FadeIn(warn, shift=UP * 0.2))
        self.at(3)
        self.play(FadeOut(VGroup(card, warn, tag)), run_time=0.5)
        nxt = plate(VGroup(T("다음 편", size=30, color=INK), T("테일러 급수", size=64, font=SERIF, weight=BOLD))
                    .arrange(DOWN, buff=0.2), buff=0.4)
        self.play(FadeIn(nxt, shift=UP * 0.2), run_time=0.6)
        self.at(4)
        self.play(FadeOut(nxt), run_time=0.4)
        logo = T("최고의 공부", size=96, font=SERIF, weight=BOLD, color=GOLD)
        sub = T("하루에 개념 하나", size=36, color=INK).next_to(logo, DOWN, buff=0.35)
        self.play(FadeIn(logo, scale=0.9), FadeIn(sub), run_time=0.8)
