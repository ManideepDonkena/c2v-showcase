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
        
        # Highlight '0' in red and shake it
        if len(num_50) > 1:
            zero = num_50[1]
            self.play(zero.animate.set_color(RED).shift(LEFT * 0.1).shift(RIGHT * 0.1).shift(LEFT * 0.1).shift(RIGHT * 0.1))
            self.wait(0.5)

        # Add large red X
        cross = Cross(stroke_width=12, scale_factor=1.5)
        cross.move_to(ORIGIN)
        self.play(Create(cross))
        self.wait(0.5)

        # Rule text
        rule_text = Text("Rule: Ending in 0 is NEVER Glint", font_size=24).next_to(title, DOWN, buff=0.5)
        self.play(Write(rule_text))
        self.wait(1.5)

        # Fade out previous elements
        self.play(FadeOut(num_50), FadeOut(cross), FadeOut(rule_text))

        # Example: 30 is not glint
        example_30 = MathTex("30").scale(2)
        example_30.move_to(ORIGIN)
        self.play(Write(example_30))
        self.wait(1)

        if len(example_30) > 1:
            zero_30 = example_30[1]
            self.play(zero_30.animate.set_color(RED).shift(LEFT * 0.1).shift(RIGHT * 0.1).shift(LEFT * 0.1).shift(RIGHT * 0.1))
            self.wait(0.5)

        not_glint = Text("NOT Glint", font_size=24).next_to(example_30, DOWN)
        self.play(Write(not_glint))
        self.wait(1.5)

        self.play(FadeOut(example_30), FadeOut(not_glint))

        # Show 13 is not glint
        example_13 = MathTex("13").scale(2)
        example_13.move_to(ORIGIN)
        self.play(Write(example_13))
        self.wait(1)
        div_13 = MathTex("13 \div 3 = ", "4.33...").next_to(example_13, DOWN)
        self.play(Write(div_13))
        self.wait(1.5)

        not_glint_13 = Text("NOT Glint", font_size=24).next_to(example_13, DOWN)
        not_glint_13.shift(0.0 * RIGHT + 0.31 * UP)  # layout: separation vector
        self.play(Write(not_glint_13))
        self.wait(1.5)

        self.play(FadeOut(example_13), FadeOut(div_13), FadeOut(not_glint_13))

        # Show 48 is glint
        example_48 = MathTex("48").scale(2)
        example_48.move_to(ORIGIN)
        self.play(Write(example_48))
        self.wait(1)

        div_48 = MathTex("48 \\div 8 = ", "6").next_to(example_48, DOWN)
        self.play(Write(div_48))
        self.wait(1.5)

        glint_48 = Text("Glint", font_size=24).next_to(example_48, DOWN)
        self.play(Write(glint_48))
        self.wait(1.5)

        self.play(FadeOut(example_48), FadeOut(div_48), FadeOut(glint_48))

        # Show 49 is not glint
        example_49 = MathTex("49").scale(2)
        example_49.move_to(ORIGIN)
        self.play(Write(example_49))
        self.wait(1)

        div_49 = MathTex("49 \\div 9 = ", "5.44...").next_to(example_49, DOWN)
        self.play(Write(div_49))
        self.wait(1.5)

        not_glint_49 = Text("NOT Glint", font_size=24).next_to(example_49, DOWN)
        not_glint_49.shift(0.0 * RIGHT + 0.31 * UP)  # layout: separation vector
        self.play(Write(not_glint_49))
        self.wait(1.5)

        self.play(FadeOut(example_49), FadeOut(div_49), FadeOut(not_glint_49))

        # Final rule summary
        final_rule = Text("Rule 2: A number ending in 0 is never a Glint number.", font_size=24).move_to(ORIGIN)
        self.play(Write(final_rule))
        self.wait(2)

        self.play(FadeOut(final_rule))
        self.wait(0.5)
