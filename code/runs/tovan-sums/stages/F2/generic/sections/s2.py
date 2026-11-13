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

        # Show the expansion
        expand_left = MathTex("= 0 + 7 + 0 \\times 7", font_size=36)
        expand_left.next_to(left_expr, DOWN, buff=0.3)
        self.play(Write(expand_left))
        self.wait(1)

        # Simplify to 7
        simplify_left = MathTex("= 0 + 7 + 0 = 7", font_size=36)
        simplify_left.next_to(expand_left, DOWN, buff=0.3)
        self.play(Write(simplify_left))
        self.wait(1.5)

        # Fade out left side
        self.play(FadeOut(left_expr), FadeOut(expand_left), FadeOut(simplify_left))

        # Right scene: 7 ⊕ 0 becomes 7
        right_expr = MathTex("7 \\oplus 0", font_size=40)
        right_expr.shift(2 * RIGHT + 1.5 * UP)
        self.play(Write(right_expr))
        self.wait(1)

        # Show the expansion
        expand_right = MathTex("= 7 + 0 + 7 \\times 0", font_size=36)
        expand_right.next_to(right_expr, DOWN, buff=0.3)
        self.play(Write(expand_right))
        self.wait(1)

        # Simplify to 7
        simplify_right = MathTex("= 7 + 0 + 0 = 7", font_size=36)
        simplify_right.next_to(expand_right, DOWN, buff=0.3)
        self.play(Write(simplify_right))
        self.wait(1.5)

        # Fade out right side
        self.play(FadeOut(right_expr), FadeOut(expand_right), FadeOut(simplify_right))

        # Show commutativity: 3 ⊕ 5 = 5 ⊕ 3
        commutative_left = MathTex("3 \\oplus 5", font_size=40)
        commutative_left.shift(2 * LEFT + 0.5 * UP)
        self.play(Write(commutative_left))
        self.wait(1)

        commutative_right = MathTex("5 \\oplus 3", font_size=40)
        commutative_right.shift(2 * RIGHT + 0.5 * UP)
        self.play(Write(commutative_right))
        self.wait(1)

        # Expand both
        expand_left_2 = MathTex("= 3 + 5 + 3 \\times 5 = 3 + 5 + 15 = 23", font_size=24)
        expand_left_2.next_to(commutative_left, DOWN, buff=0.3)
        self.play(Write(expand_left_2))
        self.wait(1)

        expand_right_2 = MathTex("= 5 + 3 + 5 \\times 3 = 5 + 3 + 15 = 23", font_size=24)
        expand_right_2.next_to(commutative_right, DOWN, buff=0.3)
        self.play(Write(expand_right_2))
        self.wait(2)

        # Fade out
        self.play(FadeOut(commutative_left), FadeOut(commutative_right),
                  FadeOut(expand_left_2), FadeOut(expand_right_2))

        # Final rule summary
        rule1 = Text("Commutativity: a ⊕ b = b ⊕ a", font_size=24)
        rule1.to_edge(DOWN).shift(0.5 * UP)
        self.play(Write(rule1))
        self.wait(1)

        rule2 = Text("Neutral element: 0 ⊕ b = b", font_size=24)
        rule2.next_to(rule1, DOWN)
        self.play(Write(rule2))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(rule1), FadeOut(rule2), FadeOut(title))
        self.wait(0.5)
