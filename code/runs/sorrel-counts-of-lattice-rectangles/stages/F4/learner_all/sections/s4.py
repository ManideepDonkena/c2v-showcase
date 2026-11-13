from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Sorrel Counts of Lattice Rectangles", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid and rectangle
        grid = NumberPlane(x_range=[-2, 4], y_range=[-2, 4], faded_line_ratio=1)
        rect = Rectangle(width=3, height=3, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        self.play(Create(grid), run_time=1)
        self.play(FadeIn(rect), run_time=0.5)

        # Interior points
        interior_points = []
        for i in range(1, 3):
            for j in range(1, 3):
                point = Dot(color=YELLOW).move_to([i, j, 0])
                interior_points.append(point)
                self.add(point)

        # Edge points
        edge_points = []
        # Top and bottom edges
        for i in [-1, 0, 1, 2, 3]:
            point1 = Dot(color=RED).move_to([i, 3, 0])
            point2 = Dot(color=RED).move_to([i, -1, 0])
            edge_points.extend([point1, point2])
            self.add(point1, point2)
        # Left and right edges
        for j in [-1, 0, 1, 2, 3]:
            point1 = Dot(color=RED).move_to([-1, j, 0])
            point2 = Dot(color=RED).move_to([3, j, 0])
            edge_points.extend([point1, point2])
            self.add(point1, point2)

        # Counting
        count_interior = Text("Interior points: 4", font_size=24).to_corner(UL)
        count_edge = Text("Edge points: 12", font_size=24).next_to(count_interior, DOWN)
        self.play(Write(count_interior), Write(count_edge))
        self.wait(1)

        # Sorrel Count Formula
        formula = MathTex(r"(w-1)(h-1) - 2(w+h)", font_size=30).to_corner(DR)
        self.play(Write(formula))
        self.wait(1)

        # Apply to 3x3
        result = MathTex(r"= (3-1)(3-1) - 2(3+3) = 4 - 12 = -8", font_size=30).next_to(formula, DOWN)
        self.play(Write(result))
        self.wait(1)

        # Highlight result
        highlight = Text("Sorrel Count: -8", font_size=30, color=RED).set_color(RED).to_edge(DOWN)
        self.play(Write(highlight))
        self.wait(1.5)

        # Rule box
        rule_box = Rectangle(width=6, height=2, color=YELLOW, fill_opacity=0.2).to_corner(DR)
        rule_text = Text("Small rectangles have negative sorrel counts.", font_size=24).move_to(rule_box.get_center())
        self.play(FadeIn(rule_box), Write(rule_text))
        self.wait(2)

        # Example: 4x5
        self.play(FadeOut(rule_box, rule_text, highlight, result, formula, count_interior, count_edge))

        # Show 4x5 example
        rect2 = Rectangle(width=4, height=5, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        self.play(FadeIn(rect2))
        self.wait(0.5)

        # Interior points for 4x5
        interior_points_45 = []
        for i in range(1, 4):
            for j in range(1, 5):
                point = Dot(color=YELLOW).move_to([i, j, 0])
                interior_points_45.append(point)
                self.add(point)

        # Edge points for 4x5
        edge_points_45 = []
        for i in [-1, 0, 1, 2, 3, 4]:
            point1 = Dot(color=RED).move_to([i, 5, 0])
            point2 = Dot(color=RED).move_to([i, -1, 0])
            edge_points_45.extend([point1, point2])
            self.add(point1, point2)
        for j in [-1, 0, 1, 2, 3, 4, 5]:
            point1 = Dot(color=RED).move_to([-1, j, 0])
            point2 = Dot(color=RED).move_to([4, j, 0])
            edge_points_45.extend([point1, point2])
            self.add(point1, point2)

        count_interior_45 = Text("Interior points: 12", font_size=24).to_corner(UL)
        count_edge_45 = Text("Edge points: 18", font_size=24).next_to(count_interior_45, DOWN)
        self.play(Write(count_interior_45), Write(count_edge_45))
        self.wait(1)

        # Sorrel Count for 4x5
        result_45 = MathTex(r"= (4-1)(5-1) - 2(4+5) = 12 - 18 = -6", font_size=30).next_to(count_edge_45, DOWN)
        self.play(Write(result_45))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(rect, rect2, grid, *interior_points, *edge_points, *interior_points_45, *edge_points_45,
                    count_interior, count_edge, count_interior_45, count_edge_45, result_45, title)
        )
        self.wait(0.5)
