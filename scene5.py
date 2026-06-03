from manim import *


WHITE_TEXT = WHITE
HIGHLIGHT_YELLOW = YELLOW


def math_item(tex, font_size=70, color=WHITE_TEXT):
    return MathTex(tex, font_size=font_size, color=color)


def text_item(text, font_size=72, color=WHITE_TEXT):
    return Text(
        text,
        font="Consolas",
        font_size=font_size,
        color=color,
        disable_ligatures=True,
    )


def make_shor_title():
    return text_item("Shor", font_size=82).to_edge(UP, buff=0.45)


def make_initial_parameters():
    n_value = math_item("N = 33", font_size=78)
    g_value = math_item("g = 5", font_size=78)
    return VGroup(n_value, g_value).arrange(DOWN, buff=0.42).move_to(ORIGIN)


def make_residue_table():
    rows = [
        [(1, 5), (11, 5), (21, 5), (31, 5)],
        [(2, 25), (12, 25), (22, 25), (32, 25)],
        [(3, 26), (13, 26), (23, 26)],
        [(4, 31), (14, 31), (24, 31)],
        [(5, 23), (15, 23), (25, 23)],
        [(6, 16), (16, 16), (26, 16)],
        [(7, 14), (17, 14), (27, 14)],
        [(8, 4), (18, 4), (28, 4)],
        [(9, 20), (19, 20), (29, 20)],
        [(10, 1), (20, 1), (30, 1)],
    ]
    column_x = [-4.9, -1.6, 1.6, 4.9]
    row_y = [1.65 - index * 0.36 for index in range(len(rows))]

    table = VGroup()
    first_row = VGroup()
    for row_index, row in enumerate(rows):
        row_group = VGroup()
        for column_index, (power, residue) in enumerate(row):
            entry = math_item(
                rf"5^{{{power}}} \equiv {residue}",
                font_size=31,
            )
            entry.move_to(RIGHT * column_x[column_index] + UP * row_y[row_index])
            row_group.add(entry)
            if row_index == 0:
                first_row.add(entry)
        table.add(row_group)

    table.move_to(DOWN * 1.08)
    return table, first_row


