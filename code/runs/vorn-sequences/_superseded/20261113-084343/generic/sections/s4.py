from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Growth Rate Analysis", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial sequence
        seq = [1, 3, 5, 11]
        terms = [MathTex(f"v({i}) = {seq[i]}", font_size=32) for i in range(len(seq))]
        terms[0].to_edge(LEFT).shift(DOWN * 0.5)
        terms[1].next_to(terms[0], RIGHT, buff=1)
        terms[2].next_to(terms[1], RIGHT, buff=1)
        terms[3].next_to(terms[2], RIGHT, buff=1)

        self.play(*[Write(term) for term in terms])
        self.wait(1)

        # Arrows and ratios
        arrows = []
        ratios = []

        for i in range(len(seq)-1):
            arrow = Arrow(terms[i].get_right(), terms[i+1].get_left(), buff=0.2, color=YELLOW)
            ratio = MathTex(f"\\frac{{{seq[i+1]}}}{{{seq[i]}}} \\approx {seq[i+1]/seq[i]:.2f}", font_size=24)
            ratio.next_to(arrow, UP, buff=0.2)
            arrows.append(arrow)
            ratios.append(ratio)

        self.play(*[Create(arrow) for arrow in arrows])
        self.wait(0.5)
        self.play(*[Write(ratio) for ratio in ratios])
        self.wait(1)

        # "Approx. 2x" text
        approx_text = Text("Approx. 2x", font_size=32, color=GREEN).to_edge(UP).shift(UP * 0.5)
        self.play(FadeIn(approx_text))
        self.wait(1.5)

        # Fade out old text and show rules
        self.play(
            *[FadeOut(term) for term in terms],
            *[FadeOut(arrow) for arrow in arrows],
            *[FadeOut(ratio) for ratio in ratios],
            FadeOut(approx_text)
        )

        rule1 = Text("Rule 1: Every term is odd", font_size=24).to_edge(LEFT).shift(UP * 0.5)
        rule2 = Text("Rule 2: Each term is about twice the one before", font_size=24).next_to(rule1, DOWN, buff=0.3)

        self.play(Write(rule1))
        self.wait(1)
        rule2.shift(1.39 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(rule2))
        self.wait(1.5)

        # Formula
        formula = MathTex("v(n) = v(n-1) + 2 \\times v(n-2)", font_size=32).to_edge(DOWN)
        self.play(Write(formula))
        self.wait(1.5)

        # Example calculation
        calc1 = MathTex("v(3) = 3 + 2 \\times 1 = 5", font_size=28).next_to(formula, UP, buff=0.5)
        calc2 = MathTex("v(4) = 5 + 2 \\times 3 = 11", font_size=28).next_to(calc1, DOWN, buff=0.3)

        self.play(Write(calc1))
        self.wait(1)
        calc2.shift(0.0 * RIGHT + 0.24 * UP)  # layout: separation vector
        self.play(Write(calc2))
        self.wait(1.5)

        # Final fade out
        self.play(
            FadeOut(rule1),
            FadeOut(rule2),
            FadeOut(formula),
            FadeOut(calc1),
            FadeOut(calc2),
            FadeOut(title)
        )
        self.wait(0.5)
