from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Zero Exclusion Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show number 50
        num_50 = MathTex("50", font_size=40)
        num_50.move_to(ORIGIN)
        self.play(Write(num_50))
        self.wait(1)
        
        # Highlight '0' in red and shake it
        if len(num_50) > 1:
            zero = num_50[1]
            self.play(zero.animate.set_color(RED), run_time=0.2)
            self.play(zero.animate.shift(RIGHT * 0.1).shift(LEFT * 0.1), run_time=0.2)
            self.play(zero.animate.shift(RIGHT * 0.1).shift(LEFT * 0.1), run_time=0.2)
        self.wait(0.5)

        # Stamp large red 'X'
        cross = Cross(stroke_color=RED, stroke_width=15, scale_factor=2)
        cross.move_to(ORIGIN)
        self.play(FadeIn(cross))
        self.wait(1)

        # Rule text
        rule_text = Text("Rule: Ending in 0 is NEVER Glint", font_size=24).move_to(DOWN * 1.5)
        rule_text.shift(0.0 * RIGHT + -0.82 * UP)  # layout: separation vector
        self.play(Write(rule_text))
        self.wait(1.5)

        # Narration key words
        self.play(FadeOut(cross, rule_text))
        self.wait(0.5)

        # Show explanation
        explanation = Text("Because division by zero is undefined", font_size=24).move_to(DOWN * 1.5)
        self.play(Write(explanation))
        self.wait(1.5)

        # Clear screen and show definition
        self.play(FadeOut(num_50, explanation, title))
        self.wait(0.5)

        # Reintroduce rules with new definitions
        rule1 = Text("Rule 1: Every number ending in 1 is glint", font_size=24).to_edge(UP)
        rule2 = Text("Rule 2: A number ending in 0 is never glint", font_size=24).next_to(rule1, DOWN)
        rule3 = Text("Rule 3: A number ending in 5 is always glint", font_size=24).next_to(rule2, DOWN)

        self.play(Write(rule1))
        self.wait(0.5)
        self.play(Write(rule2))
        self.wait(0.5)
        self.play(Write(rule3))
        self.wait(1.5)

        # Worked example
        example = Text("Example: 24 is glint because 24 ÷ 4 = 6", font_size=24).move_to(DOWN * 1.5)
        not_glint = Text("26 is not glint because 26 ÷ 6 is not whole", font_size=24).next_to(example, DOWN)

        self.play(Write(example))
        self.wait(1.5)
        self.play(Write(not_glint))
        self.wait(2)

        # Fade out
        self.play(FadeOut(rule1, rule2, rule3, example, not_glint))
        self.wait(0.5)
