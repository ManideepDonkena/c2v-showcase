from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Growth Rate Analysis", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Sequence terms
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
        for i in range(1, len(seq)):
            arrow = Arrow(terms[i-1].get_right(), terms[i].get_left(), buff=0.2)
            ratio = MathTex(f"\\frac{{v({i})}}{{v({i-1})}} = {seq[i]/seq[i-1]:.2f}", font_size=24)
            ratio.next_to(arrow, UP, buff=0.2)
            arrows.append(arrow)
            ratios.append(ratio)

        self.play(*[GrowArrow(a) for a in arrows])
        self.wait(0.5)
        self.play(*[Write(r) for r in ratios])
        self.wait(1)

        # Fade out ratios and show "Approx. 2x"
        self.play(*[FadeOut(r) for r in ratios])
        approx = Text("Approx. 2x", font_size=30).to_edge(UP).shift(UP * 0.5)
        self.play(FadeIn(approx))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(terms[0]),
            FadeOut(terms[1]),
            FadeOut(terms[2]),
            FadeOut(terms[3]),
            FadeOut(arrows[0]),
            FadeOut(arrows[1]),
            FadeOut(approx)
        )
        self.wait(0.5)
