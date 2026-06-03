from manim import *

from quantum_chip import make_quantum_chip_icon


WHITE_TEXT = WHITE
ERROR_RED = RED
STANDARD_BLUE = BLUE


def make_rsa_title():
    return Text("RSA", font_size=86, weight=BOLD, color=WHITE_TEXT).to_edge(
        UP, buff=0.45
    )


def text_item(text, font_size=44, color=WHITE_TEXT, font="Consolas", **kwargs):
    return Text(
        text,
        font=font,
        font_size=font_size,
        color=color,
        disable_ligatures=True,
        **kwargs,
    )


def make_standards_block():
    standard_font = "Microsoft YaHei"

    first_row = VGroup(
        text_item("FIPS 203 / ML-KEM", font_size=40, font="Consolas"),
        text_item("用于密钥建立", font_size=32, font=standard_font),
    ).arrange(RIGHT, buff=0.55)

    second_standard = text_item(
        "FIPS 204 / ML-DSA", font_size=40, font="Consolas"
    )
    third_standard = text_item(
        "FIPS 205 / SLH-DSA", font_size=40, font="Consolas"
    )

    signature_label = text_item("用于数字签名", font_size=32, font=standard_font)
    signature_rows = VGroup(second_standard, third_standard).arrange(
        DOWN, buff=0.44, aligned_edge=LEFT
    )
    second_and_third = VGroup(signature_rows, signature_label).arrange(
        RIGHT, buff=0.78
    )
    signature_label.move_to(
        RIGHT * signature_label.get_center()[0] + UP * signature_rows.get_center()[1]
    )

    standards = VGroup(first_row, second_and_third).arrange(
        DOWN, buff=0.48, aligned_edge=LEFT
    )
    standards.move_to(ORIGIN + DOWN * 0.2)
    return standards


class scene4(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        rsa_title = make_rsa_title()
        self.add(rsa_title)
        self.wait(1.6)

        nist = text_item(
            "National Institute of Standards and Technology",
            font_size=32,
            color=WHITE_TEXT,
        )
        nist.next_to(rsa_title, DOWN, buff=0.35)
        self.play(FadeIn(nist, shift=UP * 0.08), run_time=0.55)
        self.wait(3.0)

        standards = make_standards_block()
        self.play(FadeIn(standards, shift=UP * 0.08), run_time=0.75)
        self.wait(3.5)

        strike = Line(
            rsa_title.get_left() + LEFT * 0.18,
            rsa_title.get_right() + RIGHT * 0.18,
            color=ERROR_RED,
            stroke_width=9,
        )
        self.play(Create(strike), run_time=0.35)
        self.wait(1.25)
        self.play(
            FadeOut(VGroup(rsa_title, strike), shift=DOWN * 0.08),
            standards.animate.move_to(UP * 2.1),
            FadeOut(nist, shift=UP * 0.08),
            run_time=0.85,
            rate_func=smooth,
        )
        self.wait(0.95)

        quantum_chip = make_quantum_chip_icon(size=2.25).move_to(
            LEFT * 2.55 + DOWN * 1.25
        )
        timeout = text_item("Timeout", font_size=54, color=ERROR_RED).move_to(
            RIGHT * 2.35 + DOWN * 1.25
        )
        self.play(
            FadeIn(quantum_chip, scale=0.86),
            run_time=0.5,
        )
        self.wait(1.2)
        self.play(
            FadeIn(timeout, shift=RIGHT * 0.12),
            run_time=0.3,
        )
        self.wait(0.3)

        twenty_hours = text_item("20 hours", font_size=54, color=WHITE_TEXT).move_to(
            timeout.get_center() + UP * 0.35
        )
        self.play(Transform(timeout, twenty_hours), run_time=0.65, rate_func=smooth)
        self.wait(6.0)

        exponential = MathTex(r"O(2^n)", font_size=58, color=WHITE_TEXT)
        exponential.next_to(timeout, DOWN, buff=0.32)
        self.play(FadeIn(exponential, shift=UP * 0.08), run_time=0.45)
        self.wait(1.5)

        polynomial = MathTex(
            r"O(2^n) \rightarrow O(n^k)",
            font_size=58,
            color=WHITE_TEXT,
        ).move_to(exponential.get_center())
        self.play(Transform(exponential, polynomial), run_time=0.7, rate_func=smooth)
        self.wait(1.8)

        shor = text_item("Shor", font_size=82, color=WHITE_TEXT)
        shor.to_edge(DOWN, buff=0.42)
        self.play(FadeIn(shor, shift=UP * 0.1), run_time=0.55)
        self.wait(0.7)

        self.play(
            FadeOut(VGroup(standards, quantum_chip, timeout, exponential), run_time=0.65),
            shor.animate.to_edge(UP, buff=0.45),
            run_time=0.35,
            rate_func=smooth,
        )
        self.wait(0.35)
