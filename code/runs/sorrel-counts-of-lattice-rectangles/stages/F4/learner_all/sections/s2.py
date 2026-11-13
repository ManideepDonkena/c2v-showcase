from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Formula for w × h Rectangles", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Draw a generic rectangle
        w = 5
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

        # Combine into Sorrel Count
        sorrel_formula = MathTex("(w-1)(h-1) - 2(w+h)", font_size=36)
        sorrel_formula.move_to(ORIGIN)
        self.play(Transform(interior_formula, sorrel_formula))
        self.wait(1)

        # Fade out intermediate formulas
        self.play(FadeOut(interior_formula), FadeOut(edge_formula))

        # Show example: 4x5 rectangle
        example_text = Text("Example: 4 × 5", font_size=24)
        example_text.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(example_text))
        self.wait(0.5)

        # Show interior count
        interior_count = MathTex("3 \\times 4 = 12", font_size=28)
        interior_count.next_to(rect, UP)
        self.play(Write(interior_count))
        self.wait(0.5)

        # Show edge count
        edge_count = MathTex("2 \\times (4 + 5) = 18", font_size=28)
        edge_count.next_to(rect, DOWN)
        edge_count.shift(0.0 * RIGHT + -0.26 * UP)  # layout: separation vector
        self.play(Write(edge_count))
        self.wait(0.5)

        # Sorrel Count result
        sorrel_result = MathTex("12 - 18 = -6", font_size=32)
        sorrel_result.move_to(ORIGIN)
        self.play(Transform(interior_count, sorrel_result))
        self.wait(1)

        # Rule: small rectangles have negative counts
        rule_text = Text("Small rectangles yield negative Sorrel counts.", font_size=24)
        rule_text.to_edge(DOWN).shift(DOWN * 0.5)
        self.play(Write(rule_text))
        self.wait(1.5)

        # Show square example: 3x3
        self.play(FadeOut(example_text), FadeOut(interior_count), FadeOut(edge_count), FadeOut(rule_text))

        square = Rectangle(width=3, height=3, color=GREEN, fill_opacity=0.3)
        square.shift(DOWN * 0.5)
        self.play(Create(square))
        self.wait(0.5)

        square_label = Text("3 × 3 Square", font_size=24)
        square_label.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(square_label))
        self.wait(0.5)

        # Interior and edge counts for 3x3
        interior_3x3 = MathTex("2 \\times 2 = 4", font_size=28)
        interior_3x3.next_to(square, UP)
        self.play(Write(interior_3x3))
        self.wait(0.5)

        edge_3x3 = MathTex("2 \\times (3 + 3) = 12", font_size=28)
        edge_3x3.next_to(square, DOWN)
        edge_3x3.shift(0.0 * RIGHT + -0.26 * UP)  # layout: separation vector
        self.play(Write(edge_3x3))
        self.wait(0.5)

        # Final Sorrel Count
        final_sorrel = MathTex("4 - 12 = -8", font_size=32)
        final_sorrel.move_to(ORIGIN)
        self.play(Transform(interior_3x3, final_sorrel))
        self.wait(1.5)

        # Final rule: swapping width and height keeps the count
        swap_rule = Text("Swapping w and h keeps the Sorrel Count.", font_size=24)
        swap_rule.to_edge(DOWN).shift(DOWN * 0.5)
        self.play(Write(swap_rule))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(rect), FadeOut(w_label), FadeOut(h_label),
                  FadeOut(square), FadeOut(square_label), FadeOut(interior_3x3),
                  FadeOut(edge_3x3), FadeOut(swap_rule))
        self.wait(0.5)
