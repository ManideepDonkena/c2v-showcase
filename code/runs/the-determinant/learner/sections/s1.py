from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Geometric Interpretation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Unit square
        square = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        square.move_to(ORIGIN)
        self.play(Create(square))
        self.wait(0.5)

        # Basis vectors i-hat and j-hat
        i_hat = Arrow(ORIGIN, RIGHT, color=YELLOW, buff=0)
        j_hat = Arrow(ORIGIN, UP, color=GREEN, buff=0)
        i_label = MathTex(r"\vec{i}", font_size=24).next_to(i_hat.get_end(), DOWN)
        j_label = MathTex(r"\vec{j}", font_size=24).next_to(j_hat.get_end(), LEFT)

        self.play(Create(i_hat), Create(j_hat), Write(i_label), Write(j_label))
        self.wait(1)

        # Transformation matrix A
        A = [[2, 1], [1, 2]]
        A_matrix = Matrix(A)
        A_matrix.to_corner(UL)
        self.play(Write(A_matrix))
        self.wait(0.5)

        # Transform square into parallelogram
        def apply_transformation(mob, matrix):
            return mob.animate.apply_matrix(matrix)

        self.play(
            apply_transformation(square, A),
            run_time=2
        )
        self.wait(1)

        # Show new vectors as sides of parallelogram
        v1 = Arrow(ORIGIN, RIGHT * 2 + UP, color=RED)
        v2 = Arrow(ORIGIN, UP * 2 + RIGHT, color=RED)
        v1_label = MathTex(r"\vec{a_1}", font_size=24).next_to(v1.get_end(), UR)
        v2_label = MathTex(r"\vec{a_2}", font_size=24).next_to(v2.get_end(), UL)

        self.play(Create(v1), Create(v2), Write(v1_label), Write(v2_label))
        self.wait(1)

        # Area of parallelogram
        area_text = MathTex(r"\text{Area} = 3", font_size=30).to_edge(DOWN)
        self.play(Write(area_text))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(square),
            FadeOut(i_hat), FadeOut(j_hat),
            FadeOut(i_label), FadeOut(j_label),
            FadeOut(v1), FadeOut(v2),
            FadeOut(v1_label), FadeOut(v2_label),
            FadeOut(A_matrix),
            FadeOut(area_text)
        )
        self.wait(0.5)

        # Sequential transformations
        B = [[1, 0], [0, 2]]
        A = [[2, 1], [1, 2]]

        square2 = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        square2.move_to(ORIGIN)

        self.play(Create(square2))
        self.wait(0.5)

        # Apply B first
        self.play(
            apply_transformation(square2, B),
            run_time=1.5
        )
        self.wait(0.5)

        # Apply A second
        self.play(
            apply_transformation(square2, A),
            run_time=1.5
        )
        self.wait(1)

        # Show that determinant of combined is det(A)*det(B)
        det_A = 3
        det_B = 2
        det_AB = det_A * det_B

        result_text = MathTex(r"\det(AB) = \det(A)\det(B) =", f"{det_AB}", font_size=30).to_edge(DOWN)
        self.play(Write(result_text))
        self.wait(2)

        # Orthogonal transformation (rotation)
        self.play(FadeOut(result_text))

        R = [[0, -1], [1, 0]]  # 90-degree rotation
        square3 = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        square3.move_to(ORIGIN)

        self.play(Create(square3))
        self.wait(0.5)

        self.play(
            apply_transformation(square3, R),
            run_time=2
        )
        self.wait(1)

        # Show that area is preserved
        preserved_text = MathTex(r"\det(R) = 1", font_size=30).to_edge(DOWN)
        self.play(Write(preserved_text))
        self.wait(1.5)

        # Final cleanup
        self.play(
            FadeOut(square3),
            FadeOut(preserved_text),
            FadeOut(title)
        )
        self.wait(0.5)
