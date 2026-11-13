from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Glint Numbers", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 21
        num_21 = Integer(21, font_size=40).move_to(ORIGIN)
        last_digit_21 = num_21[1].copy()
        last_digit_21.set_color(GREEN)
        self.play(Write(num_21))
        self.play(last_digit_21.animate.scale(1.5).set_color(GREEN), run_time=0.5)
        self.wait(0.5)

        # Definition text
        definition = MathTex(r"\text{Glint Number: Last digit} \neq 0 \text{ AND } \frac{\text{Number}}{\text{Last Digit}} = \text{Whole}", font_size=24).next_to(num_21, DOWN)
        self.play(Write(definition))
        self.wait(1)

        # Checkmark for 21
        check_21 = Tex(r"$\checkmark$", color=GREEN, font_size=36).next_to(num_21, RIGHT)
        self.play(FadeIn(check_21))
        self.wait(1)

        # Fade out 21 and definition
        self.play(FadeOut(num_21), FadeOut(last_digit_21), FadeOut(definition), FadeOut(check_21))

        # Show 22 with division
        num_22 = Integer(22, font_size=40).move_to(ORIGIN)
        last_digit_22 = num_22[1].copy()
        last_digit_22.set_color(GREEN)
        self.play(Write(num_22))
        self.play(last_digit_22.animate.scale(1.5).set_color(GREEN), run_time=0.5)
        self.wait(0.5)

        # Division equation
        eq_22 = MathTex("22 \\div 2 = 11", font_size=30).next_to(num_22, DOWN)
        self.play(Write(eq_22))
        self.wait(1)

        check_22 = Tex(r"$\checkmark$", color=GREEN, font_size=36).next_to(num_22, RIGHT)
        self.play(FadeIn(check_22))
        self.wait(1.5)

        # Fade out 22 and equation
        self.play(FadeOut(num_22), FadeOut(last_digit_22), FadeOut(eq_22), FadeOut(check_22))

        # Show 21 and 24 together
        num_21 = Integer(21, font_size=40).move_to(LEFT * 2)
        last_digit_21 = num_21[1].copy()
        last_digit_21.set_color(GREEN)

        num_24 = Integer(24, font_size=40).move_to(RIGHT * 2)
        last_digit_24 = num_24[1].copy()
        last_digit_24.set_color(GREEN)

        self.play(Write(num_21), Write(num_24))
        self.play(last_digit_21.animate.scale(1.5).set_color(GREEN),
                  last_digit_24.animate.scale(1.5).set_color(GREEN), run_time=0.5)
        self.wait(0.5)

        # Show checkmarks
        check_21 = Tex(r"$\checkmark$", color=GREEN, font_size=36).next_to(num_21, RIGHT)
        check_24 = Tex(r"$\checkmark$", color=GREEN, font_size=36).next_to(num_24, RIGHT)
        self.play(FadeIn(check_21), FadeIn(check_24))
        self.wait(1.5)

        # Narration text
        narration = Text("Every number ending in 1 is a Glint number.", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)

        self.play(FadeOut(narration), FadeOut(num_21), FadeOut(last_digit_21), FadeOut(num_24), FadeOut(last_digit_24), FadeOut(check_21), FadeOut(check_24))
        self.wait(0.5)
