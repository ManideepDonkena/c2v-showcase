from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Absorbing Element (-1)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Part 1: -1 absorbs any number
        neg_one_circle = Circle(radius=1, color=BLUE, fill_color=BLUE, fill_opacity=1).move_to(LEFT * 3)
        b_circle = Circle(radius=1, color=GREEN, fill_color=GREEN, fill_opacity=1).move_to(RIGHT * 3)
        neg_one_label = MathTex("-1", font_size=36).move_to(neg_one_circle.get_center())
        b_label = MathTex("b", font_size=36).move_to(b_circle.get_center())

        self.play(Create(neg_one_circle), Create(b_circle), Write(neg_one_label), Write(b_label))
        self.wait(1)

        # Animate movement and absorption
        self.play(
            neg_one_circle.animate.move_to(RIGHT * 1.5),
            b_circle.animate.move_to(RIGHT * 1.5),
            run_time=1.5
        )
        self.play(FadeOut(b_circle), FadeOut(b_label))
        self.wait(0.5)

        # Show result
        result_label = MathTex("-1", font_size=36).move_to(neg_one_circle.get_center())
        self.play(Write(result_label))
        self.wait(1.5)

        # Narration text
        absorb_text = Text("The number negative one acts as an absorbing element.", font_size=24)
        absorb_text.shift(0.0 * RIGHT + 1.32 * UP)  # layout: separation vector
        self.play(Write(absorb_text))
        self.wait(2)
        self.play(FadeOut(absorb_text))

        # Part 2: Chain of three circles
        chain_text = Text("When chaining, we go left to right.", font_size=24).to_edge(UP)
        chain_text.shift(0.0 * RIGHT + 0.49 * UP)  # layout: separation vector
        self.play(Write(chain_text))
        self.wait(1)

        # Create circles for the chain
        circle3 = Circle(radius=0.5, color=RED, fill_color=RED, fill_opacity=1).move_to(LEFT * 2)
        circle_neg1 = Circle(radius=0.5, color=BLUE, fill_color=BLUE, fill_opacity=1).move_to(ORIGIN)
        circle7 = Circle(radius=0.5, color=GREEN, fill_color=GREEN, fill_opacity=1).move_to(RIGHT * 2)

        label3 = MathTex("3", font_size=24).move_to(circle3.get_center())
        label_neg1 = MathTex("-1", font_size=24).move_to(circle_neg1.get_center())
        label7 = MathTex("7", font_size=24).move_to(circle7.get_center())

        circle7.shift(0.36 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(circle3), Create(circle_neg1), Create(circle7))
        self.play(Write(label3), Write(label_neg1), Write(label7))
        self.wait(1)

        # First merge: 3 ⊕ (-1) = -1
        merged_circle = Circle(radius=0.5, color=BLUE, fill_color=BLUE, fill_opacity=1).move_to(ORIGIN)
        merged_label = MathTex("-1", font_size=24).move_to(merged_circle.get_center())
        self.play(
            circle3.animate.move_to(LEFT * 1),
            circle_neg1.animate.move_to(LEFT * 1),
            run_time=1
        )
        self.play(FadeOut(circle3), FadeOut(label3))
        self.play(Create(merged_circle), Write(merged_label))
        self.wait(1)

        # Second merge: (-1) ⊕ 7 = -1
        final_circle = Circle(radius=0.5, color=BLUE, fill_color=BLUE, fill_opacity=1).move_to(RIGHT * 1)
        final_label = MathTex("-1", font_size=24).move_to(final_circle.get_center())
        self.play(
            merged_circle.animate.move_to(RIGHT * 1),
            circle7.animate.move_to(RIGHT * 1),
            run_time=1
        )
        self.play(FadeOut(circle7), FadeOut(label7))
        self.play(Create(final_circle), Write(final_label))
        self.wait(1.5)

        collapse_text = Text("Because -1 swallows everything it touches, the entire chain collapses to -1.", font_size=24)
        self.play(Write(collapse_text))
        self.wait(2)
        self.play(FadeOut(collapse_text), FadeOut(chain_text))

        # Part 3: Nested parentheses
        nested_text = Text("When parentheses exist, you must solve the inside group first.", font_size=24).to_edge(UP)
        self.play(Write(nested_text))
        self.wait(1)

        # Show expression
        expr = MathTex("5 \\oplus (0 \\oplus 8)", font_size=36)
        self.play(Write(expr))
        self.wait(1.5)

        # Highlight inner parentheses
        inner_group = SurroundingRectangle(MathTex("0 \\oplus 8"), color=YELLOW, buff=0.2)
        self.play(Create(inner_group))
        self.wait(1.5)

        # Evaluate inner group: 0 ⊕ 8 = 8
        inner_result = MathTex("0 \\oplus 8 = 8", font_size=36).next_to(expr, DOWN, buff=0.5)
        self.play(Write(inner_result))
        self.wait(1.5)

        # Replace and evaluate outer operation: 5 ⊕ 8
        outer_expr = MathTex("5 \\oplus 8", font_size=36).move_to(expr.get_center())
        self.play(Transform(expr, outer_expr))
        self.wait(1)

        # Show calculation using definition a + b + ab
        calc = MathTex("5 + 8 + (5 \\times 8) = 13 + 40 = 53", font_size=36).next_to(outer_expr, DOWN, buff=0.5)
        self.play(Write(calc))
        self.wait(2)

        # Final result
        final_result = MathTex("53", font_size=36).move_to(ORIGIN)
        self.play(Transform(expr, final_result))
        self.wait(1.5)

        self.play(FadeOut(nested_text), FadeOut(expr), FadeOut(inner_group), FadeOut(inner_result), FadeOut(calc))

        # Final summary
        summary = Text("The number -1 is the absorbing element in Tovan Sums.", font_size=24).to_edge(UP)
        self.play(Write(summary))
        self.wait(2)
        self.play(FadeOut(summary))
