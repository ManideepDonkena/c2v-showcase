from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Sorrel Counts of Lattice Rectangles", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 3x3 Square Grid
        grid_3x3 = VGroup()
        for i in range(4):
            for j in range(4):
                dot = Dot(point=[i, j, 0], radius=0.05)
                grid_3x3.add(dot)
        grid_3x3.scale(0.8).move_to(ORIGIN)

        # Interior points (4)
        interior_points = VGroup(*[dot for i in range(3) for j in range(3) if (i,j) != (0,0) and (i,j) != (0,2) and (i,j) != (2,0) and (i,j) != (2,2)])
        interior_count = MathTex("4", color=GREEN).next_to(grid_3x3, DOWN, buff=0.5)
        self.play(Create(grid_3x3), run_time=1)
        self.wait(0.5)

        # Edge points count
        edge_count = MathTex("12", color=RED).next_to(interior_count, RIGHT, buff=0.5)
        self.play(Write(edge_count))
        self.wait(0.5)

        # Sorrel Count Result
        result = MathTex(r"\text{Sorrel Count} = 4 - 12 = \mathbf{-8}", color=RED, font_size=36).next_to(edge_count, RIGHT, buff=0.5)
        self.play(Write(result))
        self.wait(1)

        # Rule Box
        rule_box = Rectangle(width=5, height=1.5, color=YELLOW, fill_opacity=0.2).next_to(result, DOWN, buff=0.5)
        rule_text = Text("Small rectangles have negative sorrel counts.", font_size=24).move_to(rule_box.get_center())
        rule_text.shift(-6.21 * RIGHT + 0.0 * UP)  # layout: separation vector
        rule_box.shift(0.0 * RIGHT + 0.19 * UP)  # layout: separation vector
        self.play(Create(rule_box), Write(rule_text))
        self.wait(1.5)

        # Breakdown of edge points
        self.play(FadeOut(rule_box, rule_text))

        breakdown = Text("Top/Bottom: w+1 each\nLeft/Right: h+1 each\nCorner overlap: -4", font_size=24).to_edge(DOWN)
        self.play(Write(breakdown))
        self.wait(1.5)

        # 2x3 Rectangle
        self.play(FadeOut(breakdown))

        grid_2x3 = VGroup()
        for i in range(3):
            for j in range(4):
                dot = Dot(point=[i, j, 0], radius=0.05)
                grid_2x3.add(dot)
        grid_2x3.scale(0.7).move_to(LEFT * 3)

        interior_2x3 = MathTex("1 \\times 2 = 2", color=GREEN).next_to(grid_2x3, DOWN, buff=0.5)
        edge_2x3 = MathTex("2 \\times (2 + 3) = 10", color=RED).next_to(interior_2x3, RIGHT, buff=0.5)
        calc_2x3 = MathTex("2 - 10 = \mathbf{-8}", color=RED, font_size=36).next_to(edge_2x3, RIGHT, buff=0.5)

        self.play(Create(grid_2x3), Write(interior_2x3), Write(edge_2x3))
        self.wait(1)
        self.play(Write(calc_2x3))
        self.wait(1.5)

        # 5x2 Rectangle
        grid_5x2 = VGroup()
        for i in range(6):
            for j in range(3):
                dot = Dot(point=[i, j, 0], radius=0.05)
                grid_5x2.add(dot)
        grid_5x2.scale(0.7).move_to(RIGHT * 3)

        interior_5x2 = MathTex("4 \\times 1 = 4", color=GREEN).next_to(grid_5x2, DOWN, buff=0.5)
        edge_5x2 = MathTex("2 \\times (5 + 2) = 14", color=RED).next_to(interior_5x2, RIGHT, buff=0.5)
        calc_5x2 = MathTex("4 - 14 = \mathbf{-10}", color=RED, font_size=36).next_to(edge_5x2, RIGHT, buff=0.5)

        self.play(Create(grid_5x2), Write(interior_5x2), Write(edge_5x2))
        self.wait(1)
        self.play(Write(calc_5x2))
        self.wait(1.5)

        # Revisit 3x3 with +4 and -12
        self.play(FadeOut(grid_2x3, grid_5x2, interior_2x3, edge_2x3, calc_2x3, interior_5x2, edge_5x2, calc_5x2))

        grid_3x3_again = VGroup()
        for i in range(4):
            for j in range(4):
                dot = Dot(point=[i, j, 0], radius=0.05)
                grid_3x3_again.add(dot)
        grid_3x3_again.scale(0.8).move_to(ORIGIN)

        plus_4 = MathTex("+4", color=GREEN).next_to(grid_3x3_again, DOWN, buff=0.5)
        minus_12 = MathTex("-12", color=RED).next_to(plus_4, RIGHT, buff=0.5)
        final_result = MathTex("= \mathbf{-8}", color=RED, font_size=36).next_to(minus_12, RIGHT, buff=0.5)

        self.play(Create(grid_3x3_again), Write(plus_4), Write(minus_12))
        self.wait(1)
        self.play(Write(final_result))
        self.wait(1.5)

        # Side-by-side rectangles with same sorrel count
        self.play(FadeOut(grid_3x3_again, plus_4, minus_12, final_result))

        rect1 = Rectangle(width=4, height=2, color=BLUE).move_to(LEFT * 2)
        rect2 = Rectangle(width=2, height=4, color=BLUE).move_to(RIGHT * 2)

        label1 = Text("4x2", font_size=24).next_to(rect1, UP)
        label2 = Text("2x4", font_size=24).next_to(rect2, UP)

        count1 = MathTex("-6", color=YELLOW).next_to(rect1, DOWN)
        count2 = MathTex("-6", color=YELLOW).next_to(rect2, DOWN)

        self.play(Create(rect1), Create(rect2), Write(label1), Write(label2))
        self.wait(0.5)
        self.play(Write(count1), Write(count2))
        self.wait(1.5)

        # Show interior and edge points changing but final result same
        self.play(FadeOut(rect1, rect2, label1, label2, count1, count2))

        text1 = Text("Interior: 8 vs 1", font_size=24).to_edge(UP)
        text2 = Text("Edge: 10 vs 14", font_size=24).next_to(text1, DOWN)
        text3 = Text("Final: -2 vs -2", font_size=24).next_to(text2, DOWN)

        self.play(Write(text1), Write(text2), Write(text3))
        self.wait(1.5)

        self.play(FadeOut(title, text1, text2, text3))
