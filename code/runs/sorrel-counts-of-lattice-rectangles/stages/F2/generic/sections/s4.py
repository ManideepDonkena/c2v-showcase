from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Sorrel Counts of Lattice Rectangles", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid and rectangle
        grid = NumberPlane(x_range=[-4, 4], y_range=[-4, 4], faded_line_ratio=1)
        self.play(Create(grid), run_time=1)
        
        square = Square(side_length=6, color=BLUE, fill_opacity=0.2).move_to(ORIGIN)
        self.play(FadeIn(square), run_time=0.5)

        # Points
        interior_points = []
        for i in range(-2, 3):
            for j in range(-2, 3):
                if i != -2 and i != 2 and j != -2 and j != 2:
                    point = Dot(color=YELLOW).move_to([i, j, 0])
                    interior_points.append(point)
                    self.add(point)

        edge_points = []
        for i in range(-3, 4):
            for j in range(-3, 4):
                if i == -3 or i == 3 or j == -3 or j == 3:
                    point = Dot(color=RED).move_to([i, j, 0])
                    edge_points.append(point)
                    self.add(point)

        # Counting
        count_interior = MathTex("4", color=YELLOW).next_to(square, DOWN, buff=0.5)
        count_edge = MathTex("12", color=RED).next_to(count_interior, RIGHT, buff=0.5)
        self.play(Write(count_interior), Write(count_edge))
        self.wait(0.5)

        # Sorrel count
        sorrel_count = MathTex(r"\text{Sorrel} = 4 - 12 = \mathbf{-8}", color=RED, font_size=40).next_to(count_edge, RIGHT, buff=0.5)
        self.play(Write(sorrel_count))
        self.wait(1)

        # Rule box
        rule_box = Rectangle(height=2, width=6, color=ORANGE, fill_opacity=0.3).to_edge(DOWN)
        rule_text = Text("Small rectangles have negative sorrel counts.", font_size=24).move_to(rule_box.get_center())
        self.play(FadeIn(rule_box), Write(rule_text))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(square),
            FadeOut(count_interior),
            FadeOut(count_edge),
            FadeOut(sorrel_count),
            FadeOut(rule_box),
            FadeOut(rule_text),
            *[FadeOut(p) for p in interior_points],
            *[FadeOut(p) for p in edge_points]
        )
        self.wait(0.5)
