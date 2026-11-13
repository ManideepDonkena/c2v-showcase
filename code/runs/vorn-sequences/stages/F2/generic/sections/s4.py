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
            arrow = Arrow(terms[i].get_right(), terms[i+1].get_left(), buff=0.2, stroke_width=3)
            arrows.append(arrow)
            ratio = MathTex(f"\\frac{{v({i+1})}}{{v({i})}} = {seq[i+1]/seq[i]:.2f}", font_size=24)
            ratio.next_to(arrow, UP, buff=0.2)
            ratios.append(ratio)
        
        self.play(*[Create(arrow) for arrow in arrows])
        self.wait(0.5)
        self.play(*[Write(ratio) for ratio in ratios])
        self.wait(1)

        # "Approx. 2x" text
        approx_text = Text("Approx. 2x", font_size=32).to_edge(UP).shift(DOWN * 0.5)
        self.play(FadeIn(approx_text))
        self.wait(1.5)

        # Fade out old text and show rule explanation
        self.play(
            *[FadeOut(term) for term in terms],
            *[FadeOut(arrow) for arrow in arrows],
            *[FadeOut(ratio) for ratio in ratios],
            FadeOut(approx_text),
        )

        # Show the rule definition
        rule1 = Text("Rule 1: Every term is odd", font_size=24).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(rule1))
        self.wait(1)

        rule2 = Text("Rule 2: Each term is about twice the one before", font_size=24).next_to(rule1, DOWN, buff=0.3)
        self.play(Write(rule2))
        self.wait(1.5)

        # Show formula
        formula = MathTex("v(n) = v(n-1) + 2 \\times v(n-2)", font_size=32).next_to(rule2, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(1.5)

        # Worked example
        example = Text("Example: v(3) = 3 + 2×1 = 5", font_size=24).to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(example))
        self.wait(1.5)

        example2 = Text("v(4) = 5 + 2×3 = 11", font_size=24).next_to(example, DOWN, buff=0.3)
        self.play(Write(example2))
        self.wait(1.5)

        # Final fade out
        self.play(
            FadeOut(rule1),
            FadeOut(rule2),
            FadeOut(formula),
            FadeOut(example),
            FadeOut(example2),
            FadeOut(title),
        )
