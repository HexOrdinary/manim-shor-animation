from manim import *
import numpy as np


WHITE_TEXT = WHITE
SPHERE_BLUE = BLUE_E
GRID_BLUE = BLUE_B
VECTOR_TEAL = TEAL_A
PLANE_BLUE = BLUE_D
AMPLITUDE_ALPHA = YELLOW
AMPLITUDE_BETA = GREEN
PHASE_PURPLE = PURPLE_A


def sphere_point(radius, theta, phi):
    return np.array(
        [
            radius * np.sin(theta) * np.cos(phi),
            radius * np.sin(theta) * np.sin(phi),
            radius * np.cos(theta),
        ]
    )


def make_wire_sphere(radius=2.15):
    surface = Surface(
        lambda u, v: sphere_point(radius, u, v),
        u_range=[0, PI],
        v_range=[0, TAU],
        resolution=(28, 56),
        fill_color=SPHERE_BLUE,
        fill_opacity=0.18,
        stroke_width=0,
    )

    grid = VGroup()
    for theta in np.linspace(PI / 10, 9 * PI / 10, 9):
        grid.add(
            ParametricFunction(
                lambda t, theta=theta: sphere_point(radius, theta, t),
                t_range=[0, TAU],
                color=GRID_BLUE,
                stroke_opacity=0.45,
                stroke_width=1.4,
            )
        )

    for phi in np.linspace(0, TAU, 16, endpoint=False):
        grid.add(
            ParametricFunction(
                lambda t, phi=phi: sphere_point(radius, t, phi),
                t_range=[0, PI],
                color=GRID_BLUE,
                stroke_opacity=0.45,
                stroke_width=1.4,
            )
        )

    return VGroup(surface, grid)


def make_xoy_plane(radius=2.15):
    side = radius * 2.7
    plane = Surface(
        lambda u, v: np.array([u, v, 0]),
        u_range=[-side / 2, side / 2],
        v_range=[-side / 2, side / 2],
        resolution=(2, 2),
        fill_color=PLANE_BLUE,
        fill_opacity=0.16,
        stroke_color=GRID_BLUE,
        stroke_width=1,
    )
    border = Polygon(
        [-side / 2, -side / 2, 0],
        [side / 2, -side / 2, 0],
        [side / 2, side / 2, 0],
        [-side / 2, side / 2, 0],
        color=GRID_BLUE,
        fill_opacity=0,
        stroke_opacity=0.65,
        stroke_width=2,
    )
    return VGroup(plane, border)


def make_axes(radius=2.15):
    axis_length = radius * 1.32
    return VGroup(
        Arrow3D(
            start=[-axis_length, 0, 0],
            end=[axis_length, 0, 0],
            thickness=0.012,
            height=0.16,
            base_radius=0.045,
            color=WHITE_TEXT,
        ),
        Arrow3D(
            start=[0, -axis_length, 0],
            end=[0, axis_length, 0],
            thickness=0.012,
            height=0.16,
            base_radius=0.045,
            color=WHITE_TEXT,
        ),
        Arrow3D(
            start=[0, 0, -axis_length],
            end=[0, 0, axis_length],
            thickness=0.012,
            height=0.16,
            base_radius=0.045,
            color=WHITE_TEXT,
        ),
    )


def make_phase_arc(phi, radius=0.72):
    arc = Arc(
        radius=radius,
        start_angle=0,
        angle=phi,
        color=PHASE_PURPLE,
        stroke_width=5,
    )
    return arc


def make_theta_arc(theta, phi, radius=0.72):
    return ParametricFunction(
        lambda t: sphere_point(radius, t, phi),
        t_range=[0, theta],
        color=AMPLITUDE_ALPHA,
        stroke_width=5,
    )


def panel_row(label_text, formula, label_color, formula_color):
    label = Text(
        label_text,
        font="Microsoft YaHei",
        font_size=26,
        color=label_color,
    )
    tex = MathTex(formula, font_size=31, color=formula_color)
    return VGroup(label, tex).arrange(RIGHT, buff=0.22, aligned_edge=DOWN)


class QubitUnitSphere(ThreeDScene):
    def construct(self):
        self.camera.background_color = BLACK
        self.set_camera_orientation(
            phi=64 * DEGREES,
            theta=-48 * DEGREES,
            zoom=1.18,
        )

        radius = 2.15
        theta = 58 * DEGREES
        phi = 42 * DEGREES
        state_tip = sphere_point(radius, theta, phi)
        projection = np.array([state_tip[0], state_tip[1], 0])

        sphere = make_wire_sphere(radius)
        xoy_plane = make_xoy_plane(radius)
        axes = make_axes(radius)

        state_vector = Arrow3D(
            start=ORIGIN,
            end=state_tip,
            thickness=0.035,
            height=0.25,
            base_radius=0.09,
            color=VECTOR_TEAL,
        )
        projection_vector = Arrow3D(
            start=ORIGIN,
            end=projection,
            thickness=0.018,
            height=0.16,
            base_radius=0.055,
            color=PHASE_PURPLE,
        )
        drop_line = DashedLine(
            state_tip,
            projection,
            dash_length=0.08,
            color=GREY_B,
            stroke_width=3,
        )

        phase_arc = make_phase_arc(phi)
        theta_arc = make_theta_arc(theta, phi)

        state_label = MathTex(r"|\psi\rangle", font_size=38, color=VECTOR_TEAL)
        state_label.move_to(state_tip + np.array([0.34, 0.18, 0.18]))

        phase_label = MathTex(r"\phi", font_size=38, color=PHASE_PURPLE)
        phase_label.move_to(sphere_point(0.98, PI / 2, phi / 2) + OUT * 0.08)

        theta_label = MathTex(r"\theta", font_size=34, color=AMPLITUDE_ALPHA)
        theta_label.move_to(sphere_point(0.96, theta / 2, phi) + np.array([0.06, 0.06, 0.04]))

        title = Text(
            "单位qubit",
            font="Microsoft YaHei",
            font_size=34,
            color=WHITE_TEXT,
        )
        title.to_corner(UL, buff=0.38)

        fixed_orientation_labels = VGroup(
            state_label,
            phase_label,
            theta_label,
        )
        fixed_orientation_labels.set_opacity(0)

        self.add_fixed_in_frame_mobjects(title)
        self.add_fixed_orientation_mobjects(*fixed_orientation_labels)

        self.play(
            FadeIn(xoy_plane),
            FadeIn(sphere),
            FadeIn(axes),
            run_time=0.8,
        )
        self.play(
            FadeIn(state_vector, scale=0.92),
            FadeIn(projection_vector, scale=0.92),
            Create(drop_line),
            Create(phase_arc),
            Create(theta_arc),
            run_time=0.95,
        )
        self.play(
            fixed_orientation_labels.animate.set_opacity(1),
            run_time=0.45,
        )
        rotating_group = VGroup(
            xoy_plane,
            sphere,
            axes,
            state_vector,
            projection_vector,
            drop_line,
            phase_arc,
            theta_arc,
            state_label,
            phase_label,
            theta_label,
        )
        self.play(
            Rotate(
                rotating_group,
                angle=70 * DEGREES,
                about_point=ORIGIN,
                axis=OUT,
            ),
            run_time=5.5,
            rate_func=linear,
        )
        self.wait(0.4)
