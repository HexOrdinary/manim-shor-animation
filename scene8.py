from manim import *
import numpy as np

from computer_chip import make_computer_chip_icon
from function_machine_icon import make_function_machine_icon
from quantum_chip import make_quantum_chip_icon
from qubit_unit_sphere import (
    AMPLITUDE_ALPHA,
    PHASE_PURPLE,
    VECTOR_TEAL,
    make_axes,
    make_phase_arc,
    make_theta_arc,
    make_wire_sphere,
    make_xoy_plane,
    sphere_point,
)


WHITE_TEXT = WHITE
HIGHLIGHT_YELLOW = YELLOW
MASK_GREY = GREY_E
QFT_BLUE = "#1D4ED8"
QFT_CYAN = "#38BDF8"
BAR_GREY = "#94A3B8"


def math_item(tex, font_size=56, color=WHITE_TEXT):
    return MathTex(tex, font_size=font_size, color=color)


def make_ket(bits, font_size=52, color=WHITE_TEXT):
    return MathTex(
        rf"\left|{bits}\right\rangle",
        font_size=font_size,
        color=color,
    )


def make_classical_bits(bits="010110"):
    bit_groups = VGroup()
    for bit in bits:
        box = Square(
            side_length=0.48,
            stroke_color=WHITE_TEXT,
            stroke_width=2.5,
            fill_opacity=0,
        )
        label = math_item(bit, font_size=34)
        bit_groups.add(VGroup(box, label))

    bit_groups.arrange(RIGHT, buff=0.07)
    return bit_groups


def make_state_formula(kind="bits"):
    if kind == "bits":
        formula = MathTex(
            r"n\ \mathrm{bits}\ \to",
            r"1\ \mathrm{state}",
            font_size=40,
            color=WHITE_TEXT,
        )
    else:
        formula = MathTex(
            r"n\ \mathrm{qubits}\ \to",
            r"2^n\ \mathrm{states}",
            font_size=40,
            color=WHITE_TEXT,
        )

    formula[1].set_color(HIGHLIGHT_YELLOW)
    return formula


def make_basis_list():
    entries = VGroup(
        make_ket("000000", font_size=34),
        make_ket("000001", font_size=34),
        make_ket("000010", font_size=34),
        make_ket("000011", font_size=34),
        math_item(r"\vdots", font_size=42),
        make_ket("111111", font_size=34),
    )
    entries.arrange(DOWN, buff=0.16)
    return entries


def make_orbit_path(mobject, index, radius=0.055):
    start_angle = index * 0.73
    center = mobject.get_center() - radius * np.array(
        [np.cos(start_angle), np.sin(start_angle), 0]
    )
    return ParametricFunction(
        lambda t, center=center, start_angle=start_angle: center
        + radius * np.array([np.cos(t + start_angle), np.sin(t + start_angle), 0]),
        t_range=[0, TAU],
    )


def make_qubit_sphere_demo(radius=1.72):
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
        thickness=0.03,
        height=0.22,
        base_radius=0.08,
        color=VECTOR_TEAL,
    )
    projection_vector = Arrow3D(
        start=ORIGIN,
        end=projection,
        thickness=0.016,
        height=0.14,
        base_radius=0.05,
        color=PHASE_PURPLE,
    )
    drop_line = DashedLine(
        state_tip,
        projection,
        dash_length=0.08,
        color=GREY_B,
        stroke_width=3,
    )
    phase_arc = make_phase_arc(phi, radius=0.58)
    theta_arc = make_theta_arc(theta, phi, radius=0.58)

    state_label = MathTex(r"|\psi\rangle", font_size=34, color=VECTOR_TEAL)
    state_label.move_to(state_tip + np.array([0.28, 0.16, 0.16]))

    amplitude_label = MathTex(r"\theta", font_size=32, color=AMPLITUDE_ALPHA)
    amplitude_label.move_to(
        sphere_point(0.78, theta / 2, phi) + np.array([0.08, 0.06, 0.04])
    )

    phase_label = MathTex(r"\phi", font_size=34, color=PHASE_PURPLE)
    phase_label.move_to(sphere_point(0.78, PI / 2, phi / 2) + OUT * 0.08)

    objects = VGroup(
        xoy_plane,
        sphere,
        axes,
        state_vector,
        projection_vector,
        drop_line,
        phase_arc,
        theta_arc,
    )
    labels = VGroup(state_label, amplitude_label, phase_label)
    return objects, labels


