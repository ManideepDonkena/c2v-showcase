from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Sorrel Counts of Lattice Rectangles", font_size=36).to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Grid
        grid = VGroup()
        for i in range(4):
            for j in range(4):
                dot = Dot(point=[i, j, 0], radius=0.05)
                grid.add(dot)
        grid.scale(0.8).move_to(ORIGIN)
        self.play(Create(grid))
        self.wait(0.5)

        # Interior points
        interior_points = VGroup()
        for i in range(1, 3):
            for j in range(1, 3):
                p = Dot(point=grid[i * 4 + j].get_center(), radius=0.08, color=YELLOW)
                interior_points.add(p)
        self.play(FadeIn(interior_points))
        self.wait(0.5)

        # Edge points
        edge_points = VGroup()
        for i in range(4):
            for j in range(4):
                if i == 0 or i == 3 or j == 0 or j == 3:
                    p = Dot(point=grid[i * 4 + j].get_center(), radius=0.08, color=GREEN)
                    edge_points.add(p)
        self.play(FadeIn(edge_points))
        self.wait(0.5)

        # Count labels
        count_interior = MathTex("4", font_size=30).next_to(interior_points, DOWN, buff=0.2)
        count_edge = MathTex("12", font_size=30).next_to(edge_points, UP, buff=0.2)
        self.play(Write(count_interior), Write(count_edge))
        self.wait(0.5)

        # Sorrel count calculation
        calc = MathTex(r"\text{Sorrel} = 4 - 12 = -8", font_size=36).move_to(DOWN * 1.9)
        self.play(Write(calc))
        self.wait(1.0)

        # Highlight result in red
        result = Text("-8", font_size=40, color=RED).move_to(DOWN * 1.9)
        self.play(Transform(calc, result))
        self.wait(1.0)

        # Rule box
        rule_text = Text("Small rectangles have negative sorrel counts.", font_size=24)
        rule_box = Rectangle(width=rule_text.width + 0.6, height=1.0, color=BLUE, fill_opacity=0.2).to_edge(DOWN, buff=0.5)
        rule_text.move_to(rule_box.get_center())
        self.play(Create(rule_box), Write(rule_text))
        self.wait(1.5)

        # Clean up
        self.play(FadeOut(title, grid, interior_points, edge_points, count_interior, count_edge, calc, rule_box, rule_text))
        self.wait(0.5)
