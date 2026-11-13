from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Multiple of Ten Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Number line
        number_line = NumberLine(x_range=[0, 100, 10], include_numbers=True, length=12)
        number_line.move_to(DOWN * 0.5)
        self.play(Create(number_line))
        self.wait(0.5)

        # Dapple numbers 10 to 90
        dapple_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        labels = []
        for num in dapple_numbers:
            dot = number_line.number_to_point(num)
            label = MathTex(str(num), font_size=24).next_to(dot, DOWN)
            self.play(FadeIn(label))
            self.wait(0.3)
            label.set_color(GREEN)
            label.add_background_rectangle(color=BLACK, opacity=0.5)
            labels.append(label)

        # Label all as Dapple
        dapple_text = Text("Dapple", font_size=24, color=GREEN).next_to(number_line, DOWN)
        self.play(Write(dapple_text))
        self.wait(1)

        # Show 0 separately
        self.play(FadeOut(dapple_text))
        zero_dot = Dot(point=number_line.number_to_point(0))
        zero_label = MathTex("0", font_size=40).next_to(zero_dot, DOWN)
        zero_label.shift(-0.32 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(FadeIn(zero_label))
        self.wait(0.5)

        # Mark 0 as Not Dapple
        x_mark = Cross(zero_label, stroke_width=8, color=RED)
        self.play(Create(x_mark))
        self.wait(0.5)

        not_dapple_text = Text("Not Dapple", font_size=24, color=RED).next_to(zero_label, DOWN)
        not_dapple_text.shift(0.32 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(not_dapple_text))
        self.wait(1)

        # Explanation text
        explanation = Text("No tens digit → Not Dapple", font_size=24).next_to(not_dapple_text, DOWN)
        explanation.shift(1.22 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(explanation))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(number_line),
            *[FadeOut(label) for label in labels],
            FadeOut(zero_label),
            FadeOut(x_mark),
            FadeOut(not_dapple_text),
            FadeOut(explanation)
        )
        self.wait(0.5)