def make_psi_column(first_psi):
    rows = [first_psi]
    for _ in range(5):
        rows.append(first_psi.copy())

    column = VGroup(*rows).arrange(DOWN, buff=0.22)
    column.move_to(LEFT * 5.25 + UP * 0.05)
    return column


def make_arrows_to_box(psi_column, box):
    arrows = VGroup()
    box_left_x = box.get_left()[0]
    for psi in psi_column:
        start = psi.get_right() + RIGHT * 0.14
        end = np.array([box_left_x + 0.05, psi.get_center()[1], 0])
        arrows.add(
            Arrow(
                start,
                end,
                buff=0,
                stroke_width=4.5,
                color=WHITE_TEXT,
                max_tip_length_to_length_ratio=0.08,
            )
        )
    return arrows


def make_power_table():
    rows = [
        [r"g^0", r"g^1", r"g^2", r"g^3", r"g^4", r"g^5"],
        [r"g^6", r"g^7", r"g^8", r"g^9", r"g^{10}", r"g^{11}"],
        [r"g^{12}", r"g^{13}", r"g^{14}", r"g^{15}", r"g^{16}", r"g^{17}"],
        [r"\cdots", r"\cdots", r"\cdots", r"\cdots", r"\cdots", r"\cdots"],
        [
            r"g^{N-6}",
            r"g^{N-5}",
            r"g^{N-4}",
            r"g^{N-3}",
            r"g^{N-2}",
            r"g^{N-1}",
        ],
    ]

    table_rows = VGroup()
    for row in rows:
        entries = VGroup(
            *[MathTex(entry, font_size=26, color=WHITE_TEXT) for entry in row]
        ).arrange(RIGHT, buff=0.26)
        table_rows.add(entries)

    table_rows.arrange(DOWN, buff=0.32)
    return table_rows


def make_qft_machine(size=0.82):
    machine = make_function_machine_icon(
        size=size,
        body_color="#172554",
        stroke_color=QFT_CYAN,
        accent_color=WHITE_TEXT,
    )
    old_mark = machine[5]
    body = machine[4]
    qft_mark = MathTex(r"\mathrm{QFT}", font_size=22, color=WHITE_TEXT)
    if qft_mark.width > body.width * 0.62:
        qft_mark.scale_to_fit_width(body.width * 0.62)
    if qft_mark.height > body.height * 0.34:
        qft_mark.scale_to_fit_height(body.height * 0.34)
    qft_mark.move_to(old_mark.get_center())
    machine.remove(old_mark)
    machine.add(qft_mark)
    return machine


def make_frequency_axes(box):
    axes = Axes(
        x_range=[0, 12, 2],
        y_range=[0, 1.25, 0.25],
        x_length=max(box.width - 0.85, 2.2),
        y_length=max(box.height - 1.0, 1.35),
        tips=False,
        axis_config={
            "stroke_color": BAR_GREY,
            "stroke_width": 2,
        },
    )
    axes.move_to(box.get_center() + DOWN * 0.08)

    x_label = MathTex("f", font_size=28, color=WHITE_TEXT)
    y_label = MathTex(r"|a|", font_size=28, color=WHITE_TEXT)
    x_label.next_to(axes.x_axis.get_end(), DOWN, buff=0.08)
    y_label.next_to(axes.y_axis.get_end(), LEFT, buff=0.08)
    return VGroup(axes, x_label, y_label)


