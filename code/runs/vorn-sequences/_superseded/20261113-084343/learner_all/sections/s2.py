from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Calculating v(3) and v(4)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial sequence
        seq = MathTex("1, 3").scale(1.2)
        seq.to_corner(UL)
        self.play(Write(seq))
        self.wait(0.5)

        # Formula box
        formula = MathTex("v(n) = v(n-1) + 2 \\cdot v(n-2)")
        formula.scale(0.8).to_edge(DOWN)
        self.play(Write(formula))
        self.wait(0.5)

        # Highlight coefficient '2'
        highlight = SurroundingRectangle(formula[0][7:9], color=YELLOW, buff=0.1)
        highlight.shift(0.0 * RIGHT + 0.55 * UP)  # layout: separation vector
        self.play(Create(highlight))
        self.wait(0.5)
        self.play(FadeOut(highlight))

        # Show initial conditions
        init_label = Text("Initial conditions:", font_size=24).next_to(seq, DOWN, buff=0.5)
        init_label.shift(0.64 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(init_label))
        self.wait(0.5)

        v1 = MathTex("v(1) = 1").scale(0.8).next_to(init_label, RIGHT, buff=0.5)
        v2 = MathTex("v(2) = 3").scale(0.8).next_to(v1, RIGHT, buff=0.5)
        self.play(Write(v1), Write(v2))
        self.wait(0.5)

        # Compute v(3)
        calc3 = MathTex("v(3) = 3 + 2 \\cdot 1 = 5").scale(0.9).next_to(formula, UP, buff=0.5)
        self.play(Write(calc3))
        self.wait(0.5)

        # Highlight result
        highlight_result = SurroundingRectangle(calc3[0][7], color=GREEN, buff=0.1)
        highlight_result.shift(0.0 * RIGHT + 0.59 * UP)  # layout: separation vector
        self.play(Create(highlight_result))
        self.wait(0.5)
        self.play(FadeOut(highlight_result))

        # Compute v(4)
        calc4 = MathTex("v(4) = 5 + 2 \\cdot 3 = 11").scale(0.9).next_to(calc3, DOWN, buff=0.5)
        self.play(Write(calc4))
        self.wait(0.5)

        # Breakdown: Odd + 2 × Odd
        breakdown = MathTex("Odd + 2 \\cdot Odd").scale(0.8).to_edge(LEFT, buff=1)
        self.play(Write(breakdown))
        self.wait(0.5)

        even_part = MathTex("= Odd + Even").scale(0.8).next_to(breakdown, DOWN, buff=0.3)
        self.play(Write(even_part))
        self.wait(0.5)

        odd_result = MathTex("= Odd").scale(0.8).next_to(even_part, DOWN, buff=0.3)
        self.play(Write(odd_result))
        self.wait(0.5)

        # Algebraic proof
        alg_proof = MathTex("v(n) = v(n-1) + 2 \\cdot v(n-2)").scale(0.8).to_edge(RIGHT, buff=1)
        self.play(Write(alg_proof))
        self.wait(0.5)

        even_label = MathTex("2 \\cdot v(n-2) = Even").scale(0.7).next_to(alg_proof, DOWN, buff=0.3)
        self.play(Write(even_label))
        self.wait(0.5)

        final_odd = MathTex("v(n-1) + Even = Odd").scale(0.7).next_to(even_label, DOWN, buff=0.3)
        self.play(Write(final_odd))
        self.wait(0.5)

        # Ratio
        ratio = MathTex("\\frac{v(4)}{v(3)} = \\frac{11}{5} = 2.2").scale(0.8).next_to(calc4, DOWN, buff=0.5)
        self.play(Write(ratio))
        self.wait(0.5)

        # Explanation of growth
        growth = Text("Each term is about twice the previous one.", font_size=24).next_to(ratio, DOWN, buff=0.3)
        self.play(Write(growth))
        self.wait(0.5)

        # Emphasize v(n-1) term
        emphasize_vn1 = SurroundingRectangle(formula[0][2:6], color=BLUE, buff=0.1)
        self.play(Create(emphasize_vn1))
        self.wait(0.5)
        self.play(FadeOut(emphasize_vn1))

        # Final explanation
        explanation = Text("Because we add v(n-1) to 2 times the term before, the result is larger than 2 times the term before.", font_size=24).next_to(growth, DOWN, buff=0.3)
        self.play(Write(explanation))
        self.wait(1)

        # Cleanup
        self.play(FadeOut(title), FadeOut(seq), FadeOut(formula), FadeOut(calc3), FadeOut(calc4),
                  FadeOut(breakdown), FadeOut(even_part), FadeOut(odd_result), FadeOut(alg_proof),
                  FadeOut(even_label), FadeOut(final_odd), FadeOut(ratio), FadeOut(growth),
                  FadeOut(explanation), FadeOut(v1), FadeOut(v2), FadeOut(init_label))
        self.wait(0.5)
