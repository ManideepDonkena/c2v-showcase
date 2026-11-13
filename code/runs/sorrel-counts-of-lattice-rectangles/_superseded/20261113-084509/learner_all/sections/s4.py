from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Sorrel Counts of Lattice Rectangles", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 3x3 square grid
        grid_3x3 = VGroup()
        for i in range(4):
            for j in range(4):
                dot = Dot(point=[i, j, 0], radius=0.05)
                grid_3x3.add(dot)
        grid_3x3.scale(0.7).move_to(ORIGIN)
        self.play(Create(grid_3x3))
        self.wait(0.5)

        # Interior points (4)
        interior_points = VGroup()
        for i in range(1, 3):
            for j in range(1, 3):
                dot = Dot(point=[i, j, 0], radius=0.07, color=YELLOW)
                interior_points.add(dot)
        self.play(Create(interior_points))
        self.wait(0.5)

        # Edge points (12)
        edge_points = VGroup()
        for i in range(4):
            for j in range(4):
                if i == 0 or i == 3 or j == 0 or j == 3:
                    dot = Dot(point=[i, j, 0], radius=0.07, color=GREEN)
                    edge_points.add(dot)
        edge_points.shift(0.0 * RIGHT + -0.22 * UP)  # layout: separation vector
        self.play(Create(edge_points))
        self.wait(0.5)

        # Sorrel count calculation
        calc_text = MathTex("4 - 12 = -8", font_size=40).set_color(RED).move_to(DOWN * 1.5)
        self.play(Write(calc_text))
        self.wait(1.0)

        # Rule box
        rule_box = Rectangle(width=6, height=2, color=BLUE, fill_opacity=0.2).move_to(UP * 1.5)
        rule_text = Text("Small rectangles have negative sorrel counts.", font_size=24).move_to(rule_box.get_center())
        self.play(Create(rule_box), Write(rule_text))
        self.wait(1.0)

        # Fade out
        self.play(FadeOut(rule_box, rule_text, calc_text))

        # Show (w-1)(h-1) interior points
        w, h = 3, 3
        interior_formula = MathTex(f"({w}-1) \\times ({h}-1) = {int((w-1)*(h-1))}", font_size=30).to_edge(UP)
        self.play(Write(interior_formula))
        self.wait(0.5)

        # Show 2(w+h) edge points
        edge_formula = MathTex(f"2 \\times ({w} + {h}) = {2*(w+h)}", font_size=30).next_to(interior_formula, DOWN)
        self.play(Write(edge_formula))
        self.wait(0.5)

        # Fade out formulas
        self.play(FadeOut(interior_formula, edge_formula))

        # Show 2x3 rectangle
        grid_2x3 = VGroup()
        for i in range(3):
            for j in range(4):
                dot = Dot(point=[i, j, 0], radius=0.05)
                grid_2x3.add(dot)
        grid_2x3.scale(0.7).move_to(LEFT * 3)
        self.play(Create(grid_2x3))
        self.wait(0.5)

        # Interior points for 2x3
        interior_2x3 = VGroup()
        for i in range(1, 2):
            for j in range(1, 3):
                dot = Dot(point=[i, j, 0], radius=0.07, color=YELLOW)
                interior_2x3.add(dot)
        self.play(Create(interior_2x3))
        self.wait(0.5)

        # Edge points for 2x3
        edge_2x3 = VGroup()
        for i in range(3):
            for j in range(4):
                if i == 0 or i == 2 or j == 0 or j == 3:
                    dot = Dot(point=[i, j, 0], radius=0.07, color=GREEN)
                    edge_2x3.add(dot)
        self.play(Create(edge_2x3))
        self.wait(0.5)

        # Show calculation for 2x3
        calc_2x3 = MathTex("2 - 10 = -8", font_size=40).set_color(RED).move_to(DOWN * 1.5)
        self.play(Write(calc_2x3))
        self.wait(1.0)

        # Fade out
        self.play(FadeOut(calc_2x3, grid_2x3, interior_2x3, edge_2x3))

        # Show 5x2 rectangle
        grid_5x2 = VGroup()
        for i in range(6):
            for j in range(3):
                dot = Dot(point=[i, j, 0], radius=0.05)
                grid_5x2.add(dot)
        grid_5x2.scale(0.7).move_to(RIGHT * 3)
        self.play(Create(grid_5x2))
        self.wait(0.5)

        # Interior points for 5x2
        interior_5x2 = VGroup()
        for i in range(1, 5):
            for j in range(1, 2):
                dot = Dot(point=[i, j, 0], radius=0.07, color=YELLOW)
                interior_5x2.add(dot)
        self.play(Create(interior_5x2))
        self.wait(0.5)

        # Edge points for 5x2
        edge_5x2 = VGroup()
        for i in range(6):
            for j in range(3):
                if i == 0 or i == 5 or j == 0 or j == 2:
                    dot = Dot(point=[i, j, 0], radius=0.07, color=GREEN)
                    edge_5x2.add(dot)
        self.play(Create(edge_5x2))
        self.wait(0.5)

        # Show calculation for 5x2
        calc_5x2 = MathTex("6 - 14 = -8", font_size=40).set_color(RED).move_to(DOWN * 1.5)
        self.play(Write(calc_5x2))
        self.wait(1.0)

        # Fade out
        self.play(FadeOut(calc_5x2, grid_5x2, interior_5x2, edge_5x2))

        # Show two rectangles side-by-side
        rect1 = Rectangle(width=4, height=2).move_to(LEFT * 3)
        label1 = Text("4x2", font_size=24).next_to(rect1, UP)
        count1 = MathTex("-6", font_size=30).move_to(rect1.get_center())
        self.play(Create(rect1), Write(label1), Write(count1))
        self.wait(0.5)

        rect2 = Rectangle(width=2, height=4).move_to(RIGHT * 3)
        label2 = Text("2x4", font_size=24).next_to(rect2, UP)
        count2 = MathTex("-6", font_size=30).move_to(rect2.get_center())
        self.play(Create(rect2), Write(label2), Write(count2))
        self.wait(1.0)

        # Fade out
        self.play(FadeOut(rect1, label1, count1, rect2, label2, count2, title))
        self.wait(0.5)