def make_frequency_bars(axes_group, focus_level=0):
    axes = axes_group[0]
    x_values = np.linspace(0.45, 11.55, 32)
    peak_indices = {6, 14, 22, 30}
    initial_amp = 0.14
    peak_amp = 1.02
    low_amp = 0.045
    bars = VGroup()
    bar_width = min(0.11, axes.x_axis.width / 55)

    for index, x_value in enumerate(x_values):
        if index in peak_indices:
            amp = initial_amp + (peak_amp - initial_amp) * focus_level
            color = interpolate_color(GREY_B, HIGHLIGHT_YELLOW, focus_level)
            opacity = 0.58 + 0.36 * focus_level
        else:
            amp = initial_amp + (low_amp - initial_amp) * focus_level
            color = interpolate_color(GREY_B, GREY_D, focus_level)
            opacity = 0.58

        bottom = axes.c2p(x_value, 0)
        top = axes.c2p(x_value, amp)
        height = top[1] - bottom[1]
        bar = Rectangle(
            width=bar_width,
            height=max(height, 0.02),
            fill_color=color,
            fill_opacity=opacity,
            stroke_color=color,
            stroke_width=1.2,
        )
        bar.move_to([bottom[0], bottom[1] + height / 2, 0])
        bars.add(bar)

    return bars


def make_fourier_time_chart(overlay):
    axes = Axes(
        x_range=[0, 6, 1],
        y_range=[-1.6, 1.6, 0.8],
        x_length=7.15,
        y_length=3.0,
        tips=False,
        axis_config={
            "stroke_color": BAR_GREY,
            "stroke_width": 2,
        },
    )
    axes.move_to(overlay.get_center() + DOWN * 0.18)

    signal = axes.plot(
        lambda x: (
            0.78 * np.sin(2 * PI * 0.8 * x)
            + 0.38 * np.sin(2 * PI * 1.7 * x + 0.5)
            + 0.22 * np.sin(2 * PI * 3.0 * x)
        ),
        x_range=[0, 6],
        color=QFT_CYAN,
        stroke_width=4,
    )

    x_label = MathTex("t", font_size=30, color=WHITE_TEXT)
    y_label = MathTex(r"A", font_size=30, color=WHITE_TEXT)
    x_label.next_to(axes.x_axis.get_end(), DOWN, buff=0.08)
    y_label.next_to(axes.y_axis.get_end(), LEFT, buff=0.08)
    return VGroup(axes, signal, x_label, y_label)


def make_fourier_spectrum_chart(overlay):
    axes = Axes(
        x_range=[0, 6, 1],
        y_range=[0, 1.6, 0.4],
        x_length=7.15,
        y_length=3.0,
        tips=False,
        axis_config={
            "stroke_color": BAR_GREY,
            "stroke_width": 2,
        },
    )
    axes.move_to(overlay.get_center() + DOWN * 0.18)

    freqs = [1, 2, 3, 4, 5]
    amps = [1.28, 0.78, 0.48, 0.16, 0.1]
    colors = [QFT_CYAN, "#A78BFA", "#F472B6", GREY_B, GREY_D]
    bars = VGroup()
    for freq, amp, color in zip(freqs, amps, colors):
        bottom = axes.c2p(freq, 0)
        top = axes.c2p(freq, amp)
        bar = Rectangle(
            width=0.16,
            height=top[1] - bottom[1],
            fill_color=color,
            fill_opacity=0.9,
            stroke_color=color,
            stroke_width=2,
        )
        bar.move_to([bottom[0], (bottom[1] + top[1]) / 2, 0])
        bars.add(bar)

    x_label = MathTex("f", font_size=30, color=WHITE_TEXT)
    y_label = MathTex(r"|F|", font_size=30, color=WHITE_TEXT)
    x_label.next_to(axes.x_axis.get_end(), DOWN, buff=0.08)
    y_label.next_to(axes.y_axis.get_end(), LEFT, buff=0.08)
    return VGroup(axes, bars, x_label, y_label)


