from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Chained Operations Example", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First example: 2 ⊕ 3
        expr1 = MathTex("2 \\oplus 3", font_size=40)
        self.play(Write(expr1))
        self.wait(1)

        # Step 1: 2 + 3
        step1 = MathTex("2 + 3", font_size=40).move_to(expr1.get_center())
        self.play(Transform(expr1, step1))
        self.wait(1)

        # Step 2: add (2 × 3)
        step2 = MathTex("2 + 3 + (2 \\times 3)", font_size=40).move_to(expr1.get_center())
        self.play(Transform(expr1, step2))
        self.wait(1)

        # Step 3: resolve to 11
        step3 = MathTex("= 11", font_size=40).move_to(expr1.get_center())
        self.play(Transform(expr1, step3))
        self.wait(1.5)

        # Fade out first example
        self.play(FadeOut(expr1))

        # Show nested structure: a ⊕ (b ⊕ c)
        nested = MathTex("2 \\oplus (3 \\oplus 4)", font_size=40).to_edge(UP, buff=0.5)
        nested.shift(0.0 * RIGHT + -0.65 * UP)  # layout: separation vector
        self.play(Write(nested))
        self.wait(1)

        # Highlight inner parentheses
        inner = SurroundingRectangle(MathTex("3 \\oplus 4"), color=YELLOW, buff=0.1)
        self.play(Create(inner))
        self.wait(1)

        # Calculate inner part: 3 ⊕ 4 = 3 + 4 + 12 = 19
        calc_inner = MathTex("3 \\oplus 4 = 3 + 4 + (3 \\times 4) = 19", font_size=30)
        calc_inner.next_to(nested, DOWN, buff=0.5)
        self.play(Write(calc_inner))
        self.wait(2)

        # Show outer operation: 2 ⊕ 19
        outer = MathTex("2 \\oplus 19 = 2 + 19 + (2 \\times 19) = 43", font_size=30)
        outer.next_to(calc_inner, DOWN, buff=0.5)
        self.play(Write(outer))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(nested), FadeOut(inner), FadeOut(calc_inner), FadeOut(outer))
        self.wait(0.5)
