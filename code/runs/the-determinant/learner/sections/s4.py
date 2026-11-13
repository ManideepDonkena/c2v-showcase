from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Computational Formula", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Matrix [[a, b], [c, d]]
        matrix = Matrix([["a", "b"], ["c", "d"]], 
                        element_to_mobject=Tex).scale(1.2)
        matrix.to_corner(UL)
        self.play(Write(matrix))
        self.wait(0.5)

        # Highlight ad and bc
        ad = SurroundingRectangle(matrix.get_entries()[0], color=YELLOW, buff=0.1)
        bc = SurroundingRectangle(matrix.get_entries()[3], color=GREEN, buff=0.1)
        self.play(Create(ad), Create(bc))
        self.wait(0.5)

        # Show ad growing and bc shrinking
        ad_text = MathTex("ad", color=YELLOW).next_to(ad, DOWN)
        bc_text = MathTex("bc", color=GREEN).next_to(bc, DOWN)
        self.play(Write(ad_text), Write(bc_text))
        self.wait(0.5)

        # Show final result: ad - bc
        result = MathTex("ad - bc").scale(1.2).to_edge(DOWN)
        self.play(Write(result))
        self.wait(0.5)

        # Example with numbers 1,2,3,4
        matrix_num = Matrix([[1, 2], [3, 4]], element_to_mobject=Tex).scale(1.2).move_to(ORIGIN)
        self.play(Transform(matrix, matrix_num))
        self.wait(0.5)

        ad_val = MathTex("1 \\cdot 4 = 4", color=YELLOW).next_to(result, UP)
        bc_val = MathTex("2 \\cdot 3 = 6", color=GREEN).next_to(ad_val, DOWN)
        diff = MathTex("4 - 6 = -2").next_to(bc_val, DOWN)

        bc_val.shift(0.0 * RIGHT + 0.49 * UP)  # layout: separation vector
        self.play(Write(ad_val), Write(bc_val))
        self.wait(0.5)
        
        # Scalar multiplication
        scalar_k = ValueTracker(1)
        k_matrix = always_redraw(
            lambda: Matrix([["k", "k"], 
                           ["1", "1"]], element_to_mobject=Tex).scale(1.2).to_corner(UL)
        )
        self.play(Transform(matrix, k_matrix))
        self.wait(0.5)

        # Show change in determinant
        det_k = MathTex("k(ad - bc)").next_to(result, DOWN, buff=0.5)
        self.play(Write(det_k))
        self.wait(1)

        # Transpose matrices
        self.play(FadeOut(k_matrix), FadeOut(det_k), FadeOut(ad_val), FadeOut(bc_val), FadeOut(diff))

        mat1 = Matrix([["a", "b"], ["c", "d"]], element_to_mobject=Tex).scale(1.2)
        mat2 = Matrix([["a", "c"], ["b", "d"]], element_to_mobject=Tex).scale(1.2).next_to(mat1, RIGHT, buff=1)

        self.play(Write(mat1), Write(mat2))
        self.wait(0.5)

        det1 = MathTex("ad - bc").next_to(mat1, DOWN)
        det2 = MathTex("ad - bc").next_to(mat2, DOWN)
        self.play(Write(det1), Write(det2))
        self.wait(1)

        # Zero case: a=0, b=1, c=1, d=0
        self.play(FadeOut(mat1), FadeOut(mat2), FadeOut(det1), FadeOut(det2))

        zero_matrix = Matrix([[0, 1], [1, 0]], element_to_mobject=Tex).scale(1.2)
        self.play(Write(zero_matrix))
        self.wait(0.5)

        zero_ad = MathTex("0 \\cdot 0 = 0", color=YELLOW).next_to(result, UP)
        zero_bc = MathTex("1 \\cdot 1 = 1", color=GREEN).next_to(zero_ad, DOWN)
        zero_diff = MathTex("0 - 1 = -1").next_to(zero_bc, DOWN)

        self.play(Write(zero_ad), Write(zero_bc))
        self.wait(0.5)
        self.play(Write(zero_diff))
        self.wait(1)

        # Counter-example: (A + B) ≠ A + B
        self.play(FadeOut(zero_matrix), FadeOut(zero_ad), FadeOut(zero_bc), FadeOut(zero_diff))

        A = Matrix([[1, 0], [0, 1]], element_to_mobject=Tex).scale(1.2)
        B = Matrix([[0, 1], [1, 0]], element_to_mobject=Tex).scale(1.2).next_to(A, RIGHT, buff=1)

        self.play(Write(A), Write(B))
        self.wait(0.5)

        A_plus_B = Matrix([[1, 1], [1, 1]], element_to_mobject=Tex).scale(1.2).next_to(A, DOWN, buff=1)
        self.play(Write(A_plus_B))
        self.wait(0.5)

        det_A = MathTex("1").next_to(A, DOWN)
        det_B = MathTex("1").next_to(B, DOWN)
        det_sum = MathTex("2").next_to(A_plus_B, DOWN, buff=0.5).shift(UP * 0.93)

        self.play(Write(det_A), Write(det_B), Write(det_sum))
        self.wait(1)

        # Upper triangular matrix
        self.play(FadeOut(A), FadeOut(B), FadeOut(A_plus_B), FadeOut(det_A), FadeOut(det_B), FadeOut(det_sum))

        upper_tri = Matrix([["a", 0], ["c", "d"]], element_to_mobject=Tex).scale(1.2)
        self.play(Write(upper_tri))
        self.wait(0.5)

        det_upper = MathTex("ad").next_to(upper_tri, DOWN)
        self.play(Write(det_upper))
        self.wait(1)

        # Final cleanup
        self.play(FadeOut(title), FadeOut(matrix), FadeOut(result), FadeOut(ad), FadeOut(bc), 
                  FadeOut(ad_text), FadeOut(bc_text), FadeOut(det_upper))
