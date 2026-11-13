from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Formula for w × h Rectangles", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Generic rectangle
        w = 4
        h = 3
        rect = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.3)
        rect.shift(DOWN * 0.5)
        self.play(Create(rect))
        self.wait(0.5)

        # Labels for width and height
        w_label = MathTex("w", font_size=24).next_to(rect, DOWN)
        h_label = MathTex("h", font_size=24).next_to(rect, RIGHT)
        self.play(Write(w_label), Write(h_label))
        self.wait(0.5)

        # Interior points formula
        interior_formula = MathTex("(w-1) \\times (h-1)", font_size=32)
        interior_formula.to_edge(UP).shift(UP * 0.5)
        self.play(Write(interior_formula))
        self.wait(0.5)

        # Edge points formula
        edge_formula = MathTex("2 \\times (w+h)", font_size=32)
        edge_formula.to_edge(DOWN).shift(DOWN * 0.5)
        self.play(Write(edge_formula))
        self.wait(0.5)

        # Sorrel count formula
        sorrel_formula = MathTex(
            "\\text{Sorrel Count} = (w-1)(h-1) - 2(w+h)",
            font_size=32
        )
        sorrel_formula.move_to(ORIGIN)
        self.play(Transform(interior_formula, sorrel_formula))
        self.wait(1)

        # Show example: w=2, h=3
        example_text = Text("Example: w=2, h=3", font_size=24)
        example_text.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(example_text))
        self.wait(0.5)

        # Show interior count for w=2, h=3
        interior_val = MathTex("(2-1)(3-1) = 1 \\times 2 = 2", font_size=24)
        interior_val.to_edge(UP).shift(DOWN * 1.0)
        self.play(Write(interior_val))
        self.wait(0.5)

        # Show edge count for w=2, h=3
        edge_val = MathTex("2(2+3) = 2 \\times 5 = 10", font_size=24)
        edge_val.to_edge(DOWN).shift(UP * 1.0)
        self.play(Write(edge_val))
        self.wait(0.5)

        # Show negative result
        result = MathTex("2 - 10 = -8", font_size=32)
        result.move_to(ORIGIN)
        self.play(ReplacementTransform(interior_formula, result))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(rect),
            FadeOut(w_label),
            FadeOut(h_label),
            FadeOut(interior_formula),
            FadeOut(edge_formula),
            FadeOut(example_text),
            FadeOut(interior_val),
            FadeOut(edge_val),
            FadeOut(result)
        )
        self.wait(0.5)
