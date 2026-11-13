from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Sorrel Counts of Lattice Rectangles", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = VGroup()
        for i in range(4):
            for j in range(4):
                dot = Dot(point=[i, j, 0], color=WHITE)
                grid.add(dot)
        
        grid.scale(0.8).move_to(ORIGIN)
        self.play(Create(grid))
        self.wait(0.5)

        # Highlight 3x3 square
        square = Square(side_length=3, color=YELLOW, fill_opacity=0.1).move_to(ORIGIN)
        self.play(Create(square))
        self.wait(0.5)

        # Count interior points (4)
        interior_points = VGroup()
        for i in range(1, 3):
            for j in range(1, 3):
                p = Dot(point=[i, j, 0], color=GREEN)
                interior_points.add(p)
        self.play(Create(interior_points))
        self.wait(0.5)

        # Count edge points (12)
        edge_points = VGroup()
        for i in range(4):
            for j in range(4):
                if i == 0 or i == 3 or j == 0 or j == 3:
                    p = Dot(point=[i, j, 0], color=RED)
                    edge_points.add(p)
        edge_points.shift(0.0 * RIGHT + -0.23 * UP)  # layout: separation vector
        self.play(Create(edge_points))
        self.wait(0.5)

        # Show formula and calculation
        formula = MathTex("S = I - E", font_size=36).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(formula))
        self.wait(0.5)

        # Show values
        inside_count = MathTex("I = 4", font_size=24).next_to(formula, RIGHT, buff=0.5)
        edge_count = MathTex("E = 12", font_size=24).next_to(inside_count, RIGHT, buff=0.5)
        self.play(Write(inside_count), Write(edge_count))
        self.wait(0.5)

        # Result
        result = MathTex("S = 4 - 12 = -8", font_size=36, color=RED).next_to(edge_count, RIGHT, buff=0.5)
        self.play(Write(result))
        self.wait(1)

        # Rule box
        rule_box = Rectangle(width=5, height=2, color=BLUE, fill_opacity=0.2).to_edge(DOWN)
        rule_text = Text("Small rectangles have negative sorrel counts.", font_size=24).move_to(rule_box.get_center())
        self.play(Create(rule_box), Write(rule_text))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(title, grid, square, interior_points, edge_points, formula, inside_count, edge_count, result, rule_box, rule_text))
        self.wait(0.5)
