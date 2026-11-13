from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Computational Formula", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Matrix setup
        matrix = Matrix([[1, 2], [3, 4]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        matrix.scale(0.8).to_corner(UL)
        self.play(Write(matrix))
        self.wait(0.5)

        # Highlight ad and bc
        a = matrix.get_entries()[0]
        b = matrix.get_entries()[1]
        c = matrix.get_entries()[2]
        d = matrix.get_entries()[3]

        ad_highlight = SurroundingRectangle(matrix.get_entries()[0], color=YELLOW, buff=0.1)
        bc_highlight = SurroundingRectangle(matrix.get_entries()[3], color=GREEN, buff=0.1)

        self.play(Create(ad_highlight), Create(bc_highlight))
        self.wait(0.5)

        # Show ad - bc formula
        formula = MathTex("ad - bc", font_size=36).next_to(matrix, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(0.5)

        # Show parallelogram area
        unit_square = Square(side_length=1, color=BLUE, fill_opacity=0.2)
        v1 = Arrow(ORIGIN, RIGHT * 1 + UP * 2, color=YELLOW)
        v2 = Arrow(ORIGIN, RIGHT * 3 + UP * 4, color=GREEN)
        parallelogram = Polygon(ORIGIN, v1.get_end(), v1.get_end() + v2.get_end(), v2.get_end(), color=PURPLE, fill_opacity=0.3)

        self.play(FadeOut(ad_highlight), FadeOut(bc_highlight))
        v2.shift(0.0 * RIGHT + -0.95 * UP)  # layout: separation vector
        self.play(Write(v1), Write(v2))
        self.wait(0.5)
        parallelogram.shift(0.0 * RIGHT + -2.73 * UP)  # layout: separation vector
        self.play(Write(parallelogram))
        self.wait(0.5)

        # Show area = |det| = 2
        area_text = MathTex("Area = |ad - bc| = |1 \\cdot 4 - 2 \\cdot 3| = |-2| = 2", font_size=24).next_to(parallelogram, DOWN, buff=0.5)
        self.play(Write(area_text))
        self.wait(1)

        # Show two transformations
        matrix_A = Matrix([[2, 0], [0, 1]], bracket_h_buff=0.2, bracket_v_buff=0.2).to_corner(UR)
        matrix_B = Matrix([[1, 0], [0, 2]], bracket_h_buff=0.2, bracket_v_buff=0.2).next_to(matrix_A, LEFT)

        self.play(Transform(matrix, matrix_A))
        self.wait(0.5)
        self.play(Transform(matrix, matrix_B))
        self.wait(0.5)

        # Show orthogonal matrix (rotation)
        rot_matrix = Matrix([[0, -1], [1, 0]], bracket_h_buff=0.2, bracket_v_buff=0.2).to_corner(DR)
        self.play(Transform(matrix, rot_matrix))
        self.wait(0.5)

        # Show zero determinant case
        zero_matrix = Matrix([[1, 2], [2, 4]], bracket_h_buff=0.2, bracket_v_buff=0.2).to_corner(DL)
        self.play(Transform(matrix, zero_matrix))
        self.wait(0.5)

        # Show transpose identity
        transposed = Matrix([[1, 3], [2, 4]], bracket_h_buff=0.2, bracket_v_buff=0.2).to_edge(DOWN)
        self.play(Transform(matrix, transposed))
        self.wait(0.5)

        # Show negative determinant
        neg_matrix = Matrix([[0, 1], [1, 0]], bracket_h_buff=0.2, bracket_v_buff=0.2).to_corner(UL)
        self.play(Transform(matrix, neg_matrix))
        self.wait(0.5)

        # Show counter-example
        A = Matrix([[1, 0], [0, 1]])
        B = Matrix([[0, 1], [1, 0]])
        sum_matrix = Matrix([[1, 1], [1, 1]])

        self.play(Transform(matrix, A))
        self.wait(0.5)
        self.play(Transform(matrix, B))
        self.wait(0.5)
        self.play(Transform(matrix, sum_matrix))
        self.wait(0.5)

        # Show upper triangular
        tri_matrix = Matrix([[2, 1], [0, 3]], bracket_h_buff=0.2, bracket_v_buff=0.2).to_corner(UR)
        self.play(Transform(matrix, tri_matrix))
        self.wait(0.5)

        # Show orientation flip
        flip_matrix = Matrix([[0, -1], [1, 0]], bracket_h_buff=0.2, bracket_v_buff=0.2).to_corner(DR)
        self.play(Transform(matrix, flip_matrix))
        self.wait(0.5)

        self.play(FadeOut(title), FadeOut(matrix), FadeOut(v1), FadeOut(v2), FadeOut(parallelogram), FadeOut(area_text), FadeOut(formula))
        self.wait(0.5)
