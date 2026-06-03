from manim import *

from computer_chip import make_computer_chip_icon
from scene1 import make_hacker_icon


WHITE_TEXT = WHITE
CHECK_YELLOW = YELLOW
ERROR_RED = RED


def math_item(tex, font_size=82, color=WHITE_TEXT):
    return MathTex(tex, font_size=font_size, color=color)


def text_item(text, font_size=72, color=WHITE_TEXT):
    return Text(
        text,
        font="Consolas",
        font_size=font_size,
        color=color,
        disable_ligatures=True,
    )


def make_rsa_title():
    return Text("RSA", font_size=86, weight=BOLD, color=WHITE_TEXT).to_edge(UP, buff=0.45)


def make_algorithm_block():
    formulas = [
        r"N=p\cdot q",
        r"\phi(N)=(p-1)(q-1)",
        r"1<e<\phi(N),\ \gcd(e,\phi(N))=1",
        r"d=e^{-1}\bmod\phi(N)",
        r"c=m^e\bmod N",
        r"m=c^d\bmod N",
    ]
    block = VGroup(*[math_item(formula, font_size=46) for formula in formulas])
    block.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
    return block


class scene3(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        rsa_title = make_rsa_title()
        self.play(FadeIn(rsa_title, shift=UP * 0.1), run_time=0.55)
        self.wait(1.75)

        multiplication = VGroup(
            text_item("3221225473", font_size=58),
            math_item(r"\times", font_size=68),
            text_item("4294967291", font_size=58),
        ).arrange(RIGHT, buff=0.28).move_to(UP * 0.18)

        check = Text("√", font="Consolas", font_size=82, color=CHECK_YELLOW)
        check.next_to(multiplication, RIGHT, buff=0.45)
        self.play(FadeIn(multiplication, shift=UP * 0.08), run_time=0.65)
        self.wait(0.45)
        self.play(FadeIn(check, scale=0.85), run_time=0.38)
        self.wait(1.0)

        big_number = text_item("13835058043471003643", font_size=58).move_to(ORIGIN)
        multiplication_check = VGroup(multiplication, check)
        self.play(
            ReplacementTransform(multiplication_check, big_number),
            run_time=0.95,
            rate_func=smooth,
        )
        self.wait(0.8)

        cross = Text("×", font="Consolas", font_size=96, color=ERROR_RED)
        cross.next_to(big_number, RIGHT, buff=0.52)
        self.play(FadeIn(cross, scale=0.88), run_time=0.4)
        self.wait(2.1)

        algorithm = make_algorithm_block().move_to(ORIGIN)
        self.play(
            FadeOut(cross, scale=0.92),
            ReplacementTransform(big_number, algorithm),
            run_time=1.05,
            rate_func=smooth,
        )
        rsa_algorithm = algorithm
        self.wait(5.0)

        npq_formula = MathTex(
            "N",
            "=",
            "p",
            r"\cdot",
            "q",
            font_size=92,
            color=WHITE_TEXT,
        ).move_to(ORIGIN)
        self.play(
            ReplacementTransform(rsa_algorithm, npq_formula),
            run_time=0.9,
            rate_func=smooth,
        )
        rsa_algorithm = npq_formula
        self.wait(0.35)

        n_flash = SurroundingRectangle(rsa_algorithm[0], color=CHECK_YELLOW, buff=0.08, stroke_width=5)
        self.play(Create(n_flash), run_time=0.25)
        self.play(
            n_flash.animate.set_stroke(opacity=0),
            rsa_algorithm[0].animate.set_color(CHECK_YELLOW),
            run_time=0.4,
        )
        self.play(rsa_algorithm[0].animate.set_color(WHITE_TEXT), run_time=0.35)
        self.remove(n_flash)
        self.wait(0.35)

        hacker = make_hacker_icon().scale(0.50).move_to(LEFT * 4.35 + DOWN * 0.15)
        self.play(
            rsa_algorithm.animate.move_to(RIGHT * 2.15 + DOWN * 0.12),
            FadeIn(hacker, shift=RIGHT * 0.18),
            run_time=0.9,
            rate_func=smooth,
        )
        self.wait(0.8)

        p_flash = SurroundingRectangle(rsa_algorithm[2], color=CHECK_YELLOW, buff=0.08, stroke_width=5)
        q_flash = SurroundingRectangle(rsa_algorithm[4], color=CHECK_YELLOW, buff=0.08, stroke_width=5)
        self.play(Create(p_flash), Create(q_flash), run_time=0.25)
        self.play(
            p_flash.animate.set_stroke(opacity=0),
            q_flash.animate.set_stroke(opacity=0),
            rsa_algorithm[2].animate.set_color(CHECK_YELLOW),
            rsa_algorithm[4].animate.set_color(CHECK_YELLOW),
            run_time=0.4,
        )
        self.play(
            rsa_algorithm[2].animate.set_color(WHITE_TEXT),
            rsa_algorithm[4].animate.set_color(WHITE_TEXT),
            run_time=0.35,
        )
        self.remove(p_flash, q_flash)
        self.wait(4.35)

        n_bound = math_item(r">10^{2000}", font_size=30, color=CHECK_YELLOW)
        p_bound = math_item(r">10^{1000}", font_size=26, color=CHECK_YELLOW)
        q_bound = math_item(r">10^{1000}", font_size=26, color=CHECK_YELLOW)
        n_bound.next_to(rsa_algorithm[0], DOWN, buff=0.22)
        p_bound.next_to(rsa_algorithm[2], DOWN, buff=0.22).shift(LEFT * 0.1)
        q_bound.next_to(rsa_algorithm[4], DOWN, buff=0.22).shift(RIGHT * 0.1)
        size_bounds = VGroup(n_bound, p_bound, q_bound)
        self.play(FadeIn(size_bounds, shift=DOWN * 0.08), run_time=0.55)
        self.wait(1.0)
        rsa_algorithm = VGroup(rsa_algorithm, size_bounds)

        chip = make_computer_chip_icon(size=1.0).move_to(hacker.get_corner(DR) + RIGHT * 0.5 + DOWN * 0.15)
        chip.set_z_index(1)
        rsa_algorithm.set_z_index(2)
        self.play(FadeIn(chip, scale=0.5), run_time=0.45)
        self.play(
            rsa_algorithm.animate.scale(0.2).move_to(chip.get_center()),
            run_time=0.85,
            rate_func=smooth,
        )
        self.wait(1.35)

        timeout = VGroup(
            text_item("TimeoutError:", font_size=34, color=ERROR_RED),
            text_item("factorization exceeded", font_size=30, color=ERROR_RED),
            text_item("max iterations", font_size=30, color=ERROR_RED)
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        timeout.move_to(RIGHT * 3 + DOWN * 0.1)
        self.play(FadeIn(timeout, shift=RIGHT * 0.12), run_time=0.55)
        self.wait(5.2)

        self.play(
            FadeOut(VGroup(hacker, chip, rsa_algorithm, timeout)),
            run_time=0.65,
        )
