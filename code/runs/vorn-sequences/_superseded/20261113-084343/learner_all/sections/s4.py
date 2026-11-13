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

        for i in range(3):
            arrow = Arrow(terms[i].get_right(), terms[i+1].get_left(), buff=0.2)
            ratio = MathTex(f"\\frac{{v({i+2})}}{{v({i+1})}} = {seq[i+1]/seq[i]:.2f}")
            ratio.next_to(arrow, UP, buff=0.2)
            arrows.append(arrow)
            ratios.append(ratio)

        self.play(*[Create(arrow) for arrow in arrows])
        self.wait(0.5)
        self.play(*[Write(ratio) for ratio in ratios])
        self.wait(1)

        # "Approx. 2x" text
        approx_text = Text("Approx. 2x", font_size=30).to_edge(UP).shift(DOWN * 0.5)
        self.play(FadeIn(approx_text))
        self.wait(1.5)

        # Narration text
        narration = Text("Finally, observe the growth:", font_size=24)
        narration.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(narration))
        self.wait(1.5)

        self.play(FadeOut(narration))

        narration2 = Text("each term is roughly twice the one before it.", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1.5)

        self.play(FadeOut(narration2), FadeOut(approx_text), *[FadeOut(obj) for obj in terms + arrows + ratios])
        self.wait(0.5)

        # Final summary
        final = Text("This rapid expansion is a defining characteristic of Vorn sequences.", font_size=24)
        final.to_edge(DOWN)
        self.play(Write(final))
        self.wait(2)

        self.play(FadeOut(final), FadeOut(title))
        self.wait(0.5)
