from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Characteristic Equation", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        # Generic 2x2 matrix A
        A = Matrix([['a', 'b'], ['c', 'd']])
        A.to_corner(UL)
        A_label = Text('A =', font_size=24).next_to(A, LEFT)
        self.play(Write(A_label), Write(A))
        self.wait(1)

        # Identity matrix I
        I = Matrix([["1", "0"], ["0", "1"]], bracket_style=BRACKET)
        I.next_to(A, DOWN, buff=1.5)
        I_label = Text("I =", font_size=24).next_to(I, LEFT)
        self.play(Write(I_label), Write(I))
        self.wait(1)

        # λI
        lambda_str = MathTex(r"\lambda", font_size=30)
        lambda_I = Matrix([["\\lambda", "0"], ["0", "\\lambda"]], bracket_style=BRACKET)
        lambda_I.next_to(I, DOWN, buff=1.5)
        lambda_I_label = Text("\\lambda I =", font_size=24).next_to(lambda_I, LEFT)
        self.play(Write(lambda_I_label), Write(lambda_I))
        self.wait(1)

        # A - λI
        minus = MathTex("-", font_size=30)
        minus.next_to(A, RIGHT, buff=0.5)
        A_minus_lambda_I = Matrix([["a-\\lambda", "b"], ["c", "d-\\lambda"]], bracket_style=BRACKET)
        A_minus_lambda_I.next_to(minus, RIGHT, buff=0.5)
        self.play(Write(minus), Write(A_minus_lambda_I))
        self.wait(1.5)

        # det(A - λI) = 0
        det = MathTex(r"\det", font_size=30)
        det.next_to(A_minus_lambda_I, LEFT, buff=0.2)
        equals_zero = MathTex("= 0", font_size=30)
        equals_zero.next_to(A_minus_lambda_I, RIGHT, buff=0.2)
        self.play(Write(det), Write(equals_zero))
        self.wait(1.5)

        # Expand determinant
        det_expr = MathTex(r"(a - \lambda)(d - \lambda) - bc", font_size=30)
        det_expr.next_to(A_minus_lambda_I, DOWN, buff=1.5)
        self.play(Write(det_expr))
        self.wait(1.5)

        # Expand and collect terms
        expanded = MathTex(r"\lambda^2 - (a + d)\lambda + ad - bc", font_size=30)
        expanded.next_to(det_expr, DOWN, buff=0.5)
        self.play(Transform(det_expr, expanded))
        self.wait(1.5)

        # Highlight quadratic
        quadratic = MathTex(r"\lambda^2 - \text{tr}(A)\lambda + \det(A)", font_size=30)
        quadratic.next_to(expanded, DOWN, buff=0.5)
        self.play(Transform(expanded, quadratic))
        self.wait(1.5)

        # Roots are eigenvalues
        roots = Text("Roots are eigenvalues", font_size=24)
        roots.to_edge(DOWN)
        self.play(Write(roots))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(A), FadeOut(A_label),
                  FadeOut(I), FadeOut(I_label), FadeOut(lambda_I),
                  FadeOut(lambda_I_label), FadeOut(minus), FadeOut(A_minus_lambda_I),
                  FadeOut(det), FadeOut(equals_zero), FadeOut(det_expr),
                  FadeOut(expanded), FadeOut(roots))
        self.wait(0.5)
