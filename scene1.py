from manim import *
import numpy as np


ICON_BLUE = BLUE_E
LINE_BLUE = BLUE
SERVER_BODY = "#D8E2F0"
HACKER_RED = "#E50914"
HACKER_DARK_RED = "#4A0508"


def make_phone_icon():
    body = RoundedRectangle(
        width=2.65,
        height=4.55,
        corner_radius=0.22,
        color=GREY,
        fill_color=GREY,
        fill_opacity=1,
        stroke_width=0,
    )

    screen = RoundedRectangle(
        width=2.15,
        height=3.15,
        corner_radius=0.04,
        color=BLACK,
        fill_color=BLACK,
        fill_opacity=1,
        stroke_width=0,
    ).move_to(UP * 0.1)

    speaker = RoundedRectangle(
        width=0.62,
        height=0.11,
        corner_radius=0.05,
        color=BLACK,
        fill_color=BLACK,
        fill_opacity=1,
        stroke_width=0,
    ).move_to(UP * 1.94)

    camera = Circle(
        radius=0.035,
        color=BLACK,
        fill_color=BLACK,
        fill_opacity=1,
        stroke_width=0,
    ).next_to(speaker, LEFT, buff=0.12)

    home_outer = Circle(
        radius=0.23,
        color=BLACK,
        fill_color=BLACK,
        fill_opacity=1,
        stroke_width=0,
    ).move_to(DOWN * 1.9)

    return VGroup(body, screen, speaker, camera, home_outer).scale(1.35)


def make_chat_icon():
    bubble_body = RoundedRectangle(
        width=4.4,
        height=3.05,
        corner_radius=0.33,
        color=ICON_BLUE,
        fill_color=ICON_BLUE,
        fill_opacity=1,
        stroke_width=0,
    ).move_to(UP * 0.24)

    tail = Polygon(
        RIGHT * 0.58 + DOWN * 1.18,
        RIGHT * 1.72 + DOWN * 2.05,
        RIGHT * 1.72 + DOWN * 1.18,
        color=ICON_BLUE,
        fill_color=ICON_BLUE,
        fill_opacity=1,
        stroke_width=0,
    )

    message_lines = VGroup(
        Rectangle(
            width=3.2,
            height=0.18,
            color=LINE_BLUE,
            fill_color=LINE_BLUE,
            fill_opacity=1,
            stroke_width=0,
        ).move_to(UP * 0.95),
        Rectangle(
            width=3.2,
            height=0.18,
            color=LINE_BLUE,
            fill_color=LINE_BLUE,
            fill_opacity=1,
            stroke_width=0,
        ).move_to(UP * 0.28),
        Rectangle(
            width=2.55,
            height=0.18,
            color=LINE_BLUE,
            fill_color=LINE_BLUE,
            fill_opacity=1,
            stroke_width=0,
        ).move_to(LEFT * 0.33 + DOWN * 0.39),
    )

    return VGroup(bubble_body, tail, message_lines).scale(1.18)


def make_email_icon():
    stroke_width = 12

    envelope = RoundedRectangle(
        width=4.35,
        height=2.85,
        corner_radius=0.14,
        color=ICON_BLUE,
        fill_opacity=0,
        stroke_width=stroke_width,
    )

    flap = VGroup(
        Line(
            LEFT * 2.08 + UP * 1.22,
            ORIGIN + DOWN * 0.22,
            color=ICON_BLUE,
            stroke_width=stroke_width,
        ),
        Line(
            RIGHT * 2.08 + UP * 1.22,
            ORIGIN + DOWN * 0.22,
            color=ICON_BLUE,
            stroke_width=stroke_width,
        ),
    )

    lower_folds = VGroup(
        Line(
            LEFT * 2.08 + DOWN * 1.22,
            LEFT * 0.58 + DOWN * 0.35,
            color=ICON_BLUE,
            stroke_width=stroke_width,
        ),
        Line(
            RIGHT * 2.08 + DOWN * 1.22,
            RIGHT * 0.58 + DOWN * 0.35,
            color=ICON_BLUE,
            stroke_width=stroke_width,
        ),
    )

    return VGroup(envelope, flap, lower_folds).scale(1.16)


