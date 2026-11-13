from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Growth Rate Analysis", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Sequence terms
        sequence = [1, 3, 5, 11]
        terms = [MathTex(f"v({i+1}) = {sequence[i]}") for i in range(4)]
        terms_group = VGroup(*terms).arrange(RIGHT, buff=1.2).move_to(DOWN * 0.5)
        self.play(Write(terms_group))
        self.wait(1)

        # Arrows and ratios
        arrows = []
        ratios = []
        for i in range(1, len(sequence)):
            start = terms[i-1].get_center()
            end = terms[i].get_center()
            arrow = Arrow(start, end, buff=0.2, color=YELLOW)
            arrows.append(arrow)

            ratio_tex = MathTex(f"\\frac{{v({i+1})}}{{v({i})}} = \\frac{{{sequence[i]}}}{{{sequence[i-1]}}} = {sequence[i]/sequence[i-1]:.2f}")
            ratio_tex.scale(0.7)
            ratio_tex.next_to(arrow, UP, buff=0.2)
            ratios.append(ratio_tex)

        for arrow in arrows:
            arrow.shift(0.0 * RIGHT + -0.57 * UP)  # layout: separation vector
            self.play(GrowArrow(arrow), run_time=0.5)
        self.wait(0.5)

        for i, ratio in enumerate(ratios):
            self.play(Write(ratio), run_time=0.5)
        self.wait(1)

        # "Approx. 2x" text
        approx_text = Text("Approx. 2x", font_size=30).to_edge(UP).shift(UP * 0.5)
        self.play(FadeIn(approx_text), run_time=0.5)
        self.wait(1.5)

        # Fade out everything except title and sequence
        self.play(
            *[FadeOut(obj) for obj in arrows + ratios],
            run_time=0.5
        )
        self.wait(0.5)

        # Show final ratio explicitly
        final_ratio = MathTex("v(4)/v(3) = 11/5 = 2.2", font_size=36)
        final_ratio.to_edge(DOWN)
        self.play(Write(final_ratio), run_time=0.7)
        self.wait(1)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(terms_group),
            FadeOut(final_ratio),
            FadeOut(approx_text),
            run_time=0.5
        )
        self.wait(0.5)
