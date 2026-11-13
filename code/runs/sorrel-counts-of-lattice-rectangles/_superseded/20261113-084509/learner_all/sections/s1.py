from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Sorrel Count", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid and rectangle (0,0) to (4,2)
        grid = NumberPlane(x_range=[-1, 5], y_range=[-1, 3], faded_line_ratio=1)
        rect = Rectangle(color=WHITE, fill_opacity=0.2, stroke_width=2).scale(1).move_to(ORIGIN)
        rect.width = 4
        rect.height = 2
        rect.stretch_to_fit_width(4)
        rect.stretch_to_fit_height(2)
        rect.move_to((2, 1, 0))

        # Draw grid and rectangle
        self.play(Create(grid), run_time=1)
        self.play(Create(rect), run_time=0.5)

        # Interior points (blue)
        interior_points = VGroup()
        for i in range(1, 4):
            for j in range(1, 2):
                p = Dot(color=BLUE).move_to((i, j, 0))
                interior_points.add(p)
        self.play(FadeIn(interior_points), run_time=0.5)

        # Edge points (red)
        edge_points = VGroup()
        for i in range(5):
            p = Dot(color=RED).move_to((i, 0, 0))  # bottom
            edge_points.add(p)
        for i in range(5):
            p = Dot(color=RED).move_to((i, 2, 0))  # top
            edge_points.add(p)
        for j in range(3):
            p = Dot(color=RED).move_to((0, j, 0))  # left
            edge_points.add(p)
        for j in range(3):
            p = Dot(color=RED).move_to((4, j, 0))  # right
            edge_points.add(p)
        self.play(FadeIn(edge_points), run_time=0.5)

        # Count labels
        count_inside = MathTex("8", color=BLUE).next_to(interior_points, DOWN, buff=0.2)
        count_edge = MathTex("10", color=RED).next_to(edge_points, UP, buff=0.2)
        self.play(Write(count_inside), Write(count_edge))

        # Formula
        formula = MathTex(r"\text{Sorrel Count} = \text{Inside} - \text{Edge}").to_edge(DOWN)
        self.play(Write(formula))
        self.wait(1)

        # Show (w-1)(h-1) interior points
        self.play(FadeOut(count_inside, count_edge, formula))
        self.play(Write(MathTex(r"\text{Interior: } (4-1) \times (2-1) = 3").to_corner(UL).shift(DOWN * 0.66)))
        self.wait(0.5)

        # Show edge points as 2(w+h)
        self.play(Write(MathTex(r"\text{Edge: } 2 \times (4 + 2) = 12").to_corner(UR).shift(DOWN * 0.66)))
        self.wait(0.5)

        # Show subtraction visually
        self.play(FadeOut(grid, rect, interior_points, edge_points))
        self.play(Write(MathTex("3 - 12 = -9").move_to(ORIGIN)))
        self.wait(1)
        self.play(FadeOut(MathTex("3 - 12 = -9").move_to(ORIGIN)))

        # Example: 2x3 rectangle
        grid2 = NumberPlane(x_range=[-1, 4], y_range=[-1, 4], faded_line_ratio=1)
        rect2 = Rectangle(color=WHITE, fill_opacity=0.2, stroke_width=2).scale(1).move_to(ORIGIN)
        rect2.width = 2
        rect2.height = 3
        rect2.stretch_to_fit_width(2)
        rect2.stretch_to_fit_height(3)
        rect2.move_to((1, 1.5, 0))

        self.play(Create(grid2), run_time=0.5)
        self.play(Create(rect2), run_time=0.5)

        # Interior points (2-1)×(3-1) = 2
        interior_points2 = VGroup()
        for i in range(1, 2):
            for j in range(1, 3):
                p = Dot(color=BLUE).move_to((i, j, 0))
                interior_points2.add(p)
        self.play(FadeIn(interior_points2), run_time=0.5)

        # Edge points (2×(2+3) = 10)
        edge_points2 = VGroup()
        for i in range(4):
            p = Dot(color=RED).move_to((i, 0, 0))
            edge_points2.add(p)
        for i in range(4):
            p = Dot(color=RED).move_to((i, 3, 0))
            edge_points2.add(p)
        for j in range(4):
            p = Dot(color=RED).move_to((0, j, 0))
            edge_points2.add(p)
        for j in range(4):
            p = Dot(color=RED).move_to((2, j, 0))
            edge_points2.add(p)
        self.play(FadeIn(edge_points2), run_time=0.5)

        count_inside2 = MathTex("2", color=BLUE).next_to(interior_points2, DOWN, buff=0.2)
        count_edge2 = MathTex("10", color=RED).next_to(edge_points2, UP, buff=0.2)
        self.play(Write(count_inside2), Write(count_edge2))

        # Show subtraction
        self.play(FadeOut(count_inside2, count_edge2))
        self.play(Write(MathTex("2 - 10 = -8").move_to(ORIGIN)))
        self.wait(1)
        self.play(FadeOut(MathTex("2 - 10 = -8").move_to(ORIGIN)))

        # Example: 5x2 rectangle
        grid3 = NumberPlane(x_range=[-1, 6], y_range=[-1, 3], faded_line_ratio=1)
        rect3 = Rectangle(color=WHITE, fill_opacity=0.2, stroke_width=2).scale(1).move_to(ORIGIN)
        rect3.width = 5
        rect3.height = 2
        rect3.stretch_to_fit_width(5)
        rect3.stretch_to_fit_height(2)
        rect3.move_to((2.5, 1, 0))

        self.play(Create(grid3), run_time=0.5)
        self.play(Create(rect3), run_time=0.5)

        # Interior points (5-1)×(2-1) = 4
        interior_points3 = VGroup()
        for i in range(1, 5):
            for j in range(1, 2):
                p = Dot(color=BLUE).move_to((i, j, 0))
                interior_points3.add(p)
        self.play(FadeIn(interior_points3), run_time=0.5)

        # Edge points (2×(5+2) = 14)
        edge_points3 = VGroup()
        for i in range(6):
            p = Dot(color=RED).move_to((i, 0, 0))
            edge_points3.add(p)
        for i in range(6):
            p = Dot(color=RED).move_to((i, 2, 0))
            edge_points3.add(p)
        for j in range(3):
            p = Dot(color=RED).move_to((0, j, 0))
            edge_points3.add(p)
        for j in range(3):
            p = Dot(color=RED).move_to((5, j, 0))
            edge_points3.add(p)
        self.play(FadeIn(edge_points3), run_time=0.5)

        count_inside3 = MathTex("6", color=BLUE).next_to(interior_points3, DOWN, buff=0.2)
        count_edge3 = MathTex("14", color=RED).next_to(edge_points3, UP, buff=0.2)
        self.play(Write(count_inside3), Write(count_edge3))

        # Show subtraction
        self.play(FadeOut(count_inside3, count_edge3))
        self.play(Write(MathTex("6 - 14 = -8").move_to(ORIGIN)))
        self.wait(1)
        self.play(FadeOut(MathTex("6 - 14 = -8").move_to(ORIGIN)))

        # Side-by-side rectangles
        grid4 = NumberPlane(x_range=[-1, 5], y_range=[-1, 3], faded_line_ratio=1)
        rect4 = Rectangle(color=WHITE, fill_opacity=0.2, stroke_width=2).scale(1).move_to(ORIGIN)
        rect4.width = 4
        rect4.height = 2
        rect4.stretch_to_fit_width(4)
        rect4.stretch_to_fit_height(2)
        rect4.move_to((2, 1, 0))

        grid5 = NumberPlane(x_range=[-1, 3], y_range=[-1, 5], faded_line_ratio=1)
        rect5 = Rectangle(color=WHITE, fill_opacity=0.2, stroke_width=2).scale(1).move_to(ORIGIN)
        rect5.width = 2
        rect5.height = 4
        rect5.stretch_to_fit_width(2)
        rect5.stretch_to_fit_height(4)
        rect5.move_to((1, 2, 0))

        self.play(FadeOut(grid3, rect3, interior_points3, edge_points3))
        self.play(Create(grid4), run_time=0.5)
        self.play(Create(rect4), run_time=0.5)
        self.play(Create(grid5), run_time=0.5)
        self.play(Create(rect5), run_time=0.5)

        # Labels
        label1 = Text("4x2", font_size=24).next_to(rect4, DOWN)
        label2 = Text("2x4", font_size=24).next_to(rect5, DOWN)
        self.play(Write(label1), Write(label2))

        # Sorrel count for both
        self.play(Write(MathTex("Sorrel Count = -6").move_to(ORIGIN)))
        self.wait(1.5)

        self.play(FadeOut(grid4, rect4, grid5, rect5, label1, label2, MathTex("Sorrel Count = -6").move_to(ORIGIN)))
        self.play(FadeOut(title))
