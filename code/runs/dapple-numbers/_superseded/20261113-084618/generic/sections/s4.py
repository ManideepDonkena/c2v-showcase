from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Reversal Property", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial dapple number 52
        num_52 = MathTex("52", color=GREEN, font_size=40)
        num_52.next_to(title, DOWN, buff=0.5)
        label_52 = Text("Dapple", font_size=24)
        label_52.next_to(num_52, DOWN)
        self.play(Write(num_52), Write(label_52))
        self.wait(1)

        # Split into digits
        digit_5 = MathTex("5", color=GREEN, font_size=40)
        digit_2 = MathTex("2", color=GREEN, font_size=40)
        digit_5.move_to(num_52.get_center()).shift(LEFT * 0.3)
        digit_2.move_to(num_52.get_center()).shift(RIGHT * 0.3)
        self.play(Transform(num_52, digit_5), Transform(label_52, Text("5", font_size=24)))
        self.play(Write(digit_2))
        self.wait(0.5)

        # Swap positions to make 25
        num_25 = MathTex("25", color=RED, font_size=40)
        num_25.next_to(title, DOWN, buff=0.5)
        label_25 = Text("Not Dapple", font_size=24)
        label_25.next_to(num_25, DOWN)
        self.play(
            Transform(digit_5, digit_2),
            Transform(digit_2, digit_5),
            run_time=1
        )
        self.wait(0.5)

        # Show 25 as not dapple
        self.play(Write(num_25), Write(label_25))
        self.wait(1)

        # Arrow from 52 to 25
        arrow = Arrow(start=num_52.get_center(), end=num_25.get_center(), color=WHITE)
        arrow_label = Text("Reversal", font_size=24)
        arrow_label.next_to(arrow, UP)
        arrow.shift(0.23 * RIGHT + 0.0 * UP)  # layout: separation vector
        arrow.shift(0.0 * RIGHT + 0.33 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow), Write(arrow_label))
        self.wait(1.5)

        # Narration text
        narration = Text("A key property of dapple numbers is their behavior under reversal.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        # Clear narration and show explanation
        self.play(FadeOut(narration))

        explanation = Text("If you reverse the digits of a dapple number...", font_size=24)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(1.5)

        self.play(FadeOut(explanation))

        # Show example more clearly
        example = MathTex(r"\text{52 is dapple (5 > 2); } \text{25 is not (2 < 5)}", font_size=24)
        example.to_edge(DOWN)
        self.play(Write(example))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(example), FadeOut(title), FadeOut(num_52), FadeOut(digit_5), FadeOut(digit_2), FadeOut(num_25), FadeOut(label_52), FadeOut(label_25), FadeOut(arrow), FadeOut(arrow_label))
        self.wait(0.5)
