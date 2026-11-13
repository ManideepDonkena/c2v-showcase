from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Sorrel Count", font_size=36).to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Grid and rectangle
        grid = NumberPlane(
            x_range=[-1, 5, 1],
            y_range=[-1, 3, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY}
        )
        grid.scale(0.8)
        grid.shift(DOWN * 0.5)

        rect = Rectangle(
            width=4,
            height=2,
            color=BLUE,
            fill_opacity=0.2,
            stroke_width=2
        ).move_to((2, 1, 0))

        self.play(Create(grid), run_time=1)
        self.play(Write(rect), run_time=0.5)
        self.wait(0.5)

        # Highlight interior points in blue
        interior_points = []
        for x in range(1, 4):
            for y in range(1, 2):
                point = Dot(color=BLUE).scale(0.7).move_to((x, y, 0))
                interior_points.append(point)
                self.add(point)

        # Count interior points
        count_inside = Text("8", font_size=24).next_to(rect, UP, buff=0.3)
        self.play(Write(count_inside))
        self.wait(0.5)

        # Highlight edge points in red
        edge_points = []
        for x in [0, 1, 2, 3, 4]:
            for y in [0, 2]:
                if not (x == 0 and y == 0) and not (x == 4 and y == 2):
                    point = Dot(color=RED).scale(0.7).move_to((x, y, 0))
                    edge_points.append(point)
                    self.add(point)

        for x in [0, 4]:
            for y in [1]:
                point = Dot(color=RED).scale(0.7).move_to((x, y, 0))
                edge_points.append(point)
                self.add(point)

        # Count edge points
        count_edge = Text("10", font_size=24).next_to(rect, DOWN, buff=0.3)
        self.play(Write(count_edge))
        self.wait(0.5)

        # Formula
        formula = MathTex("Sorrel\\ Count = Inside - Edge", font_size=36)
        formula.next_to(title, DOWN, buff=0.8)
        self.play(Write(formula))
        self.wait(1)

        # Narration text
        narration = Text("We define the sorrel count...", font_size=24).to_edge(DOWN, buff=0.5)
        self.play(Write(narration))
        self.wait(1.5)

        self.play(FadeOut(narration))
        self.wait(0.5)

        # Example: 3x3 square
        self.play(FadeOut(count_inside, count_edge, formula))
        self.wait(0.5)

        example_rect = Rectangle(width=3, height=3, color=BLUE, fill_opacity=0.2, stroke_width=2).move_to((1.5, 1.5, 0))
        self.play(Write(example_rect))
        self.wait(0.5)

        # Interior points for 3x3
        example_interior = []
        for x in range(1, 3):
            for y in range(1, 3):
                point = Dot(color=BLUE).scale(0.7).move_to((x, y, 0))
                example_interior.append(point)
                self.add(point)

        # Edge points for 3x3
        example_edge = []
        for x in [0, 1, 2, 3]:
            for y in [0, 3]:
                if not (x == 0 and y == 0) and not (x == 3 and y == 3):
                    point = Dot(color=RED).scale(0.7).move_to((x, y, 0))
                    example_edge.append(point)
                    self.add(point)

        for x in [0, 3]:
            for y in [1, 2]:
                point = Dot(color=RED).scale(0.7).move_to((x, y, 0))
                example_edge.append(point)
                self.add(point)

        # Show counts
        count_inside_3 = Text("4", font_size=24).next_to(example_rect, UP, buff=0.3)
        count_edge_3 = Text("12", font_size=24).next_to(example_rect, DOWN, buff=0.3)
        self.play(Write(count_inside_3), Write(count_edge_3))
        self.wait(1)

        # Final sorrel count
        final_count = MathTex("Sorrel\\ Count = 4 - 12 = -8", font_size=30).next_to(example_rect, DOWN, buff=1)
        self.play(Write(final_count))
        self.wait(1.5)

        self.play(FadeOut(title, grid, rect, example_rect, count_inside_3, count_edge_3, final_count))
        self.wait(0.5)
