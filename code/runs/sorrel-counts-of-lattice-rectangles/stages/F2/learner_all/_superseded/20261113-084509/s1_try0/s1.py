from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Sorrel Count", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid and rectangle
        grid = NumberPlane(
            x_range=[-1, 5, 1],
            y_range=[-1, 3, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY}
        )
        self.play(Create(grid), run_time=1)
        self.wait(0.5)

        # Rectangle from (0,0) to (4,2)
        rect = Rectangle(
            width=4,
            height=2,
            color=BLUE,
            fill_opacity=0.2,
            stroke_width=2
        ).move_to([2, 1, 0])
        self.play(Create(rect), run_time=0.5)
        self.wait(0.5)

        # Interior points (blue)
        inside_points = []
        for x in range(1, 4):
            for y in range(1, 2):
                point = Dot([x, y, 0], color=BLUE)
                inside_points.append(point)
                self.add(point)
        self.wait(0.5)

        # Edge points (red)
        edge_points = []
        # Top and bottom edges
        for x in range(0, 5):
            point1 = Dot([x, 2, 0], color=RED)
            point2 = Dot([x, 0, 0], color=RED)
            edge_points.extend([point1, point2])
            self.add(point1, point2)
        # Left and right edges
        for y in range(0, 3):
            point1 = Dot([0, y, 0], color=RED)
            point2 = Dot([4, y, 0], color=RED)
            edge_points.extend([point1, point2])
            self.add(point1, point2)
        self.wait(0.5)

        # Count labels
        inside_count = MathTex("8", color=BLUE).next_to(rect, DOWN, buff=0.2)
        edge_count = MathTex("10", color=RED).next_to(rect, LEFT, buff=0.2)
        self.play(Write(inside_count), Write(edge_count))
        self.wait(1)

        # Formula
        formula = MathTex("Sorrel Count =", "8", "-", "10", "=", "-2")
        formula.scale(1.2).to_edge(DOWN)
        self.play(Write(formula))
        self.wait(1.5)

        # Explanation text
        explanation = Text(
            "Interior points - Edge points",
            font_size=24,
            color=YELLOW
        ).next_to(formula, UP, buff=0.3)
        self.play(Write(explanation))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(rect),
            FadeOut(inside_count),
            FadeOut(edge_count),
            FadeOut(formula),
            FadeOut(explanation)
        )
        self.wait(0.5)

        # Worked example: 3x3 square
        title2 = Text("Worked Example: 3×3 Square", font_size=36).to_edge(UP)
        self.play(Write(title2))
        self.wait(0.5)

        grid2 = NumberPlane(
            x_range=[-1, 4, 1],
            y_range=[-1, 4, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY}
        )
        self.play(Create(grid2), run_time=0.5)
        self.wait(0.5)

        rect2 = Rectangle(
            width=3,
            height=3,
            color=BLUE,
            fill_opacity=0.2,
            stroke_width=2
        ).move_to([1.5, 1.5, 0])
        self.play(Create(rect2), run_time=0.5)
        self.wait(0.5)

        # Inside points (3-1) × (3-1) = 4
        inside_points2 = []
        for x in range(1, 3):
            for y in range(1, 3):
                point = Dot([x, y, 0], color=BLUE)
                inside_points2.append(point)
                self.add(point)
        self.wait(0.5)

        # Edge points: 2×(3+3) = 12
        edge_points2 = []
        for x in range(0, 4):
            point1 = Dot([x, 3, 0], color=RED)
            point2 = Dot([x, 0, 0], color=RED)
            edge_points2.extend([point1, point2])
            self.add(point1, point2)
        for y in range(0, 4):
            point1 = Dot([0, y, 0], color=RED)
            point2 = Dot([3, y, 0], color=RED)
            edge_points2.extend([point1, point2])
            self.add(point1, point2)
        self.wait(0.5)

        # Counts
        inside_count2 = MathTex("4", color=BLUE).next_to(rect2, DOWN, buff=0.2)
        edge_count2 = MathTex("12", color=RED).next_to(rect2, LEFT, buff=0.2)
        self.play(Write(inside_count2), Write(edge_count2))
        self.wait(1)

        # Sorrel count formula
        formula2 = MathTex("Sorrel Count =", "4", "-", "12", "=", "-8")
        formula2.scale(1.2).to_edge(DOWN)
        self.play(Write(formula2))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title2),
            FadeOut(grid2),
            FadeOut(rect2),
            FadeOut(inside_count2),
            FadeOut(edge_count2),
            FadeOut(formula2)
        )
        self.wait(0.5)
