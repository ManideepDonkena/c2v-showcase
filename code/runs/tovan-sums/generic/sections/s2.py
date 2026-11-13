from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Commutativity and Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Left scene: 0 ⊕ 7 becomes 7
        left_expr = MathTex("0 \\oplus 7", font_size=40)
        left_expr.shift(2 * LEFT + 1.5 * UP)
        self.play(Write(left_expr))
        self.wait(1)

        # Show the transformation step by step
        step1 = MathTex("= 0 + 7 + 0 \\times 7", font_size=40)
        step1.next_to(left_expr, DOWN, buff=0.5)
        self.play(Write(step1))
        self.wait(1)

        step2 = MathTex("= 0 + 7 + 0", font_size=40)
        step2.next_to(left_expr, DOWN, buff=0.5)
        self.play(Transform(step1, step2))
        self.wait(1)

        step3 = MathTex("= 7", font_size=40)
        step3.next_to(left_expr, DOWN, buff=0.5)
        self.play(Transform(step1, step3))
        self.wait(1.5)

        # Fade out left side
        self.play(FadeOut(left_expr), FadeOut(step1))

        # Right scene: 0 ⊕ 7 again, but with fading zero
        right_expr = MathTex("0 \\oplus 7", font_size=40)
        right_expr.shift(2 * RIGHT + 1.5 * UP)
        self.play(Write(right_expr))
        self.wait(1)

        # Show the same steps
        step1_right = MathTex("= 0 + 7 + 0 \\times 7", font_size=40)
        step1_right.next_to(right_expr, DOWN, buff=0.5)
        self.play(Write(step1_right))
        self.wait(1)

        # Fade out the zero term
        zero_term = MathTex("0 \\times 7", font_size=40).set_color(YELLOW)
        zero_term.next_to(step1_right, RIGHT, buff=0.2)
        self.play(Write(zero_term))
        self.wait(1)

        self.play(FadeOut(zero_term))

        step2_right = MathTex("= 0 + 7 + 0", font_size=40)
        step2_right.next_to(right_expr, DOWN, buff=0.5)
        self.play(Transform(step1_right, step2_right))
        self.wait(1)

        step3_right = MathTex("= 7", font_size=40)
        step3_right.next_to(right_expr, DOWN, buff=0.5)
        self.play(Transform(step1_right, step3_right))
        self.wait(1.5)

        # Fade out right side
        self.play(FadeOut(right_expr), FadeOut(step1_right))

        # Show commutativity: 3 ⊕ 5 = 5 ⊕ 3
        commutative_text = Text("Commutativity", font_size=24).to_edge(UP)
        self.play(Transform(title, commutative_text))
        self.wait(0.5)

        expr1 = MathTex("3 \\oplus 5", font_size=40)
        expr1.shift(2 * LEFT + 1.5 * UP)
        self.play(Write(expr1))
        self.wait(1)

        result1 = MathTex("= 3 + 5 + 3 \\times 5", font_size=40)
        result1.next_to(expr1, DOWN, buff=0.5)
        self.play(Write(result1))
        self.wait(1)

        calc1 = MathTex("= 3 + 5 + 15 = 23", font_size=40)
        calc1.next_to(result1, DOWN, buff=0.5)
        self.play(Write(calc1))
        self.wait(1.5)

        # Now show reverse: 5 ⊕ 3
        expr2 = MathTex("5 \\oplus 3", font_size=40)
        expr2.shift(2 * RIGHT + 1.5 * UP)
        self.play(Write(expr2))
        self.wait(1)

        result2 = MathTex("= 5 + 3 + 5 \\times 3", font_size=40)
        result2.next_to(expr2, DOWN, buff=0.5)
        self.play(Write(result2))
        self.wait(1)

        calc2 = MathTex("= 5 + 3 + 15 = 23", font_size=40)
        calc2.next_to(result2, DOWN, buff=0.5)
        self.play(Write(calc2))
        self.wait(1.5)

        # Final summary
        summary = Text("a ⊕ b = b ⊕ a", font_size=30).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(1.5)

        self.play(FadeOut(expr1), FadeOut(result1), FadeOut(calc1),
                  FadeOut(expr2), FadeOut(result2), FadeOut(calc2),
                  FadeOut(summary), FadeOut(title))
