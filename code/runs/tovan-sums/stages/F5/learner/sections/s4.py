from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Chained Operations Example", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial expression: 2 ⊕ 3
        expr1 = MathTex("2 \\oplus 3", font_size=40)
        self.play(Write(expr1))
        self.wait(1)

        # Step 1: Expand to 2 + 3
        expr2 = MathTex("2 + 3", font_size=40)
        expr2.next_to(expr1, RIGHT, buff=0.5)
        self.play(ReplacementTransform(expr1, expr2))
        self.wait(1)

        # Step 2: Add (2 × 3)
        expr3 = MathTex("+ (2 \\times 3)", font_size=40)
        expr3.next_to(expr2, RIGHT, buff=0.5)
        self.play(Write(expr3))
        self.wait(1)

        # Step 3: Resolve to 11
        expr4 = MathTex("= 11", font_size=40)
        expr4.next_to(expr3, RIGHT, buff=0.5)
        self.play(Write(expr4))
        self.wait(2)

        # Narration text
        narration = Text("Left to right", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1)
        self.play(FadeOut(narration))

        # Fade out everything
        self.play(FadeOut(expr1), FadeOut(expr2), FadeOut(expr3), FadeOut(expr4), FadeOut(title))
        self.wait(0.5)

        # New nested structure: 5 ⊕ (0 ⊕ 8)
        nested_expr = MathTex("5 \\oplus (0 \\oplus 8)", font_size=40).to_edge(UP)
        self.play(Write(nested_expr))
        self.wait(1)

        # Highlight inner parentheses
        inner_group = SurroundingRectangle(MathTex("0 \\oplus 8"), color=YELLOW, buff=0.1)
        self.play(Create(inner_group))
        self.wait(1)

        # Say explanation
        explanation = Text("When parentheses exist, you must solve the inside group before applying the outside operation, just like standard order of operations.", font_size=24).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(3)
        self.play(FadeOut(explanation))

        # First evaluate inner term
        inner_result = MathTex("0 \\oplus 8 = 8", font_size=36).next_to(nested_expr, DOWN, buff=0.5)
        self.play(Write(inner_result))
        self.wait(2)

        # Substitute back into outer expression
        outer_expr = MathTex("5 \\oplus 8", font_size=40).next_to(inner_result, DOWN, buff=0.5)
        self.play(Transform(inner_result, outer_expr))
        self.wait(1)

        # Show calculation of 5 ⊕ 8 using definition
        calc = MathTex("= 5 + 8 + (5 \\times 8) = 13 + 40 = 53", font_size=36).next_to(outer_expr, DOWN, buff=0.5)
        self.play(Write(calc))
        self.wait(3)

        # Fade out everything
        self.play(FadeOut(nested_expr), FadeOut(inner_group), FadeOut(inner_result), FadeOut(calc))
        self.wait(0.5)
