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
        # Highlight '0' in red and shake it
        zero = num[0]
        self.play(
            zero.animate.set_color(RED),
            ApplyMethod(zero.shift, UR * 0.1),
            ApplyMethod(zero.shift, DL * 0.1),
            run_time=0.5
        )
        self.wait(0.5)

        # Shake again
        self.play(
            ApplyMethod(zero.shift, UR * 0.1),
            ApplyMethod(zero.shift, DL * 0.1),
            run_time=0.5
        )
        self.wait(0.5)

        # Stamp with large red X
        x_mark = Cross(stroke_color=RED, stroke_width=12, scale_factor=2)
        x_mark.move_to(num)
        self.play(FadeIn(x_mark))
        self.wait(1)

        # Rule text
        rule = Text("Rule: Ending in 0 is NEVER Glint", font_size=24).next_to(num, DOWN)
        rule.shift(0.0 * RIGHT + -1.76 * UP)  # layout: separation vector
        self.play(Write(rule))
        self.wait(1.5)

        # Narration key words
        self.play(FadeOut(x_mark))
        self.wait(0.5)

        # Explanation text
        explanation = Text("This is because division by zero is undefined", font_size=24).next_to(rule, DOWN)
        self.play(Write(explanation))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(num),
            FadeOut(rule),
            FadeOut(explanation),
            FadeOut(title)
        )
        self.wait(0.5)