def make_web_icon():
    stroke_width = 12

    window = RoundedRectangle(
        width=4.25,
        height=3.55,
        corner_radius=0.24,
        color=ICON_BLUE,
        fill_opacity=0,
        stroke_width=stroke_width,
    )

    top_bar = Line(
        LEFT * 2.08 + UP * 1.18,
        RIGHT * 2.08 + UP * 1.18,
        color=ICON_BLUE,
        stroke_width=stroke_width,
    )

    dots = VGroup(
        *[
            Circle(
                radius=0.12,
                color=ICON_BLUE,
                fill_color=ICON_BLUE,
                fill_opacity=1,
                stroke_width=0,
            ).move_to(LEFT * (1.7 - i * 0.34) + UP * 1.45)
            for i in range(3)
        ]
    )

    return VGroup(window, top_bar, dots).scale(1.05)


def make_yuan_icon():
    left_arm = Polygon(
        [-1.35, 1.8, 0],
        [-0.88, 1.8, 0],
        [0.0, 0.35, 0],
        [-0.42, 0.35, 0],
        color=ICON_BLUE,
        fill_color=ICON_BLUE,
        fill_opacity=1,
        stroke_width=0,
    )
    right_arm = Polygon(
        [0.88, 1.8, 0],
        [1.35, 1.8, 0],
        [0.42, 0.35, 0],
        [0.0, 0.35, 0],
        color=ICON_BLUE,
        fill_color=ICON_BLUE,
        fill_opacity=1,
        stroke_width=0,
    )

    stem = Rectangle(
        width=0.52,
        height=2.35,
        color=ICON_BLUE,
        fill_color=ICON_BLUE,
        fill_opacity=1,
        stroke_width=0,
    ).move_to(DOWN * 0.78)

    upper_bar = Rectangle(
        width=2.7,
        height=0.44,
        color=ICON_BLUE,
        fill_color=ICON_BLUE,
        fill_opacity=1,
        stroke_width=0,
    ).move_to(DOWN * 0.12)

    lower_bar = Rectangle(
        width=2.7,
        height=0.44,
        color=ICON_BLUE,
        fill_color=ICON_BLUE,
        fill_opacity=1,
        stroke_width=0,
    ).move_to(DOWN * 0.9)

    return VGroup(left_arm, right_arm, stem, upper_bar, lower_bar).scale(1.35)


def make_lock_icon():
    shackle = Arc(
        radius=1.0,
        start_angle=0,
        angle=PI,
        color=LINE_BLUE,
        stroke_width=14,
    ).move_to(UP * 0.75)

    body = RoundedRectangle(
        width=2.6,
        height=1.8,
        corner_radius=0.18,
        color=LINE_BLUE,
        fill_color=ICON_BLUE,
        fill_opacity=1,
        stroke_width=4,
    ).move_to(DOWN * 0.55)

    keyhole_top = Circle(
        radius=0.18,
        color=YELLOW,
        fill_color=YELLOW,
        fill_opacity=1,
        stroke_width=0,
    ).move_to(DOWN * 0.35)

    keyhole_bottom = Rectangle(
        width=0.16,
        height=0.45,
        color=YELLOW,
        fill_color=YELLOW,
        fill_opacity=1,
        stroke_width=0,
    )
    keyhole_bottom.next_to(keyhole_top, DOWN, buff=-0.03)

    return VGroup(shackle, body, keyhole_top, keyhole_bottom)


