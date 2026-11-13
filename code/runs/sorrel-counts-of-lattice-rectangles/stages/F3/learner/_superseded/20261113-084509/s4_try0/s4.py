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
                grid.add(Dot([i, j, 0], color=WHITE))
        grid.scale(0.8).shift(LEFT * 2 + DOWN * 0.5)
        self.play(Create(grid))
        self.wait(0.5)

        # Count interior points
        interior = VGroup()
        for i in range(1, 3):
            for j in range(1, 3):
                dot = Dot([i, j, 0], color=YELLOW)
                interior.add(dot)
        self.play(FadeIn(interior))
        self.wait(0.5)

        # Count edge points
        edge_dots = VGroup()
        # Top and bottom edges
        for i in range(4):
            edge_dots.add(Dot([i, 0, 0], color=BLUE))
            edge_dots.add(Dot([i, 3, 0], color=BLUE))
        # Left and right edges (excluding corners already added)
        for j in range(1, 3):
            edge_dots.add(Dot([0, j, 0], color=BLUE))
            edge_dots.add(Dot([3, j, 0], color=BLUE))
        edge_dots.shift(0.0 * RIGHT + -0.23 * UP)  # layout: separation vector
        self.play(FadeIn(edge_dots))
        self.wait(0.5)

        # Text labels
        interior_label = Text("4 interior points", font_size=24).next_to(interior, DOWN)
        edge_label = Text("12 edge points", font_size=24).next_to(edge_dots, UP)
        edge_label.shift(0.0 * RIGHT + 0.55 * UP)  # layout: separation vector
        interior_label.shift(0.0 * RIGHT + -0.28 * UP)  # layout: separation vector
        self.play(Write(interior_label), Write(edge_label))
        self.wait(0.5)

        # Sorrel count calculation
        calc_text = MathTex("4 - 12 = -8", font_size=40).set_color(RED).to_edge(DOWN)
        self.play(Write(calc_text))
        self.wait(1.5)

        # Rule box
        rule_box = Rectangle(width=6, height=2, color=YELLOW, fill_opacity=0.2).to_edge(UP)
        rule_text = Text("Small rectangles have negative sorrel counts.", font_size=24).move_to(rule_box.get_center())
        self.play(Create(rule_box), Write(rule_text))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(interior),
            FadeOut(edge_dots),
            FadeOut(interior_label),
            FadeOut(edge_label),
            FadeOut(calc_text),
            FadeOut(rule_box),
            FadeOut(rule_text)
        )
        self.wait(0.5)
