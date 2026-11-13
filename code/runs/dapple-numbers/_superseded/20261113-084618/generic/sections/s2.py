from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Multiple of Ten Rule", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Number line
        number_line = NumberLine(
            x_range=[0, 100, 10],
            include_numbers=True,
            numbers_to_include=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90],
            unit_size=0.8,
            color=WHITE
        )
        number_line.move_to(DOWN * 0.5)
        number_line.shift(33.08 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(number_line))
        self.wait(0.5)

        # Show 0 separately
        zero_label = MathTex("0", font_size=40)
        zero_label.next_to(number_line.n2p(0), DOWN, buff=0.3)
        x_mark = Cross(zero_label, stroke_width=8, color=RED)
        not_dapple_text = Text("Not Dapple (No Tens Digit)", font_size=24)
        not_dapple_text.next_to(zero_label, DOWN, buff=0.5)
        self.play(Write(zero_label))
        self.play(Create(x_mark))
        self.play(Write(not_dapple_text))
        self.wait(1)

        # Fade out 0 elements
        self.play(FadeOut(zero_label), FadeOut(x_mark), FadeOut(not_dapple_text))

        # Slide in multiples of ten
        dapple_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        for num in dapple_numbers:
            num_label = MathTex(str(num), font_size=40)
            num_label.move_to(number_line.n2p(num))
            self.play(Write(num_label))
            self.play(num_label.animate.set_color(GREEN))
            dapple_text = Text("Dapple", font_size=24)
            dapple_text.next_to(num_label, DOWN, buff=0.3)
            self.play(Write(dapple_text))
            self.wait(0.5)
            self.play(FadeOut(dapple_text))

        # Narration text
        narration = Text("Consider multiples of ten: 10, 20, up to 90.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        narration2 = Text("Since their units digit is always 0...", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1.5)
        self.play(FadeOut(narration2))

        narration3 = Text("Every multiple of ten from 10 to 90 is automatically a dapple number.", font_size=24)
        narration3.to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(2)
        self.play(FadeOut(narration3))

        # Final wait
        self.wait(1)

        self.play(FadeOut(title), FadeOut(number_line))
