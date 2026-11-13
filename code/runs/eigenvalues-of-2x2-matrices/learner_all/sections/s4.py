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
        
        # Matrix
        A = [[2, 1], [1, 2]]
        matrix_tex = MathTex("A =", "\\begin{bmatrix} 2 & 1 \\\\ 1 & 2 \\end{bmatrix}")
        matrix_tex.to_corner(UL)
        self.play(Write(matrix_tex))
        self.wait(0.5)

        # Apply transformation
        transformed_circle = always_redraw(
            lambda: Circle(radius=1, color=RED, fill_opacity=0.2).scale(2).rotate(PI/4)
        )
        
        self.play(Create(circle), run_time=1)
        self.wait(0.5)
        
        # Show ellipse
        ellipse = Ellipse(width=3.5, height=1.5, color=RED, fill_opacity=0.2)
        ellipse.move_to(ORIGIN)
        self.play(Transform(circle, ellipse), run_time=2)
        self.wait(1)

        # Axes of ellipse
        major_axis = Line(LEFT * 1.75, RIGHT * 1.75, color=YELLOW, stroke_width=6)
        minor_axis = Line(UP * 0.75, DOWN * 0.75, color=YELLOW, stroke_width=6)
        
        self.play(Create(major_axis), Create(minor_axis), run_time=1)
        self.wait(0.5)

        # Labels
        lambda1 = MathTex("\\lambda_1 = 3", font_size=24).next_to(major_axis, UP)
        lambda2 = MathTex("\\lambda_2 = 1", font_size=24).next_to(minor_axis, LEFT)
        
        self.play(Write(lambda1), Write(lambda2))
        self.wait(1.5)

        # Basis vectors
        i_hat = Vector(RIGHT, color=GREEN)
        j_hat = Vector(UP, color=GREEN)
        i_hat_label = MathTex("\\vec{i}", font_size=24).next_to(i_hat.get_end(), UR, buff=0.1)
        j_hat_label = MathTex("\\vec{j}", font_size=24).next_to(j_hat.get_end(), UL, buff=0.1)
        
        j_hat.shift(0.0 * RIGHT + 0.61 * UP)  # layout: separation vector
        j_hat_label.shift(-0.17 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(i_hat), Create(j_hat), Write(i_hat_label), Write(j_hat_label))
        self.wait(0.5)

        # Transformed vectors
        i_hat_transformed = Vector(RIGHT * 3, color=RED)
        j_hat_transformed = Vector(UP * 1, color=RED)
        
        self.play(Transform(i_hat, i_hat_transformed), Transform(j_hat, j_hat_transformed))
        self.wait(1.5)

        # Summary text
        summary = Text("Eigenvalues show stretching along invariant directions", font_size=24)
        summary.to_edge(DOWN)
        self.play(Write(summary))
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(matrix_tex),
            FadeOut(circle),
            FadeOut(major_axis),
            FadeOut(minor_axis),
            FadeOut(lambda1),
            FadeOut(lambda2),
            FadeOut(i_hat),
            FadeOut(j_hat),
            FadeOut(i_hat_label),
            FadeOut(j_hat_label),
            FadeOut(summary)
        )
