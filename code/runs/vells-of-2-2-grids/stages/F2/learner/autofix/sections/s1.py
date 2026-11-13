from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Vell Formula", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid with labels
        grid = Matrix([[ "a", "b" ], [ "c", "d" ]], bracket_h_buff=0.4, bracket_v_buff=0.4)
        grid.to_edge(LEFT).shift(DOWN * 0.5)
        self.play(Write(grid))
        self.wait(0.5)

        # Highlight a and d with arrow
        a = grid.get_entries()[0]
        d = grid.get_entries()[3]
        arrow = Arrow(start=a.get_center() + LEFT * 0.2 + UP * 0.2,
                      end=d.get_center() + RIGHT * 0.2 + DOWN * 0.2,
                      color=YELLOW, buff=0.1)
        self.play(Create(arrow))
        self.wait(0.5)

        # Cross out b and c
        b = grid.get_entries()[1]
        c = grid.get_entries()[2]
        cross_b = Cross(b, color=RED)
        cross_c = Cross(c, color=RED)
        self.play(Create(cross_b), Create(cross_c))
        self.wait(0.5)

        # Equation
        equation = MathTex("a \\times d - b - c", font_size=40).next_to(grid, RIGHT, buff=1.5)
        self.play(Write(equation))
        self.wait(1)

        # Fade out arrow and crosses
        self.play(FadeOut(arrow), FadeOut(cross_b), FadeOut(cross_c))
        self.wait(0.5)

        # Example
        example = MathTex("\\text{Example: } \\begin{bmatrix} 2 & 1 \\\\ 3 & 4 \\end{bmatrix} \\Rightarrow 2 \\times 4 - 1 - 3 = 4", font_size=24)
        example.to_edge(DOWN)
        self.play(Write(example))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(grid), FadeOut(equation), FadeOut(example))
        self.wait(0.5)
