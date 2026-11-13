from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Sorrel Count", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid and rectangle (4x2)
        grid = NumberPlane(x_range=[-1, 5], y_range=[-1, 3], faded_line_ratio=1)
        rect = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.2).move_to(ORIGIN)
        self.play(Create(grid), run_time=1)
        self.play(Create(rect), run_time=0.5)

        # Interior points (blue)
        interior_points = VGroup()
        for i in range(1, 4):
            for j in range(1, 2):
                point = Dot([i, j, 0], color=BLUE)
                interior_points.add(point)
        self.play(FadeIn(interior_points), run_time=0.5)
        count_inside = MathTex("8", font_size=30).next_to(interior_points, DOWN)
        count_inside.shift(0.21 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(count_inside))
        self.wait(0.5)

        # Edge points (red)
        edge_points = VGroup()
        for i in range(5):
            point = Dot([i, 0, 0], color=RED)
            edge_points.add(point)
            point = Dot([i, 2, 0], color=RED)
            edge_points.add(point)
        for j in range(3):
            point = Dot([0, j, 0], color=RED)
            edge_points.add(point)
            point = Dot([4, j, 0], color=RED)
            edge_points.add(point)
        self.play(FadeIn(edge_points), run_time=0.5)
        count_edge = MathTex("10", font_size=30).next_to(edge_points, DOWN)
        count_edge.shift(0.29 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(count_edge))
        self.wait(0.5)

        # Formula
        formula = MathTex(r"\text{Sorrel Count} = \text{Inside} - \text{Edge}", font_size=36)
        formula.to_edge(DOWN)
        self.play(Write(formula))
        self.wait(1)

        # Breakdown of edge points
        self.play(FadeOut(count_inside, count_edge, interior_points, edge_points))
        breakdown = MathTex(r"\text{Top/Bottom: } (w+1) \text{ each}", font_size=24).to_corner(UL)
        self.play(Write(breakdown))
        self.wait(0.5)
        breakdown2 = MathTex(r"\text{Left/Right: } (h+1) \text{ each}", font_size=24).next_to(breakdown, DOWN)
        self.play(Write(breakdown2))
        self.wait(0.5)
        breakdown3 = MathTex(r"\text{Total: } 2(w+1) + 2(h+1) - 4 = 2w + 2h", font_size=24).next_to(breakdown2, DOWN)
        breakdown3.shift(0.45 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(breakdown3))
        self.wait(1)

        # Clear
        self.play(FadeOut(breakdown, breakdown2, breakdown3, formula))

        # Example: 2x3 rectangle
        grid2 = NumberPlane(x_range=[-1, 3], y_range=[-1, 4], faded_line_ratio=1)
        rect2 = Rectangle(width=2, height=3, color=BLUE, fill_opacity=0.2).move_to(ORIGIN)
        self.play(Create(grid2), run_time=0.5)
        self.play(Create(rect2), run_time=0.5)

        # Interior points
        interior_points2 = VGroup()
        for i in range(1, 2):
            for j in range(1, 3):
                point = Dot([i, j, 0], color=BLUE)
                interior_points2.add(point)
        self.play(FadeIn(interior_points2), run_time=0.5)
        count_inside2 = MathTex("2", font_size=30).next_to(interior_points2, DOWN)
        self.play(Write(count_inside2))
        self.wait(0.5)

        # Edge points
        edge_points2 = VGroup()
        for i in range(3):
            point = Dot([i, 0, 0], color=RED)
            edge_points2.add(point)
            point = Dot([i, 3, 0], color=RED)
            edge_points2.add(point)
        for j in range(4):
            point = Dot([0, j, 0], color=RED)
            edge_points2.add(point)
            point = Dot([2, j, 0], color=RED)
            edge_points2.add(point)
        self.play(FadeIn(edge_points2), run_time=0.5)
        count_edge2 = MathTex("10", font_size=30).next_to(edge_points2, DOWN)
        self.play(Write(count_edge2))
        self.wait(0.5)

        # Subtraction
        result = MathTex("2 - 10 = -8", font_size=40).to_edge(DOWN)
        self.play(Write(result))
        self.wait(1.5)

        # Clear
        self.play(FadeOut(grid2, rect2, count_inside2, count_edge2, interior_points2, edge_points2, result))

        # Example: 5x2 rectangle
        grid3 = NumberPlane(x_range=[-1, 6], y_range=[-1, 3], faded_line_ratio=1)
        rect3 = Rectangle(width=5, height=2, color=BLUE, fill_opacity=0.2).move_to(ORIGIN)
        self.play(Create(grid3), run_time=0.5)
        self.play(Create(rect3), run_time=0.5)

        # Interior points
        interior_points3 = VGroup()
        for i in range(1, 5):
            for j in range(1, 2):
                point = Dot([i, j, 0], color=BLUE)
                interior_points3.add(point)
        self.play(FadeIn(interior_points3), run_time=0.5)
        count_inside3 = MathTex("6", font_size=30).next_to(interior_points3, DOWN)
        self.play(Write(count_inside3))
        self.wait(0.5)

        # Edge points
        edge_points3 = VGroup()
        for i in range(6):
            point = Dot([i, 0, 0], color=RED)
            edge_points3.add(point)
            point = Dot([i, 2, 0], color=RED)
            edge_points3.add(point)
        for j in range(3):
            point = Dot([0, j, 0], color=RED)
            edge_points3.add(point)
            point = Dot([5, j, 0], color=RED)
            edge_points3.add(point)
        self.play(FadeIn(edge_points3), run_time=0.5)
        count_edge3 = MathTex("14", font_size=30).next_to(edge_points3, DOWN)
        self.play(Write(count_edge3))
        self.wait(0.5)

        # Subtraction
        result2 = MathTex("6 - 14 = -8", font_size=40).to_edge(DOWN)
        self.play(Write(result2))
        self.wait(1.5)

        # Clear
        self.play(FadeOut(grid3, rect3, count_inside3, count_edge3, interior_points3, edge_points3, result2))

        # Example: 3x3 square
        grid4 = NumberPlane(x_range=[-1, 4], y_range=[-1, 4], faded_line_ratio=1)
        rect4 = Rectangle(width=3, height=3, color=BLUE, fill_opacity=0.2).move_to(ORIGIN)
        self.play(Create(grid4), run_time=0.5)
        self.play(Create(rect4), run_time=0.5)

        # Interior points
        interior_points4 = VGroup()
        for i in range(1, 3):
            for j in range(1, 3):
                point = Dot([i, j, 0], color=BLUE)
                interior_points4.add(point)
        self.play(FadeIn(interior_points4), run_time=0.5)
        count_inside4 = MathTex("4", font_size=30).next_to(interior_points4, DOWN)
        self.play(Write(count_inside4))
        self.wait(0.5)

        # Edge points
        edge_points4 = VGroup()
        for i in range(4):
            point = Dot([i, 0, 0], color=RED)
            edge_points4.add(point)
            point = Dot([i, 3, 0], color=RED)
            edge_points4.add(point)
        for j in range(4):
            point = Dot([0, j, 0], color=RED)
            edge_points4.add(point)
            point = Dot([3, j, 0], color=RED)
            edge_points4.add(point)
        self.play(FadeIn(edge_points4), run_time=0.5)
        count_edge4 = MathTex("12", font_size=30).next_to(edge_points4, DOWN)
        self.play(Write(count_edge4))
        self.wait(0.5)

        # Subtraction
        result3 = MathTex("4 - 12 = -8", font_size=40).to_edge(DOWN)
        self.play(Write(result3))
        self.wait(1.5)

        # Clear
        self.play(FadeOut(grid4, rect4, count_inside4, count_edge4, interior_points4, edge_points4, result3))

        # Side-by-side rectangles: 4x2 vs 2x4
        grid5 = NumberPlane(x_range=[-1, 5], y_range=[-1, 3], faded_line_ratio=1)
        rect5a = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.2).move_to(LEFT * 2)
        rect5b = Rectangle(width=2, height=4, color=BLUE, fill_opacity=0.2).move_to(RIGHT * 2)
        self.play(Create(grid5), run_time=0.5)
        self.play(Create(rect5a), Create(rect5b), run_time=0.5)

        # Labels
        label_a = Text("4x2", font_size=24).next_to(rect5a, DOWN)
        label_b = Text("2x4", font_size=24).next_to(rect5b, DOWN)
        self.play(Write(label_a), Write(label_b))
        self.wait(0.5)

        # Sorrel count calculation
        calc1 = MathTex(r"(4-1)(2-1) = 3", font_size=24).next_to(label_a, UP)
        calc2 = MathTex(r"2(4+2) = 12", font_size=24).next_to(calc1, DOWN)
        self.play(Write(calc1), Write(calc2))
        self.wait(0.5)

        calc3 = MathTex(r"(2-1)(4-1) = 3", font_size=24).next_to(label_b, UP)
        calc4 = MathTex(r"2(2+4) = 12", font_size=24).next_to(calc3, DOWN)
        self.play(Write(calc3), Write(calc4))
        self.wait(0.5)

        # Final result
        final = MathTex("3 - 12 = -9", font_size=30).to_edge(DOWN)
        self.play(Write(final))
        self.wait(1.5)

        # Clear
        self.play(FadeOut(grid5, rect5a, rect5b, label_a, label_b, calc1, calc2, calc3, calc4, final))

        # Final example: 4x2 vs 2x4 with correct count
        grid6 = NumberPlane(x_range=[-1, 5], y_range=[-1, 3], faded_line_ratio=1)
        rect6a = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.2).move_to(LEFT * 2)
        rect6b = Rectangle(width=2, height=4, color=BLUE, fill_opacity=0.2).move_to(RIGHT * 2)
        self.play(Create(grid6), run_time=0.5)
        self.play(Create(rect6a), Create(rect6b), run_time=0.5)

        label_a2 = Text("4x2", font_size=24).next_to(rect6a, DOWN)
        label_b2 = Text("2x4", font_size=24).next_to(rect6b, DOWN)
        self.play(Write(label_a2), Write(label_b2))
        self.wait(0.5)

        # Interior and edge counts
        inside_a = MathTex(r"(4-1)(2-1) = 3", font_size=24).next_to(label_a2, UP)
        edge_a = MathTex(r"2(4+2) = 12", font_size=24).next_to(inside_a, DOWN)
        self.play(Write(inside_a), Write(edge_a))
        self.wait(0.5)

        inside_b = MathTex(r"(2-1)(4-1) = 3", font_size=24).next_to(label_b2, UP)
        edge_b = MathTex(r"2(2+4) = 12", font_size=24).next_to(inside_b, DOWN)
        self.play(Write(inside_b), Write(edge_b))
        self.wait(0.5)

        # Final result
        final2 = MathTex("3 - 12 = -9", font_size=30).to_edge(DOWN)
        self.play(Write(final2))
        self.wait(1.5)

        # Clear
        self.play(FadeOut(grid6, rect6a, rect6b, label_a2, label_b2, inside_a, edge_a, inside_b, edge_b, final2))

        # Final statement
        final_text = Text("The Sorrel Count is the same for both rectangles.", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(title, final_text))
