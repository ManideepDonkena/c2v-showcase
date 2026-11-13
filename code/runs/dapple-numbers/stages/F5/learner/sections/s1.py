from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Condition", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Digits 5 and 2
        tens_digit = Integer(5, font_size=72).shift(LEFT * 1.5)
        units_digit = Integer(2, font_size=72).shift(RIGHT * 1.5)
        self.play(Write(tens_digit), Write(units_digit))
        self.wait(0.5)

        # Comparison operator
        compare = MathTex(">", font_size=72, color=WHITE).shift(DOWN * 0.5)
        self.play(Write(compare))
        self.wait(0.5)

        # Make comparison green
        self.play(compare.animate.set_color(GREEN))
        self.wait(1)

        # Number 52 with golden glow
        number = MathTex("52", font_size=80).shift(UP * 1.5)
        pulse = number.copy().set_stroke(color=YELLOW, width=10)
        self.play(Write(number))
        number.shift(0.0 * RIGHT + 0.72 * UP)  # layout: separation vector
        self.play(Write(pulse))
        self.play(FadeOut(pulse))
        self.wait(0.5)

        # Text "Tens > Units"
        condition = Text("Tens > Units", font_size=36).shift(DOWN * 2)
        self.play(Write(condition))
        self.wait(1.5)

        # Narration text
        narration = Text("A whole number is 'dapple' if its tens digit is strictly greater than its units digit.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        # Example: 61 is dapple
        example_title = Text("Example: 61 is dapple", font_size=36).to_edge(UP)
        example_title.shift(0.0 * RIGHT + -0.66 * UP)  # layout: separation vector
        self.play(Write(example_title))
        self.wait(0.5)

        tens_digit_61 = Integer(6, font_size=72).shift(LEFT * 1.5 + UP * 0.5)
        units_digit_61 = Integer(1, font_size=72).shift(RIGHT * 1.5 + UP * 0.5)
        self.play(Write(tens_digit_61), Write(units_digit_61))
        self.wait(0.5)

        compare_61 = MathTex(">", font_size=72, color=WHITE).shift(DOWN * 0.5)
        self.play(Write(compare_61))
        self.wait(0.5)

        self.play(compare_61.animate.set_color(GREEN))
        self.wait(1)

        number_61 = MathTex("61", font_size=80).shift(UP * 1.5)
        pulse_61 = number_61.copy().set_stroke(color=YELLOW, width=10)
        self.play(Write(number_61))
        number_61.shift(0.0 * RIGHT + 0.72 * UP)  # layout: separation vector
        self.play(Write(pulse_61))
        self.play(FadeOut(pulse_61))
        self.wait(0.5)

        checkmark = MathTex("\checkmark", font_size=80, color=GREEN).shift(DOWN * 2)
        self.play(Write(checkmark))
        self.wait(1.5)

        # Counter-example: 16 is not dapple
        counter_title = Text("Counter-example: 16 is NOT dapple", font_size=36).to_edge(UP)
        self.play(Write(counter_title))
        self.wait(0.5)

        tens_digit_16 = Integer(1, font_size=72).shift(LEFT * 1.5 + UP * 0.5)
        units_digit_16 = Integer(6, font_size=72).shift(RIGHT * 1.5 + UP * 0.5)
        self.play(Write(tens_digit_16), Write(units_digit_16))
        self.wait(0.5)

        compare_16 = MathTex("<", font_size=72, color=WHITE).shift(DOWN * 0.5)
        self.play(Write(compare_16))
        self.wait(0.5)

        number_16 = MathTex("16", font_size=80).shift(UP * 1.5)
        pulse_16 = number_16.copy().set_stroke(color=YELLOW, width=10)
        self.play(Write(number_16))
        number_16.shift(0.0 * RIGHT + 0.72 * UP)  # layout: separation vector
        self.play(Write(pulse_16))
        self.play(FadeOut(pulse_16))
        self.wait(0.5)

        self.play(FadeOut(title), FadeOut(tens_digit), FadeOut(units_digit),
                  FadeOut(compare), FadeOut(number), FadeOut(condition), FadeOut(narration),
                  FadeOut(example_title), FadeOut(tens_digit_61), FadeOut(units_digit_61),
                  FadeOut(compare_61), FadeOut(number_61), FadeOut(checkmark),
                  FadeOut(counter_title), FadeOut(tens_digit_16), FadeOut(units_digit_16),
                  FadeOut(compare_16), FadeOut(number_16))
        self.wait(0.5)
