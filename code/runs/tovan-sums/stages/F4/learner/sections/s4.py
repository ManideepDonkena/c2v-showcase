from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Chained Operations Example", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First example: 2 ⊕ 3
        expr1 = MathTex("2 \\oplus 3", font_size=40)
        self.play(Write(expr1))
        self.wait(1)

        # Step 1: 2 + 3
        step1 = MathTex("2 + 3", font_size=40).move_to(expr1.get_center())
        self.play(Transform(expr1, step1))
        self.wait(1)

        # Step 2: add (2 × 3)
        step2 = MathTex("2 + 3 + (2 \\times 3)", font_size=40).move_to(expr1.get_center())
        self.play(Transform(expr1, step2))
        self.wait(1)

        # Step 3: resolve to 11
        step3 = MathTex("= 11", font_size=40).move_to(expr1.get_center())
        self.play(Transform(expr1, step3))
        self.wait(1.5)

        # Fade out first example
        self.play(FadeOut(expr1))

        # Narration text for left-to-right chaining
        narration1 = Text("When chaining operations, we always work from left to right.", font_size=24)
        self.play(Write(narration1))
        self.wait(2)
        self.play(FadeOut(narration1))

        # Nested example: 5 ⊕ (0 ⊕ 8)
        expr2 = MathTex("5 \\oplus (0 \\oplus 8)", font_size=40).to_edge(UP, buff=0.5)
        expr2.shift(0.0 * RIGHT + -0.65 * UP)  # layout: separation vector
        self.play(Write(expr2))
        self.wait(1)

        # Highlight inner parentheses
        inner_group = SurroundingRectangle(MathTex("0 \\oplus 8"), color=YELLOW, buff=0.1)
        self.play(Create(inner_group))
        self.wait(1)

        # Narration: inner group must be solved first
        narration2 = Text("When parentheses exist, you must solve the inside group before applying the outside operation.", font_size=24)
        inner_group.shift(0.0 * RIGHT + 0.6 * UP)  # layout: separation vector
        narration2.shift(0.61 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(narration2))
        self.wait(2.5)
        self.play(FadeOut(narration2))

        # Evaluate inner: 0 ⊕ 8
        inner_result = MathTex("0 \\oplus 8 = 8", font_size=36).next_to(expr2, DOWN, buff=0.5)
        self.play(Write(inner_result))
        self.wait(1.5)

        # Replace inner group with result
        expr3 = MathTex("5 \\oplus 8", font_size=40).move_to(expr2.get_center())
        self.play(Transform(expr2, expr3), FadeOut(inner_group))
        self.wait(1)

        # Calculate 5 ⊕ 8 using definition: a + b + a×b
        calc_step1 = MathTex("5 + 8 + (5 \\times 8)", font_size=40).next_to(expr2, DOWN, buff=0.5)
        self.play(Write(calc_step1))
        self.wait(1.5)

        calc_step2 = MathTex("= 13 + 40 = 53", font_size=40).next_to(calc_step1, DOWN, buff=0.5)
        self.play(Write(calc_step2))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(expr2), FadeOut(inner_result), FadeOut(calc_step1), FadeOut(calc_step2), FadeOut(title))
        self.wait(0.5)
