from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Scalar Multiplication", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Vector V
        V = Vector([2, 1], color=BLACK)
        v_label = MathTex("\\vec{v}", font_size=24).next_to(V.get_end(), UR)
        self.play(Create(V), Write(v_label))
        self.wait(1)

        # Slider k
        slider = NumberLine(x_range=[-2, 2, 1], include_numbers=True, length=4)
        slider.next_to(V.get_start(), DOWN, buff=0.5)
        k_label = Text("k", font_size=24).next_to(slider, UP)
        self.play(Create(slider), Write(k_label))
        self.wait(0.5)

        # Animate k from 1 to 2
        k_tracker = ValueTracker(1)
        V_copy = always_redraw(lambda: Vector([2*k_tracker.get_value(), k_tracker.get_value()], color=BLACK))
        self.play(k_tracker.animate.set_value(2), run_time=1.5)
        self.wait(0.5)

        # Animate k to -1
        self.play(k_tracker.animate.set_value(-1), run_time=1.5)
        self.wait(0.5)

        # Text: scalar changes magnitude and direction
        text1 = Text("Multiplying a vector by a scalar changes its magnitude.", font_size=24).to_edge(DOWN)
        self.play(Write(text1))
        self.wait(1.5)
        self.play(FadeOut(text1))

        text2 = Text("If the scalar is positive, direction remains the same.", font_size=24).to_edge(DOWN)
        self.play(Write(text2))
        self.wait(1.5)
        self.play(FadeOut(text2))

        text3 = Text("If negative, vector points in opposite direction.", font_size=24).to_edge(DOWN)
        self.play(Write(text3))
        self.wait(1.5)
        self.play(FadeOut(text3))

        # Two perpendicular vectors
        v1 = Vector([2, 0], color=BLUE)
        v2 = Vector([0, 2], color=RED)
        v1_label = MathTex("\\vec{v_1}", font_size=24).next_to(v1.get_end(), UR)
        v2_label = MathTex("\\vec{v_2}", font_size=24).next_to(v2.get_end(), UR)
        v1.shift(0.24 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(v1), Create(v2), Write(v1_label), Write(v2_label))
        self.wait(0.5)

        # Right angle symbol
        right_angle = Square(side_length=0.3, color=WHITE).rotate(45 * DEGREES).move_to(v1.get_start())
        right_angle.shift(0.22 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(right_angle))
        self.wait(0.5)

        text4 = Text("When the angle between them is exactly 90 degrees, they are perpendicular.", font_size=24).to_edge(DOWN)
        self.play(Write(text4))
        self.wait(2)
        self.play(FadeOut(text4))

        # Rotate vectors to overlap
        self.play(Rotate(v1, angle=PI/2), Rotate(v2, angle=PI/2), run_time=1.5)
        self.wait(0.5)

        text5 = Text("When the angle is 0 or 180 degrees, they are parallel.", font_size=24).to_edge(DOWN)
        self.play(Write(text5))
        self.wait(2)
        self.play(FadeOut(text5))

        # Matrix multiplication
        A = Matrix([[1, 2], [3, 4]], v_buff=0.4, h_buff=0.8)
        B = Matrix([[5, 6], [7, 8]], v_buff=0.4, h_buff=0.8)
        A.next_to(LEFT * 3, DOWN)
        B.next_to(RIGHT * 3, DOWN)

        self.play(Write(A), Write(B))
        self.wait(1)

        # Highlight inner dimensions
        col_A = SurroundingRectangle(A.get_columns()[0], color=GREEN, fill_opacity=0.2)
        row_B = SurroundingRectangle(B.get_rows()[0], color=GREEN, fill_opacity=0.2)
        self.play(Create(col_A), Create(row_B))
        self.wait(1)

        text6 = Text("Matrix multiplication combines columns of A with rows of B.", font_size=24).to_edge(DOWN)
        self.play(Write(text6))
        self.wait(2)
        self.play(FadeOut(text6))

        # Matrix transformations
        grid = always_redraw(lambda: NumberPlane(x_range=[-3, 3], y_range=[-2, 2]))
        self.play(Create(grid))
        self.wait(0.5)

        basis_vectors = [Vector([1, 0]), Vector([0, 1])]
        self.play(Create(basis_vectors[0]), Create(basis_vectors[1]))
        basis_vectors[0].shift(UP * 0.24)
        basis_vectors[1].shift(UP * 0.24)
        self.wait(0.5)

        # Apply A then B
        A_matrix = [[2, 1], [1, 1]]
        B_matrix = [[1, 0], [0, 2]]

        def apply_transformation(v, M):
            return np.dot(M, v)

        v1_transformed = always_redraw(lambda: Vector(apply_transformation([1, 0], A_matrix), color=BLUE))
        v2_transformed = always_redraw(lambda: Vector(apply_transformation([0, 1], A_matrix), color=RED))

        self.play(Create(v1_transformed), Create(v2_transformed))
        self.wait(1)

        # Apply B then A
        v1_transformed_BA = always_redraw(lambda: Vector(apply_transformation(apply_transformation([1, 0], A_matrix), B_matrix), color=BLUE))
        v2_transformed_BA = always_redraw(lambda: Vector(apply_transformation(apply_transformation([0, 1], A_matrix), B_matrix), color=RED))

        self.play(Transform(v1_transformed, v1_transformed_BA), Transform(v2_transformed, v2_transformed_BA))
        self.wait(1.5)

        text7 = Text("Order matters in matrix multiplication.", font_size=24).to_edge(DOWN)
        self.play(Write(text7))
        self.wait(2)
        self.play(FadeOut(text7))

        # Cross product of collinear vectors
        v3 = Vector([1, 0], color=BLUE)
        v4 = Vector([-1, 0], color=RED)
        self.play(Create(v3), Create(v4))
        self.wait(0.5)

        cross_product = Vector([0, 0], color=YELLOW)
        self.play(Create(cross_product))
        self.wait(0.5)

        text8 = Text("When vectors are collinear, their cross product is zero.", font_size=24).to_edge(DOWN)
        self.play(Write(text8))
        self.wait(2)
        self.play(FadeOut(text8))

        # Collinear basis vectors
        v5 = Vector([1, 0], color=BLUE)
        v6 = Vector([2, 0], color=RED)
        self.play(Create(v5), Create(v6))
        self.wait(0.5)

        text9 = Text("Collinear vectors cannot span a plane.", font_size=24).to_edge(DOWN)
        self.play(Write(text9))
        self.wait(2)
        self.play(FadeOut(text9))

        # Singular matrix
        self.play(FadeOut(v5), FadeOut(v6))
        self.wait(0.5)

        # Show transformation collapsing to line
        self.play(grid.animate.scale(0.1))
        self.wait(0.5)

        text10 = Text("Singular matrix has determinant zero.", font_size=24).to_edge(DOWN)
        self.play(Write(text10))
        self.wait(2)
        self.play(FadeOut(text10))

        # Span of one vector
        v7 = Vector([1, 0], color=BLUE)
        self.play(Create(v7))
        self.wait(0.5)

        scalar_line = NumberLine(x_range=[-3, 3], include_numbers=True).next_to(v7.get_start(), DOWN)
        self.play(Create(scalar_line))
        self.wait(0.5)

        text11 = Text("Span of one vector is infinite line.", font_size=24).to_edge(DOWN)
        self.play(Write(text11))
        self.wait(2)
        self.play(FadeOut(text11))

        # Orthogonal eigenvectors
        v8 = Vector([1, 0], color=BLUE)
        v9 = Vector([0, 1], color=RED)
        self.play(Create(v8), Create(v9))
        self.wait(0.5)

        text12 = Text("For symmetric matrices, eigenvectors are orthogonal.", font_size=24).to_edge(DOWN)
        self.play(Write(text12))
        self.wait(2)
        self.play(FadeOut(text12))

        # Vector transpose
        v_vec = Matrix([[3], [4]], v_buff=0.4, h_buff=0.8)
        v_transpose = Matrix([[3, 4]], v_buff=0.4, h_buff=0.8)
        v_vec.next_to(LEFT * 3, DOWN)
        v_transpose.next_to(RIGHT * 3, DOWN)

        self.play(Write(v_vec), Write(v_transpose))
        self.wait(1)

        result = MathTex("3^2 + 4^2 = 9 + 16 = 25", font_size=24)
        result.to_edge(DOWN)
        self.play(Write(result))
        self.wait(2)
        self.play(FadeOut(result))

        text13 = Text("Length is found using Pythagorean theorem.", font_size=24).to_edge(DOWN)
        self.play(Write(text13))
        self.wait(2)
        self.play(FadeOut(text13))

        # Final cleanup
        self.play(FadeOut(title), FadeOut(V), FadeOut(v_label), FadeOut(slider), FadeOut(k_label), FadeOut(k_tracker),
                  FadeOut(v1), FadeOut(v2), FadeOut(v1_label), FadeOut(v2_label), FadeOut(right_angle),
                  FadeOut(A), FadeOut(B), FadeOut(col_A), FadeOut(row_B),
                  FadeOut(grid), FadeOut(v1_transformed), FadeOut(v2_transformed),
                  FadeOut(cross_product), FadeOut(v3), FadeOut(v4), FadeOut(v5), FadeOut(v6),
                  FadeOut(v7), FadeOut(scalar_line), FadeOut(v8), FadeOut(v9),
                  FadeOut(v_vec), FadeOut(v_transpose), FadeOut(result))
        self.wait(0.5)
