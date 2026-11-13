from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Commutativity and Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Left scene: 3 ⊕ 5
        left_expr = MathTex("3 \\oplus 5", font_size=40)
        left_expr.shift(2 * LEFT + 1.5 * UP)
        self.play(Write(left_expr))
        self.wait(1)

        # Show transformation to 3 + 5 + 15
        left_result = MathTex("3 + 5 + 3 \\times 5", font_size=40)
        left_result.shift(2 * LEFT + 0.5 * UP)
        self.play(Transform(left_expr, left_result))
        self.wait(1)

        # Show final result
        left_final = MathTex("= 3 + 5 + 15 = 23", font_size=40)
        left_final.shift(2 * LEFT - 0.5 * UP)
        self.play(Transform(left_expr, left_final))
        self.wait(1.5)

        # Right scene: 5 ⊕ 3
        right_expr = MathTex("5 \\oplus 3", font_size=40)
        right_expr.shift(2 * RIGHT + 1.5 * UP)
        self.play(Write(right_expr))
        self.wait(1)

        # Show transformation to 5 + 3 + 15
        right_result = MathTex("5 + 3 + 5 \\times 3", font_size=40)
        right_result.shift(2 * RIGHT + 0.5 * UP)
        self.play(Transform(right_expr, right_result))
        self.wait(1)

        # Show final result
        right_final = MathTex("= 5 + 3 + 15 = 23", font_size=40)
        right_final.shift(2 * RIGHT - 0.5 * UP)
        self.play(Transform(right_expr, right_final))
        self.wait(1.5)

        # Fade out left and right expressions
        self.play(FadeOut(left_expr), FadeOut(right_expr))

        # Show commutativity text
        commutative = Text("Commutativity", font_size=24).to_edge(UP)
        self.play(ReplacementTransform(title, commutative))
        self.wait(0.5)

        commutative_text = Text("a ⊕ b = b ⊕ a", font_size=30).move_to(ORIGIN)
        self.play(Write(commutative_text))
        self.wait(2)

        # Fade out commutativity text
        self.play(FadeOut(commutative_text))

        # Show identity element: 0 ⊕ 7
        zero_expr = MathTex("0 \\oplus 7", font_size=40)
        zero_expr.shift(1.5 * UP)
        self.play(Write(zero_expr))
        self.wait(1)

        # Transform to 0 + 7 + 0*7 = 7
        zero_result = MathTex("0 + 7 + 0 \\times 7", font_size=40)
        zero_result.shift(0.5 * UP)
        self.play(Transform(zero_expr, zero_result))
        self.wait(1)

        # Show final result
        zero_final = MathTex("= 0 + 7 + 0 = 7", font_size=40)
        zero_final.shift(-0.5 * UP)
        self.play(Transform(zero_expr, zero_final))
        self.wait(2)

        # Fade out zero expression
        self.play(FadeOut(zero_expr))

        # Show identity text
        identity = Text("Identity Element", font_size=24).to_edge(UP)
        identity.shift(0.0 * RIGHT + 0.48 * UP)  # layout: separation vector
        self.play(Write(identity))
        self.wait(0.5)

        identity_text = Text("0 ⊕ b = b", font_size=30).move_to(ORIGIN)
        self.play(Write(identity_text))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(identity), FadeOut(identity_text))
        self.wait(0.5)
