from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Formula for w × h Rectangles", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial rectangle and labels
        w, h = 4, 3
        rect = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.2)
        w_label = MathTex("w", font_size=24).next_to(rect, DOWN)
        h_label = MathTex("h", font_size=24).next_to(rect, RIGHT)
        self.play(Create(rect), Write(w_label), Write(h_label))
        self.wait(1)

        # Interior points formula
        interior_formula = MathTex("(w-1) \\times (h-1)", font_size=30).to_edge(UP).shift(UP*0.5)
        self.play(Write(interior_formula))
        self.wait(1)

        # Show intervals between grid points
        self.play(FadeOut(w_label, h_label))
        self.play(rect.animate.stretch_to_fit_width(w-1).stretch_to_fit_height(h-1))
        self.wait(0.5)
        self.play(rect.animate.stretch_to_fit_width(w).stretch_to_fit_height(h))
        self.wait(0.5)

        # Edge points formula
        edge_formula = MathTex("2 \\times (w + h)", font_size=30).to_edge(DOWN).shift(DOWN*0.5)
        self.play(Write(edge_formula))
        self.wait(1)

        # Show 2x3 example
        self.play(FadeOut(interior_formula, edge_formula))
        rect_2x3 = Rectangle(width=2, height=3, color=GREEN, fill_opacity=0.2).to_edge(LEFT)
        self.play(Create(rect_2x3))
        self.wait(0.5)

        # Interior points
        interior_count = MathTex("(2-1) \\times (3-1) = 2", font_size=24).next_to(rect_2x3, DOWN)
        self.play(Write(interior_count))
        self.wait(1)

        # Edge points
        edge_count = MathTex("2 \\times (2 + 3) = 10", font_size=24).next_to(interior_count, DOWN)
        self.play(Write(edge_count))
        self.wait(1)

        # Sorrel count
        sorrel = MathTex("2 - 10 = -8", font_size=24).next_to(edge_count, DOWN)
        self.play(Write(sorrel))
        self.wait(1.5)

        # Show 5x2 example
        self.play(FadeOut(rect_2x3, interior_count, edge_count, sorrel))
        rect_5x2 = Rectangle(width=5, height=2, color=ORANGE, fill_opacity=0.2).to_edge(RIGHT)
        self.play(Create(rect_5x2))
        self.wait(0.5)

        # Interior points
        interior_count_5x2 = MathTex("(5-1) \\times (2-1) = 4", font_size=24).next_to(rect_5x2, DOWN)
        self.play(Write(interior_count_5x2))
        self.wait(1)

        # Edge points
        edge_count_5x2 = MathTex("2 \\times (5 + 2) = 14", font_size=24).next_to(interior_count_5x2, DOWN)
        self.play(Write(edge_count_5x2))
        self.wait(1)

        # Sorrel count
        sorrel_5x2 = MathTex("4 - 14 = -10", font_size=24).next_to(edge_count_5x2, DOWN)
        self.play(Write(sorrel_5x2))
        self.wait(1.5)

        # Show two rectangles side-by-side
        self.play(FadeOut(rect_5x2, interior_count_5x2, edge_count_5x2, sorrel_5x2))

        rect_4x2 = Rectangle(width=4, height=2, color=PURPLE, fill_opacity=0.2).to_edge(LEFT)
        rect_2x4 = Rectangle(width=2, height=4, color=YELLOW, fill_opacity=0.2).to_edge(RIGHT)

        rect_2x4.shift(0.0 * RIGHT + 0.9 * UP)  # layout: separation vector
        self.play(Create(rect_4x2), Create(rect_2x4))
        self.wait(0.5)

        # Label rectangles
        label_4x2 = MathTex("4 \\times 2", font_size=24).next_to(rect_4x2, DOWN)
        label_2x4 = MathTex("2 \\times 4", font_size=24).next_to(rect_2x4, DOWN)
        label_4x2.shift(0.0 * RIGHT + -0.4 * UP)  # layout: separation vector
        self.play(Write(label_4x2), Write(label_2x4))
        self.wait(1)

        # Sorrel counts
        count_4x2 = MathTex("(4-1)(2-1) - 2(4+2) = 3 - 12 = -9", font_size=20).next_to(rect_4x2, DOWN)
        count_2x4 = MathTex("(2-1)(4-1) - 2(2+4) = 3 - 12 = -9", font_size=20).next_to(rect_2x4, DOWN)
        self.play(Write(count_4x2), Write(count_2x4))
        self.wait(2)

        # Final correction
        self.play(FadeOut(count_4x2, count_2x4, label_4x2, label_2x4))
        final_sorrel = MathTex("Sorrel Count = (w-1)(h-1) - 2(w+h)", font_size=30).to_edge(UP)
        self.play(Write(final_sorrel))
        self.wait(2)

        # Final example with correct calculation
        correct_example = MathTex("(3-1)(3-1) - 2(3+3) = 4 - 12 = -8", font_size=24).to_edge(DOWN)
        self.play(Write(correct_example))
        self.wait(2)

        self.play(FadeOut(final_sorrel, correct_example, rect_4x2, rect_2x4))
        self.wait(0.5)
