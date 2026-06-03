from manim import *


WHITE_TEXT = WHITE
HIGHLIGHT_YELLOW = YELLOW


def math_item(tex, font_size=64, color=WHITE_TEXT):
    return MathTex(tex, font_size=font_size, color=color)


def make_factor_formula(font_size=58):
    plus_factor = math_item(r"(g^{r/2}+1)", font_size=font_size)
    cdot = math_item(r"\cdot", font_size=font_size)
    minus_factor = math_item(r"(g^{r/2}-1)", font_size=font_size)
    equals = math_item(r"=", font_size=font_size)
    right_side = math_item(r"kN", font_size=font_size)

    cdot.next_to(plus_factor, RIGHT, buff=0.35)
    minus_factor.next_to(cdot, RIGHT, buff=0.35)
    equals.next_to(minus_factor, RIGHT, buff=0.35)
    right_side.next_to(equals, RIGHT, buff=0.35)
    return VGroup(plus_factor, cdot, minus_factor, equals, right_side)


class scene6(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        n_formula = MathTex(
            "N",
            "=",
            "p",
            r"\cdot",
            "q",
            font_size=48,
            color=WHITE_TEXT,
        ).move_to(UP * 3.12)
        period_formula = MathTex(
            "f(x+",
            "r",
            ")=f(x)",
            font_size=48,
            color=WHITE_TEXT,
        ).move_to(UP * 1.45)

        self.add(n_formula, period_formula)
        self.wait(0.8)

        self.play(
            n_formula.animate.scale(64 / 48).move_to(UP * 2.95),
            period_formula.animate.scale(64 / 48).move_to(UP * 2.18),
            run_time=0.75,
            rate_func=smooth,
        )
        self.wait(0.35)

        self.play(
            n_formula[0].animate.scale(1.8),
            rate_func=there_and_back,
            run_time=0.62,
        )
        self.wait(0.25)
        self.play(
            period_formula[1].animate.scale(1.8),
            rate_func=there_and_back,
            run_time=0.62,
        )
        self.wait(0.45)

        identity = math_item(r"g^0 \equiv 1 \pmod N", font_size=62)
        identity.next_to(period_formula, DOWN, buff=0.32)
        self.play(FadeIn(identity, shift=UP * 0.08), run_time=0.55)
        self.wait(0.8)

        period_relation = math_item(r"g^r - 1 = kN", font_size=66)
        period_relation.move_to(identity.get_center())
        self.play(
            ReplacementTransform(identity, period_relation),
            run_time=0.72,
            rate_func=smooth,
        )
        self.wait(0.75)

        factored_relation = make_factor_formula(font_size=58).move_to(
            period_relation.get_center()
        )
        self.play(
            ReplacementTransform(period_relation, factored_relation),
            run_time=0.75,
            rate_func=smooth,
        )
        self.wait(0.65)

        plus_factor = factored_relation[0]
        minus_factor = factored_relation[2]

        gcd_plus = math_item(r"\gcd(g^{r/2}+1,N)", font_size=42)
        gcd_minus = math_item(r"\gcd(g^{r/2}-1,N)", font_size=42)
        gcd_y = factored_relation.get_center()[1] - 1.38
        gcd_plus.move_to(RIGHT * plus_factor.get_center()[0] + UP * gcd_y)
        gcd_minus.move_to(RIGHT * minus_factor.get_center()[0] + UP * gcd_y)
        gcd_group = VGroup(gcd_plus, gcd_minus)

        arrow_start_y = min(
            plus_factor.get_bottom()[1],
            minus_factor.get_bottom()[1],
        ) - 0.12
        arrow_end_y = max(
            gcd_plus.get_top()[1],
            gcd_minus.get_top()[1],
        ) + 0.12

        plus_arrow = Arrow(
            [plus_factor.get_center()[0], arrow_start_y, 0],
            [plus_factor.get_center()[0], arrow_end_y, 0],
            buff=0,
            color=HIGHLIGHT_YELLOW,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.18,
        )
        minus_arrow = Arrow(
            [minus_factor.get_center()[0], arrow_start_y, 0],
            [minus_factor.get_center()[0], arrow_end_y, 0],
            buff=0,
            color=HIGHLIGHT_YELLOW,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.18,
        )
        self.play(GrowArrow(plus_arrow), GrowArrow(minus_arrow), run_time=0.45)
        self.wait(0.25)
        self.play(
            FadeIn(gcd_plus, shift=DOWN * 0.08),
            FadeIn(gcd_minus, shift=DOWN * 0.08),
            run_time=0.55,
        )
        self.wait(0.9)

        factors = VGroup(
            math_item("p", font_size=88, color=HIGHLIGHT_YELLOW),
            math_item("q", font_size=88, color=HIGHLIGHT_YELLOW),
        ).arrange(RIGHT, buff=2.25)
        factors.move_to(gcd_group.get_center())
        self.play(
            Transform(gcd_group, factors),
            FadeOut(VGroup(plus_arrow, minus_arrow), shift=DOWN * 0.05),
            run_time=0.72,
            rate_func=smooth,
        )
        self.wait(0.75)

        self.play(n_formula[0].animate.set_color(HIGHLIGHT_YELLOW), run_time=0.35)
        self.wait(0.25)
        self.play(period_formula[1].animate.set_color(HIGHLIGHT_YELLOW), run_time=0.35)
        self.wait(0.9)

        self.play(
            FadeOut(VGroup(factored_relation, gcd_group), shift=DOWN * 0.05),
            run_time=0.72,
            rate_func=smooth,
        )

        self.wait(1)