def make_server_icon():
    rows = VGroup()

    for y in [0.75, 0.0, -0.75]:
        rack = RoundedRectangle(
            width=2.85,
            height=0.58,
            corner_radius=0.12,
            color=SERVER_BODY,
            fill_color=SERVER_BODY,
            fill_opacity=1,
            stroke_width=0,
        ).move_to(UP * y)

        status_bar = RoundedRectangle(
            width=1.58,
            height=0.14,
            corner_radius=0.07,
            color=LINE_BLUE,
            fill_color=LINE_BLUE,
            fill_opacity=1,
            stroke_width=0,
        ).move_to(LEFT * 0.36 + UP * y)

        status_dot = Circle(
            radius=0.085,
            color=LINE_BLUE,
            fill_color=LINE_BLUE,
            fill_opacity=1,
            stroke_width=0,
        ).move_to(RIGHT * 0.92 + UP * y)

        rows.add(VGroup(rack, status_bar, status_dot))

    return rows


def make_user_icon():
    head = Circle(
        radius=0.46,
        color=ICON_BLUE,
        fill_color=ICON_BLUE,
        fill_opacity=1,
        stroke_width=0,
    ).move_to(UP * 0.68)

    shoulder_points = [
        [-1.02, -0.92, 0],
        [1.02, -0.92, 0],
    ]
    shoulder_points += [
        [1.02 * np.cos(theta), -0.92 + 1.14 * np.sin(theta), 0]
        for theta in np.linspace(0, PI, 36)
    ]

    body = Polygon(
        *shoulder_points,
        color=ICON_BLUE,
        fill_color=ICON_BLUE,
        fill_opacity=1,
        stroke_width=0,
    ).move_to(DOWN * 0.38)

    return VGroup(head, body)


def make_key_icon(color=YELLOW):
    ring = Circle(
        radius=0.2,
        color=color,
        fill_opacity=0,
        stroke_width=6,
    ).move_to(UP * 0.44)

    shaft = Line(
        UP * 0.24,
        DOWN * 0.5,
        color=color,
        stroke_width=6,
    )

    teeth = VGroup(
        Line(
            DOWN * 0.26,
            RIGHT * 0.25 + DOWN * 0.26,
            color=color,
            stroke_width=6,
        ),
        Line(
            RIGHT * 0.25 + DOWN * 0.26,
            RIGHT * 0.25 + DOWN * 0.47,
            color=color,
            stroke_width=6,
        ),
    )

    return VGroup(ring, shaft, teeth)


