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
        interior_formula = MathTex("(w-1) \\times (h-1)", font_size=30).to_edge(UP).shift(UP * 0.5)
        self.play(Write(interior_formula))
        self.wait(1)

        # Show intervals between grid points
        v_lines = VGroup()
        h_lines = VGroup()
        for i in range(w):
            v_line = Line(start=rect.get_left() + RIGHT * i, end=rect.get_left() + RIGHT * i + UP * h, color=YELLOW)
            v_lines.add(v_line)
        for j in range(h):
            h_line = Line(start=rect.get_bottom() + UP * j, end=rect.get_bottom() + UP * j + RIGHT * w, color=YELLOW)
            h_lines.add(h_line)
        self.play(Create(v_lines), Create(h_lines))
        self.wait(1)

        # Show (w-1) intervals horizontally and (h-1) vertically
        h_intervals = MathTex("w - 1", font_size=24).next_to(rect, DOWN)
        v_intervals = MathTex("h - 1", font_size=24).next_to(rect, RIGHT)
        h_intervals.shift(0.0 * RIGHT + -0.26 * UP)  # layout: separation vector
        v_intervals.shift(0.27 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(h_intervals), Write(v_intervals))
        self.wait(1.5)

        # Fade out interval lines and labels
        self.play(FadeOut(v_lines), FadeOut(h_lines), FadeOut(h_intervals), FadeOut(v_intervals))

        # Edge points formula
        edge_formula = MathTex("2 \\times (w + h)", font_size=30).to_edge(DOWN).shift(DOWN * 0.5)
        self.play(Write(edge_formula))
        self.wait(1)

        # Show edge point count breakdown
        top_points = MathTex("w + 1", font_size=24).next_to(rect, UP)
        bottom_points = MathTex("w + 1", font_size=24).next_to(rect, DOWN)
        left_points = MathTex("h + 1", font_size=24).next_to(rect, LEFT)
        right_points = MathTex("h + 1", font_size=24).next_to(rect, RIGHT)
        bottom_points.shift(0.0 * RIGHT + -0.26 * UP)  # layout: separation vector
        self.play(Write(top_points), Write(bottom_points), Write(left_points), Write(right_points))
        self.wait(1.5)

        # Show total edge points and subtract corners
        total_edge = MathTex("2w + 2h + 4 - 4 = 2(w+h)", font_size=24).next_to(edge_formula, DOWN)
        self.play(Write(total_edge))
        self.wait(1.5)

        # Fade out edge labels
        self.play(FadeOut(top_points), FadeOut(bottom_points), FadeOut(left_points), FadeOut(right_points), FadeOut(total_edge))

        # Example: 2x3 rectangle
        self.play(FadeOut(interior_formula), FadeOut(edge_formula), FadeOut(title))
        rect_2x3 = Rectangle(width=2, height=3, color=BLUE, fill_opacity=0.2).shift(LEFT * 2)
        self.play(Create(rect_2x3))
        self.wait(0.5)

        interior_count = MathTex("(2-1) \\times (3-1) = 2", font_size=30).to_edge(UP)
        edge_count = MathTex("2 \\times (2 + 3) = 10", font_size=30).to_edge(DOWN)
        self.play(Write(interior_count), Write(edge_count))
        self.wait(1.5)

        # Show subtraction visually
        result = MathTex("2 - 10 = -8", font_size=30).move_to(ORIGIN)
        self.play(ReplacementTransform(interior_count, result))
        self.wait(1.5)

        # Example: 5x2 rectangle
        self.play(FadeOut(result), FadeOut(edge_count), FadeOut(rect_2x3))
        rect_5x2 = Rectangle(width=5, height=2, color=BLUE, fill_opacity=0.2).shift(RIGHT * 2)
        self.play(Create(rect_5x2))
        self.wait(0.5)

        interior_count_2 = MathTex("(5-1) \\times (2-1) = 4", font_size=30).to_edge(UP)
        edge_count_2 = MathTex("2 \\times (5 + 2) = 14", font_size=30).to_edge(DOWN)
        self.play(Write(interior_count_2), Write(edge_count_2))
        self.wait(1.5)

        # Show final result
        final_result = MathTex("4 - 14 = -10", font_size=30).move_to(ORIGIN)
        self.play(ReplacementTransform(interior_count_2, final_result))
        self.wait(1.5)

        # Final summary
        self.play(FadeOut(final_result), FadeOut(edge_count_2), FadeOut(rect_5x2))
        summary = Text("Sorrel Count = (w-1)(h-1) - 2(w+h)", font_size=24).to_edge(UP)
        self.play(Write(summary))
        self.wait(1.5)

        # Show that it's always negative for small rectangles
        note = Text("Note: Small rectangles have negative sorrel counts", font_size=20).to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)

        self.play(FadeOut(summary), FadeOut(note))
