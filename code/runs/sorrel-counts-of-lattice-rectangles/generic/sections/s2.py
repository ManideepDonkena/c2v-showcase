from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Formula for w × h Rectangles", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Draw a generic rectangle
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
        edge_formula = MathTex("2 \\times (w + h)", font_size=32)
        edge_formula.to_edge(DOWN).shift(DOWN * 0.5)
        self.play(Write(edge_formula))
        self.wait(0.5)

        # Combine into final sorrel count
        final_formula = MathTex("\\text{Sorrel Count} = (w-1)(h-1) - 2(w+h)", font_size=32)
        final_formula.move_to(ORIGIN)
        self.play(Transform(interior_formula, final_formula))
        self.wait(1)

        # Show example: 3x3 square
        self.play(FadeOut(interior_formula), FadeOut(edge_formula))

        example_rect = Rectangle(width=3, height=3, color=GREEN, fill_opacity=0.3)
        example_rect.shift(DOWN * 0.5)
        self.play(Create(example_rect))
        self.wait(0.5)

        # Show interior and edge counts
        inside_count = MathTex("4 \\text{ inside}", font_size=24).next_to(example_rect, UP)
        edge_count = MathTex("12 \\text{ on edges}", font_size=24).next_to(example_rect, DOWN)
        self.play(Write(inside_count), Write(edge_count))
        self.wait(1)

        # Show sorrel count
        sorrel_result = MathTex("\\text{Sorrel Count} = 4 - 12 = -8", font_size=32)
        sorrel_result.move_to(ORIGIN)
        self.play(Transform(inside_count, sorrel_result))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(title), FadeOut(example_rect), FadeOut(inside_count), FadeOut(edge_count))
        self.wait(0.5)
