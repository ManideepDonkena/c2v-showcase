from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Zero Exclusion Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 50
        num_50 = MathTex("50").scale(2)
        self.play(Write(num_50))
        self.wait(1)
        # Make last digit '0' red and shake
        if len(num_50) > 1:
            zero_50 = num_50[1]
            self.play(zero_50.animate.set_color(RED).shift(RIGHT * 0.1).shift(LEFT * 0.1).shift(RIGHT * 0.1).shift(LEFT * 0.1))
        self.wait(0.5)

        # Add large red X
        cross = Cross(stroke_color=RED, stroke_width=12, scale_factor=2)
        cross.move_to(num_50)
        self.play(Create(cross))
        self.wait(1)

        # Rule text
        rule_text = Text("Rule: Ending in 0 is NEVER Glint", font_size=24).next_to(num_50, DOWN)
        rule_text.shift(0.0 * RIGHT + -1.56 * UP)  # layout: separation vector
        self.play(Write(rule_text))
        self.wait(2)

        # Clear screen
        self.play(FadeOut(num_50), FadeOut(cross), FadeOut(rule_text))

        # Show 10
        num_10 = MathTex("10").scale(2)
        self.play(Write(num_10))
        self.wait(1)

        # Make last digit '0' red and shake
        if len(num_10) > 1:
            zero_10 = num_10[1]
            self.play(zero_10.animate.set_color(RED).shift(RIGHT * 0.1).shift(LEFT * 0.1).shift(RIGHT * 0.1).shift(LEFT * 0.1))
        self.wait(0.5)

        # Add large red X
        cross_10 = Cross(stroke_color=RED, stroke_width=12, scale_factor=2)
        cross_10.move_to(num_10)
        self.play(Create(cross_10))
        self.wait(1)

        # Rule text again
        rule_text_2 = Text("Ending in 0 is NEVER Glint", font_size=24).next_to(num_10, DOWN)
        rule_text_2.shift(0.0 * RIGHT + -1.56 * UP)  # layout: separation vector
        self.play(Write(rule_text_2))
        self.wait(2)

        # Clear screen
        self.play(FadeOut(num_10), FadeOut(cross_10), FadeOut(rule_text_2))

        # Show 22
        num_22 = MathTex("22").scale(2)
        self.play(Write(num_22))
        self.wait(1)

        # Make last digit '2' pulse
        if len(num_22) > 1:
            two_22 = num_22[1]
            self.play(two_22.animate.scale(1.2).scale(1/1.2))
        self.wait(0.5)

        # Show equation and checkmark
        eq = MathTex("22 \\div 2 = 11").scale(1.5)
        check = Tex("\\checkmark", color=GREEN).scale(2)
        group = VGroup(eq, check).arrange(RIGHT, buff=0.5).next_to(num_22, DOWN)
        self.play(Write(eq))
        self.wait(0.5)
        self.play(Write(check))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(num_22), FadeOut(group))

        self.wait(0.5)
