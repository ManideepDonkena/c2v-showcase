from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Absorbing Element (-1)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial circles
        minus_one = Circle(radius=1.2, color=BLUE, fill_color=BLUE, fill_opacity=0.8)
        minus_one_label = MathTex(r"-1", font_size=40).move_to(minus_one.get_center())
        b = Circle(radius=1.2, color=RED, fill_color=RED, fill_opacity=0.8)
        b_label = MathTex(r"b", font_size=40).move_to(b.get_center())

        # Position circles
        minus_one.to_edge(LEFT, buff=2)
        b.to_edge(RIGHT, buff=2)

        self.play(Create(minus_one), Write(minus_one_label))
        b_label.shift(0.0 * RIGHT + 0.43 * UP)  # layout: separation vector
        self.play(Create(b), Write(b_label))
        self.wait(1)

        # Move -1 towards b
        self.play(minus_one.animate.move_to((minus_one.get_center() + b.get_center()) / 2), run_time=1.5)
        self.wait(0.5)

        # Collision effect: b disappears, -1 stays
        self.play(FadeOut(b), FadeOut(b_label))
        self.wait(0.5)

        # Show result
        result_text = MathTex(r"(-1) \oplus b = -1", font_size=32).to_edge(DOWN)
        self.play(Write(result_text))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(minus_one), FadeOut(minus_one_label), FadeOut(result_text))
        self.wait(0.5)

        # Chain example
        circle3 = Circle(radius=0.6, color=GREEN, fill_color=GREEN, fill_opacity=0.8)
        circle3_label = MathTex(r"3", font_size=24).move_to(circle3.get_center())
        circle_neg1 = Circle(radius=0.6, color=YELLOW, fill_color=YELLOW, fill_opacity=0.8)
        circle_neg1_label = MathTex(r"(-1)", font_size=24).move_to(circle_neg1.get_center())
        circle7 = Circle(radius=0.6, color=ORANGE, fill_color=ORANGE, fill_opacity=0.8)
        circle7_label = MathTex(r"7", font_size=24).move_to(circle7.get_center())

        # Arrange horizontally
        group = VGroup(circle3, circle_neg1, circle7).arrange(RIGHT, buff=0.5)
        labels = VGroup(circle3_label, circle_neg1_label, circle7_label).arrange(RIGHT, buff=0.5)
        group_labels = VGroup(labels)

        self.play(Create(group), Write(group_labels))
        self.wait(0.5)

        # Say: When chaining, we go left to right.
        self.play(Write(Text("When chaining, we go left to right.", font_size=24).to_edge(DOWN)))
        self.wait(1.5)
        self.play(FadeOut(Text("When chaining, we go left to right.", font_size=24).to_edge(DOWN)))

        # Merge first two circles
        merged_circle = Circle(radius=0.6, color=DARK_BROWN, fill_color=DARK_BROWN, fill_opacity=0.8)
        merged_label = MathTex(r"-1", font_size=24).move_to(merged_circle.get_center())
        merged_label.shift(0.0 * RIGHT + 0.32 * UP)  # layout: separation vector
        self.play(
            ReplacementTransform(circle3, merged_circle),
            Transform(circle_neg1, merged_circle),
            ReplacementTransform(circle3_label, merged_label),
            Transform(circle_neg1_label, merged_label),
            run_time=1.5
        )
        self.wait(0.5)

        # Move merged circle to merge with third
        self.play(
            merged_circle.animate.move_to((merged_circle.get_center() + circle7.get_center()) / 2),
            merged_label.animate.move_to((merged_circle.get_center() + circle7.get_center()) / 2),
            run_time=1.5
        )
        self.wait(0.5)

        # Merge with third circle
        final_circle = Circle(radius=0.6, color=DARK_BROWN, fill_color=DARK_BROWN, fill_opacity=0.8)
        final_label = MathTex(r"-1", font_size=24).move_to(final_circle.get_center())
        self.play(
            Transform(merged_circle, final_circle),
            Transform(merged_label, final_label),
            run_time=1.5
        )
        self.wait(0.5)

        # Say: Because -1 swallows everything it touches, the entire chain collapses to -1.
        self.play(Write(Text("Because -1 swallows everything it touches, the entire chain collapses to -1.", font_size=24).to_edge(DOWN)))
        self.wait(2)
        self.play(FadeOut(Text("Because -1 swallows everything it touches, the entire chain collapses to -1.", font_size=24).to_edge(DOWN)))

        # Nested structure example
        nested_expr = MathTex(r"5 \oplus (0 \oplus 8)", font_size=36)
        self.play(Write(nested_expr))
        self.wait(1.5)

        # Say: When parentheses exist, you must solve the inside group before applying the outside operation, just like standard order of operations.
        self.play(Write(Text("When parentheses exist, you must solve the inside group before applying the outside operation, just like standard order of operations.", font_size=24).to_edge(DOWN)))
        self.wait(2.5)
        self.play(FadeOut(Text("When parentheses exist, you must solve the inside group before applying the outside operation, just like standard order of operations.", font_size=24).to_edge(DOWN)))

        # Worked example
        inner_result = MathTex(r"0 \oplus 8 = 8", font_size=30)
        self.play(Write(inner_result))
        self.wait(1.5)

        outer_expr = MathTex(r"5 \oplus 8", font_size=30)
        self.play(ReplacementTransform(inner_result, outer_expr))
        self.wait(1.5)

        final_calc = MathTex(r"5 + 8 + (5 \times 8) = 13 + 40 = 53", font_size=30)
        self.play(Transform(outer_expr, final_calc))
        self.wait(2.5)

        # Fade out everything
        self.play(FadeOut(nested_expr), FadeOut(inner_result), FadeOut(outer_expr))
        self.wait(0.5)