class scene5(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        shor = make_shor_title()
        self.add(shor)
        self.wait(0.35)
        self.play(
            shor.animate.to_corner(UL, buff=0.45).scale(0.62),
            run_time=0.75,
            rate_func=smooth,
        )
        self.wait(0.35)

        parameters = make_initial_parameters()
        n_value, g_value = parameters
        self.play(
            FadeIn(n_value, shift=UP * 0.08),
            run_time=0.45,
        )
        self.wait(0.45)
        self.play(
            FadeIn(g_value, shift=UP * 0.08),
            run_time=0.45,
        )
        self.wait(0.8)

        top_parameters = parameters.copy().scale(0.52).move_to(UP * 2.9)
        self.play(
            Transform(parameters, top_parameters),
            run_time=0.75,
            rate_func=smooth,
        )
        self.wait(0.35)

        function_definition = math_item(r"f(x) = 5^x \bmod 33", font_size=52)
        function_definition.next_to(parameters, DOWN, buff=0.15)
        self.play(
            FadeIn(function_definition, shift=UP * 0.06),
            run_time=0.45,
        )
        self.wait(0.65)

        residue_table, first_row = make_residue_table()
        self.play(FadeIn(residue_table, shift=UP * 0.08), run_time=0.8)
        self.wait(1.1)

        row_highlight = SurroundingRectangle(
            first_row,
            color=HIGHLIGHT_YELLOW,
            buff=0.07,
            stroke_width=5,
        )
        period_formula = math_item(
            r"f(x+r)=f(x),\ r=10",
            font_size=48,
        )
        period_formula.next_to(function_definition, DOWN, buff=0.15)
        self.play(
            Create(row_highlight),
            FadeIn(period_formula, shift=UP * 0.06),
            run_time=0.38,
        )
        self.play(first_row.animate.set_color(HIGHLIGHT_YELLOW), run_time=0.3)
        self.play(
            row_highlight.animate.set_stroke(opacity=0),
            first_row.animate.set_color(WHITE_TEXT),
            run_time=0.45,
        )
        self.remove(row_highlight)
        self.wait(0.75)

        zero_remainder = math_item(r"5^0 \equiv 1", font_size=52)
        zero_remainder.move_to(DOWN * 1.5 + RIGHT * 4.85)
        self.play(FadeIn(zero_remainder, shift=UP * 0.08), run_time=0.45)
        self.wait(1.0)

        power_relation = math_item(r"5^{10} = k\cdot33 + 1", font_size=76)
        power_relation.move_to(DOWN * 0.4)
        
        residue_group = VGroup(residue_table, zero_remainder)

        self.play(
            ReplacementTransform(residue_group, power_relation),
            FadeOut(function_definition, shift=UP * 0.05),
            run_time=0.85,
            rate_func=smooth,
        )
        self.wait(1.05)

        shifted_relation = math_item(r"5^{10} - 1 = k\cdot33", font_size=76)
        shifted_relation.move_to(power_relation.get_center())
        self.play(
            ReplacementTransform(power_relation, shifted_relation),
            run_time=0.65,
            rate_func=smooth,
        )
        power_relation = shifted_relation
        self.wait(0.95)

        factored_relation = MathTex(
            r"(5^5+1)",
            r"\cdot",
            r"(5^5-1)",
            r"=",
            r"k\cdot33",
            font_size=70,
            color=WHITE_TEXT,
        )
        factored_relation.move_to(power_relation.get_center())
        self.play(
            ReplacementTransform(power_relation, factored_relation),
            run_time=0.75,
            rate_func=smooth,
        )
        power_relation = factored_relation
        self.wait(0.75)

        plus_factor = power_relation[0]
        minus_factor = power_relation[2]
        plus_flash = SurroundingRectangle(
            plus_factor,
            color=HIGHLIGHT_YELLOW,
            buff=0.08,
            stroke_width=5,
        )
        minus_flash = SurroundingRectangle(
            minus_factor,
            color=HIGHLIGHT_YELLOW,
            buff=0.08,
            stroke_width=5,
        )
        self.play(Create(plus_flash), Create(minus_flash), run_time=0.25)
        self.play(
            plus_flash.animate.set_stroke(opacity=0),
            minus_flash.animate.set_stroke(opacity=0),
            plus_factor.animate.set_color(HIGHLIGHT_YELLOW),
            minus_factor.animate.set_color(HIGHLIGHT_YELLOW),
            run_time=0.42,
        )
        self.play(
            plus_factor.animate.set_color(WHITE_TEXT),
            minus_factor.animate.set_color(WHITE_TEXT),
            run_time=0.28,
        )
        self.remove(plus_flash, minus_flash)
        self.wait(0.6)

        p_hint = math_item("p?", font_size=48)
        q_hint = math_item("q?", font_size=48)
        p_hint.next_to(plus_factor, DOWN, buff=0.35)
        q_hint.next_to(minus_factor, DOWN, buff=0.35)
        self.play(
            FadeIn(p_hint, shift=DOWN * 0.08),
            FadeIn(q_hint, shift=DOWN * 0.08),
            run_time=0.45,
        )
        self.wait(0.9)

        gcd_plus = math_item(r"\gcd(5^5+1,33)", font_size=42)
        gcd_minus = math_item(r"\gcd(5^5-1,33)", font_size=42)
        gcd_plus.move_to(p_hint.get_center())
        gcd_minus.move_to(q_hint.get_center())
        self.play(
            Transform(p_hint, gcd_plus),
            Transform(q_hint, gcd_minus),
            run_time=0.65,
            rate_func=smooth,
        )
        self.wait(0.75)

        gcd_group = VGroup(p_hint, q_hint)
        gcd_target = gcd_group.copy().arrange(RIGHT, buff=1.0).move_to(ORIGIN)
        self.play(
            FadeOut(power_relation, shift=DOWN * 0.05),
            Transform(gcd_group, gcd_target),
            run_time=0.75,
            rate_func=smooth,
        )
        self.wait(0.85)

        factors = VGroup(
            math_item("3", font_size=88),
            math_item("11", font_size=88),
        ).arrange(RIGHT, buff=1.9).move_to(ORIGIN)
        self.play(
            Transform(gcd_group, factors),
            run_time=0.7,
            rate_func=smooth,
        )
        self.wait(1.05)

        self.play(
            FadeOut(VGroup(shor, parameters[1], gcd_group)),
            run_time=0.55,
        )
        self.wait(0.3)

        n_factor_form = math_item(r"N=p\cdot q", font_size=48)
        n_factor_form.move_to(UP * 3.12)
        generic_period = math_item(r"f(x+r)=f(x)", font_size=48)
        generic_period.move_to(UP * 1.45)
        self.play(
            Transform(parameters[0], n_factor_form),
            Transform(period_formula, generic_period),
            run_time=0.75,
            rate_func=smooth,
        )
        self.wait(0.8)
