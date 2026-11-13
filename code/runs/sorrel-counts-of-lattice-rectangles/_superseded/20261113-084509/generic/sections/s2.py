from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Formula for w × h Rectangles", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Draw a generic rectangle
        w = 4
        h = 3
        rect = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        self.play(Create(rect))
        self.wait(0.5)

        # Labels for width and height
        w_label = MathTex("w", font_size=24).next_to(rect, DOWN)
        h_label = MathTex("h", font_size=24).next_to(rect, RIGHT)
        self.play(Write(w_label), Write(h_label))
        self.wait(0.5)

        # Interior points formula
        interior_formula = MathTex("(w-1) \\times (h-1)", font_size=32).to_edge(UP).shift(UP * 0.5)
        self.play(Write(interior_formula))
        self.wait(0.5)

        # Edge points formula
        edge_formula = MathTex("2 \\times (w + h)", font_size=32).to_edge(DOWN).shift(DOWN * 0.5)
        self.play(Write(edge_formula))
        self.wait(0.5)

        # Combine into final sorrel count
        sorrel_formula = MathTex("(w-1)(h-1) - 2(w+h)", font_size=32).move_to(ORIGIN)
        self.play(Transform(interior_formula, sorrel_formula))
        self.wait(1)

        # Narration text
        narration1 = Text("For any rectangle...", font_size=24).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(narration1))
        self.wait(1)
        self.play(FadeOut(narration1))

        narration2 = Text("There are (w-1)×(h-1) points inside.", font_size=24).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(narration2))
        self.wait(1)
        self.play(FadeOut(narration2))

        narration3 = Text("The number on edges is 2×(w+h).", font_size=24).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(narration3))
        self.wait(1)
        self.play(FadeOut(narration3))

        # Example: 3x3 square
        example_rect = Rectangle(width=3, height=3, color=GREEN, fill_opacity=0.3).move_to(ORIGIN)
        interior_formula.shift(0.0 * RIGHT + 1.82 * UP)  # layout: separation vector
        self.play(Transform(rect, example_rect))
        self.wait(0.5)

        example_text = Text("Example: 3×3 square", font_size=24).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(example_text))
        self.wait(1)
        self.play(FadeOut(example_text))

        # Show inside and edge counts
        inside_count = MathTex("4 \\text{ inside}", font_size=24).next_to(rect, UP)
        edge_count = MathTex("12 \\text{ on edges}", font_size=24).next_to(rect, DOWN)
        edge_count.shift(0.0 * RIGHT + -0.26 * UP)  # layout: separation vector
        inside_count.shift(0.0 * RIGHT + 0.39 * UP)  # layout: separation vector
        self.play(Write(inside_count), Write(edge_count))
        self.wait(1)

        # Sorrel count result
        sorrel_result = MathTex("\\text{Sorrel count} = 4 - 12 = -8", font_size=24).move_to(ORIGIN)
        self.play(Transform(inside_count, sorrel_result))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(rect),
            FadeOut(w_label),
            FadeOut(h_label),
            FadeOut(interior_formula),
            FadeOut(edge_formula),
            FadeOut(inside_count),
            FadeOut(edge_count),
            FadeOut(title)
        )
        self.wait(0.5)
