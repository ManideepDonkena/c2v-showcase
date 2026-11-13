from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Tovan Sums", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Main definition: a ⊕ b = a + b + a*b
        a_op_b = MathTex("a \\oplus b", font_size=40)
        a_op_b.move_to(ORIGIN)
        self.play(Write(a_op_b))
        self.wait(1)

        arrow = Arrow(start=DOWN, end=UP, color=WHITE).next_to(a_op_b, DOWN)
        self.play(GrowArrow(arrow))

        formula = MathTex("a + b + a \\times b", font_size=40)
        formula.next_to(arrow, DOWN)
        self.play(Write(formula))
        self.wait(2)

        # Circles for a and b merging
        circle_a = Circle(radius=0.5, color=BLUE).move_to(LEFT * 2)
        label_a = Text("a", font_size=24).move_to(circle_a.get_center())
        circle_b = Circle(radius=0.5, color=GREEN).move_to(RIGHT * 2)
        label_b = Text("b", font_size=24).move_to(circle_b.get_center())

        self.play(Create(circle_a), Create(circle_b), Write(label_a), Write(label_b))
        self.wait(1)

        # Merge into one result circle
        result_circle = Circle(radius=0.8, color=YELLOW).move_to(ORIGIN)
        result_label = Text("Result", font_size=24).move_to(result_circle.get_center())
        result_label.shift(0.0 * RIGHT + 0.44 * UP)  # layout: separation vector
        self.play(
            ReplacementTransform(circle_a, result_circle),
            Transform(circle_b, result_circle),
            ReplacementTransform(label_a, result_label)
        )
        self.wait(1.5)

        # Chain example: 3 ⊕ (-1) ⊕ 7
        self.play(FadeOut(a_op_b), FadeOut(formula), FadeOut(arrow), FadeOut(result_circle), FadeOut(result_label))

        text_chain = Text("When chaining, we go left to right.", font_size=24).to_edge(UP)
        text_chain.shift(0.0 * RIGHT + 0.49 * UP)  # layout: separation vector
        self.play(Write(text_chain))
        self.wait(0.5)

        circle_3 = Circle(radius=0.4, color=RED).move_to(LEFT * 3)
        label_3 = Text("3", font_size=20).move_to(circle_3.get_center())
        circle_neg1 = Circle(radius=0.4, color=PURPLE).move_to(LEFT)
        label_neg1 = Text("-1", font_size=20).move_to(circle_neg1.get_center())
        circle_7 = Circle(radius=0.4, color=ORANGE).move_to(RIGHT * 2)
        label_7 = Text("7", font_size=20).move_to(circle_7.get_center())

        label_7.shift(0.3 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(circle_3), Create(circle_neg1), Create(circle_7), Write(label_3), Write(label_neg1), Write(label_7))
        self.wait(1)

        # First merge: 3 ⊕ (-1)
        merged_circle = Circle(radius=0.6, color=DARK_BROWN).move_to(LEFT)
        label_merged = Text("-1", font_size=20).move_to(merged_circle.get_center())
        self.play(
            Transform(circle_3, merged_circle),
            Transform(circle_neg1, merged_circle),
            Transform(label_3, label_merged),
            Transform(label_neg1, label_merged)
        )
        self.wait(1.5)

        # Second merge: (-1) ⊕ 7
        final_circle = Circle(radius=0.6, color=DARK_BROWN).move_to(RIGHT * 2)
        label_final = Text("-1", font_size=20).move_to(final_circle.get_center())
        self.play(
            ReplacementTransform(merged_circle, final_circle),
            Transform(circle_7, final_circle),
            ReplacementTransform(label_merged, label_final),
            Transform(label_7, label_final)
        )
        self.wait(1.5)

        # Collapse explanation
        collapse_text = Text("Because -1 swallows everything it touches, the entire chain collapses to -1.", font_size=24).to_edge(DOWN)
        self.play(Write(collapse_text))
        self.wait(2)

        # Parentheses example: 5 ⊕ (0 ⊕ 8)
        self.play(FadeOut(text_chain), FadeOut(collapse_text), FadeOut(final_circle), FadeOut(label_final))

        paren_example = MathTex("5 \\oplus (0 \\oplus 8)", font_size=36).move_to(ORIGIN)
        self.play(Write(paren_example))
        self.wait(1.5)

        # Highlight inner group
        inner_group = SurroundingRectangle(MathTex("0 \\oplus 8", font_size=36), color=YELLOW, buff=0.2)
        self.play(Create(inner_group))
        self.wait(1.5)

        # Solve inner group: 0 ⊕ 8 = 8 (since 0 is neutral)
        inner_result = MathTex("0 \\oplus 8 = 8", font_size=36).next_to(paren_example, DOWN)
        self.play(Write(inner_result))
        self.wait(1.5)

        # Replace inner group with result
        paren_example_new = MathTex("5 \\oplus 8", font_size=36).move_to(ORIGIN)
        self.play(Transform(paren_example, paren_example_new), FadeOut(inner_group), FadeOut(inner_result))

        # Compute outer operation: 5 ⊕ 8 = 5 + 8 + (5 × 8) = 13 + 40 = 53
        step1 = MathTex("= 5 + 8 + (5 \\times 8)", font_size=36).next_to(paren_example, DOWN)
        self.play(Write(step1))
        self.wait(1.5)

        step2 = MathTex("= 13 + 40", font_size=36).next_to(step1, DOWN)
        self.play(Write(step2))
        self.wait(1.5)

        final_result = MathTex("= 53", font_size=36).next_to(step2, DOWN)
        self.play(Write(final_result))
        self.wait(2)

        # Final summary
        summary = Text("When parentheses exist, you must solve the inside group before applying the outside operation, just like standard order of operations.", font_size=24).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)

        self.play(FadeOut(paren_example), FadeOut(step1), FadeOut(step2), FadeOut(final_result), FadeOut(summary), FadeOut(title))
