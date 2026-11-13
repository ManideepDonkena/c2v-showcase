from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Geometric Interpretation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial unit square and basis vectors
        square = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        square.move_to(ORIGIN)
        i_hat = Arrow(ORIGIN, RIGHT, color=YELLOW, buff=0)
        j_hat = Arrow(ORIGIN, UP, color=YELLOW, buff=0)
        i_label = MathTex(r"\vec{i}", font_size=24).next_to(i_hat.get_end(), DOWN)
        j_label = MathTex(r"\vec{j}", font_size=24).next_to(j_hat.get_end(), LEFT)

        self.play(Create(square), Create(i_hat), Create(j_hat), Write(i_label), Write(j_label))
        self.wait(1)

        # Transformation to parallelogram
        matrix_A = [[1, 2], [3, 4]]
        transform = Matrix(matrix_A).scale(0.7).to_corner(UL)
        self.play(Write(transform))
        self.wait(0.5)

        # Apply transformation
        new_square = square.copy()
        new_square.shift(UP * 2 + RIGHT * 1)
        self.play(Transform(square, new_square), run_time=1.5)
        self.wait(0.5)

        # Show area of parallelogram
        area_label = MathTex(r"\text{Area} = -2", font_size=30).to_edge(DOWN)
        self.play(Write(area_label))
        self.wait(1)

        # Show that determinant equals area
        det_label = MathTex(r"\det(A) = ad - bc = (1)(4) - (2)(3) = -2", font_size=24).next_to(area_label, UP)
        self.play(Write(det_label))
        self.wait(1.5)

        # Show two sequential transformations
        matrix_B = [[2, 0], [0, 1]]
        matrix_A = [[1, 1], [0, 1]]
        B_matrix = Matrix(matrix_B).scale(0.6).to_corner(UR)
        A_matrix = Matrix(matrix_A).scale(0.6).next_to(B_matrix, DOWN)

        self.play(Write(B_matrix), Write(A_matrix))
        self.wait(1)

        # Show that det(AB) = det(A)*det(B)
        det_B = MathTex(r"\det(B) = 2", font_size=24).next_to(B_matrix, DOWN)
        det_A = MathTex(r"\det(A) = 1", font_size=24).next_to(A_matrix, DOWN)
        self.play(Write(det_B), Write(det_A))
        self.wait(1)

        # Show orthogonal matrix (rotation)
        rot_matrix = [[0, -1], [1, 0]]
        rot_label = MathTex(r"\text{Rotation: } \det(R) = 1", font_size=24).to_edge(DOWN).shift(UP*0.3)
        rot_label.shift(0.0 * RIGHT + 0.38 * UP)  # layout: separation vector
        rot_label.shift(0.0 * RIGHT + 0.19 * UP)  # layout: separation vector
        self.play(Write(rot_label))
        self.wait(1)

        # Show zero determinant case (identical vectors)
        vec1 = Arrow(ORIGIN, RIGHT, color=RED)
        vec2 = Arrow(ORIGIN, RIGHT, color=RED)
        zero_area = Polygon(ORIGIN, vec1.get_end(), vec2.get_end(), ORIGIN, color=RED, fill_opacity=0.3)
        self.play(Create(vec1), Create(vec2), Create(zero_area))
        self.wait(1)

        # Show lines with no solution vs infinite solutions
        line1 = Line([-5, 0, 0], [5, 0, 0], color=GREEN)
        line2 = Line([-5, 1, 0], [5, 1, 0], color=GREEN)
        self.play(Create(line1), Create(line2))
        self.wait(0.5)

        # Show transposed matrices
        mat1 = Matrix([[1, 2], [3, 4]]).scale(0.6).to_corner(DL)
        mat2 = Matrix([[1, 3], [2, 4]]).scale(0.6).next_to(mat1, DOWN)
        self.play(Write(mat1), Write(mat2))
        det1 = MathTex(r"\det = -2", font_size=24).next_to(mat1, RIGHT)
        det2 = MathTex(r"\det = -2", font_size=24).next_to(mat2, RIGHT)
        self.play(Write(det1), Write(det2))
        self.wait(1)

        # Show negative determinant
        neg_matrix = Matrix([[0, 1], [1, 0]]).scale(0.6).to_corner(DR)
        self.play(Write(neg_matrix))
        neg_det = MathTex(r"\det = -1", font_size=24).next_to(neg_matrix, DOWN)
        self.play(Write(neg_det))
        self.wait(1)

        # Show counter-example
        A = [[1, 0], [0, 1]]
        B = [[0, 1], [1, 0]]
        C = [[1, 1], [1, 1]]
        sum_matrix = Matrix(C).scale(0.6).to_edge(LEFT)
        self.play(Write(sum_matrix))
        self.wait(1)

        # Show upper triangular matrix
        tri_matrix = Matrix([[2, 1], [0, 3]]).scale(0.6).to_edge(RIGHT)
        self.play(Write(tri_matrix))
        det_tri = MathTex(r"\det = 6", font_size=24).next_to(tri_matrix, DOWN)
        self.play(Write(det_tri))
        self.wait(1)

        # Swap basis vectors
        swap_vec1 = Arrow(ORIGIN, UP, color=BLUE)
        swap_vec2 = Arrow(ORIGIN, RIGHT, color=BLUE)
        swapped_square = Polygon(ORIGIN, swap_vec1.get_end(), swap_vec2.get_end(), ORIGIN, color=BLUE, fill_opacity=0.5)
        self.play(Create(swap_vec1), Create(swap_vec2), Create(swapped_square))
        self.wait(1)

        # Final summary
        final_text = Text("Determinant measures area scaling and orientation", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(square), FadeOut(i_hat), FadeOut(j_hat), FadeOut(i_label), FadeOut(j_label),
                  FadeOut(transform), FadeOut(area_label), FadeOut(det_label), FadeOut(B_matrix), FadeOut(A_matrix),
                  FadeOut(det_B), FadeOut(det_A), FadeOut(rot_label), FadeOut(vec1), FadeOut(vec2), FadeOut(zero_area),
                  FadeOut(line1), FadeOut(line2), FadeOut(mat1), FadeOut(mat2), FadeOut(det1), FadeOut(det2),
                  FadeOut(neg_matrix), FadeOut(neg_det), FadeOut(sum_matrix), FadeOut(tri_matrix), FadeOut(det_tri),
                  FadeOut(swap_vec1), FadeOut(swap_vec2), FadeOut(swapped_square), FadeOut(final_text))
