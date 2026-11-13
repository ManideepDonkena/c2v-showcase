from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Seed and the Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial seeds
        v1 = MathTex("v(1) = 1", font_size=40).to_corner(UL)
        v2 = MathTex("v(2) = 3", font_size=40).next_to(v1, DOWN)
        self.play(Write(v1), Write(v2))
        self.wait(1)

        # Arrow to formula
        arrow = Arrow(start=v1.get_bottom(), end=v1.get_bottom() + DOWN * 1.5, buff=0.1)
        arrow.shift(0.0 * RIGHT + -0.71 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Formula box
        formula_box = Rectangle(width=6, height=2, color=BLUE, fill_opacity=0.2).next_to(arrow, DOWN)
        formula = MathTex("v(n) = v(n-1) + 2 \\cdot v(n-2)", font_size=36).move_to(formula_box.get_center())
        self.play(Create(formula_box), Write(formula))
        self.wait(1)

        # Highlight coefficients
        coeff1 = formula[0][5:6]  # '1'
        coeff2 = formula[0][9:10]  # '2'
        self.play(
            Flash(coeff1, color=YELLOW),
            Flash(coeff2, color=YELLOW)
        )
        self.wait(1)

        # Show calculation breakdown
        calc1 = MathTex("Odd + 2 \\times Odd", font_size=36).to_edge(DOWN)
        self.play(Write(calc1))
        self.wait(1)

        calc2 = MathTex("Odd + Even", font_size=36).next_to(calc1, DOWN)
        self.play(Write(calc2))
        self.wait(1)

        # Visual demonstration
        odd1 = Circle(radius=0.5, color=GREEN).shift(LEFT * 2)
        even1 = Circle(radius=0.5, color=BLUE).shift(RIGHT * 2)
        plus = MathTex("+", font_size=36).next_to(odd1, RIGHT)
        self.play(Create(odd1), Create(even1), Write(plus))
        self.wait(0.5)

        result = MathTex("Odd", font_size=36).next_to(plus, RIGHT)
        self.play(Write(result))
        self.wait(1)

        # Algebraic breakdown
        self.play(FadeOut(calc1), FadeOut(calc2), FadeOut(odd1), FadeOut(even1), FadeOut(plus), FadeOut(result))

        alg = MathTex("Odd + 2 \\cdot Odd", font_size=36).to_edge(DOWN)
        self.play(Write(alg))
        self.wait(0.5)

        even_term = MathTex("2 \\cdot Odd = Even", font_size=30).next_to(alg, DOWN)
        self.play(Write(even_term))
        self.wait(1)

        final = MathTex("Odd + Even = Odd", font_size=36).next_to(even_term, DOWN)
        self.play(Write(final))
        self.wait(1.5)

        # Show ratio
        self.play(FadeOut(alg), FadeOut(even_term), FadeOut(final))

        ratio = MathTex("\\frac{v(4)}{v(3)} = \\frac{11}{5} = 2.2", font_size=36).to_edge(DOWN)
        self.play(Write(ratio))
        self.wait(1.5)

        # Show that v(n) > 2*v(n-2)
        self.play(FadeOut(ratio))

        comparison = MathTex("v(n) = v(n-1) + 2 \\cdot v(n-2)", font_size=36).to_edge(DOWN)
        self.play(Write(comparison))
        self.wait(1)

        highlight_vn1 = MathTex("v(n-1)", font_size=36, color=YELLOW).next_to(comparison[0][5:9], DOWN)
        self.play(Write(highlight_vn1))
        self.wait(1)

        statement = Text("Because we add v(n-1) to 2 times the term before,\nthe result is larger than 2 times the term before.", font_size=24).next_to(comparison, DOWN)
        self.play(Write(statement))
        self.wait(2)

        # Cleanup
        self.play(FadeOut(comparison), FadeOut(highlight_vn1), FadeOut(statement), FadeOut(title))
        self.wait(0.5)
