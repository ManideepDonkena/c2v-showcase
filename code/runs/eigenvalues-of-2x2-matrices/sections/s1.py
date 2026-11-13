from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Concept of Invariance", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Axes
        axes = Axes(x_range=[-4, 4, 1], y_range=[-2, 2, 1], 
                    axis_config={"stroke_color": WHITE}, 
                    x_length=8, y_length=4)
        axes.to_edge(DOWN)
        self.play(Create(axes))
        self.wait(0.5)

        # Original vector v
        v = Vector([1, 1], color=YELLOW)
        v_label = MathTex(r"\vec{v}", font_size=24).next_to(v.get_end(), UR, buff=0.1)
        self.play(Create(v), Write(v_label))
        self.wait(0.5)
        # Matrix M
        M = Matrix([['a', 'b'], ['c', 'd']])
        M.to_edge(UP).shift(DOWN)
        M.shift(-0.19 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(M))
        self.wait(0.5)

        # Transformation
        A = [[2, 0], [0, 1]]  # Example transformation matrix
        Av = Vector([2, 1], color=GREEN)
        # Highlight invariance
        line = Line(axes.c2p(-3, -3), axes.c2p(3, 3), color=BLUE)
        line.shift(0.0 * RIGHT + 0.65 * UP)  # layout: separation vector
        self.play(Create(line))
        self.wait(0.5)

        # Fade out
        self.play(FadeOut(title), FadeOut(M), FadeOut(line))
        self.wait(0.5)
