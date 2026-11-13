from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Formula for w × h Rectangles", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial rectangle
        w, h = 4, 3
        rect = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.2).move_to(ORIGIN)
        w_label = MathTex("w", font_size=24).next_to(rect, DOWN)
        h_label = MathTex("h", font_size=24).next_to(rect, LEFT)

        self.play(Create(rect), Write(w_label), Write(h_label))
        self.wait(0.5)

        # Interior points formula
        interior_formula = MathTex("(w-1) \\times (h-1)", font_size=30)
        interior_formula.to_edge(UP).shift(UP * 0.5)
        self.play(Write(interior_formula))
        self.wait(0.5)

        # Edge points formula
        edge_formula = MathTex("2 \\times (w + h)", font_size=30)
        edge_formula.to_edge(DOWN).shift(DOWN * 0.5)
        self.play(Write(edge_formula))
        self.wait(0.5)

        # Sorrel count formula
        sorrel_formula = MathTex("(w-1)(h-1) - 2(w+h)", font_size=30)
        sorrel_formula.move_to(ORIGIN)
        self.play(Transform(interior_formula, sorrel_formula))
        self.wait(1)

        # Visual breakdown of edge points
        self.play(FadeOut(interior_formula), FadeOut(edge_formula))

        # Show edge point counts per side
        top_edge = Line(start=LEFT * w/2, end=RIGHT * w/2, color=YELLOW)
        bottom_edge = Line(start=LEFT * w/2, end=RIGHT * w/2, color=YELLOW).shift(DOWN * h)
        left_edge = Line(start=UP * h/2, end=DOWN * h/2, color=YELLOW)
        right_edge = Line(start=UP * h/2, end=DOWN * h/2, color=YELLOW).shift(RIGHT * w)

        top_label = MathTex("w+1", font_size=24).next_to(top_edge, UP)
        bottom_label = MathTex("w+1", font_size=24).next_to(bottom_edge, DOWN)
        left_label = MathTex("h+1", font_size=24).next_to(left_edge, LEFT)
        right_label = MathTex("h+1", font_size=24).next_to(right_edge, RIGHT)

        self.play(Create(top_edge), Write(top_label))
        self.play(Create(bottom_edge), Write(bottom_label))
        self.play(Create(left_edge), Write(left_label))
        self.play(Create(right_edge), Write(right_label))

        # Show corner overlap
        corner_text = Text("4 corners counted twice", font_size=24).next_to(rect, DOWN)
        corner_text.shift(0.0 * RIGHT + -0.26 * UP)  # layout: separation vector
        self.play(Write(corner_text))
        self.wait(1)

        # Correct edge count: 2(w + h)
        correct_edge = MathTex("2w + 2h + 4 - 4 = 2(w+h)", font_size=24)
        correct_edge.next_to(corner_text, DOWN)
        self.play(Write(correct_edge))
        self.wait(1.5)

        # Clear the edge breakdown
        self.play(FadeOut(top_edge), FadeOut(bottom_edge), FadeOut(left_edge), FadeOut(right_edge),
                  FadeOut(top_label), FadeOut(bottom_label), FadeOut(left_label), FadeOut(right_label),
                  FadeOut(corner_text), FadeOut(correct_edge))

        # Example: 2x3 rectangle
        self.play(rect.animate.scale(0.5).move_to(ORIGIN))
        w, h = 2, 3
        rect.scale(2)
        self.wait(0.5)

        interior_count = MathTex("(2-1) \\times (3-1) = 2", font_size=24).to_edge(UP)
        edge_count = MathTex("2 \\times (2 + 3) = 10", font_size=24).to_edge(DOWN)

        interior_count.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        self.play(Write(interior_count))
        self.wait(0.5)
        self.play(Write(edge_count))
        self.wait(0.5)

        # Show subtraction
        result = MathTex("2 - 10 = -8", font_size=30).move_to(ORIGIN)
        self.play(Transform(interior_count, result))
        self.wait(1.5)

        # Clear and show next example: 5x2 rectangle
        self.play(FadeOut(interior_count), FadeOut(edge_count))

        w, h = 5, 2
        rect.scale(0.4)
        self.wait(0.5)

        interior_count2 = MathTex("(5-1) \\times (2-1) = 4", font_size=24).to_edge(UP)
        edge_count2 = MathTex("2 \\times (5 + 2) = 14", font_size=24).to_edge(DOWN)

        interior_count2.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        self.play(Write(interior_count2))
        self.wait(0.5)
        self.play(Write(edge_count2))
        self.wait(0.5)

        # Show subtraction
        result2 = MathTex("4 - 14 = -8", font_size=30).move_to(ORIGIN)
        self.play(Transform(interior_count2, result2))
        self.wait(1.5)

        # Final summary
        self.play(FadeOut(interior_count2), FadeOut(edge_count2), FadeOut(rect),
                  FadeOut(w_label), FadeOut(h_label), FadeOut(title))
        final_text = Text("Sorrel Count = (w-1)(h-1) - 2(w+h)", font_size=30).move_to(ORIGIN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(final_text))