def make_open_lock_icon(size=2.65):
    shackle_arc = Arc(
        radius=1.0,
        start_angle=0,
        angle=PI,
        color=BLUE,
        stroke_width=14,
    )
    shackle_arc.move_to(UP * 1.35)

    left_leg = Line(
        shackle_arc.get_end(),
        shackle_arc.get_end() + DOWN * 0.76,
        color=BLUE,
        stroke_width=14,
    )

    body = RoundedRectangle(
        width=2.6,
        height=1.8,
        corner_radius=0.18,
        color=BLUE,
        fill_color=BLUE_E,
        fill_opacity=1,
        stroke_width=4,
    )
    body.move_to(DOWN * 0.55)

    keyhole_top = Circle(
        radius=0.18,
        color=YELLOW,
        fill_color=YELLOW,
        fill_opacity=1,
        stroke_width=0,
    )
    keyhole_top.move_to(DOWN * 0.35)

    keyhole_bottom = Rectangle(
        width=0.16,
        height=0.45,
        color=YELLOW,
        fill_color=YELLOW,
        fill_opacity=1,
        stroke_width=0,
    )
    keyhole_bottom.next_to(keyhole_top, DOWN, buff=-0.03)

    lock = VGroup(shackle_arc, left_leg, body, keyhole_top, keyhole_bottom)
    lock.scale(size / 2.65)
    return lock


