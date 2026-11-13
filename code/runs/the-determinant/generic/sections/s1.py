from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Geometric Interpretation", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Unit square
        square = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        square.move_to(ORIGIN)
        
        # Basis vectors
        i_hat = Arrow(ORIGIN, RIGHT, color=YELLOW)
        j_hat = Arrow(ORIGIN, UP, color=YELLOW)
        
        # Labels for basis vectors
        i_label = MathTex("\\hat{i}", color=YELLOW).next_to(i_hat.get_end(), DOWN)
        j_label = MathTex("\\hat{j}", color=YELLOW).next_to(j_hat.get_end(), LEFT).shift(DOWN * 0.5)
        
        # Initial setup
        self.play(Create(square), run_time=0.5)
        self.play(Create(i_hat), Create(j_hat), Write(i_label), Write(j_label))
        self.wait(1)
        # Transformation matrix
        matrix = Matrix([[2, 1], [1, 2]])
        matrix.to_corner(UL)
        matrix_label = Text("Transformation Matrix", font_size=24).next_to(matrix, DOWN)
        matrix_label.shift(0.35 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(matrix), Write(matrix_label))
        self.wait(1)

        # Transform square to parallelogram
        new_square = Square(side_length=1, color=RED, fill_opacity=0.5)
        new_square.move_to(ORIGIN)
        
        # Apply transformation
        j_label.shift(0.0 * RIGHT + 1.12 * UP)  # layout: separation vector
        self.play(
            square.animate.apply_matrix([[2, 1], [1, 2]]),
            i_hat.animate.apply_matrix([[2, 1], [1, 2]]),
            j_hat.animate.apply_matrix([[2, 1], [1, 2]]),
            i_label.animate.apply_matrix([[2, 1], [1, 2]]),
            j_label.animate.apply_matrix([[2, 1], [1, 2]]),
            run_time=2
        )
        
        # Show area calculation
        area_text = MathTex("\\text{Area} = 3", font_size=40).to_edge(DOWN)
        self.play(Write(area_text))
        self.wait(1.5)

        # Explanation text
        explanation = Text("Determinant = 3", font_size=24).next_to(area_text, UP)
        self.play(Write(explanation))
        self.wait(1.5)

        # Fade out everything except title and area
        self.play(
            FadeOut(square),
            FadeOut(i_hat),
            FadeOut(j_hat),
            FadeOut(i_label),
            FadeOut(j_label),
            FadeOut(matrix),
            FadeOut(matrix_label),
            FadeOut(explanation)
        )
        
        # Final area display
        final_area = MathTex("\\det(A) = 3", font_size=40).to_edge(DOWN)
        self.play(Write(final_area))
        self.wait(2)

        self.play(FadeOut(final_area), FadeOut(title))
