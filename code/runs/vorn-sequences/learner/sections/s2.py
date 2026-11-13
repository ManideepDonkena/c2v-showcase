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

        # Formula
        formula = MathTex("v(n) = v(n-1) + 2 \\cdot v(n-2)").scale(1.2)
        formula.to_edge(UP).shift(DOWN * 1.8)
        self.play(Write(formula))
        self.wait(0.5)

        # Highlight v(n-1) in formula
        highlight = SurroundingRectangle(formula[0][3:6], color=YELLOW, buff=0.1)
        highlight.shift(0.0 * RIGHT + 0.85 * UP)  # layout: separation vector
        self.play(Create(highlight))
        self.wait(0.5)
        self.play(FadeOut(highlight))

        # Show v(3) calculation
        calc3 = MathTex("v(3) = 3 + 2 \\cdot 1 = 5").scale(1.2)
        calc3.next_to(seq, DOWN, buff=0.8)
        calc3.shift(0.0 * RIGHT + -0.43 * UP)  # layout: separation vector
        self.play(Write(calc3))
        self.wait(1)

        # Show v(4) calculation
        calc4 = MathTex("v(4) = 5 + 2 \\cdot 3 = 11").scale(1.2)
        calc4.next_to(calc3, DOWN, buff=0.8)
        self.play(Write(calc4))
        self.wait(1)

        # Explanation text
        explanation = Text("Because we add v(n-1) to 2 times the term before, the result is larger than 2 times the term before.", font_size=24).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(seq),
            FadeOut(formula),
            FadeOut(calc3),
            FadeOut(calc4),
            FadeOut(explanation)
        )
        self.wait(0.5)
