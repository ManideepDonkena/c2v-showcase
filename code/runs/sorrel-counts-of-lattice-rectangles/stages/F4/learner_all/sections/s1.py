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
        rect = Rectangle(width=4, height=2, color=YELLOW, fill_opacity=0.3).move_to((2, 1, 0))
        self.play(Create(rect), run_time=0.5)
        self.wait(0.5)

        # Interior points
        interior_points = []
        for x in range(1, 4):
            for y in range(1, 2):
                point = Dot(color=BLUE).move_to((x, y, 0))
                interior_points.append(point)
                self.play(FadeIn(point), run_time=0.1)

        # Count interior points
        count_int = MathTex("8", color=BLUE, font_size=30).next_to(rect, DOWN)
        self.play(Write(count_int))
        self.wait(0.5)

        # Edge points
        edge_points = []
        # Top and bottom edges
        for x in range(0, 5):
            point1 = Dot(color=RED).move_to((x, 2, 0))
            point2 = Dot(color=RED).move_to((x, 0, 0))
            edge_points.append(point1)
            edge_points.append(point2)
        # Left and right edges (excluding corners already added)
        for y in range(1, 2):
            point3 = Dot(color=RED).move_to((0, y, 0))
            point4 = Dot(color=RED).move_to((4, y, 0))
            edge_points.append(point3)
            edge_points.append(point4)

        for p in edge_points:
            self.play(FadeIn(p), run_time=0.05)

        # Count edge points
        count_edge = MathTex("10", color=RED, font_size=30).next_to(count_int, RIGHT, buff=1)
        self.play(Write(count_edge))
        self.wait(0.5)

        # Formula
        formula = MathTex(r"\text{Sorrel Count} = \text{Inside} - \text{Edge}", font_size=36)
        formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(1)

        # Show the general formula
        general_formula = MathTex(
            r"\text{Sorrel Count} = (w-1)(h-1) - 2(w+h)",
            font_size=30
        ).next_to(formula, DOWN)
        self.play(Write(general_formula))
        self.wait(1)

        # Example: 4x5 rectangle
        example_text = Text("Example: 4×5 rectangle", font_size=24).to_edge(DOWN)
        self.play(Write(example_text))
        self.wait(0.5)

        w, h = 4, 5
        inside_count = (w - 1) * (h - 1)
        edge_count = 2 * (w + h)
        result = inside_count - edge_count

        example_inside = MathTex(f"Interior: ({w}-1)({h}-1) = {inside_count}", font_size=24).to_edge(LEFT, buff=0.5)
        example_edge = MathTex(f"Edge: 2({w}+{h}) = {edge_count}", font_size=24).next_to(example_inside, DOWN, aligned_edge=LEFT)
        example_result = MathTex(f"Count: {inside_count} - {edge_count} = {result}", font_size=24).next_to(example_edge, DOWN, aligned_edge=LEFT)

        self.play(Write(example_inside))
        self.wait(0.5)
        self.play(Write(example_edge))
        self.wait(0.5)
        self.play(Write(example_result))
        self.wait(1)

        # Rule: small rectangles have negative counts
        rule = Text("Small rectangles have negative sorrel counts", font_size=24).to_edge(DOWN)
        self.play(Transform(example_text, rule))
        self.wait(0.5)

        # 3x3 square example
        square_example = Text("Example: 3×3 square", font_size=24).to_edge(DOWN)
        self.play(Transform(example_text, square_example))
        self.wait(0.5)

        w2, h2 = 3, 3
        inside_count2 = (w2 - 1) * (h2 - 1)
        edge_count2 = 2 * (w2 + h2)
        result2 = inside_count2 - edge_count2

        example_inside2 = MathTex(f"Interior: ({w2}-1)({h2}-1) = {inside_count2}", font_size=24).to_edge(LEFT, buff=0.5).shift(DOWN * 0.4)
        example_edge2 = MathTex(f"Edge: 2({w2}+{h2}) = {edge_count2}", font_size=24).next_to(example_inside2, DOWN, aligned_edge=LEFT).shift(DOWN * 0.4)
        example_result2 = MathTex(f"Count: {inside_count2} - {edge_count2} = {result2}", font_size=24).next_to(example_edge2, DOWN, aligned_edge=LEFT).shift(DOWN * 0.4)

        self.play(Write(example_inside2))
        self.wait(0.5)
        self.play(Write(example_edge2))
        self.wait(0.5)
        self.play(Write(example_result2))
        self.wait(1)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(rect),
            *[FadeOut(p) for p in interior_points],
            *[FadeOut(p) for p in edge_points],
            FadeOut(count_int),
            FadeOut(count_edge),
            FadeOut(formula),
            FadeOut(general_formula),
            FadeOut(example_text),
            FadeOut(example_inside),
            FadeOut(example_edge),
            FadeOut(example_result),
            FadeOut(example_inside2),
            FadeOut(example_edge2),
            FadeOut(example_result2),
            run_time=1
        )
