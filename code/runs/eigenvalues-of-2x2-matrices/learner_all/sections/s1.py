from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Concept of Invariance", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial vector v
        v = Vector([1, 1], color=YELLOW)
        v_label = MathTex(r"\vec{v}", font_size=24).next_to(v.get_end(), UR)
        self.play(Create(v), Write(v_label))
        self.wait(0.5)

        # Matrix A
        A = Matrix([[1, -1], [1, 1]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        A_label = MathTex(r"A =", font_size=24).next_to(A, LEFT)
        self.play(Write(A_label), Write(A))
        self.wait(0.5)

        # Transformation Av
        Av = Vector([0, 2], color=GREEN)
        Av_label = MathTex(r"A\vec{v}", font_size=24).next_to(Av.get_end(), UR)
        self.play(Transform(v, Av), Transform(v_label, Av_label))
        self.wait(0.5)
        # Highlight invariance
        line = Line(ORIGIN, v.get_end(), color=BLUE)
        line_label = MathTex(r"\text{same line}", font_size=24).next_to(line, UR)
        line_label.shift(0.0 * RIGHT + -0.33 * UP)  # layout: separation vector
        self.play(Create(line), Write(line_label))
        self.wait(1)

        # Fade out
        self.play(FadeOut(v), FadeOut(v_label), FadeOut(A), FadeOut(A_label), FadeOut(line), FadeOut(line_label))

        # Show A - λI
        A_minus_lambda_I = Matrix([["1-\\lambda", "-1"], ["1", "1-\\lambda"]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        A_minus_lambda_I_label = MathTex(r"A - \lambda I =", font_size=24).next_to(A_minus_lambda_I, LEFT)
        self.play(Write(A_minus_lambda_I_label), Write(A_minus_lambda_I))
        self.wait(1)

        # Determinant
        det_expr = MathTex(r"\det(A - \lambda I) = (1-\lambda)^2 + 1 = 0", font_size=24)
        det_expr.shift(0.0 * RIGHT + 1.07 * UP)  # layout: separation vector
        self.play(TransformMatchingTex(A_minus_lambda_I_label, det_expr))
        self.wait(1.5)

        # Quadratic form
        quadratic = MathTex(r"\lambda^2 - 2\lambda + 2 = 0", font_size=24).to_edge(DOWN)
        self.play(Write(quadratic))
        self.wait(1.5)

        # Trace and determinant
        trace_expr = MathTex(r"\text{trace}(A) = 2", font_size=24).next_to(quadratic, UP)
        det_expr = MathTex(r"\det(A) = 2", font_size=24).next_to(trace_expr, UP)
        self.play(Write(trace_expr), Write(det_expr))
        self.wait(1.5)

        # Vieta's formulas
        vieta = MathTex(r"x^2 - Sx + P = 0 \Rightarrow \text{sum of roots} = S", font_size=24).to_edge(DOWN)
        self.play(Transform(quadratic, vieta))
        self.wait(1.5)

        # Eigenvalues are roots
        eigenvals = MathTex(r"\lambda_1 + \lambda_2 = 2", font_size=24).next_to(vieta, UP)
        eigenvals.shift(0.0 * RIGHT + -0.36 * UP)  # layout: separation vector
        self.play(Write(eigenvals))
        self.wait(1.5)

        # Product of roots
        product = MathTex(r"\lambda_1 \cdot \lambda_2 = 2", font_size=24).next_to(eigenvals, UP)
        self.play(Write(product))
        self.wait(1.5)

        # Diagonal matrix case
        diag_matrix = Matrix([[3, 0], [0, 5]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        diag_label = MathTex(r"\text{Eigenvalues: } 3, 5", font_size=24).next_to(diag_matrix, DOWN)
        self.play(Write(diag_matrix), Write(diag_label))
        self.wait(1.5)

        # Repeated root example
        repeated = MathTex(r"(1 - \lambda)^2 = 0 \Rightarrow \lambda = 1", font_size=24).to_edge(DOWN)
        self.play(Transform(quadratic, repeated))
        self.wait(1.5)

        # Generic matrix determinant
        generic = Matrix([["a", "b"], ["c", "d"]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        generic_label = MathTex(r"\det(A - \lambda I) =", font_size=24).next_to(generic, LEFT)
        self.play(Write(generic_label), Write(generic))
        self.wait(1)

        # Final quadratic
        final_quad = MathTex(r"\lambda^2 - (a+d)\lambda + (ad-bc) = 0", font_size=24).to_edge(DOWN)
        self.play(TransformMatchingTex(generic_label, final_quad))
        self.wait(1.5)

        # Trace again
        trace_again = MathTex(r"= \lambda^2 - \text{tr}(A)\lambda + \det(A) = 0", font_size=24).to_edge(DOWN)
        self.play(TransformMatchingTex(final_quad, trace_again))
        self.wait(1.5)

        # Zero determinant case
        zero_det = MathTex(r"\det(A) = 0 \Rightarrow \lambda^2 - \text{tr}(A)\lambda = 0", font_size=24).to_edge(DOWN)
        self.play(TransformMatchingTex(trace_again, zero_det))
        self.wait(1.5)

        # Factor
        factored = MathTex(r"\lambda(\lambda - \text{tr}(A)) = 0 \Rightarrow \lambda = 0", font_size=24).to_edge(DOWN)
        self.play(TransformMatchingTex(zero_det, factored))
        self.wait(1.5)

        # Imaginary eigenvalues
        imag = MathTex(r"\lambda^2 + 1 = 0 \Rightarrow \lambda = \pm i", font_size=24).to_edge(DOWN)
        self.play(TransformMatchingTex(factored, imag))
        self.wait(1.5)

        # Eigenvectors for distinct eigenvalues
        e1 = Vector([1, 0], color=PURPLE)
        e2 = Vector([1, 1], color=ORANGE)
        e1_label = MathTex(r"\vec{v}_1", font_size=24).next_to(e1.get_end(), UR)
        e2_label = MathTex(r"\vec{v}_2", font_size=24).next_to(e2.get_end(), UR)
        self.play(Create(e1), Create(e2), Write(e1_label), Write(e2_label))
        self.wait(1.5)

        # Linear independence
        linear_indep = MathTex(r"\text{Linearly independent}", font_size=24).to_edge(DOWN)
        self.play(TransformMatchingTex(imag, linear_indep))
        self.wait(1.5)

        # Orthogonality note
        ortho_note = MathTex(r"\text{Only guaranteed orthogonal for symmetric matrices}", font_size=24).to_edge(DOWN)
        self.play(TransformMatchingTex(linear_indep, ortho_note))
        self.wait(1.5)

        # Inverse eigenvalue
        inverse = MathTex(r"A^{-1}\vec{v} = \frac{1}{\lambda}\vec{v}", font_size=24).to_edge(DOWN)
        self.play(TransformMatchingTex(ortho_note, inverse))
        self.wait(1.5)

        # Scaling example
        scale_example = MathTex(r"A\vec{v} = 3\vec{v} \Rightarrow \lambda = 3", font_size=24).to_edge(DOWN)
        self.play(TransformMatchingTex(inverse, scale_example))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(title), FadeOut(scale_example), FadeOut(e1), FadeOut(e2), FadeOut(e1_label), FadeOut(e2_label))
