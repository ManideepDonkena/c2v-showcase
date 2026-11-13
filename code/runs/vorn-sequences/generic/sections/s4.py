from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Growth Rate Analysis", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial sequence
        seq = [1, 3, 5, 11]
        terms = [MathTex(f"v({i})={seq[i]}", font_size=32) for i in range(len(seq))]
        terms[0].to_edge(LEFT).shift(UP * 0.5)
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
            ratio = MathTex(f"\\frac{{v({i+1})}}{{v({i})}} = {seq[i+1]/seq[i]:.2f}", font_size=24)
            ratio.next_to(arrow, UP, buff=0.2)
            arrows.append(arrow)
            ratios.append(ratio)

        self.play(*[Create(arrow) for arrow in arrows])
        self.wait(0.5)
        self.play(*[Write(ratio) for ratio in ratios])
        self.wait(1)

        # "Approx. 2x" text
        approx_text = Text("Approx. 2x", font_size=32).to_edge(UP).shift(DOWN * 0.5)
        self.play(FadeIn(approx_text))
        self.wait(1.5)

        # Narration text
        narration = Text("Each term is roughly twice the size of the one before it.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        self.play(FadeOut(narration), FadeOut(approx_text))

        # Show rule
        rule = Text("v(n) = v(n-1) + 2×v(n-2)", font_size=30)
        rule.to_edge(UP).shift(DOWN * 1.5)
        self.play(Write(rule))
        self.wait(1)

        # Example calculation
        calc = MathTex("v(3) = 3 + 2 \\times 1 = 5", font_size=30)
        calc.next_to(rule, DOWN, buff=0.5)
        self.play(Write(calc))
        self.wait(1)

        calc2 = MathTex("v(4) = 5 + 2 \\times 3 = 11", font_size=30)
        calc2.next_to(calc, DOWN, buff=0.5)
        self.play(Write(calc2))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(terms[0]), FadeOut(terms[1]), FadeOut(terms[2]), FadeOut(terms[3]),
            FadeOut(arrows[0]), FadeOut(arrows[1]), FadeOut(arrows[2]),
            FadeOut(ratios[0]), FadeOut(ratios[1]), FadeOut(ratios[2]),
            FadeOut(rule),
            FadeOut(calc),
            FadeOut(calc2)
        )
        self.wait(0.5)
