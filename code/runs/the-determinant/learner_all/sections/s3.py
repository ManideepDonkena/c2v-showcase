from manim import *

class S3(Scene):
    def construct(self):
        title = Text("Singularity and Collapse", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show matrix with specific values
        matrix = Matrix([[1, 2], [3, 4]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        matrix.to_corner(UL)
        self.play(Write(matrix))
        self.wait(0.5)

        # Show ad - bc formula
        formula = MathTex("ad - bc", font_size=36).next_to(matrix, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(0.5)

        # Show calculation: 1*4 - 2*3 = -2
        calc = MathTex("1 \\cdot 4 - 2 \\cdot 3 = 4 - 6 = -2", font_size=24).next_to(formula, DOWN)
        self.play(Write(calc))
        self.wait(1)

        # Show unit square and transformation
        square = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        square.move_to(ORIGIN)
        self.play(Create(square))
        self.wait(0.5)

        # Transform with matrix [1,2; 3,4]
        transform = [[1, 2], [3, 4]]
        transformed_square = square.copy().apply_matrix(transform)
        self.play(Transform(square, transformed_square))
        self.wait(1)

        # Show area scaling factor
        area_label = MathTex("Area = -2", font_size=24).next_to(square, DOWN)
        self.play(Write(area_label))
        self.wait(1.5)

        # Show two parallel lines (no solution) and one line with infinite solutions
        line1 = Line([-3, 1, 0], [3, 1, 0], color=YELLOW)
        line2 = Line([-3, 2, 0], [3, 2, 0], color=YELLOW)
        self.play(Create(line1), Create(line2))
        self.wait(0.5)

        # Show one line with all points valid solution
        line3 = Line([-3, 0, 0], [3, 0, 0], color=GREEN)
        self.play(Transform(line1, line3))
        self.wait(1)

        # Show basis vectors becoming collinear
        v1 = Arrow(ORIGIN, [1, 0, 0], color=RED)
        v2 = Arrow(ORIGIN, [1, 0, 0], color=GREEN)
        self.play(Create(v1), Create(v2))
        self.wait(0.5)

        # Collapse to zero area
        self.play(Transform(v2, Arrow(ORIGIN, [0, 0, 0], color=GREEN)))
        self.wait(0.5)

        # Show determinant = 0 label
        det_zero = MathTex("\\det(A) = 0", font_size=36).to_edge(DOWN)
        self.play(Write(det_zero))
        self.wait(1.5)

        # Show transpose matrices
        A = Matrix([[2, 1], [1, 2]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        At = Matrix([[2, 1], [1, 2]], bracket_h_buff=0.2, bracket_v_buff=0.2).next_to(A, RIGHT, buff=1)
        self.play(Write(A), Write(At))
        self.wait(0.5)

        # Show same determinant
        det_A = MathTex("\\det(A) = 3", font_size=24).next_to(A, DOWN)
        det_At = MathTex("\\det(A^T) = 3", font_size=24).next_to(At, DOWN)
        self.play(Write(det_A), Write(det_At))
        self.wait(1.5)

        # Show negative determinant example
        B = Matrix([[0, 1], [1, 0]], bracket_h_buff=0.2, bracket_v_buff=0.2).to_corner(UR)
        self.play(Transform(A, B))
        self.wait(0.5)

        det_B = MathTex("\\det(B) = -1", font_size=24).next_to(B, DOWN)
        self.play(Write(det_B))
        self.wait(1.5)

        # Show counter-example: (A + B) ≠ A + B
        C = Matrix([[1, 0], [0, 1]], bracket_h_buff=0.2, bracket_v_buff=0.2).to_corner(DL)
        D = Matrix([[1, 0], [0, 1]], bracket_h_buff=0.2, bracket_v_buff=0.2).next_to(C, RIGHT, buff=1)
        self.play(Write(C), Write(D))
        self.wait(0.5)

        # Show sum of determinants vs determinant of sum
        det_sum = MathTex("\\det(A) + \\det(B) = 3 + 3 = 6", font_size=24).next_to(C, DOWN)
        self.play(Write(det_sum))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(VGroup(title, matrix, formula, calc, square, line1, line2, line3, v1, v2, det_zero, A, At, det_A, det_At, B, det_B, C, D, det_sum)))
        self.wait(0.5)
