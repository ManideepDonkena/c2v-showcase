from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Geometric Interpretation", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Setup axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            axis_config={"color": WHITE},
            tips=False
        )
        axes.to_edge(DOWN)
        self.play(Create(axes))
        self.wait(0.5)

        # Unit circle
        circle = Circle(radius=1, color=BLUE, fill_opacity=0.3)
        circle.move_to(ORIGIN)
        self.play(Create(circle))
        self.wait(0.5)

        # Matrix A
        A = [[2, 0.5], [0.5, 1.5]]
        matrix_tex = MathTex("A =", "\\begin{bmatrix} 2 & 0.5 \\\\ 0.5 & 1.5 \\end{bmatrix}")
        matrix_tex.to_edge(UP).shift(DOWN * 0.5)
        matrix_tex.shift(0.0 * RIGHT + 0.85 * UP)  # layout: separation vector
        matrix_tex.shift(0.0 * RIGHT + -1.0 * UP)  # layout: separation vector
        self.play(Write(matrix_tex))
        self.wait(0.5)

        # Apply transformation
        transformed_circle = always_redraw(
            lambda: Circle(radius=1, color=RED, fill_opacity=0.3).scale(2).rotate(30 * DEGREES)
        )
        self.play(Transform(circle, transformed_circle), run_time=2)
        self.wait(1)

        # Ellipse axes
        major_axis = Line(LEFT * 2.5, RIGHT * 2.5, color=YELLOW, stroke_width=4)
        minor_axis = Line(UP * 1.2, DOWN * 1.2, color=PURPLE, stroke_width=4)

        # Labels for axes
        major_label = MathTex("\\lambda_1 = 2.5", font_size=24).next_to(major_axis, UP)
        minor_label = MathTex("\\lambda_2 = 1.0", font_size=24).next_to(minor_axis, LEFT)

        self.play(Create(major_axis), Create(minor_axis))
        self.play(Write(major_label), Write(minor_label))
        self.wait(1)

        # Basis vectors
        i_hat = Vector(RIGHT, color=GREEN)
        j_hat = Vector(UP, color=ORANGE)
        i_label = MathTex("\\vec{i}", font_size=24).next_to(i_hat.get_end(), RIGHT)
        j_label = MathTex("\\vec{j}", font_size=24).next_to(j_hat.get_end(), UP)

        self.play(Create(i_hat), Create(j_hat))
        self.play(Write(i_label), Write(j_label))
        self.wait(0.5)

        # Transformed basis vectors
        i_transformed = Vector(RIGHT * 2.5, color=GREEN)
        j_transformed = Vector(UP * 1.0, color=ORANGE)
        i_trans_label = MathTex("\\lambda_1 \\vec{v}_1", font_size=24).next_to(i_transformed.get_end(), RIGHT)
        j_trans_label = MathTex("\\lambda_2 \\vec{v}_2", font_size=24).next_to(j_transformed.get_end(), UP)

        self.play(Transform(i_hat, i_transformed), Transform(j_hat, j_transformed))
        self.play(Write(i_trans_label), Write(j_trans_label))
        self.wait(1.5)

        # Text explanation
        text1 = Text("Eigenvectors from different eigenvalues", font_size=24)
        text2 = Text("are always linearly independent", font_size=24)
        text3 = Text("but they are only guaranteed to be orthogonal", font_size=24)
        text4 = Text("if the matrix is symmetric.", font_size=24)

        explanation_group = VGroup(text1, text2, text3, text4).arrange(DOWN, aligned_edge=LEFT)
        explanation_group.to_corner(UP + LEFT)
        self.play(Write(explanation_group))
        self.wait(2.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(circle),
            FadeOut(major_axis),
            FadeOut(minor_axis),
            FadeOut(major_label),
            FadeOut(minor_label),
            FadeOut(i_hat),
            FadeOut(j_hat),
            FadeOut(i_label),
            FadeOut(j_label),
            FadeOut(i_trans_label),
            FadeOut(j_trans_label),
            FadeOut(matrix_tex),
            FadeOut(explanation_group)
        )
        self.wait(0.5)
