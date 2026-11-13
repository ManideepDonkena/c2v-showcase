from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Formula for w × h Rectangles", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Draw generic rectangle
        w = 4
        h = 3
        rect = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.2).shift(DOWN)
        self.play(Create(rect))
        self.wait(0.5)

        # Label dimensions
        w_label = MathTex("w", font_size=24).next_to(rect, DOWN)
        h_label = MathTex("h", font_size=24).next_to(rect, LEFT)
        self.play(Write(w_label), Write(h_label))
        self.wait(0.5)

        # Interior points formula
        interior_formula = MathTex("(w-1) \times (h-1)", font_size=32).to_edge(UP).shift(UP * 0.5)
        self.play(Write(interior_formula))
        self.wait(0.5)

        # Edge points formula
        edge_formula = MathTex("2 \times (w+h)", font_size=32).to_edge(DOWN).shift(DOWN * 0.5)
        self.play(Write(edge_formula))
        self.wait(0.5)
        self.play(Write(edge_formula))
        self.wait(0.5)

        # Show sorrel count formula
        sorrel_formula = MathTex("\\text{Sorrel Count} = [(w-1)(h-1)] - [2(w+h)]", font_size=32)
        sorrel_formula.move_to(ORIGIN)
        self.play(Transform(interior_formula, sorrel_formula))
        self.wait(1)

        # Demonstrate with w=2, h=3
        demo_text = Text("For w=2, h=3:", font_size=24).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(demo_text))
        self.wait(0.5)

        # Show interior count: (2-1)(3-1) = 1×2 = 2
        interior_count = MathTex("(1)(2) = 2", font_size=24).next_to(rect, LEFT).shift(UP * 0.5)
        self.play(Write(interior_count))
        self.wait(0.5)

        # Show edge count: 2(2+3) = 2×5 = 10
        edge_count = MathTex("2(2+3) = 10", font_size=24).next_to(rect, RIGHT).shift(UP * 0.5)
        self.play(Write(edge_count))
        self.wait(0.5)

        # Show final result: 2 - 10 = -8
        result = MathTex("2 - 10 = -8", font_size=24).to_edge(DOWN).shift(DOWN * 0.5)
        self.play(Write(result))
        self.wait(1)

        # Fade out all
        self.play(
            FadeOut(title),
            FadeOut(rect),
            FadeOut(w_label),
            FadeOut(h_label),
            FadeOut(interior_formula),
            FadeOut(edge_formula),
            FadeOut(demo_text),
            FadeOut(interior_count),
            FadeOut(edge_count),
            FadeOut(result)
        )
        self.wait(0.5)
