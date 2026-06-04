from manim import *


class QuantumChipIcon(VGroup):
    def __init__(
        self,
        size=3.2,
        chip_color=BLUE_E,
        stroke_color=BLUE,
        mark_color=WHITE,
        **kwargs,
    ):
        super().__init__(**kwargs)

        pin_fill = BLUE_E
        pin_stroke = BLUE
        inner_color = BLACK

        chip_body = RoundedRectangle(
            width=3.2,
            height=3.2,
            corner_radius=0.18,
            fill_color=chip_color,
            fill_opacity=1,
            stroke_color=stroke_color,
            stroke_width=5,
        )

        inner_panel = RoundedRectangle(
            width=2.35,
            height=2.35,
            corner_radius=0.12,
            fill_color=inner_color,
            fill_opacity=1,
            stroke_color=stroke_color,
            stroke_width=2,
        )

        q_mark = MathTex(
            r"\left|Q\right\rangle",
            font_size=104,
            color=mark_color,
        )
        q_mark.set_stroke(stroke_color, width=1.6, opacity=0.75)

        self.pins = self._make_pins(pin_fill, pin_stroke)
        self.body = chip_body
        self.inner_panel = inner_panel
        self.mark = q_mark

        self.add(self.pins, self.body, self.inner_panel, self.mark)
        self.scale(size / 3.2)

    @staticmethod
    def _make_pins(pin_fill, pin_stroke):
        pins = VGroup()
        offsets = [-1.2, -0.4, 0.4, 1.2]

        for x in offsets:
            top_pin = Rectangle(
                width=0.18,
                height=0.68,
                fill_color=pin_fill,
                fill_opacity=1,
                stroke_color=pin_stroke,
                stroke_width=1.5,
            ).move_to([x, 1.94, 0])
            bottom_pin = top_pin.copy().move_to([x, -1.94, 0])
            pins.add(top_pin, bottom_pin)

        for y in offsets:
            left_pin = Rectangle(
                width=0.68,
                height=0.18,
                fill_color=pin_fill,
                fill_opacity=1,
                stroke_color=pin_stroke,
                stroke_width=1.5,
            ).move_to([-1.94, y, 0])
            right_pin = left_pin.copy().move_to([1.94, y, 0])
            pins.add(left_pin, right_pin)

        return pins


def make_quantum_chip_icon(size=3.2, **kwargs):
    return QuantumChipIcon(size=size, **kwargs)


class QuantumChip(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        chip = QuantumChipIcon()
        self.add(chip)
        self.wait()
