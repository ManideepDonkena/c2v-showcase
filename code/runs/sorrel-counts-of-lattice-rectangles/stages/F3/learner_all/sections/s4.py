from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Sorrel Counts of Lattice Rectangles", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 3x3 square grid
        grid = VGroup()
        for i in range(4):
            for j in range(4):
                dot = Dot(point=[i, j, 0], color=WHITE)
                grid.add(dot)
        grid.scale(0.7).to_edge(LEFT, buff=1)
        self.play(Create(grid))
        self.wait(0.5)

        # Interior points (3-1)x(3-1) = 4
        interior_count = MathTex("4", font_size=30)
        interior_count.next_to(grid, DOWN, buff=0.3)
        self.play(Write(interior_count))
        self.wait(0.5)

        # Edge points 2x(3+3) = 12
        edge_count = MathTex("12", font_size=30)
        edge_count.next_to(interior_count, DOWN, buff=0.3)
        self.play(Write(edge_count))
        self.wait(0.5)

        # Sorrel count calculation: 4 - 12 = -8
        sorrel_calc = MathTex("4 - 12 =", font_size=30)
        sorrel_calc.next_to(edge_count, DOWN, buff=0.3)
        result = MathTex("-8", font_size=40, color=RED)
        result.next_to(sorrel_calc, RIGHT, buff=0.3)
        self.play(Write(sorrel_calc), Write(result))
        self.wait(1)

        # Rule box
        rule_box = Rectangle(width=5, height=2, color=YELLOW, fill_opacity=0.2)
        rule_box.to_edge(DOWN, buff=0.5)
        rule_text = Text("Small rectangles have negative sorrel counts.", font_size=24)
        rule_text.move_to(rule_box.get_center())
        rule_text.shift(0.0 * RIGHT + 1.32 * UP)  # layout: separation vector
        self.play(Create(rule_box), Write(rule_text))
        self.wait(1.5)

        # Fade out previous
        self.play(FadeOut(title, grid, interior_count, edge_count, sorrel_calc, result, rule_box, rule_text))

        # Generic w x h rectangle
        generic_grid = VGroup()
        for i in range(3):
            for j in range(4):
                dot = Dot(point=[i, j, 0], color=WHITE)
                generic_grid.add(dot)
        generic_grid.scale(0.6).to_edge(LEFT, buff=1)

        # Labels
        w_label = MathTex("w", font_size=24)
        h_label = MathTex("h", font_size=24)
        w_label.next_to(generic_grid, DOWN, buff=0.2)
        h_label.next_to(generic_grid, RIGHT, buff=0.2)

        # Interior points: (w-1)(h-1)
        interior_label = MathTex("(w-1)(h-1)", font_size=24)
        interior_label.to_edge(UP, buff=0.5).shift(RIGHT * 2)
        self.play(Create(generic_grid), Write(w_label), Write(h_label))
        self.wait(0.5)

        # Edge points: 2(w+h)
        edge_label = MathTex("2(w+h)", font_size=24)
        edge_label.to_edge(DOWN, buff=0.5).shift(RIGHT * 2)
        self.play(Write(edge_label))
        self.wait(0.5)

        # Sorrel count formula
        formula = MathTex(r"\text{Sorrel Count} = (w-1)(h-1) - 2(w+h)", font_size=30)
        formula.to_edge(UP, buff=0.5).shift(LEFT * 2)
        self.play(Write(formula))
        self.wait(1)

        # Example: w=2, h=3
        example = MathTex("w=2, h=3", font_size=24)
        example.next_to(formula, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait(0.5)

        # Compute interior term (1x2 = 2)
        term1 = MathTex("1 \\times 2 = 2", font_size=24)
        term1.next_to(example, DOWN, buff=0.3)
        self.play(Write(term1))
        self.wait(0.5)

        # Compute edge term (2x5 = 10)
        term2 = MathTex("2 \\times 5 = 10", font_size=24)
        term2.next_to(term1, DOWN, buff=0.3)
        self.play(Write(term2))
        self.wait(0.5)

        # Final result: negative
        final_result = MathTex("\\text{Negative!}", font_size=30, color=RED)
        final_result.next_to(term2, DOWN, buff=0.3)
        self.play(Write(final_result))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(generic_grid, w_label, h_label, edge_label, formula, example, term1, term2, final_result))
