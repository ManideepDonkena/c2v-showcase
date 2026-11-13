from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Vell Formula", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid with labels
        grid = Matrix([["a", "b"], ["c", "d"]], bracket_h_buff=0.4, bracket_v_buff=0.4)
        grid.to_corner(UL)
        grid_label = Text("Grid: ", font_size=24).next_to(grid, LEFT)
        grid_group = VGroup(grid_label, grid).arrange(RIGHT, buff=0.5)
        self.play(Write(grid_group))
        self.wait(1)

        # Highlight a and d
        a = grid.get_entries()[0]
        d = grid.get_entries()[3]
        highlight_a = SurroundingRectangle(a, color=YELLOW, buff=0.1)
        highlight_d = SurroundingRectangle(d, color=YELLOW, buff=0.1)
        self.play(Create(highlight_a), Create(highlight_d))
        self.wait(0.5)

        # Cross out b and c
        b = grid.get_entries()[1]
        c = grid.get_entries()[2]
        cross_b = Cross(b, color=RED)
        cross_c = Cross(c, color=RED)
        self.play(Create(cross_b), Create(cross_c))
        self.wait(0.5)

        # Show formula
        formula = MathTex("a \\times d - b - c", font_size=40).next_to(grid, RIGHT, buff=1)
        self.play(Write(formula))
        self.wait(1.5)

        # Demonstrate subtracting zero
        demo_text = Text("Subtracting zero leaves number unchanged:", font_size=24).to_edge(DOWN)
        self.play(Write(demo_text))
        self.wait(0.5)
        demo_eq = MathTex("5 - 0 = 5", font_size=30).next_to(demo_text, DOWN)
        self.play(Write(demo_eq))
        self.wait(1)
        self.play(FadeOut(demo_text), FadeOut(demo_eq))

        # Show incorrect multiplication
        wrong_grid = Matrix([["a", "b"], ["c", "d"]], bracket_h_buff=0.4, bracket_v_buff=0.4).to_corner(DR)
        wrong_label = Text("Wrong: Multiply all", font_size=24).next_to(wrong_grid, LEFT)
        # Adjust position to avoid overlap
        wrong_label.shift(UP * 0.45)
        wrong_group = VGroup(wrong_label, wrong_grid).arrange(RIGHT, buff=0.5)
        self.play(Write(wrong_group))
        x_wrong = Cross(wrong_grid, color=RED)
        self.play(Create(x_wrong))
        self.wait(1)

        # Fade out
        self.play(FadeOut(grid_group), FadeOut(formula), FadeOut(highlight_a), FadeOut(highlight_d),
                  FadeOut(cross_b), FadeOut(cross_c), FadeOut(wrong_group), FadeOut(x_wrong))

        # Show final equation with result = 0
        final_eq = MathTex("a \\times d - b - c = 0", font_size=40).to_edge(UP)
        # Adjust position to avoid overlap
        final_eq.shift(DOWN * 0.45)
        self.play(Write(final_eq))
        self.wait(1)

        # Rearrange equation
        rearranged = MathTex("a \\times d = b + c", font_size=40).next_to(final_eq, DOWN, buff=0.5)
        self.play(Write(rearranged))
        self.wait(2)

        # Fade out
        self.play(FadeOut(final_eq), FadeOut(rearranged), FadeOut(title))
        self.wait(0.5)
