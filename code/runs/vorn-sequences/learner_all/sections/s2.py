from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Calculating v(3) and v(4)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial sequence
        seq = MathTex("1, 3").scale(1.2)
        seq.to_edge(UP).shift(DOWN * 0.8)
        self.play(Write(seq))
        self.wait(0.5)

        # v(3) calculation
        calc3 = MathTex("v(3) =", "3", "+", "2 \\times", "1", "=", "5")
        calc3.scale(1.2)
        calc3.next_to(seq, DOWN, buff=0.5)
        self.play(Write(calc3))
        self.wait(1)

        # Highlight result
        self.play(Indicate(calc3[6]))
        self.wait(0.5)

        # v(4) calculation
        calc4 = MathTex("v(4) =", "5", "+", "2 \\times", "3", "=", "11")
        calc4.scale(1.2)
        calc4.next_to(calc3, DOWN, buff=0.5)
        self.play(Write(calc4))
        self.wait(1)

        # Odd + 2×Odd breakdown
        self.play(FadeOut(calc3), FadeOut(calc4))

        odd_plus = MathTex("Odd", "+", "2 \\times", "Odd")
        odd_plus.scale(1.2)
        odd_plus.to_edge(UP).shift(DOWN * 1.5)
        self.play(Write(odd_plus))
        self.wait(0.5)

        # Breakdown
        step1 = MathTex("Odd", "+", "Even")
        step1.scale(1.2)
        step1.next_to(odd_plus, DOWN, buff=0.5)
        self.play(ReplacementTransform(odd_plus[0], step1[0]), ReplacementTransform(odd_plus[3], step1[2]))
        self.wait(0.5)

        # Odd + Even = Odd
        result = MathTex("Odd", "+", "Even", "=", "Odd")
        result.scale(1.2)
        result.next_to(step1, DOWN, buff=0.5)
        self.play(Write(result))
        self.wait(1)

        # Ratio of consecutive terms
        self.play(FadeOut(odd_plus), FadeOut(step1), FadeOut(result))

        ratio = MathTex("\\frac{v(4)}{v(3)} =", "\\frac{11}{5} =", "2.2")
        ratio.scale(1.2)
        ratio.to_edge(UP).shift(DOWN * 1.5)
        ratio.shift(0.0 * RIGHT + -0.62 * UP)  # layout: separation vector
        self.play(Write(ratio))
        self.wait(1)

        # Statement about ratio
        ratio_text = Text("Ratio ≈ 2", font_size=24).next_to(ratio, DOWN, buff=0.5)
        self.play(Write(ratio_text))
        self.wait(1)

        # Formula v(n) = v(n-1) + 2*v(n-2)
        self.play(FadeOut(ratio), FadeOut(ratio_text))

        formula = MathTex("v(n) =", "v(n-1)", "+", "2 \\times", "v(n-2)")
        formula.scale(1.2)
        formula.to_edge(UP).shift(DOWN * 1.5)
        formula.shift(0.0 * RIGHT + -0.62 * UP)  # layout: separation vector
        self.play(Write(formula))
        self.wait(1)

        # Emphasize v(n-1) and statement
        self.play(Indicate(formula[1]))
        self.wait(0.5)

        statement = Text("Because we add v(n-1) to 2 times the term before, the result is larger than 2 times the term before.", font_size=24)
        statement.next_to(formula, DOWN, buff=0.5)
        statement.shift(0.78 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(statement))
        self.wait(2)

        # Clean up
        self.play(FadeOut(formula), FadeOut(statement), FadeOut(title))
        self.wait(0.5)
