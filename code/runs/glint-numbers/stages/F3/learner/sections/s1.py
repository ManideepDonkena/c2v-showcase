from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Glint Numbers", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 21
        num_21 = Integer(21, font_size=40).move_to(ORIGIN)
        last_digit_21 = num_21[-1].copy()
        self.play(Write(num_21))
        self.wait(0.5)

        # Pulse last digit '1' green
        last_digit_21.set_color(GREEN)
        num_21.shift(-0.3 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(last_digit_21.animate.scale(1.2).set_color(GREEN), run_time=0.5)
        self.play(last_digit_21.animate.scale(1/1.2).set_color(WHITE), run_time=0.5)

        # Fade rest of number
        num_21_copy = num_21.copy()
        num_21.shift(0.0 * RIGHT + 0.43 * UP)  # layout: separation vector
        self.play(num_21_copy.animate.set_opacity(0.4), run_time=0.5)

        # Definition text
        definition = Text("Glint Number: Last digit ≠ 0 AND Number ÷ Last Digit = Whole", font_size=24)
        definition.next_to(num_21, DOWN, buff=0.5)
        self.play(Write(definition))
        self.wait(0.5)

        # Checkmark
        check = Tex(r"$\checkmark$").set_color(GREEN).scale(1.5)
        check.next_to(num_21, RIGHT, buff=0.5)
        self.play(FadeIn(check))
        self.wait(1)

        # Fade out 21 elements
        self.play(FadeOut(num_21_copy), FadeOut(last_digit_21), FadeOut(definition), FadeOut(check))

        # Show 22 with last digit '2' pulsing
        num_22 = Integer(22, font_size=40).move_to(ORIGIN)
        self.play(Write(num_22))
        self.wait(0.5)

        last_digit_22 = num_22[-1].copy()
        last_digit_22.set_color(GREEN)
        num_22.shift(-0.33 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(last_digit_22.animate.scale(1.2).set_color(GREEN), run_time=0.5)
        self.play(last_digit_22.animate.scale(1/1.2).set_color(WHITE), run_time=0.5)

        # Equation
        equation = MathTex("22 \\div 2 = 11", font_size=36)
        equation.next_to(num_22, DOWN, buff=0.5)
        self.play(Write(equation))
        self.wait(0.5)

        # Green checkmark
        check2 = Tex(r"$\checkmark$").set_color(GREEN).scale(1.5)
        check2.next_to(equation, RIGHT, buff=0.5)
        self.play(FadeIn(check2))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(num_22), FadeOut(last_digit_22), FadeOut(equation), FadeOut(check2), FadeOut(title))
        self.wait(0.5)
