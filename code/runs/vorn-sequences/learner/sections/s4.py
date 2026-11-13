from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Growth Rate Analysis", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Sequence terms
        sequence = [1, 3, 5, 11]
        terms = [MathTex(f"v({i}) = {val}") for i, val in enumerate(sequence, 1)]
        terms_group = VGroup(*terms).arrange(RIGHT, buff=1).move_to(DOWN * 0.5)
        self.play(Write(terms_group))
        self.wait(1)

        # Arrows and ratios
        arrows = []
        ratios = []
        for i in range(1, len(sequence)):
            start = terms[i-1].get_center()
            end = terms[i].get_center()
            arrow = Arrow(start, end, buff=0.2)
            ratio = MathTex(f"\\frac{{v({i+1})}}{{v({i})}} = {sequence[i]/sequence[i-1]:.2f}")
            ratio.next_to(arrow, UP, buff=0.2)
            arrows.append(arrow)
            ratios.append(ratio)

        arrow_group = VGroup(*arrows)
        ratio_group = VGroup(*ratios)

        arrow_group.shift(0.0 * RIGHT + -0.57 * UP)  # layout: separation vector
        self.play(Create(arrow_group))
        self.wait(0.5)
        self.play(Write(ratio_group))
        self.wait(1.5)

        # Fade out ratios and show "Approx. 2x"
        self.play(FadeOut(ratio_group))
        approx_text = Text("Approx. 2x", font_size=30).move_to(UP * 1.5)
        self.play(FadeIn(approx_text))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(terms_group), FadeOut(arrow_group), FadeOut(approx_text))
        self.wait(0.5)
