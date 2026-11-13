from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Calculating v(3) and v(4)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial sequence
        seq = MathTex("1, 3").scale(1.2)
        seq.to_edge(LEFT).shift(DOWN * 0.5)
        self.play(Write(seq))
        self.wait(0.5)

        # Formula
        formula = MathTex("v(n) = v(n-1) + 2 \\cdot v(n-2)")
        formula.scale(0.8).to_edge(UP).shift(DOWN * 0.8)
        self.play(Write(formula))
        self.wait(0.5)

        # Highlight v(n-1) in formula
        highlight = SurroundingRectangle(formula[0][3:6], color=YELLOW, buff=0.05)
        highlight.shift(0.0 * RIGHT + -0.6 * UP)  # layout: separation vector
        self.play(Create(highlight))
        self.wait(0.5)
        self.play(FadeOut(highlight))

        # Show v(3) calculation
        calc1 = MathTex("v(3) = 3 + 2 \\cdot 1 = 5")
        calc1.scale(0.9).next_to(seq, DOWN, buff=0.5)
        calc1.shift(1.13 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(calc1))
        self.wait(1)

        # Show v(4) calculation
        calc2 = MathTex("v(4) = 5 + 2 \\cdot 3 = 11")
        calc2.scale(0.9).next_to(calc1, DOWN, buff=0.5)
        self.play(Write(calc2))
        self.wait(1)

        # Narration text
        narration1 = Text("To find v(3), we add 3 to twice 1, resulting in 5.", font_size=24)
        narration1.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(narration1))
        self.wait(1.5)
        self.play(FadeOut(narration1))

        narration2 = Text("For v(4), we take that 5 and add it to twice 3, giving us 11.", font_size=24)
        narration2.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(narration2))
        self.wait(1.5)
        self.play(FadeOut(narration2))

        # Explanation about growth
        explanation = Text("Because we add v(n-1) to 2 times the term before, the result is larger than 2 times the term before.", font_size=24)
        explanation.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(explanation))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(seq),
            FadeOut(calc1),
            FadeOut(calc2),
            FadeOut(formula),
            FadeOut(explanation),
            FadeOut(title)
        )
        self.wait(0.5)
