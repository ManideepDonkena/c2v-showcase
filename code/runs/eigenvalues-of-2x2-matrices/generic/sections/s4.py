from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Geometric Interpretation", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Unit circle
        circle = Circle(radius=1, color=BLUE, fill_opacity=0.2)
        circle.move_to(ORIGIN)
        self.play(Create(circle))
        self.wait(0.5)

        # Matrix
        matrix = Matrix([[2, 1], [1, 2]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        matrix.scale(0.8)
        matrix.to_corner(UL)
        self.play(Write(matrix))
        self.wait(0.5)

        # Transform circle into ellipse
        ellipse = Ellipse(width=3.5, height=1.5, color=RED, fill_opacity=0.2)
        ellipse.move_to(ORIGIN)
        self.play(Transform(circle, ellipse))
        self.wait(1)

        # Major and minor axes
        major_axis = Line(LEFT * 1.75, RIGHT * 1.75, color=YELLOW, stroke_width=3)
        minor_axis = Line(UP * 0.75, DOWN * 0.75, color=YELLOW, stroke_width=3)
        major_axis_label = MathTex("\\lambda_1 = 3", font_size=24).next_to(major_axis, UP)
        minor_axis_label = MathTex("\\lambda_2 = 1", font_size=24).next_to(minor_axis, LEFT)

        self.play(Create(major_axis), Create(minor_axis))
        self.play(Write(major_axis_label), Write(minor_axis_label))
        self.wait(1.5)

        # Basis vectors
        i_hat = Vector(RIGHT, color=GREEN)
        j_hat = Vector(UP, color=GREEN)
        i_hat_label = MathTex("\\vec{e}_1", font_size=20).next_to(i_hat.get_end(), UR, buff=0.1)
        j_hat_label = MathTex("\\vec{e}_2", font_size=20).next_to(j_hat.get_end(), UL, buff=0.1)

        j_hat.shift(0.49 * RIGHT + 0.61 * UP)  # layout: separation vector
        self.play(Create(i_hat), Create(j_hat))
        j_hat_label.shift(-0.17 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(i_hat_label), Write(j_hat_label))
        self.wait(0.5)

        # Transform basis vectors
        i_transformed = Vector(RIGHT * 3, color=RED)
        j_transformed = Vector(RIGHT * 1 + UP * 2, color=RED)
        i_transformed_label = MathTex("\\lambda_1 \\vec{e}_1", font_size=20).next_to(i_transformed.get_end(), UR, buff=0.1)
        j_transformed_label = MathTex("\\lambda_2 \\vec{e}_2", font_size=20).next_to(j_transformed.get_end(), UL, buff=0.1)

        self.play(Transform(i_hat, i_transformed), Transform(j_hat, j_transformed))
        self.play(Write(i_transformed_label), Write(j_transformed_label))
        self.wait(1.5)

        # Summary text
        summary = Text("Eigenvalues indicate scaling factors", font_size=24)
        summary.to_edge(DOWN)
        self.play(Write(summary))
        self.wait(1)

        self.play(FadeOut(title, matrix, circle, major_axis, minor_axis, 
                          major_axis_label, minor_axis_label, i_hat, j_hat,
                          i_hat_label, j_hat_label, i_transformed, j_transformed,
                          i_transformed_label, j_transformed_label, summary))
        self.wait(0.5)
