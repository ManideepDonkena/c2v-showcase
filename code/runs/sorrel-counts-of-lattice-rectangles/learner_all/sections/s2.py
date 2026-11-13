from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Formula for w × h Rectangles", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial formula setup
        formula1 = MathTex("(w-1)(h-1)", font_size=40).to_edge(UP, buff=1)
        formula2 = MathTex("2(w+h)", font_size=40).next_to(formula1, DOWN, buff=0.5)
        self.play(Write(formula1))
        self.wait(0.5)
        self.play(Write(formula2))
        self.wait(1)

        # Show visual breakdown of edge points
        rect = Rectangle(width=3, height=2, color=BLUE, fill_opacity=0.2).shift(LEFT * 2)
        self.play(Create(rect))
        self.wait(0.5)

        # Label edges
        w_label = MathTex("w", font_size=24).next_to(rect, DOWN)
        h_label = MathTex("h", font_size=24).next_to(rect, RIGHT)
        self.play(Write(w_label), Write(h_label))
        self.wait(0.5)

        # Show edge count breakdown
        top_edge = Line(start=rect.get_top() + LEFT * 1.5, end=rect.get_top() + RIGHT * 1.5, color=YELLOW)
        bottom_edge = Line(start=rect.get_bottom() + LEFT * 1.5, end=rect.get_bottom() + RIGHT * 1.5, color=YELLOW)
        left_edge = Line(start=rect.get_left() + UP, end=rect.get_left() + DOWN, color=YELLOW)
        right_edge = Line(start=rect.get_right() + UP, end=rect.get_right() + DOWN, color=YELLOW)

        self.play(Create(top_edge), Create(bottom_edge), Create(left_edge), Create(right_edge))
        self.wait(0.5)

        # Show point counts
        top_count = MathTex("w+1", font_size=24).next_to(top_edge, UP)
        bottom_count = MathTex("w+1", font_size=24).next_to(bottom_edge, DOWN)
        left_count = MathTex("h+1", font_size=24).next_to(left_edge, LEFT)
        right_count = MathTex("h+1", font_size=24).next_to(right_edge, RIGHT)

        bottom_count.shift(0.0 * RIGHT + -0.26 * UP)  # layout: separation vector
        right_count.shift(0.27 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(top_count), Write(bottom_count), Write(left_count), Write(right_count))
        self.wait(1)

        # Show correction
        total = MathTex("2(w+h) + 4 - 4 = 2(w+h)", font_size=30).next_to(rect, DOWN, buff=1)
        self.play(Write(total))
        self.wait(1.5)
        self.play(FadeOut(top_count), FadeOut(bottom_count), FadeOut(left_count), FadeOut(right_count))

        # Show example: 2x3 rectangle
        rect2 = Rectangle(width=2, height=3, color=BLUE, fill_opacity=0.2).shift(RIGHT * 2)
        self.play(Transform(rect, rect2))
        self.wait(0.5)

        interior_points = MathTex("(2-1)(3-1) = 2", font_size=30).to_edge(UP, buff=1)
        edge_points = MathTex("2(2+3) = 10", font_size=30).next_to(interior_points, DOWN, buff=0.5)
        interior_points.shift(0.0 * RIGHT + 0.46 * UP)  # layout: separation vector
        self.play(Write(interior_points), Write(edge_points))
        self.wait(1)

        # Show subtraction
        result = MathTex("2 - 10 = -8", font_size=30).next_to(edge_points, DOWN, buff=0.5)
        self.play(Write(result))
        self.wait(1.5)
        self.play(FadeOut(interior_points), FadeOut(edge_points), FadeOut(result))

        # Show 5x2 rectangle
        rect3 = Rectangle(width=5, height=2, color=BLUE, fill_opacity=0.2).shift(LEFT * 2)
        self.play(Transform(rect, rect3))
        self.wait(0.5)

        interior_points_52 = MathTex("(5-1)(2-1) = 4", font_size=30).to_edge(UP, buff=1)
        edge_points_52 = MathTex("2(5+2) = 14", font_size=30).next_to(interior_points_52, DOWN, buff=0.5)
        self.play(Write(interior_points_52), Write(edge_points_52))
        self.wait(1)

        result_52 = MathTex("4 - 14 = -10", font_size=30).next_to(edge_points_52, DOWN, buff=0.5)
        self.play(Write(result_52))
        self.wait(1.5)
        self.play(FadeOut(interior_points_52), FadeOut(edge_points_52), FadeOut(result_52))

        # Show 3x3 square
        rect4 = Rectangle(width=3, height=3, color=BLUE, fill_opacity=0.2).shift(RIGHT * 2)
        self.play(Transform(rect, rect4))
        self.wait(0.5)

        interior_33 = MathTex("4", font_size=30).to_edge(UP, buff=1)
        edge_33 = MathTex("12", font_size=30).next_to(interior_33, DOWN, buff=0.5)
        self.play(Write(interior_33), Write(edge_33))
        self.wait(1)

        final_33 = MathTex("4 - 12 = -8", font_size=30).next_to(edge_33, DOWN, buff=0.5)
        self.play(Write(final_33))
        self.wait(1.5)
        self.play(FadeOut(interior_33), FadeOut(edge_33), FadeOut(final_33))

        # Show side-by-side rectangles
        rect5 = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.2).shift(LEFT * 2)
        rect6 = Rectangle(width=2, height=4, color=BLUE, fill_opacity=0.2).shift(RIGHT * 2)

        self.play(Transform(rect, rect5))
        self.wait(0.5)

        label_42 = MathTex("4 \\times 2", font_size=30).next_to(rect5, DOWN)
        self.play(Write(label_42))
        self.wait(0.5)

        interior_42 = MathTex("(4-1)(2-1) = 3", font_size=24).to_edge(UP, buff=1)
        edge_42 = MathTex("2(4+2) = 12", font_size=24).next_to(interior_42, DOWN, buff=0.5)
        self.play(Write(interior_42), Write(edge_42))
        self.wait(1)

        result_42 = MathTex("3 - 12 = -9", font_size=24).next_to(edge_42, DOWN, buff=0.5)
        self.play(Write(result_42))
        self.wait(1.5)
        self.play(FadeOut(interior_42), FadeOut(edge_42), FadeOut(result_42))

        # Show second rectangle
        self.play(Transform(rect, rect6))
        self.wait(0.5)

        label_24 = MathTex("2 \\times 4", font_size=30).next_to(rect6, DOWN)
        self.play(Write(label_24))
        self.wait(0.5)

        interior_24 = MathTex("(2-1)(4-1) = 3", font_size=24).to_edge(UP, buff=1)
        edge_24 = MathTex("2(2+4) = 12", font_size=24).next_to(interior_24, DOWN, buff=0.5)
        self.play(Write(interior_24), Write(edge_24))
        self.wait(1)

        result_24 = MathTex("3 - 12 = -9", font_size=24).next_to(edge_24, DOWN, buff=0.5)
        self.play(Write(result_24))
        self.wait(1.5)
        self.play(FadeOut(interior_24), FadeOut(edge_24), FadeOut(result_24))

        # Final summary
        final = MathTex("Sorrel Count = (w-1)(h-1) - 2(w+h)", font_size=30).to_edge(UP, buff=1)
        self.play(Write(final))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(rect), FadeOut(label_42), FadeOut(label_24), FadeOut(final))
        self.wait(0.5)
