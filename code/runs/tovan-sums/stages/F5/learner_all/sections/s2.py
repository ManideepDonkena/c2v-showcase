from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Commutativity and Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Left scene: 0 ⊕ 7
        left_expr = MathTex("0 \\oplus 7", font_size=40)
        left_expr.shift(2 * LEFT + 1.5 * UP)
        self.play(Write(left_expr))
        self.wait(1)

        zero_fade = left_expr[0][0]
        self.play(FadeOut(zero_fade))
        self.wait(0.5)

        left_result = MathTex("= 7", font_size=40).next_to(left_expr, RIGHT)
        self.play(Write(left_result))
        self.wait(1.5)

        # Right scene: 7 ⊕ 0
        right_expr = MathTex("7 \\oplus 0", font_size=40)
        right_expr.shift(2 * RIGHT + 1.5 * UP)
        self.play(Write(right_expr))
        self.wait(1)

        # Check if the index exists before accessing
        if len(right_expr[0]) > 3:
            zero_fade_right = right_expr[0][3]
            self.play(FadeOut(zero_fade_right))
            self.wait(0.5)
        else:
            self.wait(0.5)

        right_result = MathTex("= 7", font_size=40).next_to(right_expr, RIGHT)
        self.play(Write(right_result))
        self.wait(1.5)

        # Commutativity
        commutative_text = Text("a ⊕ b = b ⊕ a", font_size=24).to_edge(DOWN)
        self.play(Write(commutative_text))
        self.wait(1.5)

        # Fade out all
        self.play(
            FadeOut(left_expr),
            FadeOut(right_expr),
            FadeOut(left_result),
            FadeOut(right_result),
            FadeOut(commutative_text),
            FadeOut(title)
        )
        self.wait(0.5)

        # Chain example
        chain_title = Text("Chaining", font_size=36).to_edge(UP)
        self.play(Write(chain_title))
        self.wait(0.5)

        # Show three circles labeled '3', '(-1)', and '7'
        circle3 = Circle(color=BLUE, radius=0.5).shift(2 * LEFT)
        label3 = Text("3", font_size=24).move_to(circle3.get_center())
        circle_neg1 = Circle(color=RED, radius=0.5).shift(ORIGIN)
        label_neg1 = Text("(-1)", font_size=24).move_to(circle_neg1.get_center())
        circle7 = Circle(color=GREEN, radius=0.5).shift(2 * RIGHT)
        label7 = Text("7", font_size=24).move_to(circle7.get_center())

        self.play(Create(circle3), Write(label3))
        self.wait(0.5)
        self.play(Create(circle_neg1), Write(label_neg1))
        self.wait(0.5)
        self.play(Create(circle7), Write(label7))
        self.wait(0.5)

        # Say "When chaining, we go left to right."
        self.play(Write(Text("When chaining, we go left to right.", font_size=24).to_edge(DOWN)))
        self.wait(1.5)

        # Animate first two circles merging into a dark circle labeled '-1'
        merged_circle = Circle(color=DARK_BROWN, radius=0.5).shift(ORIGIN)
        merged_label = Text("-1", font_size=24).move_to(merged_circle.get_center())
        self.play(
            ReplacementTransform(circle3, merged_circle),
            ReplacementTransform(label3, merged_label),
            FadeOut(circle_neg1),
            FadeOut(label_neg1)
        )
        self.wait(1.5)

        # Move the merged circle to merge with third circle
        self.play(
            Transform(merged_circle, Circle(color=DARK_BROWN, radius=0.5).shift(2 * RIGHT)),
            Transform(merged_label, Text("-1", font_size=24).move_to(Circle(color=DARK_BROWN, radius=0.5).shift(2 * RIGHT).get_center())),
            FadeOut(circle7),
            FadeOut(label7)
        )
        self.wait(1.5)

        # Say "Because -1 swallows everything it touches, the entire chain collapses to -1."
        self.play(Write(Text("Because -1 swallows everything it touches, the entire chain collapses to -1.", font_size=24).to_edge(DOWN)))
        self.wait(2)

        # Fade out chain elements
        self.play(
            FadeOut(merged_circle),
            FadeOut(merged_label),
            FadeOut(chain_title)
        )
        self.wait(0.5)

        # Nested structure example
        nested_title = Text("Nested Operations", font_size=36).to_edge(UP)
        self.play(Write(nested_title))
        self.wait(0.5)

        # Show 5 ⊕ (0 ⊕ 8) with highlighted inner parentheses
        nested_expr = MathTex("5 \\oplus (0 \\oplus 8)", font_size=40).to_edge(UP)
        self.play(Write(nested_expr))
        self.wait(1.5)

        # Say "When parentheses exist, you must solve the inside group before applying the outside operation, just like standard order of operations."
        self.play(Write(Text("When parentheses exist, you must solve the inside group before applying the outside operation, just like standard order of operations.", font_size=24).to_edge(DOWN)))
        self.wait(3)

        # Highlight inner parentheses
        inner_group = nested_expr[0][5:9]
        inner_group_copy = inner_group.copy()
        self.play(
            inner_group.animate.set_color(YELLOW),
            FadeOut(inner_group_copy)
        )
        self.wait(1.5)

        # Worked example: 0 ⊕ 8 = 8
        step1 = MathTex("0 \\oplus 8 = 8", font_size=36).to_edge(DOWN)
        self.play(Write(step1))
        self.wait(2)

        # Substitute back into outer expression
        step2 = MathTex("5 \\oplus 8", font_size=36).to_edge(DOWN)
        self.play(Transform(step1, step2))
        self.wait(1.5)

        # Calculate 5 ⊕ 8 using definition a + b + a×b
        calc = MathTex("5 + 8 + (5 \\times 8) = 13 + 40 = 53", font_size=36).to_edge(DOWN)
        self.play(Transform(step1, calc))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(nested_expr),
            FadeOut(step1),
            FadeOut(nested_title)
        )
        self.wait(0.5)