class new_scene8(ThreeDScene):
    def construct(self):
        self.camera.background_color = BLACK

        carryover_chip = make_quantum_chip_icon(size=2.45).move_to(
            LEFT * 2.55 + DOWN * 0.34
        )
        self.add(carryover_chip)
        self.wait(0.3)

        classical_chip = make_computer_chip_icon(size=1.05).move_to(
            LEFT * 4.75 + UP * 2.72
        )
        quantum_chip_target = make_quantum_chip_icon(size=1.05).move_to(
            RIGHT * 2.15 + UP * 2.72
        )
        self.play(
            TransformFromCopy(carryover_chip, classical_chip),
            Transform(carryover_chip, quantum_chip_target),
            run_time=0.85,
            rate_func=smooth,
        )
        quantum_chip = carryover_chip
        self.wait(0.35)

        classical_bits = make_classical_bits().next_to(
            classical_chip, DOWN, buff=0.5
        )
        classical_formula = make_state_formula("bits").next_to(
            classical_bits, DOWN, buff=0.35
        )
        self.play(
            LaggedStart(
                *[FadeIn(bit, shift=UP * 0.05) for bit in classical_bits],
                lag_ratio=0.08,
            ),
            run_time=0.55,
        )
        self.wait(0.25)
        self.play(FadeIn(classical_formula, shift=UP * 0.06), run_time=0.45)
        self.wait(0.45)

        quantum_state = make_ket("010110", font_size=56).next_to(
            quantum_chip, DOWN, buff=0.5
        )
        self.play(FadeIn(quantum_state, shift=UP * 0.06), run_time=0.42)

        base_center = quantum_state.get_center()
        changing_bits = ["110010", "001101", "101011", "011100", "111001", "010110"]
        jitters = [
            RIGHT * 0.08,
            LEFT * 0.07 + UP * 0.03,
            RIGHT * 0.04 + DOWN * 0.04,
            LEFT * 0.06 + DOWN * 0.02,
            RIGHT * 0.07 + UP * 0.03,
            ORIGIN,
        ]
        for bits, jitter in zip(changing_bits, jitters):
            target = make_ket(bits, font_size=56).move_to(base_center + jitter)
            self.play(
                Transform(quantum_state, target),
                run_time=0.13,
                rate_func=smooth,
            )
            self.play(quantum_state.animate.set_opacity(0.55), run_time=0.05)
            self.play(quantum_state.animate.set_opacity(1), run_time=0.05)

        quantum_formula = make_state_formula("qubits").move_to(
            classical_formula.get_center() + RIGHT * 6.85
        )
        self.play(
            TransformFromCopy(classical_formula, quantum_formula),
            run_time=0.65,
            rate_func=smooth,
        )
        self.wait(0.45)

        basis_list = make_basis_list()
        basis_list.next_to(quantum_formula, DOWN, buff=0.22)
        basis_list.align_to(quantum_formula, ORIGIN)
        self.play(
            LaggedStart(
                *[FadeIn(entry, shift=DOWN * 0.08) for entry in basis_list],
                lag_ratio=0.04,
            ),
            run_time=0.72,
        )
        orbit_paths = [
            make_orbit_path(entry, index) for index, entry in enumerate(basis_list)
        ]
        self.play(
            AnimationGroup(
                *[
                    MoveAlongPath(entry, path)
                    for entry, path in zip(basis_list, orbit_paths)
                ],
                lag_ratio=0.08,
            ),
            run_time=1.25,
            rate_func=linear,
        )
        self.wait(0.35)

        classical_group = VGroup(classical_chip, classical_bits, classical_formula)
        quantum_group = VGroup(
            quantum_chip,
            quantum_state,
            quantum_formula,
            basis_list,
        )
        centered_quantum_group = quantum_group.copy().move_to(ORIGIN)
        self.play(
            FadeOut(classical_group, shift=LEFT * 0.18),
            Transform(quantum_group, centered_quantum_group),
            run_time=0.82,
            rate_func=smooth,
        )
        self.wait(0.35)

        self.play(
            FadeOut(VGroup(quantum_chip, quantum_state, quantum_formula, basis_list), scale=0.82),
            run_time=0.42,
        )

        self.move_camera(
            phi=64 * DEGREES,
            theta=-48 * DEGREES,
            zoom=1.16,
            run_time=0.75,
        )

        sphere_objects, sphere_labels = make_qubit_sphere_demo()
        sphere_labels.set_opacity(0)
        self.add_fixed_orientation_mobjects(*sphere_labels)
        self.play(
            FadeIn(sphere_objects[0]),
            FadeIn(sphere_objects[1]),
            FadeIn(sphere_objects[2]),
            run_time=0.75,
        )
        self.play(
            FadeIn(sphere_objects[3], scale=0.92),
            FadeIn(sphere_objects[4], scale=0.92),
            Create(sphere_objects[5]),
            Create(sphere_objects[6]),
            Create(sphere_objects[7]),
            sphere_labels.animate.set_opacity(1),
            run_time=0.95,
        )
        rotating_group = VGroup(sphere_objects, sphere_labels)
        self.play(
            Rotate(
                rotating_group,
                angle=64 * DEGREES,
                about_point=ORIGIN,
                axis=OUT,
            ),
            run_time=3.5,
            rate_func=linear,
        )
        self.wait(0.25)

        self.play(FadeOut(rotating_group, scale=0.86), run_time=0.55)
        self.move_camera(
            phi=0,
            theta=-90 * DEGREES,
            zoom=1,
            run_time=0.55,
        )

        psi_symbol = MathTex(
            r"\left|\Psi\right\rangle",
            font_size=62,
            color=VECTOR_TEAL,
        )
        self.play(FadeIn(psi_symbol, scale=1.1), run_time=0.4)
        self.play(
            psi_symbol.animate.move_to(LEFT * 5.25 + UP * 1.55).scale(0.78),
            run_time=0.58,
            rate_func=smooth,
        )

        psi_column_target = make_psi_column(psi_symbol.copy())
        psi_copies = VGroup(*[psi_column_target[index] for index in range(1, 6)])
        self.play(
            Transform(psi_symbol, psi_column_target[0]),
            LaggedStart(
                *[TransformFromCopy(psi_symbol, psi_copy) for psi_copy in psi_copies],
                lag_ratio=0.08,
            ),
            run_time=0.78,
            rate_func=smooth,
        )
        psi_column = VGroup(psi_symbol, *psi_copies)
        self.wait(0.25)

        input_box = Rectangle(
            width=6.2,
            height=4.35,
            stroke_color=WHITE_TEXT,
            stroke_width=3,
            fill_opacity=0,
        ).move_to(RIGHT * 1.65)
        arrows = make_arrows_to_box(psi_column, input_box)
        self.play(Create(input_box), run_time=0.35)
        self.play(
            LaggedStart(*[GrowArrow(arrow) for arrow in arrows], lag_ratio=0.05),
            run_time=0.65,
        )
        self.wait(0.25)

        function_formula = MathTex(
            r"g^x \bmod N",
            font_size=50,
            color=WHITE_TEXT,
        ).to_edge(UP, buff=0.9)
        self.play(FadeIn(function_formula, shift=UP * 0.06), run_time=0.4)
        x_formula = math_item("x", font_size=58).move_to(function_formula)
        self.play(
            Transform(function_formula, x_formula),
            run_time=0.5,
            rate_func=smooth,
        )
        self.wait(0.2)

        x_tokens = VGroup()
        for arrow in arrows:
            token = function_formula.copy().scale(0.62)
            token.move_to(arrow.get_start() + RIGHT * 0.28)
            x_tokens.add(token)

        self.play(
            LaggedStart(
                *[TransformFromCopy(function_formula, token) for token in x_tokens],
                lag_ratio=0.06,
            ),
            run_time=0.62,
        )
        self.play(FadeOut(function_formula, shift=DOWN * 0.05), run_time=0.25)
        self.play(
            AnimationGroup(
                *[
                    token.animate.move_to(
                        np.array(
                            [
                                input_box.get_left()[0] + 0.58,
                                token.get_center()[1],
                                0,
                            ]
                        )
                    ).set_opacity(0)
                    for token in x_tokens
                ],
                lag_ratio=0.04,
            ),
            run_time=0.72,
            rate_func=smooth,
        )
        self.remove(x_tokens)

        power_table = make_power_table().move_to(input_box.get_center())
        if power_table.width > input_box.width - 0.55:
            power_table.scale_to_fit_width(input_box.width - 0.55)
        if power_table.height > input_box.height - 0.65:
            power_table.scale_to_fit_height(input_box.height - 0.65)
        self.play(FadeIn(power_table, shift=UP * 0.08), run_time=0.72)
        self.wait(0.55)

        mask = Rectangle(
            width=input_box.width - 0.06,
            height=input_box.height - 0.06,
            fill_color=MASK_GREY,
            fill_opacity=0.64,
            stroke_width=0,
        ).move_to(input_box)
        period_formula = MathTex(
            r"f(x+",
            "r",
            r")=f(x)",
            font_size=54,
            color=WHITE_TEXT,
        )
        period_formula.move_to(input_box.get_top() + DOWN * 2.0)
        self.play(FadeIn(mask), FadeIn(period_formula), run_time=0.45)
        self.wait(0.25)
        self.play(
            period_formula[1].animate.scale(1.75),
            run_time=0.55,
            rate_func=there_and_back,
        )
        self.play(period_formula[1].animate.set_color(HIGHLIGHT_YELLOW), run_time=0.3)
        self.wait(0.45)

        power_table.set_z_index(1)
        mask.set_z_index(2)
        period_formula.set_z_index(3)
        input_box.set_z_index(4)
        delta_theta = MathTex(
            r"\Delta\theta",
            font_size=92,
            color=WHITE_TEXT,
        )
        delta_theta.next_to(period_formula, DOWN, buff=0.48)
        delta_theta.set_z_index(1)
        self.play(
            Transform(power_table, delta_theta),
            run_time=0.72,
            rate_func=smooth,
        )
        self.wait(0.45)

        self.play(
            FadeOut(
                VGroup(
                    power_table,
                    mask,
                    period_formula,
                )
            ),
            run_time=0.75,
        )
        self.wait(0.2)

        qft_title = Text(
            "Quantum Fourier Transform",
            font_size=40,
            color=WHITE_TEXT,
        ).to_edge(UP, buff=0.32)
        qft_title.set_z_index(30)
        self.play(Write(qft_title), run_time=0.75)
        self.wait(0.25)

        qft_short = Text("QFT", font_size=56, color=WHITE_TEXT)
        qft_short.to_edge(UP, buff=0.26)
        qft_short.set_z_index(30)
        self.play(Transform(qft_title, qft_short), run_time=0.55, rate_func=smooth)
        self.wait(0.2)

        qft_machines = VGroup()
        for arrow in arrows:
            machine = make_qft_machine(size=0.92)
            machine.move_to(arrow.get_center())
            qft_machines.add(machine)

        self.play(
            LaggedStart(
                *[TransformFromCopy(qft_title, machine) for machine in qft_machines],
                lag_ratio=0.08,
            ),
            run_time=0.85,
            rate_func=smooth,
        )
        self.wait(0.25)

        power_table_recall = make_power_table().move_to(input_box.get_center())
        if power_table_recall.width > input_box.width - 0.55:
            power_table_recall.scale_to_fit_width(input_box.width - 0.55)
        if power_table_recall.height > input_box.height - 0.65:
            power_table_recall.scale_to_fit_height(input_box.height - 0.65)
        power_table_recall.set_opacity(0.62)
        self.play(FadeIn(power_table_recall, shift=UP * 0.04), run_time=0.28)

        frequency_axes = make_frequency_axes(input_box)
        noise_bars = make_frequency_bars(frequency_axes, focus_level=0)
        frequency_chart = VGroup(frequency_axes, noise_bars)
        self.play(
            ReplacementTransform(power_table_recall, frequency_axes),
            run_time=0.62,
            rate_func=smooth,
        )
        self.play(
            LaggedStart(
                *[GrowFromEdge(bar, DOWN) for bar in noise_bars],
                lag_ratio=0.015,
            ),
            run_time=1.65,
        )
        self.wait(0.22)

        pulse_bars = make_frequency_bars(frequency_axes, focus_level=0.45)
        final_bars = make_frequency_bars(frequency_axes, focus_level=1)
        self.play(Transform(noise_bars, pulse_bars), Transform(noise_bars, final_bars), run_time=4.28, rate_func=linear)
        self.play(
            noise_bars[6].animate.set_fill(HIGHLIGHT_YELLOW, opacity=1),
            noise_bars[14].animate.set_fill(HIGHLIGHT_YELLOW, opacity=1),
            noise_bars[22].animate.set_fill(HIGHLIGHT_YELLOW, opacity=1),
            noise_bars[30].animate.set_fill(HIGHLIGHT_YELLOW, opacity=1),
            run_time=0.25,
        )
        self.wait(0.25)

        brace_y = (
            max(noise_bars[6].get_top()[1], noise_bars[14].get_top()[1]) - 0.1
        )
        spacing_brace = BraceBetweenPoints(
            [noise_bars[6].get_center()[0], brace_y, 0],
            [noise_bars[14].get_center()[0], brace_y, 0],
            direction=UP,
            color=HIGHLIGHT_YELLOW,
        )
        spacing_label = MathTex(
            r"\Delta k=\frac{N}{r}",
            font_size=28,
            color=HIGHLIGHT_YELLOW,
        ).next_to(spacing_brace, UP, buff=0.02)
        self.play(Create(spacing_brace), FadeIn(spacing_label, shift=UP * 0.05))
        self.wait(0.35)

        overlay = Rectangle(
            width=config.frame_width - 0.7,
            height=5.45,
            fill_color=BLACK,
            fill_opacity=0.96,
            stroke_color=GREY_B,
            stroke_width=2,
        ).move_to(DOWN * 0.36)
        overlay.set_z_index(20)
        fourier_title = Text(
            "Fourier Transform",
            font_size=38,
            color=WHITE_TEXT,
        )
        fourier_title.move_to(overlay.get_top() + DOWN * 0.42)
        time_chart = make_fourier_time_chart(overlay)
        spectrum_chart = make_fourier_spectrum_chart(overlay)
        for mobject in (fourier_title, time_chart, spectrum_chart):
            mobject.set_z_index(21)

        self.play(GrowFromCenter(overlay), run_time=0.42)
        self.play(FadeIn(fourier_title, shift=DOWN * 0.04), run_time=0.25)
        self.play(
            Create(time_chart[0]),
            Create(time_chart[1]),
            FadeIn(VGroup(time_chart[2], time_chart[3])),
            run_time=1.9,
            rate_func=linear,
        )
        self.wait(0.25)
        self.play(
            ReplacementTransform(time_chart, spectrum_chart),
            run_time=0.9,
            rate_func=smooth,
        )
        self.wait(0.35)
        self.play(
            FadeOut(VGroup(overlay, fourier_title, spectrum_chart), scale=0.18),
            run_time=0.62,
            rate_func=smooth,
        )
        self.wait(0.25)

        r_from_spacing = MathTex(
            r"r=\frac{N}{\Delta k}",
            font_size=48,
            color=HIGHLIGHT_YELLOW,
        )
        r_from_spacing.to_edge(RIGHT, buff=0.6).shift(UP * 0.25)
        self.play(Transform(spacing_label, r_from_spacing), run_time=0.62)
        self.wait(0.3)

        row_y = -0.22
        single_psi = MathTex(
            r"\left|\Psi\right\rangle",
            font_size=52,
            color=VECTOR_TEAL,
        ).move_to(LEFT * 4.5 + UP * row_y)
        single_qft_machine = make_qft_machine(size=1.05).move_to(
            LEFT * 1.5 + UP * row_y
        )
        compact_box = Rectangle(
            width=3.35,
            height=2.28,
            stroke_color=WHITE_TEXT,
            stroke_width=3,
            fill_opacity=0,
        ).move_to(RIGHT * 1.5 + UP * row_y)
        compact_frequency_axes = make_frequency_axes(compact_box)
        compact_bars = make_frequency_bars(compact_frequency_axes, focus_level=1)
        compact_frequency_group = VGroup(
            compact_box,
            compact_frequency_axes,
            compact_bars,
        )
        compact_r_formula = MathTex(
            r"r=\frac{N}{\Delta k}",
            font_size=42,
            color=HIGHLIGHT_YELLOW,
        ).move_to(RIGHT * 4.5 + UP * row_y)
        frequency_group = VGroup(input_box, frequency_chart)

        self.play(
            ReplacementTransform(psi_column, single_psi),
            FadeOut(arrows, shift=RIGHT * 0.08),
            ReplacementTransform(qft_machines, single_qft_machine),
            Transform(frequency_group, compact_frequency_group),
            FadeOut(spacing_brace, shift=UP * 0.05),
            Transform(spacing_label, compact_r_formula),
            run_time=0.95,
            rate_func=smooth,
        )
        self.wait(0.35)

        alpha_beta = MathTex(
            r"\alpha|0\rangle+\beta|1\rangle",
            font_size=40,
            color=VECTOR_TEAL,
        ).move_to(single_psi)
        self.play(Transform(single_psi, alpha_beta), run_time=0.45)
        self.play(Indicate(single_psi, color=HIGHLIGHT_YELLOW), run_time=0.55)
        self.play(Indicate(single_qft_machine, color=HIGHLIGHT_YELLOW), run_time=0.55)
        self.play(Indicate(frequency_group, color=HIGHLIGHT_YELLOW), run_time=0.55)
        self.play(Indicate(spacing_label, color=HIGHLIGHT_YELLOW), run_time=0.55)
        self.wait(0.25)

        r_symbol = MathTex(
            "r",
            font_size=92,
            color=HIGHLIGHT_YELLOW,
        ).next_to(qft_title, DOWN, buff=0.56)
        self.play(
            FadeOut(VGroup(single_psi, single_qft_machine, frequency_group)),
            Transform(spacing_label, r_symbol),
            run_time=0.72,
            rate_func=smooth,
        )
        self.wait(0.25)

        final_period_formula = MathTex(
            r"f(x+",
            "r",
            r")=f(x)",
            font_size=62,
            color=WHITE_TEXT,
        ).next_to(spacing_label, DOWN, buff=0.34)
        final_period_formula[1].set_color(HIGHLIGHT_YELLOW)
        final_n_formula = MathTex(
            "N",
            "=",
            "p",
            r"\cdot",
            "q",
            font_size=60,
            color=WHITE_TEXT,
        ).next_to(final_period_formula, DOWN, buff=0.38)
        self.play(FadeIn(final_period_formula, shift=UP * 0.06), run_time=0.46)
        self.play(FadeIn(final_n_formula, shift=UP * 0.06), run_time=0.46)
        self.wait(0.45)

        open_lock = make_open_lock_icon(size=3.05).move_to(ORIGIN)
        closing_group = VGroup(
            qft_title,
            spacing_label,
            final_period_formula,
            final_n_formula,
        )
        self.play(
            FadeOut(closing_group, scale=0.96),
            FadeIn(open_lock, scale=0.96),
            run_time=0.55,
            rate_func=smooth,
        )
        self.wait(1.0)
