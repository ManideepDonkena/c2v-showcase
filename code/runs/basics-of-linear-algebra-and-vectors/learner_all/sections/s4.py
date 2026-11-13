from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Linear Combinations", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Basis vectors i and j
        i_vec = Arrow(start=ORIGIN, end=[2, 0, 0], color=RED, stroke_width=6)
        j_vec = Arrow(start=ORIGIN, end=[0, 2, 0], color=BLUE, stroke_width=6)
        i_label = MathTex("\\mathbf{i}", font_size=24).next_to(i_vec.get_end(), DOWN)
        j_label = MathTex("\\mathbf{j}", font_size=24).next_to(j_vec.get_end(), LEFT)

        self.play(Create(i_vec), Create(j_vec), Write(i_label), Write(j_label))
        self.wait(1)

        # Vector v = 2i + 3j
        v_vec = Arrow(start=ORIGIN, end=[2, 3, 0], color=GREEN, stroke_width=6)
        v_label = MathTex("\\mathbf{v} = 2\\mathbf{i} + 3\\mathbf{j}", font_size=24).next_to(v_vec.get_end(), UR)
        v_label.shift(0.0 * RIGHT + -0.3 * UP)  # layout: separation vector
        self.play(Create(v_vec), Write(v_label))
        self.wait(1.5)

        # Show perpendicular vectors
        perp_i = Arrow(start=ORIGIN, end=[1, 0, 0], color=RED, stroke_width=6)
        perp_j = Arrow(start=ORIGIN, end=[0, 1, 0], color=BLUE, stroke_width=6)
        square = Square(side_length=0.2, color=WHITE).move_to(ORIGIN)
        self.play(Transform(i_vec, perp_i), Transform(j_vec, perp_j), Create(square))
        self.wait(1)

        # Text: perpendicular
        perp_text = Text("Perpendicular", font_size=24).next_to(v_vec, DOWN)
        perp_text.shift(0.0 * RIGHT + -0.17 * UP)  # layout: separation vector
        perp_text.shift(0.0 * RIGHT + -0.36 * UP)  # layout: separation vector
        self.play(Write(perp_text))
        self.wait(1.5)

        # Rotate to parallel
        parallel_i = Arrow(start=ORIGIN, end=[1, 0, 0], color=RED, stroke_width=6)
        parallel_j = Arrow(start=ORIGIN, end=[1, 0, 0], color=BLUE, stroke_width=6)
        self.play(Transform(i_vec, parallel_i), Transform(j_vec, parallel_j), FadeOut(square))
        self.wait(1)

        # Text: parallel
        para_text = Text("Parallel", font_size=24).next_to(v_vec, DOWN)
        self.play(Write(para_text))
        self.wait(1.5)

        # Matrix multiplication
        A = [[2, 1], [1, 2]]
        B = [[1, 0], [0, 1]]

        matrix_A = Matrix(A, v_buff=0.4, h_buff=0.6).set_color(BLUE)
        matrix_B = Matrix(B, v_buff=0.4, h_buff=0.6).set_color(RED)

        A_label = Text("A", font_size=24).next_to(matrix_A, UP)
        B_label = Text("B", font_size=24).next_to(matrix_B, UP)

        self.play(FadeOut(perp_text), FadeOut(para_text))
        self.play(matrix_A.animate.to_edge(LEFT), matrix_B.animate.to_edge(RIGHT), Write(A_label), Write(B_label))
        self.wait(1.5)

        # Highlight inner dimensions
        col_A = matrix_A.get_columns()[0].set_color(YELLOW)
        row_B = matrix_B.get_rows()[0].set_color(YELLOW)
        self.play(Write(col_A), Write(row_B))
        self.wait(1.5)

        # Matrix multiplication effect
        self.play(FadeOut(col_A), FadeOut(row_B))

        # Transformations A then B vs B then A
        grid = VGroup(*[Line([x, y, 0], [x+1, y, 0]) for x in range(-2, 3) for y in range(-2, 3)])
        self.play(Create(grid))
        self.wait(0.5)

        # Apply A then B
        self.play(grid.animate.shift([1, 1, 0]).scale(1.5))
        self.wait(0.5)

        # Apply B then A
        self.play(grid.animate.shift([-1, -1, 0]).scale(0.7))
        self.wait(1)

        # Collinear vectors in 3D
        vec1 = Arrow(start=ORIGIN, end=[1, 0, 0], color=YELLOW)
        vec2 = Arrow(start=ORIGIN, end=[2, 0, 0], color=YELLOW)
        self.play(Transform(vec1, vec1), Transform(vec2, vec2))
        self.wait(0.5)

        cross_vec = Arrow(start=ORIGIN, end=[0, 0, 0], color=PURPLE)
        self.play(Create(cross_vec))
        self.wait(0.5)
        self.play(FadeOut(cross_vec))

        # Collinear basis vectors
        collinear_i = Arrow(start=ORIGIN, end=[1, 0, 0], color=RED)
        collinear_j = Arrow(start=ORIGIN, end=[2, 0, 0], color=BLUE)
        self.play(Transform(i_vec, collinear_i), Transform(j_vec, collinear_j))
        self.wait(1)

        # Show squashing
        self.play(i_vec.animate.shift([0, -1, 0]), j_vec.animate.shift([0, -1, 0]))
        self.wait(1)

        # Scalar sweep
        scalar_line = NumberLine(x_range=[-3, 3], include_numbers=True).to_edge(DOWN)
        point = Dot(scalar_line.n2p(-2), color=GREEN)
        self.play(Create(scalar_line))
        self.play(point.animate.move_to(scalar_line.n2p(3)), run_time=2)
        self.wait(1)

        # Orthogonal eigenvectors
        ortho_i = Arrow(start=ORIGIN, end=[1, 0, 0], color=RED)
        ortho_j = Arrow(start=ORIGIN, end=[0, 1, 0], color=BLUE)
        self.play(Transform(i_vec, ortho_i), Transform(j_vec, ortho_j))
        self.wait(1)

        # Vector transpose
        v_col = Matrix([[3], [4]], v_buff=0.4, h_buff=0.6).set_color(GREEN)
        v_row = Matrix([[3, 4]], v_buff=0.4, h_buff=0.6).set_color(GREEN)
        self.play(Write(v_col), Write(v_row))
        self.wait(1)

        # Multiply v^T * v
        result = MathTex("3^2 + 4^2 = 9 + 16 = 25", font_size=24)
        self.play(Write(result))
        self.wait(1.5)

        # Pythagorean triangle
        triangle = Polygon([0, 0, 0], [3, 0, 0], [3, 4, 0], color=YELLOW)
        self.play(Create(triangle))
        self.wait(1)

        # Final text
        final_text = Text("Length = 5", font_size=24).next_to(triangle, DOWN)
        self.play(Write(final_text))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(i_vec), FadeOut(j_vec), FadeOut(v_vec), FadeOut(v_label),
                  FadeOut(matrix_A), FadeOut(matrix_B), FadeOut(A_label), FadeOut(B_label),
                  FadeOut(grid), FadeOut(scalar_line), FadeOut(point), FadeOut(v_col), FadeOut(v_row),
                  FadeOut(result), FadeOut(triangle), FadeOut(final_text))
