from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Zero Exclusion Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show number 50
        num = MathTex("50", font_size=40)
        self.play(Write(num))
        self.wait(1)
        # Highlight the '0' in red and shake it
        zero = num[1]
        self.play(
            zero.animate.set_color(RED),
            zero.animate.shift(LEFT * 0.1),
            zero.animate.shift(RIGHT * 0.1),
        )
        self.play(
            zero.animate.shift(LEFT * 0.1).shift(RIGHT * 0.1).shift(LEFT * 0.1).shift(RIGHT * 0.1),
            run_time=0.5
        )
        self.wait(0.5)

        # Stamp large red 'X' over the screen
        cross = Cross(stroke_color=RED, stroke_width=15, scale_factor=2)
        self.play(Write(cross))
        self.wait(0.5)

        # Show rule text
        rule_text = Text("Rule: Ending in 0 is NEVER Glint", font_size=24).next_to(num, DOWN)
        self.play(Write(rule_text))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(num),
            FadeOut(cross),
            FadeOut(rule_text)
        )
        self.wait(0.5)
