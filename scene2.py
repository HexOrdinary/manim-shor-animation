from manim import *

from computer_chip import make_computer_chip_icon


WHITE_TEXT = WHITE
PRIME_RED = RED
FOUND_YELLOW = YELLOW


def math_item(tex, font_size=88, color=WHITE_TEXT):
    return MathTex(tex, font_size=font_size, color=color)


def target_row(items, y=0, font_size=88, buff=0.28):
    row = VGroup(*[math_item(item, font_size=font_size) for item in items])
    row.arrange(RIGHT, buff=buff).move_to(UP * y)
    return row


def make_prime_row(values, y, color=PRIME_RED):
    numbers = VGroup()
    column_step = 1.2
    start_x = -column_step * 4.5

    for index, value in enumerate(values):
        number = math_item(str(value), font_size=60, color=color)
        number.move_to(RIGHT * (start_x + index * column_step) + UP * y)
        numbers.add(number)

    return numbers


def make_classical_chip():
    return make_computer_chip_icon(size=3.2)


def make_large_number_block():
    rows = 18
    columns = 58
    seed = 29083
    row_mobjects = VGroup()

    for row_index in range(rows):
        chars = []
        for column_index in range(columns):
            if row_index == 0 and column_index < 5:
                chars.append("29083"[column_index])
                continue
            seed = (
                seed * 1103515245
                + 12345
                + row_index * 97
                + column_index * 53
            ) % 2147483647
            chars.append(str(seed % 10))
        row_mobjects.add(
            Text(
                "".join(chars),
                font="Consolas",
                font_size=28,
                color=WHITE_TEXT,
                disable_ligatures=True,
            )
        )

    row_mobjects.arrange(DOWN, buff=0.02, aligned_edge=LEFT)
    max_width = config.frame_width - 0.65
    max_height = config.frame_height - 1.55
    if row_mobjects.width > max_width:
        row_mobjects.scale_to_fit_width(max_width)
    if row_mobjects.height > max_height:
        row_mobjects.scale_to_fit_height(max_height)

    subtitle_space = 1.05
    top_margin = 0.2
    available_bottom = -config.frame_height / 2 + subtitle_space
    available_top = config.frame_height / 2 - top_margin
    row_mobjects.move_to(UP * ((available_top + available_bottom) / 2))
    return row_mobjects


class scene2(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        left_factor = math_item("61")
        right_factor = math_item("53")
        left_factor.move_to(LEFT * 1.5)
        right_factor.move_to(RIGHT * 1.5)

        self.play(
            FadeIn(left_factor, shift=UP * 0.08),
            FadeIn(right_factor, shift=UP * 0.08),
            run_time=0.65,
        )
        self.wait(0.25)

        multiply = math_item(r"\times")
        multiply.move_to(ORIGIN)
        self.play(FadeIn(multiply, scale=0.9), run_time=0.4)
        self.wait(1.7)

        equal = math_item("=")
        product_3233 = math_item("3233")
        first_formula_target = target_row(
            ["61", r"\times", "53", "=", "3233"],
            font_size=88,
            buff=0.75,
        )
        equal.move_to(first_formula_target[3].get_center())
        product_3233.move_to(first_formula_target[4].get_center())

        self.play(
            left_factor.animate.move_to(first_formula_target[0].get_center()),
            multiply.animate.move_to(first_formula_target[1].get_center()),
            right_factor.animate.move_to(first_formula_target[2].get_center()),
            FadeIn(equal, shift=RIGHT * 0.12),
            FadeIn(product_3233, shift=RIGHT * 0.12),
            run_time=0.85,
            rate_func=smooth,
        )
        first_formula = VGroup(
            left_factor,
            multiply,
            right_factor,
            equal,
            product_3233,
        )
        self.wait(2.65)

        self.play(
            first_formula.animate.move_to(UP * 2.7),
            run_time=0.85,
            rate_func=smooth,
        )

        product_29083 = math_item("29083", font_size=94)
        self.play(FadeIn(product_29083, scale=0.92), run_time=0.55)
        self.wait(0.55)

        question_left = math_item("?", font_size=86)
        question_times = math_item(r"\times", font_size=86)
        question_right = math_item("?", font_size=86)
        question_equal = math_item("=", font_size=86)
        question_target = target_row(
            ["?", r"\times", "?", "=", "29083"],
            font_size=86,
            buff=0.75,
        )

        question_left.move_to(question_target[0].get_center())
        question_times.move_to(question_target[1].get_center())
        question_right.move_to(question_target[2].get_center())
        question_equal.move_to(question_target[3].get_center())

        self.play(
            product_29083.animate.move_to(question_target[4].get_center()),
            FadeIn(VGroup(question_left, question_times, question_right, question_equal)),
            run_time=0.85,
            rate_func=smooth,
        )
        self.wait(0.65)

        second_formula = VGroup(
            question_left,
            question_times,
            question_right,
            question_equal,
            product_29083,
        )
        self.play(
            second_formula.animate.move_to(UP * 1.55),
            run_time=2.0,
            rate_func=smooth,
        )
        self.wait(0.25)

        first_prime_row = make_prime_row(
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
            y=0.25,
        )
        second_prime_row = make_prime_row(
            [31, 37, 41, 43, 47, 53, 59, 61, 67, 71],
            y=-0.65,
        )
        third_prime_row = make_prime_row(
            [73, 79, 83, 89, 97, 101, 103, 107, 109, 113],
            y=-1.45,
        )
        found_prime = math_item("127", font_size=72, color=FOUND_YELLOW)
        found_prime.move_to(DOWN * 2.5)
        prime_rows = VGroup(
            first_prime_row,
            second_prime_row,
            third_prime_row,
        )

        for row in [first_prime_row, second_prime_row, third_prime_row]:
            self.play(FadeIn(row, shift=UP * 0.06), run_time=0.45)
            self.wait(0.12)
        self.play(FadeIn(found_prime, scale=0.92), run_time=0.45)
        self.wait(0.55)

        replacement_229 = math_item("229", font_size=86)
        replacement_229.move_to(question_right.get_center())
        self.play(
            found_prime.animate.move_to(question_left.get_center()).scale(86 / 72),
            FadeOut(question_left, scale=0.92),
            run_time=0.9,
            rate_func=smooth,
        )
        self.wait(0.25)
        self.play(
            Transform(question_right, replacement_229),
            run_time=0.55,
            rate_func=smooth,
        )
        self.wait(0.5)

        classical_chip = make_classical_chip().move_to(prime_rows.get_center() + DOWN * 1)
        self.play(
            Transform(prime_rows, classical_chip),
            run_time=0.95,
            rate_func=smooth,
        )
        self.wait(1.85)

        self.play(
            FadeOut(
                VGroup(
                    first_formula,
                    found_prime,
                    question_times,
                    question_right,
                    question_equal,
                    prime_rows,
                )
            ),
            run_time=0.8,
        )
        self.wait(0.25)

        large_number = make_large_number_block()
        self.play(
            Transform(product_29083, large_number),
            run_time=1.15,
            rate_func=smooth,
        )
        self.wait(4.5)
        self.play(FadeOut(product_29083),run_time=0.5)
