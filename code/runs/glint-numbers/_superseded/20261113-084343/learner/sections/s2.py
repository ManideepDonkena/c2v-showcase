from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Zero Exclusion Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show number 50
        num_50 = MathTex("50").scale(2)
        num_50.move_to(ORIGIN)
        self.play(Write(num_50))
        self.wait(1)
        # Highlight last digit '0' and make it shake
        zero_50 = num_50[-1]
        self.play(
            zero_50.animate.set_color(RED),
            zero_50.animate.shift(LEFT * 0.1).shift(RIGHT * 0.1).shift(LEFT * 0.1).shift(RIGHT * 0.1),
            run_time=0.5
        )
        self.wait(0.5)

        # Add large red X
        cross = Cross(stroke_color=RED, stroke_width=12, scale_factor=1.5)
        cross.move_to(ORIGIN)
        self.play(GrowFromCenter(cross))
        self.wait(0.5)

        # Rule text
        rule_text = Text("Rule: Ending in 0 is NEVER Glint", font_size=24).next_to(cross, DOWN)
        self.play(Write(rule_text))
        self.wait(1.5)

        # Fade out previous elements
        self.play(FadeOut(num_50), FadeOut(zero_50), FadeOut(cross), FadeOut(rule_text))

        # Show number 10
        num_10 = MathTex("10").scale(2)
        num_10.move_to(ORIGIN)
        self.play(Write(num_10))
        self.wait(1)

        # Highlight last digit '0' and make it shake
        zero_10 = num_10[-1]  # Use [-1] to get the last character, which is '0'
        self.play(
            zero_10.animate.set_color(RED),
            zero_10.animate.shift(LEFT * 0.1).shift(RIGHT * 0.1).shift(LEFT * 0.1).shift(RIGHT * 0.1),
            run_time=0.5
        )
        self.wait(0.5)

        # Add text: Division by Zero is Impossible
        div_text = Text("Division by Zero is Impossible", font_size=24).next_to(num_10, DOWN)
        self.play(Write(div_text))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(num_10), FadeOut(zero_10), FadeOut(div_text))
        self.wait(0.5)
