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
                dot = Dot(point=[i-1.5, j-1.5, 0], radius=0.05)
                grid.add(dot)
        
        grid.scale(0.8).move_to(ORIGIN)
        self.play(Create(grid))
        self.wait(0.5)

        # Highlight interior points
        interior_points = VGroup(
            Dot([0, 0, 0], color=GREEN),
            Dot([1, 0, 0], color=GREEN),
            Dot([0, 1, 0], color=GREEN),
            Dot([1, 1, 0], color=GREEN)
        )
        interior_points.scale(0.8).move_to(ORIGIN)

        # Animate counting interior points
        self.play(FadeIn(interior_points))
        self.wait(0.5)

        # Count interior points
        count_interior = MathTex("4", color=GREEN, font_size=40).next_to(interior_points, DOWN)
        self.play(Write(count_interior))
        self.wait(0.5)

        # Highlight edge points
        edge_points = VGroup(
            Dot([-1, -1, 0], color=RED),
            Dot([0, -1, 0], color=RED),
            Dot([1, -1, 0], color=RED),
            Dot([2, -1, 0], color=RED),
            Dot([2, 0, 0], color=RED),
            Dot([2, 1, 0], color=RED),
            Dot([2, 2, 0], color=RED),
            Dot([1, 2, 0], color=RED),
            Dot([0, 2, 0], color=RED),
            Dot([-1, 2, 0], color=RED),
            Dot([-1, 1, 0], color=RED),
            Dot([-1, 0, 0], color=RED)
        )
        edge_points.scale(0.8).move_to(ORIGIN)

        self.play(FadeIn(edge_points))
        self.wait(0.5)

        # Count edge points
        count_edge = MathTex("12", color=RED, font_size=40).next_to(edge_points, DOWN)
        self.play(Write(count_edge))
        self.wait(0.5)

        # Show formula and calculation
        formula = MathTex(r"\text{Sorrel Count} = \text{Interior} - \text{Edge}", font_size=24)
        formula.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(formula))
        self.wait(0.5)

        # Show calculation
        calc = MathTex("4 - 12 = -8", color=RED, font_size=40)
        calc.next_to(formula, DOWN)
        self.play(Write(calc))
        self.wait(1.0)

        # Rule box
        rule_box = Rectangle(height=2, width=5, color=YELLOW, fill_opacity=0.3).to_edge(DOWN)
        rule_text = Text("Small rectangles have negative sorrel counts.", font_size=24)
        rule_text.move_to(rule_box.get_center())
        self.play(Create(rule_box), Write(rule_text))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(interior_points),
            FadeOut(edge_points),
            FadeOut(count_interior),
            FadeOut(count_edge),
            FadeOut(formula),
            FadeOut(calc),
            FadeOut(rule_box),
            FadeOut(rule_text)
        )
        self.wait(0.5)
