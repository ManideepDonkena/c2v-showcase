from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Formula for w × h Rectangles", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Draw generic rectangle
        w = 4
        h = 5
        rect = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.3)
        rect.move_to(ORIGIN)
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

        # Combine into Sorrel Count
        sorrel_count = MathTex("(w-1)(h-1) - 2(w+h)", font_size=32)
        sorrel_count.move_to(ORIGIN)
        self.play(Transform(interior_formula, sorrel_count))
        self.wait(0.5)

        # Fade out intermediate formulas
        self.play(FadeOut(interior_formula), FadeOut(edge_formula))

        # Example: 4x5 rectangle
        example_text = Text("Example: 4 × 5", font_size=24)
        example_text.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(example_text))
        self.wait(0.5)

        # Show interior points count
        interior_count = MathTex("(4-1) \\times (5-1) = 3 \\times 4 = 12", font_size=24)
        interior_count.to_edge(UP).shift(DOWN * 1.0)
        self.play(Write(interior_count))
        self.wait(0.5)

        # Show edge points count
        edge_count = MathTex("2 \\times (4 + 5) = 2 \\times 9 = 18", font_size=24)
        edge_count.to_edge(DOWN).shift(UP * 1.0)
        self.play(Write(edge_count))
        self.wait(0.5)

        # Final Sorrel Count
        final_sorrel = MathTex("12 - 18 = -6", font_size=24)
        final_sorrel.move_to(ORIGIN)
        self.play(Transform(interior_count, final_sorrel))
        self.wait(0.5)

        # Rule: small rectangles have negative counts
        rule_text = Text("Small rectangles yield negative Sorrel counts.", font_size=20)
        rule_text.to_edge(DOWN).shift(DOWN * 1.5)
        rule_text.shift(0.0 * RIGHT + 1.15 * UP)  # layout: separation vector
        self.play(Write(rule_text))
        self.wait(1.0)

        # Example: 3x3 square
        square_example = Text("Example: 3 × 3 square", font_size=24)
        square_example.to_edge(UP).shift(DOWN * 0.5)
        self.play(Transform(example_text, square_example))
        self.wait(0.5)

        # Interior and edge counts for 3x3
        interior_3x3 = MathTex("(3-1) \\times (3-1) = 2 \\times 2 = 4", font_size=24)
        interior_3x3.to_edge(UP).shift(DOWN * 1.0)
        self.play(Write(interior_3x3))
        self.wait(0.5)

        edge_3x3 = MathTex("2 \\times (3 + 3) = 2 \\times 6 = 12", font_size=24)
        edge_3x3.to_edge(DOWN).shift(UP * 1.0)
        edge_3x3.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        self.play(Write(edge_3x3))
        self.wait(0.5)

        # Final Sorrel Count for 3x3
        final_sorrel_3x3 = MathTex("4 - 12 = -8", font_size=24)
        final_sorrel_3x3.move_to(ORIGIN)
        final_sorrel_3x3.shift(0.0 * RIGHT + 0.32 * UP)  # layout: separation vector
        self.play(ReplacementTransform(interior_3x3, final_sorrel_3x3))
        self.wait(0.5)

        # Rule: swapping width and height keeps the count
        swap_rule = Text("Swapping width and height keeps the count.", font_size=20)
        swap_rule.to_edge(DOWN).shift(DOWN * 1.5)
        self.play(Write(swap_rule))
        self.wait(1.0)

        # Fade everything out
        self.play(
            FadeOut(title),
            FadeOut(rect),
            FadeOut(w_label),
            FadeOut(h_label),
            FadeOut(example_text),
            FadeOut(interior_count),
            FadeOut(edge_count),
            FadeOut(final_sorrel_3x3),
            FadeOut(rule_text),
            FadeOut(swap_rule)
        )
        self.wait(0.5)
