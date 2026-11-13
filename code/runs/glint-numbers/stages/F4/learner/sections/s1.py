from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Glint Numbers", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial number 21
        num_21 = MathTex("21").scale(2).move_to(ORIGIN)
        last_digit_21 = num_21[-1].copy()
        self.play(Write(num_21))
        self.wait(0.5)

        # Highlight last digit 1 in green
        self.play(last_digit_21.animate.set_color(GREEN))
        self.wait(0.5)

        # Fade out rest of number
        self.play(FadeOut(num_21[:1]), FadeOut(num_21[2:]))
        self.wait(0.5)

        # Definition text
        definition = Text("Glint Number: Last digit ≠ 0 AND Number ÷ Last Digit = Whole", font_size=24).next_to(num_21, DOWN)
        self.play(Write(definition))
        self.wait(1)

        # Checkmark
        check = Tex(r"$\checkmark$").scale(2).next_to(definition, RIGHT)
        self.play(Write(check))
        self.wait(1.5)

        # Fade out previous content
        self.play(FadeOut(title), FadeOut(num_21), FadeOut(definition), FadeOut(check))

        # Rule 1: Every number ending in 1 is glint
        rule1 = Text("Rule (1): Every number ending in 1 is a Glint number", font_size=24).to_edge(UP)
        self.play(Write(rule1))
        self.wait(0.5)

        # Show example: 13 is NOT glint
        num_13 = MathTex("13").scale(2).move_to(ORIGIN)
        num_13.shift(0.0 * RIGHT + 0.83 * UP)  # layout: separation vector
        self.play(Write(num_13))
        self.wait(0.5)

        # Highlight last digit 3 in red
        if len(num_13) > 1:
            last_digit_13 = num_13[-1].copy()
            self.play(last_digit_13.animate.set_color(RED))
            self.wait(0.5)

        # Show division check
        div_check = MathTex("13 \\div 3 = 4.33...").next_to(num_13, DOWN)
        self.play(Write(div_check))
        self.wait(1)

        # Not glint
        not_glint = Text("Not a Glint number", font_size=24).next_to(div_check, DOWN)
        self.play(Write(not_glint))
        self.wait(1.5)

        # Fade out 13 example
        self.play(FadeOut(num_13), FadeOut(div_check), FadeOut(not_glint))

        # Show 48 is glint
        num_48 = MathTex("48").scale(2).move_to(ORIGIN)
        last_digit_48 = num_48[-1].copy()
        self.play(Write(num_48))
        self.wait(0.5)

        # Highlight last digit 8 in green
        self.play(last_digit_48.animate.set_color(GREEN))
        self.wait(0.5)

        div_check_48 = MathTex("48 \\div 8 = 6").next_to(num_48, DOWN)
        self.play(Write(div_check_48))
        self.wait(1)

        glint_48 = Text("Is a Glint number", font_size=24).next_to(div_check_48, DOWN)
        self.play(Write(glint_48))
        self.wait(1.5)

        # Fade out 48 example
        self.play(FadeOut(num_48), FadeOut(div_check_48), FadeOut(glint_48))

        # Show 49 is NOT glint
        num_49 = MathTex("49").scale(2).move_to(ORIGIN)
        last_digit_49 = num_49[-1].copy()
        self.play(Write(num_49))
        self.wait(0.5)

        # Highlight last digit 9 in red
        self.play(last_digit_49.animate.set_color(RED))
        self.wait(0.5)

        div_check_49 = MathTex("49 \\div 9 = 5.44...").next_to(num_49, DOWN)
        self.play(Write(div_check_49))
        self.wait(1)

        not_glint_49 = Text("Not a Glint number", font_size=24).next_to(div_check_49, DOWN)
        self.play(Write(not_glint_49))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(num_49), FadeOut(div_check_49), FadeOut(not_glint_49), FadeOut(rule1))
        self.wait(0.5)