def make_hacker_icon():
    stroke = 10

    hood_outer = Arc(
        radius=1.45,
        start_angle=15 * DEGREES,
        angle=150 * DEGREES,
        color=HACKER_RED,
        stroke_width=stroke,
    ).move_to(UP * 0.35)

    hood_sides = VGroup(
        Line(
            LEFT * 1.42 + UP * 0.72,
            LEFT * 0.62 + DOWN * 1.18,
            color=HACKER_RED,
            stroke_width=stroke,
        ),
        Line(
            RIGHT * 1.42 + UP * 0.72,
            RIGHT * 0.62 + DOWN * 1.18,
            color=HACKER_RED,
            stroke_width=stroke,
        ),
    )

    face_shadow = Polygon(
        LEFT * 0.88 + UP * 0.36,
        RIGHT * 0.88 + UP * 0.36,
        RIGHT * 0.42 + DOWN * 0.74,
        ORIGIN + DOWN * 1.05,
        LEFT * 0.42 + DOWN * 0.74,
        color=HACKER_DARK_RED,
        fill_color=HACKER_DARK_RED,
        fill_opacity=1,
        stroke_width=0,
    )

    mask = RoundedRectangle(
        width=1.35,
        height=0.52,
        corner_radius=0.12,
        color=HACKER_RED,
        fill_color=BLACK,
        fill_opacity=1,
        stroke_width=7,
    ).move_to(DOWN * 0.1)

    eyes = VGroup(
        Polygon(
            LEFT * 0.45 + UP * 0.01,
            LEFT * 0.18 + UP * 0.08,
            LEFT * 0.24 + DOWN * 0.07,
            color=HACKER_RED,
            fill_color=HACKER_RED,
            fill_opacity=1,
            stroke_width=0,
        ),
        Polygon(
            RIGHT * 0.45 + UP * 0.01,
            RIGHT * 0.18 + UP * 0.08,
            RIGHT * 0.24 + DOWN * 0.07,
            color=HACKER_RED,
            fill_color=HACKER_RED,
            fill_opacity=1,
            stroke_width=0,
        ),
    )

    shoulders = VGroup(
        Line(
            LEFT * 0.72 + DOWN * 1.08,
            LEFT * 1.82 + DOWN * 1.82,
            color=HACKER_RED,
            stroke_width=stroke,
        ),
        Line(
            RIGHT * 0.72 + DOWN * 1.08,
            RIGHT * 1.82 + DOWN * 1.82,
            color=HACKER_RED,
            stroke_width=stroke,
        ),
    )

    terminal = RoundedRectangle(
        width=3.7,
        height=1.08,
        corner_radius=0.12,
        color=HACKER_RED,
        fill_color=BLACK,
        fill_opacity=1,
        stroke_width=7,
    ).move_to(DOWN * 2.0)

    prompt_mark = VGroup(
        Line(
            LEFT * 1.38 + DOWN * 1.92,
            LEFT * 1.18 + DOWN * 2.08,
            color=HACKER_RED,
            stroke_width=7,
        ),
        Line(
            LEFT * 1.38 + DOWN * 2.24,
            LEFT * 1.18 + DOWN * 2.08,
            color=HACKER_RED,
            stroke_width=7,
        ),
    )
    code_line = Line(
        LEFT * 0.78 + DOWN * 2.22,
        RIGHT * 0.65 + DOWN * 2.22,
        color=HACKER_RED,
        stroke_width=7,
    )
    cursor = Line(
        RIGHT * 0.92 + DOWN * 2.23,
        RIGHT * 1.24 + DOWN * 2.23,
        color=HACKER_RED,
        stroke_width=7,
    )

    return VGroup(
        shoulders,
        hood_outer,
        hood_sides,
        face_shadow,
        mask,
        eyes,
        terminal,
        prompt_mark,
        code_line,
        cursor,
    ).scale(1.12)


