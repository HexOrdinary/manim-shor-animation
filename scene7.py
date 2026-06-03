from manim import *

from computer_chip import make_computer_chip_icon
from quantum_chip import make_quantum_chip_icon


WHITE_TEXT = WHITE
HIGHLIGHT_YELLOW = YELLOW
SLOW_RED = RED
FAST_GREEN = GREEN


def math_item(tex, font_size=60, color=WHITE_TEXT):
    return MathTex(tex, font_size=font_size, color=color)


def make_carryover_formulas():
    n_formula = MathTex(
        "N",
        "=",
        "p",
        r"\cdot",
        "q",
        font_size=64,
        color=WHITE_TEXT,
    ).move_to(UP * 2.95)
    n_formula[0].set_color(HIGHLIGHT_YELLOW)

    period_formula = MathTex(
        "f(x+",
        "r",
        ")=f(x)",
        font_size=64,
        color=WHITE_TEXT,
    ).move_to(UP * 2.18)
    period_formula[1].set_color(HIGHLIGHT_YELLOW)

    return n_formula, period_formula


def make_prime_row(values):
    row = VGroup(
        *[math_item(str(value), font_size=38) for value in values]
    ).arrange(RIGHT, buff=0.28)
    return row


def make_prime_table():
    rows = VGroup(
        make_prime_row([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
        make_prime_row([31, 37, 41, 43, 47, 53, 59, 61, 67]),
        make_prime_row([71, 73, 79, 83, 89, 97, 101, 103, 107]),
    )
    ellipsis = math_item(r"\cdots", font_size=50)
    root_limit = math_item(r"\sqrt{N}", font_size=54)
    table = VGroup(*rows, ellipsis, root_limit).arrange(DOWN, buff=0.34)
    table.move_to(DOWN * 0.38)

    max_width = config.frame_width - 1.25
    if table.width > max_width:
        table.scale_to_fit_width(max_width)

    return table, rows, ellipsis, root_limit


def make_progress_bar(color, width=3.65, height=0.24):
    outline = RoundedRectangle(
        width=width,
        height=height,
        corner_radius=0.06,
        fill_opacity=0,
        stroke_color=color,
        stroke_width=3,
    )
    fill = Rectangle(
        width=0.01,
        height=height * 0.72,
        fill_color=color,
        fill_opacity=1,
        stroke_width=0,
    )
    fill.move_to(outline.get_left() + RIGHT * fill.width / 2)
    return VGroup(outline, fill)


def set_bar_progress(fill, outline, progress):
    target_width = max(outline.width * progress, 0.01)
    fill.generate_target()
    fill.target.stretch_to_fit_width(target_width)
    fill.target.move_to(outline.get_left() + RIGHT * target_width / 2)
    return MoveToTarget(fill)


class scene7(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        n_formula, period_formula = make_carryover_formulas()
        self.add(n_formula, period_formula)
        self.wait(0.35)
        self.play(
            n_formula[0].animate.set_color(WHITE_TEXT),
            period_formula[1].animate.set_color(WHITE_TEXT),
            run_time=0.35,
        )
        self.wait(0.2)

        question = math_item("?", font_size=176)
        self.play(FadeIn(question, scale=0.95), run_time=0.3)
        self.wait(0.5)
        self.play(
            question.animate.scale(0.42).to_corner(UL, buff=0.45),
            run_time=0.5,
            rate_func=smooth,
        )
        self.wait(0.3)

        prime_table, prime_rows, ellipsis, root_limit = make_prime_table()
        for row in prime_rows:
            self.play(
                LaggedStart(
                    *[FadeIn(number, shift=UP * 0.05) for number in row],
                    lag_ratio=0.04,
                ),
                run_time=0.3,
            )
            self.wait(0.08)

        self.wait(0.2)
        self.play(FadeIn(ellipsis, scale=0.92), run_time=0.3)
        self.wait(0.3)
        self.play(FadeIn(root_limit, shift=UP * 0.06), run_time=0.3)
        self.wait(0.4)

        classical_chip = make_computer_chip_icon(size=2.45).move_to(
            LEFT * 2.55 + DOWN * 0.34
        )
        self.play(
            prime_table.animate.shift(RIGHT * 3.36),
            FadeIn(classical_chip, scale=0.86),
            run_time=0.8,
            rate_func=smooth,
        )
        self.wait(0.55)

        chip_right = classical_chip.get_center() + RIGHT * 2.6
        r_symbol = math_item("r", font_size=54, color=SLOW_RED).move_to(
            chip_right + UP * 0.8
        )
        sqrt_symbol = math_item(r"\sqrt{N}", font_size=42, color=HIGHLIGHT_YELLOW)
        sqrt_symbol.move_to(chip_right + DOWN * 0.8)

        self.play(
            ReplacementTransform(prime_table, sqrt_symbol),
            TransformFromCopy(period_formula[1], r_symbol),
            run_time=0.9,
            rate_func=smooth,
        )
        self.wait(0.45)

        r_bar = make_progress_bar(SLOW_RED).next_to(r_symbol, RIGHT, buff=0.48)
        sqrt_bar = make_progress_bar(HIGHLIGHT_YELLOW).next_to(
            sqrt_symbol, RIGHT, buff=0.28
        )
        self.play(FadeIn(r_bar), FadeIn(sqrt_bar), run_time=0.35)
        self.wait(0.15)
        self.play(
            set_bar_progress(r_bar[1], r_bar[0], 0.18),
            set_bar_progress(sqrt_bar[1], sqrt_bar[0], 0.56),
            run_time=2.4,
            rate_func=linear,
        )
        self.wait(0.45)

        quantum_chip = make_quantum_chip_icon(size=2.45).move_to(
            classical_chip.get_center()
        )
        self.play(
            Transform(classical_chip, quantum_chip),
            r_symbol.animate.set_color(FAST_GREEN),
            r_bar[0].animate.set_stroke(color=FAST_GREEN),
            r_bar[1].animate.set_fill(FAST_GREEN),
            run_time=0.65,
            rate_func=smooth,
        )
        self.wait(0.18)
        self.play(
            set_bar_progress(r_bar[1], r_bar[0], 0.96),
            set_bar_progress(sqrt_bar[1], sqrt_bar[0], 0.68),
            run_time=0.72,
            rate_func=smooth,
        )
        self.wait(0.4)

        self.play(
            FadeOut(
                VGroup(
                    n_formula,
                    period_formula,
                    question,
                    r_symbol,
                    sqrt_symbol,
                    r_bar,
                    sqrt_bar,
                )
            ),
            run_time=0.35,
        )
        self.wait(0.45)
