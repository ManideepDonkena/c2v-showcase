from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Vector Addition", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Vector A and B
        A = Arrow(start=[-3, 0, 0], end=[0, 2, 0], color=RED, buff=0)
        B = Arrow(start=[0, 2, 0], end=[3, 2, 0], color=BLUE, buff=0)
        C = Arrow(start=[-3, 0, 0], end=[3, 2, 0], color=GREEN, buff=0)

        A_label = MathTex("A").next_to(A, DOWN, buff=0.2)
        B_label = MathTex("B").next_to(B, RIGHT, buff=0.2)
        C_label = MathTex("A + B").next_to(C, UR, buff=0.2)

        self.play(Create(A), Write(A_label))
        self.wait(0.5)
        self.play(Create(B), Write(B_label))
        self.wait(1)
        self.play(Transform(B, Arrow(start=[-3, 2, 0], end=[0, 2, 0], color=BLUE, buff=0)))
        self.wait(0.5)
        self.play(Create(C), Write(C_label))
        self.wait(1)

        # Perpendicular vectors
        self.play(FadeOut(A_label), FadeOut(B_label), FadeOut(C_label))
        A_perp = Arrow(start=[-2, 0, 0], end=[0, 2, 0], color=RED, buff=0)
        B_perp = Arrow(start=[0, 2, 0], end=[2, 2, 0], color=BLUE, buff=0)
        square = Square(side_length=0.3, color=WHITE).move_to([0, 2, 0])
        self.play(Create(A_perp), Create(B_perp), Create(square))
        self.wait(1)

        # Text: perpendicular
        perp_text = Text("Perpendicular (orthogonal)", font_size=24).to_edge(DOWN)
        self.play(Write(perp_text))
        self.wait(1.5)
        self.play(FadeOut(perp_text))

        # Parallel vectors
        self.play(Transform(A_perp, Arrow(start=[-2, 0, 0], end=[2, 0, 0], color=RED, buff=0)),
                  Transform(B_perp, Arrow(start=[-2, 0, 0], end=[2, 0, 0], color=BLUE, buff=0)))
        self.wait(1)

        # Text: parallel
        para_text = Text("Parallel (same or opposite direction)", font_size=24).to_edge(DOWN)
        self.play(Write(para_text))
        self.wait(1.5)
        self.play(FadeOut(para_text))

        # Matrix multiplication
        self.play(FadeOut(A_perp), FadeOut(B_perp), FadeOut(square))
        A_mat = Matrix([[1, 2], [3, 4]], v_buff=0.5, h_buff=0.8).set_color(RED)
        B_mat = Matrix([[5, 6], [7, 8]], v_buff=0.5, h_buff=0.8).set_color(BLUE)
        A_mat.next_to([-3, 1, 0], RIGHT)
        B_mat.next_to([1, 1, 0], LEFT)

        self.play(Write(A_mat), Write(B_mat))
        self.wait(1)

        # Highlight inner dimensions
        col_A = SurroundingRectangle(A_mat.get_columns()[0], color=RED, fill_opacity=0.2)
        row_B = SurroundingRectangle(B_mat.get_rows()[0], color=BLUE, fill_opacity=0.2)
        self.play(Create(col_A), Create(row_B))
        self.wait(1.5)
        self.play(FadeOut(col_A), FadeOut(row_B))

        # Matrix multiplication result
        result_text = Text("Resulting matrix", font_size=24).next_to([3, 1, 0], RIGHT)
        self.play(Write(result_text))
        self.wait(1.5)
        self.play(FadeOut(A_mat), FadeOut(B_mat), FadeOut(result_text))

        # Matrix transformations
        grid = NumberPlane()
        self.play(Create(grid))
        self.wait(0.5)

        A_trans = Matrix([[2, 0], [0, 1]], v_buff=0.5, h_buff=0.8).set_color(RED)
        B_trans = Matrix([[1, 0], [0, 2]], v_buff=0.5, h_buff=0.8).set_color(BLUE)
        A_trans.next_to([-3, -1, 0], RIGHT)
        B_trans.next_to([1, -1, 0], LEFT)

        self.play(Write(A_trans), Write(B_trans))
        self.wait(1)

        # Apply transformations
        self.play(Transform(grid, grid.copy().apply_matrix([[2, 0], [0, 1]])))
        self.wait(0.5)
        self.play(Transform(grid, grid.copy().apply_matrix([[1, 0], [0, 2]])))
        self.wait(1)

        # Reverse order
        self.play(Transform(grid, grid.copy().apply_matrix([[1, 0], [0, 2]])))
        self.wait(0.5)
        self.play(Transform(grid, grid.copy().apply_matrix([[2, 0], [0, 1]])))
        self.wait(1)

        self.play(FadeOut(A_trans), FadeOut(B_trans), FadeOut(grid))

        # Cross product
        vec1 = Arrow(start=[-3, 0, 0], end=[3, 0, 0], color=RED)
        vec2 = Arrow(start=[-3, 0, 0], end=[3, 0, 0], color=BLUE)
        self.play(Create(vec1), Create(vec2))
        self.wait(1)

        cross_vec = Arrow(start=[-3, 0, 0], end=[-3, 0, 0], color=GREEN)
        self.play(Create(cross_vec))
        self.wait(0.5)
        self.play(Transform(cross_vec, Arrow(start=[-3, 0, 0], end=[-3, 0, 0], color=GREEN, buff=0)))
        self.wait(1)
        self.play(FadeOut(vec1), FadeOut(vec2), FadeOut(cross_vec))

        # Collinear vectors
        vec_a = Arrow(start=[-2, -1, 0], end=[2, 1, 0], color=RED)
        vec_b = Arrow(start=[-2, -1, 0], end=[2, 1, 0], color=BLUE)
        self.play(Create(vec_a), Create(vec_b))
        self.wait(1)

        # Show determinant = 0
        det_text = Text("Determinant = 0", font_size=24).to_edge(DOWN)
        self.play(Write(det_text))
        self.wait(1.5)
        self.play(FadeOut(det_text), FadeOut(vec_a), FadeOut(vec_b))

        # Eigenvalue = 0
        self.play(Create(NumberPlane()))
        self.wait(0.5)

        # Singular matrix
        self.play(Transform(grid, grid.copy().apply_matrix([[1, 0], [0, 0]])))
        self.wait(1)
        self.play(FadeOut(grid))

        # Span of one vector
        vec = Arrow(start=[0, 0, 0], end=[2, 0, 0], color=RED)
        self.play(Create(vec))
        self.wait(0.5)

        scalar_line = NumberLine(x_range=[-3, 3, 1], include_numbers=True).move_to([0, -2, 0])
        self.play(Create(scalar_line))
        self.wait(0.5)

        # Scalar sweep
        dot = Dot(color=RED).move_to([2, 0, 0])
        self.play(Write(dot))
        self.wait(0.5)
        self.play(MoveAlongPath(dot, scalar_line), run_time=2)
        self.wait(1)
        self.play(FadeOut(vec), FadeOut(scalar_line), FadeOut(dot))

        # Orthogonal eigenvectors
        vec_orth1 = Arrow(start=[-2, 0, 0], end=[0, 2, 0], color=RED)
        vec_orth2 = Arrow(start=[0, 2, 0], end=[2, 0, 0], color=BLUE)
        self.play(Create(vec_orth1), Create(vec_orth2))
        self.wait(1)

        ortho_text = Text("Orthogonal eigenvectors", font_size=24).to_edge(DOWN)
        self.play(Write(ortho_text))
        self.wait(1.5)
        self.play(FadeOut(ortho_text), FadeOut(vec_orth1), FadeOut(vec_orth2))

        # Vector transpose
        v = Matrix([[3], [4]], v_buff=0.5, h_buff=0.8).set_color(RED)
        v_T = Matrix([[3, 4]], v_buff=0.5, h_buff=0.8).set_color(BLUE)
        v.next_to([-3, -1, 0], RIGHT)
        v_T.next_to([1, -1, 0], LEFT)

        self.play(Write(v), Write(v_T))
        self.wait(1)

        # Multiply
        result = MathTex("3^2 + 4^2 = 9 + 16 = 25").next_to([0, -2, 0], DOWN)
        self.play(Write(result))
        self.wait(1.5)
        self.play(FadeOut(v), FadeOut(v_T), FadeOut(result))

        # Pythagorean theorem
        triangle = Polygon([-3, 0, 0], [0, 0, 0], [0, 4, 0], color=RED)
        triangle.shift(0.0 * RIGHT + -1.03 * UP)  # layout: separation vector
        self.play(Create(triangle))
        self.wait(1)

        pyth_text = Text("Length = √(3² + 4²) = 5", font_size=24).to_edge(DOWN)
        self.play(Write(pyth_text))
        self.wait(1.5)
        self.play(FadeOut(triangle), FadeOut(pyth_text))

        # Final cleanup
        self.play(FadeOut(title))
        self.wait(0.5)
