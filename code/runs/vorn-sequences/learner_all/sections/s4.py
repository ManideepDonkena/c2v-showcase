from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Growth Rate Analysis", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Sequence terms
        seq = [1, 3, 5, 11]
        terms = [MathTex(f"v({i+1}) = {seq[i]}") for i in range(4)]
        terms[0].to_edge(LEFT).shift(UP * 0.5)
        terms[1].next_to(terms[0], RIGHT, buff=1)
        terms[2].next_to(terms[1], RIGHT, buff=1)
        terms[3].next_to(terms[2], RIGHT, buff=1)

        self.play(*[Write(term) for term in terms])
        self.wait(1)

        # Arrows and ratios
        arrows = []
        ratios = []
        for i in range(1, 4):
            arrow = Arrow(terms[i-1].get_right(), terms[i].get_left(), buff=0.2)
            ratio = MathTex(f"\\frac{{v({i+1})}}{{v({i})}} = {seq[i]/seq[i-1]:.2f}")
            ratio.next_to(arrow, UP, buff=0.2)
            arrows.append(arrow)
            ratios.append(ratio)

        self.play(*[Create(arrow) for arrow in arrows])
        self.wait(0.5)
        self.play(*[Write(ratio) for ratio in ratios])
        self.wait(1)

        # Fade out ratios and show "Approx. 2x"
        self.play(*[FadeOut(ratio) for ratio in ratios])
        approx = Text("Approx. 2x", font_size=30).next_to(arrows[0], UP, buff=0.5)
        self.play(Write(approx))
        self.wait(1.5)

        # Fade out arrows and approx
        self.play(*[FadeOut(arrow) for arrow in arrows], FadeOut(approx))

        # Odd + 2×Odd breakdown
        odd_plus = MathTex("Odd + 2 \\times Odd")
        odd_plus.to_edge(LEFT).shift(DOWN * 1.5)
        self.play(Write(odd_plus))
        self.wait(0.5)

        plus_even = MathTex("= Odd + Even")
        plus_even.next_to(odd_plus, RIGHT, buff=0.5)
        self.play(Write(plus_even))
        self.wait(0.5)

        result = MathTex("= Odd")
        result.next_to(plus_even, RIGHT, buff=0.5)
        self.play(Write(result))
        self.wait(1)

        # Fade out breakdown
        self.play(FadeOut(odd_plus), FadeOut(plus_even), FadeOut(result))

        # Formula v(n) = v(n-1) + 2*v(n-2)
        formula = MathTex("v(n) = v(n-1) + 2 \\cdot v(n-2)")
        formula.to_edge(UP).shift(DOWN * 2.5)
        formula.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        self.play(Write(formula))
        self.wait(1)

        # Emphasize v(n-1)
        v_n_minus_1 = MathTex("v(n-1)")
        v_n_minus_1.next_to(formula, DOWN, buff=0.3).shift(RIGHT * 1.5)
        v_n_minus_1.set_color(YELLOW)
        v_n_minus_1.shift(0.0 * RIGHT + -0.5 * UP)  # layout: separation vector
        self.play(Write(v_n_minus_1))
        self.wait(0.5)

        # Say: "Because we add v(n-1) to 2 times the term before..."
        explanation = Text("Because we add v(n-1) to 2 times the term before, the result is larger than 2 times the term before.", font_size=24)
        explanation.next_to(v_n_minus_1, DOWN, buff=0.5)
        explanation.shift(-2.28 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(explanation))
        self.wait(2)

        # Fade out
        self.play(FadeOut(formula), FadeOut(v_n_minus_1), FadeOut(explanation))

        # Final narration text
        final_text = Text("Finally, observe the growth: each term is roughly twice the size of the one before it. This rapid expansion is a defining characteristic of Vorn sequences.", font_size=24)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)

        self.play(FadeOut(final_text), FadeOut(title))
