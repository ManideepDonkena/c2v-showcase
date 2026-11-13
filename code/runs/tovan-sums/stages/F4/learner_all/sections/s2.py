from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Commutativity and Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Left scene: 0 ⊕ 7 → 7
        left_expr = MathTex("0 \oplus 7", font_size=40)
        left_expr.shift(2 * LEFT + 1.5 * UP)
        self.play(Write(left_expr))
        self.wait(1)

        zero = always_redraw(lambda: Circle(color=RED, radius=0.3).shift(2 * LEFT + 2.11 * UP))
        seven = always_redraw(lambda: Circle(color=BLUE, radius=0.3).shift(0.5 * RIGHT + 1.5 * UP))
        zero_label = MathTex("0", font_size=24).move_to(zero.get_center())
        seven_label = MathTex("7", font_size=24).move_to(seven.get_center())

        self.play(Create(zero), Create(seven), Write(zero_label), Write(seven_label))
        self.wait(1)

        # Fade out zero
        self.play(FadeOut(zero), FadeOut(zero_label))
        self.wait(0.5)

        # Show result: 7
        final_seven = always_redraw(lambda: Circle(color=BLUE, radius=0.3).shift(0.5 * RIGHT + 1.5 * UP))
        final_label = MathTex("7", font_size=24).move_to(final_seven.get_center())
        self.play(Create(final_seven), Write(final_label))
        self.wait(1.5)

        # Right scene: 3 ⊕ 5 → 38
        right_expr = MathTex("3 \\oplus 5", font_size=40)
        right_expr.shift(2 * RIGHT + 1.5 * UP)
        self.play(Write(right_expr))
        self.wait(1)

        # Show transformation to 3 + 5 + 15 = 38
        result = MathTex("3 + 5 + 15 = 38", font_size=40)
        result.shift(2 * RIGHT + 1.5 * UP)
        self.play(Transform(right_expr, result))
        self.wait(1.5)

        # Commutativity: 5 ⊕ 3 → 38
        comm_expr = MathTex("5 \\oplus 3", font_size=40)
        comm_expr.shift(2 * RIGHT + 0.5 * UP)
        self.play(Write(comm_expr))
        self.wait(1)

        comm_result = MathTex("5 + 3 + 15 = 38", font_size=40)
        comm_result.shift(2 * RIGHT + 0.5 * UP)
        self.play(Transform(comm_expr, comm_result))
        self.wait(1.5)

        # Chain example: 3, -1, 7
        chain_title = Text("Chaining from left to right", font_size=24).to_edge(UP)
        self.play(Transform(title, chain_title))
        self.wait(0.5)

        circle_3 = Circle(color=GREEN, radius=0.3).shift(3 * LEFT + 0.5 * DOWN)
        circle_neg1 = Circle(color=YELLOW, radius=0.3).shift(1.5 * LEFT + 0.5 * DOWN)
        circle_7 = Circle(color=BLUE, radius=0.3).shift(0.0 * LEFT + 0.5 * DOWN)

        label_3 = MathTex("3", font_size=24).move_to(circle_3.get_center())
        label_neg1 = MathTex("-1", font_size=24).move_to(circle_neg1.get_center())
        label_7 = MathTex("7", font_size=24).move_to(circle_7.get_center())

        self.play(Create(circle_3), Create(circle_neg1), Create(circle_7),
                  Write(label_3), Write(label_neg1), Write(label_7))
        self.wait(1)

        # Merge first two circles
        merged_circle = Circle(color=YELLOW, radius=0.3).shift(1.5 * LEFT + 0.5 * DOWN)
        merged_label = MathTex("-1", font_size=24).move_to(merged_circle.get_center())
        self.play(Transform(circle_neg1, merged_circle), Transform(label_neg1, merged_label))
        self.wait(1)

        # Merge with third circle
        final_circle = Circle(color=YELLOW, radius=0.3).shift(0.0 * LEFT + 0.5 * DOWN)
        final_label = MathTex("-1", font_size=24).move_to(final_circle.get_center())
        self.play(Transform(circle_7, final_circle), Transform(label_7, final_label))
        self.wait(1.5)

        # Nested structure: 5 ⊕ (0 ⊕ 8)
        nested_title = Text("Parentheses must be evaluated first", font_size=24).to_edge(UP)
        self.play(Transform(title, nested_title))
        self.wait(0.5)

        expr_nested = MathTex("5 \\oplus (0 \\oplus 8)", font_size=40)
        expr_nested.shift(3 * LEFT + 1.5 * UP)
        self.play(Write(expr_nested))
        self.wait(1)

        # Highlight inner group
        inner_group = always_redraw(lambda: SurroundingRectangle(MathTex("0 \\oplus 8", font_size=40), color=YELLOW, buff=0.1))
        self.play(Create(inner_group))
        self.wait(1)

        # Evaluate inner group
        inner_eval = MathTex("0 \\oplus 8 = 8", font_size=36)
        inner_eval.shift(3 * LEFT + 0.5 * UP)
        self.play(ReplacementTransform(expr_nested, inner_eval))
        self.wait(1)

        # Replace with outer operation
        outer_expr = MathTex("5 \\oplus 8", font_size=40)
        outer_expr.shift(3 * LEFT + 1.5 * UP)
        self.play(ReplacementTransform(inner_eval, outer_expr))
        self.wait(1)

        # Compute final result: 5 + 8 + (5×8) = 53
        final_result = MathTex("5 + 8 + (5 \\times 8) = 13 + 40 = 53", font_size=36)
        final_result.shift(3 * LEFT + 0.5 * UP)
        self.play(Transform(outer_expr, final_result))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(expr_nested), FadeOut(inner_eval), FadeOut(outer_expr),
                  FadeOut(circle_3), FadeOut(circle_neg1), FadeOut(circle_7),
                  FadeOut(label_3), FadeOut(label_neg1), FadeOut(label_7),
                  FadeOut(inner_group))
        self.wait(0.5)
