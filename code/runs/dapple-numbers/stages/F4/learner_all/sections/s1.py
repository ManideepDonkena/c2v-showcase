from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Condition", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Digits 5 and 2
        tens_digit = Integer(5, font_size=80).shift(LEFT * 1.5)
        units_digit = Integer(2, font_size=80).shift(RIGHT * 1.5)
        self.play(Write(tens_digit), Write(units_digit))
        self.wait(0.5)

        # Comparison operator
        compare_op = MathTex(">", font_size=60, color=WHITE).shift(DOWN * 0.2)
        self.play(Write(compare_op))
        self.wait(0.5)

        # Make comparison green
        self.play(compare_op.animate.set_color(GREEN))
        self.wait(0.5)

        # Number 52 with golden glow
        number = MathTex("52", font_size=80).shift(DOWN * 1.5)
        pulse = number.copy().set_stroke(color=YELLOW, width=10)
        self.play(Write(number))
        number.shift(0.0 * RIGHT + 0.72 * UP)  # layout: separation vector
        self.play(Create(pulse), run_time=0.5)
        self.play(FadeOut(pulse))
        self.wait(0.5)

        # Text "Tens > Units"
        condition = Text("Tens > Units", font_size=32).next_to(number, DOWN)
        self.play(Write(condition))
        self.wait(1)

        # Fade out first example
        self.play(FadeOut(tens_digit), FadeOut(units_digit), FadeOut(compare_op), FadeOut(number), FadeOut(condition))

        # Second example: 61
        tens_digit2 = Integer(6, font_size=80).shift(LEFT * 1.5)
        units_digit2 = Integer(1, font_size=80).shift(RIGHT * 1.5)
        self.play(Write(tens_digit2), Write(units_digit2))
        self.wait(0.5)

        compare_op2 = MathTex(">", font_size=60, color=WHITE).shift(DOWN * 0.2)
        self.play(Write(compare_op2))
        self.wait(0.5)

        self.play(compare_op2.animate.set_color(GREEN))
        self.wait(0.5)
        number2 = MathTex("61", font_size=80).shift(DOWN * 1.5)
        self.play(Write(number2))
        self.wait(0.5)

        # Green checkmark
        check = VMobject().set_points_as_corners([ORIGIN, UP, RIGHT]).scale(0.5).next_to(number2, DOWN)
        self.play(Write(check))
        self.wait(1)

        # Fade out second example
        self.play(FadeOut(tens_digit2), FadeOut(units_digit2), FadeOut(compare_op2), FadeOut(number2), FadeOut(check))
        # Third example: 16 (not dapple)
        tens_digit3 = Integer(1, font_size=80).shift(LEFT * 1.5)
        units_digit3 = Integer(6, font_size=80).shift(RIGHT * 1.5)
        self.play(Write(tens_digit3), Write(units_digit3))
        self.wait(0.5)

        compare_op3 = MathTex("<", font_size=60, color=WHITE).shift(DOWN * 0.2)
        self.play(Write(compare_op3))
        self.wait(0.5)

        number3 = MathTex("16", font_size=80).shift(DOWN * 1.5)
        self.play(Write(number3))
        self.wait(0.5)

        # Red X mark
        cross = Cross().scale(0.5).next_to(number3, DOWN)
        self.play(Write(cross))
        self.wait(1)

        # Fade out everything
        self.play(FadeOut(tens_digit3), FadeOut(units_digit3), FadeOut(compare_op3), FadeOut(number3), FadeOut(cross))
        self.wait(0.5)

        # Final definition text
        final_def = Text("A whole number is 'dapple' if its tens digit is strictly greater than its units digit.", font_size=24).to_edge(DOWN)
        self.play(Write(final_def))
        self.wait(1)

        self.play(FadeOut(final_def), FadeOut(title))
