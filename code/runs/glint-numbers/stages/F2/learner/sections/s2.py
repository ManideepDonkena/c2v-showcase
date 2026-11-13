from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Zero Exclusion Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 50
        num_50 = MathTex("50", font_size=40)
        num_50.move_to(ORIGIN)
        self.play(Write(num_50))
        self.wait(1)
        # Make last digit '0' red and shake
        if len(num_50) > 1:
            zero_50 = num_50[1]
            self.play(zero_50.animate.set_color(RED).animate.shift(RIGHT * 0.1).shift(LEFT * 0.1).shift(RIGHT * 0.1).shift(LEFT * 0.1))
        self.wait(0.5)

        # Add large red X
        cross = Cross(stroke_width=12, scale_factor=1.5)
        cross.move_to(ORIGIN)
        self.play(Create(cross))
        self.wait(0.5)

        # Show text
        rule_text = Text("Rule: Ending in 0 is NEVER Glint", font_size=24).next_to(num_50, DOWN)
        rule_text.shift(0.0 * RIGHT + -1.26 * UP)  # layout: separation vector
        self.play(Write(rule_text))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(num_50), FadeOut(zero_50) if 'zero_50' in locals() else FadeOut(VGroup()), FadeOut(cross), FadeOut(rule_text))

        # Show 30
        num_30 = MathTex("30", font_size=40)
        num_30.move_to(ORIGIN)
        self.play(Write(num_30))
        self.wait(1)

        # Create zero and cross
        zero_30 = MathTex("0", font_size=40).next_to(num_30, RIGHT)
        cross_30 = Cross(zero_30)
        self.play(Write(zero_30), Write(cross_30))
        self.wait(1)

        # Make last digit '0' red and shake
        if len(num_30) > 1:
            zero_30 = num_30[1]
            self.play(zero_30.animate.set_color(RED).animate.shift(RIGHT * 0.1).shift(LEFT * 0.1).shift(RIGHT * 0.1).shift(LEFT * 0.1))
        self.wait(0.5)

        # Add large red X
        cross2 = Cross(stroke_width=12, scale_factor=1.5)
        cross2.move_to(ORIGIN)
        self.play(Create(cross2))
        self.wait(0.5)

        # Show text
        rule_text2 = Text("Rule: Ending in 0 is NEVER Glint", font_size=24).next_to(num_30, DOWN)
        cross2.shift(0.0 * RIGHT + 1.26 * UP)  # layout: separation vector
        self.play(Write(rule_text2))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(num_30), FadeOut(zero_30) if 'zero_30' in locals() else FadeOut(VGroup()), FadeOut(cross2), FadeOut(rule_text2))

        # Show 10
        num_10 = MathTex("10", font_size=40)
        num_10.move_to(ORIGIN)
        self.play(Write(num_10))
        self.wait(1)

        # Make last digit '0' red and shake
        if len(num_10) > 1:
            zero_10 = num_10[1]
            self.play(zero_10.animate.set_color(RED).animate.shift(RIGHT * 0.1).shift(LEFT * 0.1).shift(RIGHT * 0.1).shift(LEFT * 0.1))
        self.wait(0.5)

        # Add large red X
        cross3 = Cross(stroke_width=12, scale_factor=1.5)
        cross3.move_to(ORIGIN)
        self.play(Create(cross3))
        self.wait(0.5)

        # Show text: Division by Zero is Impossible
        div_text = Text("Division by Zero is Impossible", font_size=24).next_to(num_10, DOWN)
        div_text.shift(0.0 * RIGHT + -1.26 * UP)  # layout: separation vector
        self.play(Write(div_text))
        self.wait(2)

        # Fade out
        self.play(FadeOut(num_10), FadeOut(zero_10) if 'zero_10' in locals() else FadeOut(VGroup()), FadeOut(cross3), FadeOut(div_text))

        # Final fade out of title
        self.play(FadeOut(title))
        self.wait(0.5)
