from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Sorrel Count", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid and rectangle
        grid = NumberPlane(x_range=[-1, 5], y_range=[-1, 3], faded_line_ratio=1)
        self.play(Create(grid))
        self.wait(0.5)

        rect = Rectangle(color=WHITE, fill_opacity=0.2, stroke_width=3).scale(1).move_to([2, 1, 0])
        rect.stretch_to_fit_width(4)
        rect.stretch_to_fit_height(2)
        self.play(Create(rect))
        self.wait(0.5)

        # Interior points (blue)
        interior_points = VGroup()
        for x in range(1, 4):
            for y in range(1, 2):
                p = Dot([x, y, 0], color=BLUE)
                interior_points.add(p)
        self.play(FadeIn(interior_points))
        self.wait(0.5)

        # Edge points (red)
        edge_points = VGroup()
        for x in [0, 1, 2, 3, 4]:
            for y in [0, 2]:
                if not (x == 0 and y == 0) and not (x == 4 and y == 2):
                    p = Dot([x, y, 0], color=RED)
                    edge_points.add(p)
        for x in [0, 4]:
            for y in range(1, 2):
                p = Dot([x, y, 0], color=RED)
                edge_points.add(p)
        self.play(FadeIn(edge_points))
        self.wait(0.5)

        # Count labels
        count_inside = MathTex("8", color=BLUE).next_to(interior_points, DOWN, buff=0.2)
        count_edge = MathTex("10", color=RED).next_to(edge_points, UP, buff=0.2)
        self.play(Write(count_inside), Write(count_edge))
        self.wait(1)

        # Formula
        formula = MathTex(r"\text{Sorrel Count} = \text{Inside} - \text{Edge}", font_size=36).to_edge(DOWN)
        self.play(Write(formula))
        self.wait(1.5)

        # Fade out first rectangle and points
        self.play(FadeOut(rect), FadeOut(interior_points), FadeOut(edge_points), FadeOut(count_inside), FadeOut(count_edge))

        # Generic w x h rectangle
        generic_rect = Rectangle(color=WHITE, fill_opacity=0.2, stroke_width=3).scale(1).move_to([0, 0, 0])
        generic_rect.stretch_to_fit_width(2)
        generic_rect.stretch_to_fit_height(1.5)
        self.play(Create(generic_rect))
        self.wait(0.5)

        # Interior points
        interior_label = MathTex(r"(w-1) \times (h-1)", color=BLUE).next_to(generic_rect, DOWN)
        self.play(Write(interior_label))
        self.wait(0.5)

        # Edge points
        edge_label = MathTex(r"2 \times (w+h)", color=RED).next_to(generic_rect, UP)
        self.play(Write(edge_label))
        self.wait(0.5)

        # Sorrel count formula
        sorrel_formula = MathTex(
            r"\text{Sorrel Count} = (w-1)(h-1) - 2(w+h)",
            font_size=30
        ).to_edge(DOWN)
        sorrel_formula.shift(0.0 * RIGHT + -0.46 * UP)  # layout: separation vector
        self.play(Write(sorrel_formula))
        self.wait(1.5)

        # Example: w=2, h=3
        example_text = Text("Example: w=2, h=3", font_size=24).to_corner(UL)
        self.play(Write(example_text))
        self.wait(0.5)

        calc_inside = MathTex("1 \\times 2 = 2", color=BLUE).next_to(interior_label, DOWN)
        calc_edge = MathTex("2 \\times 5 = 10", color=RED).next_to(edge_label, DOWN)
        self.play(Write(calc_inside), Write(calc_edge))
        self.wait(1)

        result = MathTex(r"2 - 10 = -8", font_size=30).next_to(sorrel_formula, DOWN)
        self.play(Write(result))
        self.wait(1.5)

        # Final rule
        rule = Text("Rule: Small rectangles have negative sorrel counts.", font_size=24).to_edge(DOWN)
        self.play(ReplacementTransform(sorrel_formula, rule))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(grid), FadeOut(generic_rect), FadeOut(interior_label),
                  FadeOut(edge_label), FadeOut(calc_inside), FadeOut(calc_edge), FadeOut(result),
                  FadeOut(example_text), FadeOut(rule))