class scene1(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        phone = make_phone_icon().move_to(DOWN * 5.2)
        self.play(phone.animate.move_to(ORIGIN), run_time=0.8, rate_func=smooth)

        screen_cover = phone[1].copy()
        screen_cover.set_z_index(4)
        full_black = Rectangle(
            width=config.frame_width + 0.2,
            height=config.frame_height + 0.2,
            color=BLACK,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0,
        ).set_z_index(4)
        phone_shell = VGroup(phone[0], phone[2], phone[3], phone[4])
        self.add(screen_cover)
        self.play(
            Transform(screen_cover, full_black),
            FadeOut(phone_shell, scale=1.08),
            run_time=0.8,
            rate_func=smooth,
        )
        self.camera.background_color = BLACK
        self.remove(phone, screen_cover)

        icons = VGroup(
            make_chat_icon(),
            make_email_icon(),
            make_web_icon(),
            make_yuan_icon(),
        )
        icons.arrange(RIGHT, buff=1.1).scale(0.42).move_to(ORIGIN)

        frame = Square(
            side_length=5.0,
            color=LINE_BLUE,
            stroke_width=8,
            fill_opacity=0,
        )
        frame.surround(icons, buff=0.42)

        protected_apps = VGroup(icons, frame)
        small_protected_apps = protected_apps.copy().scale(0.34).move_to(ORIGIN)
        lock = make_lock_icon().scale(0.65).move_to(ORIGIN)

        for index, icon in enumerate(icons):
            self.play(FadeIn(icon, scale=0.88), run_time=0.7)
            if index < len(icons) - 1:
                self.wait(0.25)

        self.play(Create(frame), run_time=0.5)
        self.play(
            Transform(protected_apps, small_protected_apps),
            run_time=0.5,
            rate_func=smooth,
        )
        self.play(Transform(protected_apps, lock), run_time=1.2)
        self.play(
            protected_apps.animate.move_to(LEFT * 3.0),
            run_time=0.9,
            rate_func=smooth,
        )

        rsa_text = Text("RSA", font_size=88, weight="BOLD", color=WHITE)
        rsa_text.to_corner(UR, buff=0.82).shift(LEFT * 2 + DOWN * 0.15)
        self.play(FadeIn(rsa_text, shift=UP * 0.12), run_time=0.55)

        self.wait(5)

        server_icon = make_server_icon().scale(0.60).move_to(LEFT * 3.0 + UP * 3)
        user_icon = make_user_icon().scale(0.65).move_to(LEFT * 3.0 + DOWN * 3)
        server_arrow = Arrow(
            server_icon.get_bottom() + DOWN * 0.12,
            protected_apps.get_top() + UP * 0.18,
            color=WHITE,
            buff=0,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.5,
        )
        user_arrow = Arrow(
            protected_apps.get_bottom() + DOWN * 0.18,
            user_icon.get_top() + UP * 0.12,
            color=WHITE,
            buff=0,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.5,
        )
        server_key = make_key_icon(YELLOW).scale(0.72).move_to(
            server_arrow.get_center() + RIGHT * 0.48
        )
        user_key = make_key_icon(RED).rotate(PI).scale(0.72).move_to(
            user_arrow.get_center() + RIGHT * 0.48
        )

        self.play(
            FadeIn(server_icon, shift=DOWN * 0.12),
            GrowArrow(server_arrow),
            FadeIn(server_key, scale=0.9),
            run_time=0.9,
        )
        self.wait(1.5)
        self.play(
            FadeIn(user_icon, shift=UP * 0.12),
            GrowArrow(user_arrow),
            FadeIn(user_key, scale=0.9),
            run_time=0.9,
        )
        self.wait(1.3)

        hacker = make_hacker_icon().scale(0.55).move_to(RIGHT * 7.1)
        self.play(
            FadeIn(hacker, shift=LEFT * 0.35),
            hacker.animate.move_to(LEFT * 0.62 + DOWN * 0.02),
            run_time=1.15,
            rate_func=smooth,
        )

        ripple = Circle(
            radius=0.72,
            color=LINE_BLUE,
            fill_opacity=0,
            stroke_width=7,
        ).move_to(protected_apps.get_center())
        self.add(ripple)
        self.play(
            ripple.animate.scale(3.1).set_stroke(opacity=0, width=1),
            protected_apps.animate.scale(1.08),
            hacker.animate.move_to(RIGHT * 5.3 + UP * 0.22).rotate(-18 * DEGREES),
            run_time=0.85,
            rate_func=smooth,
        )
        self.play(protected_apps.animate.scale(1 / 1.08), run_time=0.25)
        self.remove(ripple)

        scene_objects = VGroup(
            server_icon,
            server_arrow,
            server_key,
            user_icon,
            user_arrow,
            user_key,
            hacker,
        )
        self.play(FadeOut(scene_objects), run_time=1.0)
        self.play(
            rsa_text.animate.move_to(UP * 3),
            protected_apps.animate.move_to(ORIGIN),
            run_time=0.8,
            rate_func=smooth,
        )
        self.wait(3)
        rsa_formula = MathTex(
            r"N = p \times q",
            font_size=96,
            color=WHITE,
        ).move_to(ORIGIN)
        self.play(
            Transform(protected_apps, rsa_formula),
            run_time=1.0,
            rate_func=smooth,
        )
        self.wait(3.3)
        last_objects = VGroup(
            rsa_text,
            protected_apps,
        )
        self.play(FadeOut(last_objects), run_time=0.5)
