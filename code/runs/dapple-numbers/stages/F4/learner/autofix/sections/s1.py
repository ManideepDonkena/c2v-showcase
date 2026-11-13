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

        self.play(FadeOut(title), FadeOut(tens_digit), FadeOut(units_digit),
                  FadeOut(compare), FadeOut(number), FadeOut(condition), FadeOut(narration))
        self.wait(0.5)
