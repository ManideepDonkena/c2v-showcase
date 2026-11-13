from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Multiple of Ten Rule", font_size=36)
        title.to_edge(UP, buff=0.2)

        # Number line
        number_line = NumberLine(
            x_range=[0, 100, 10],
            include_numbers=True,
            numbers_to_include=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90],
            unit_size=0.8,
            color=WHITE
        )
        number_line.move_to(DOWN * 0.5)

        # Add title and number line
        number_line.shift(33.08 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(title), Create(number_line))
        self.wait(0.5)

        # Show 0 separately
        zero_label = Text("0", font_size=24).next_to(number_line.n2p(0), DOWN, buff=0.2)
        zero_x = Cross(stroke_width=8, scale_factor=0.3).move_to(number_line.n2p(0))
        not_dapple_text = Text("Not Dapple (No Tens Digit)", font_size=24).next_to(zero_x, DOWN, buff=0.3)
        self.play(FadeIn(zero_label), FadeIn(zero_x), Write(not_dapple_text))
        self.wait(1)

        # Remove 0 text and cross
        self.play(FadeOut(zero_label), FadeOut(zero_x), FadeOut(not_dapple_text))

        # Animate multiples of ten
        dapple_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        for num in dapple_numbers:
            num_label = Text(str(num), font_size=24).next_to(number_line.n2p(num), DOWN, buff=0.2)
            self.play(Write(num_label))
            self.wait(0.3)
            # Change color to green
            num_label.set_color(GREEN)
            dapple_text = Text("Dapple", font_size=24).next_to(num_label, DOWN, buff=0.3)
            self.play(Write(dapple_text))
            self.wait(0.7)

        # Narration text at bottom
        narration = Text("Every multiple of ten from 10 to 90 is dapple.", font_size=24)
        narration.to_edge(DOWN, buff=0.3)
        self.play(Write(narration))
        self.wait(2)

        # Clean up
        self.play(FadeOut(title), FadeOut(number_line), *[FadeOut(mob) for mob in self.mobjects])
