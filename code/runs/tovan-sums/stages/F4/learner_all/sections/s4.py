from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Tovan Sums", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First example: 2 ⊕ 3
        step1 = MathTex("2 \\oplus 3", font_size=40)
        self.play(Write(step1))
        self.wait(1)

        step2 = MathTex("2 + 3", font_size=40).next_to(step1, RIGHT, buff=0.5)
        self.play(Write(step2))
        self.wait(1)

        step3 = MathTex("+ (2 \\times 3)", font_size=40).next_to(step2, RIGHT, buff=0.5)
        self.play(Write(step3))
        self.wait(1)

        step4 = MathTex("= 11", font_size=40).next_to(step3, RIGHT, buff=0.5)
        self.play(Write(step4))
        self.wait(1.5)

        # Fade out first example
        self.play(FadeOut(step1), FadeOut(step2), FadeOut(step3), FadeOut(step4))

        # Chain of three circles: 3, (-1), 7
        circle1 = Circle(color=BLUE, radius=0.5).move_to(LEFT * 2)
        label1 = MathTex("3", font_size=24).move_to(circle1.get_center())
        circle2 = Circle(color=RED, radius=0.5).move_to(ORIGIN)
        label2 = MathTex("-1", font_size=24).move_to(circle2.get_center())
        circle3 = Circle(color=GREEN, radius=0.5).move_to(RIGHT * 2)
        label3 = MathTex("7", font_size=24).move_to(circle3.get_center())

        self.play(Create(circle1), Write(label1))
        self.wait(0.5)
        self.play(Create(circle2), Write(label2))
        self.wait(0.5)
        self.play(Create(circle3), Write(label3))
        self.wait(0.5)

        # Left to right: 3 ⊕ (-1) = -1
        merge1 = Circle(color=DARK_BROWN, radius=0.7).move_to(LEFT * 1)
        label_merge1 = MathTex("-1", font_size=24).move_to(merge1.get_center())
        self.play(
            Transform(circle1, merge1),
            Transform(label1, label_merge1),
            FadeOut(circle2),
            FadeOut(label2)
        )
        self.wait(1)

        # Now -1 ⊕ 7 = -1
        merge2 = Circle(color=DARK_BROWN, radius=0.7).move_to(RIGHT * 1)
        label_merge2 = MathTex("-1", font_size=24).move_to(merge2.get_center())
        self.play(
            Transform(circle3, merge2),
            Transform(label3, label_merge2),
            FadeOut(circle1),
            FadeOut(label1)
        )
        self.wait(1.5)

        # Fade out circles
        self.play(FadeOut(circle3), FadeOut(label3))

        # Parentheses example: 5 ⊕ (0 ⊕ 8)
        paren_text = MathTex("5 \\oplus (0 \\oplus 8)", font_size=40).to_edge(UP)
        paren_text.shift(0.0 * RIGHT + -0.53 * UP)  # layout: separation vector
        self.play(Write(paren_text))
        self.wait(1)

        # Highlight inner group
        inner_group = SurroundingRectangle(MathTex("0 \\oplus 8", font_size=36), color=YELLOW, buff=0.2)
        self.play(Create(inner_group))
        self.wait(1)

        # Evaluate inner: 0 ⊕ 8 = 8
        inner_result = MathTex("0 \\oplus 8 = 8", font_size=36).next_to(paren_text, DOWN, buff=0.5)
        self.play(Write(inner_result))
        self.wait(1)

        # Replace inner group with result
        self.play(FadeOut(inner_group), FadeOut(inner_result))

        # Outer operation: 5 ⊕ 8
        outer_expr = MathTex("5 \\oplus 8", font_size=40).next_to(paren_text, DOWN, buff=0.5)
        self.play(Write(outer_expr))
        self.wait(1)

        # Evaluate 5 ⊕ 8 = 5 + 8 + (5×8) = 13 + 40 = 53
        step_a = MathTex("= 5 + 8 + (5 \\times 8)", font_size=36).next_to(outer_expr, DOWN, buff=0.5)
        self.play(Write(step_a))
        self.wait(1)

        step_b = MathTex("= 13 + 40", font_size=36).next_to(step_a, DOWN, buff=0.5)
        self.play(Write(step_b))
        self.wait(1)

        step_c = MathTex("= 53", font_size=36).next_to(step_b, DOWN, buff=0.5)
        self.play(Write(step_c))
        self.wait(1.5)

        # Fade everything
        self.play(FadeOut(paren_text), FadeOut(outer_expr), FadeOut(step_a), FadeOut(step_b), FadeOut(step_c))
        self.wait(0.5)
