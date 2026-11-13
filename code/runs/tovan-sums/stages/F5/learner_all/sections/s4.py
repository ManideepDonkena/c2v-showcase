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

        # New part: Chain of three circles
        circle1 = Circle(color=BLUE, fill_color=BLUE, fill_opacity=1).scale(0.5)
        label1 = MathTex("3", font_size=24).move_to(circle1.get_center())
        circle1.add(label1)

        circle2 = Circle(color=RED, fill_color=RED, fill_opacity=1).scale(0.5)
        label2 = MathTex("(-1)", font_size=24).move_to(circle2.get_center())
        circle2.add(label2)

        circle3 = Circle(color=GREEN, fill_color=GREEN, fill_opacity=1).scale(0.5)
        label3 = MathTex("7", font_size=24).move_to(circle3.get_center())
        circle3.add(label3)

        # Arrange horizontally
        circles = VGroup(circle1, circle2, circle3).arrange(RIGHT, buff=1)
        self.play(Write(circles))
        self.wait(1)

        # Narration: When chaining, we go left to right.
        narration2 = Text("When chaining, we go left to right.", font_size=24).to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1)
        self.play(FadeOut(narration2))

        # Merge first two circles into one dark circle
        merged_circle1 = Circle(color=DARK_BROWN, fill_color=DARK_BROWN, fill_opacity=1).scale(0.5)
        label_merged1 = MathTex("-1", font_size=24).move_to(merged_circle1.get_center())
        merged_circle1.add(label_merged1)

        self.play(ReplacementTransform(VGroup(circle1, circle2), merged_circle1))
        self.wait(1)

        # Move merged circle to merge with third circle
        self.play(merged_circle1.animate.move_to(circle3.get_center()))
        self.wait(0.5)

        # Merge with third circle
        final_circle = Circle(color=DARK_BROWN, fill_color=DARK_BROWN, fill_opacity=1).scale(0.5)
        label_final = MathTex("-1", font_size=24).move_to(final_circle.get_center())
        final_circle.add(label_final)

        self.play(ReplacementTransform(merged_circle1, final_circle))
        self.wait(1)

        # Narration: Because -1 swallows everything it touches, the entire chain collapses to -1.
        narration3 = Text("Because -1 swallows everything it touches, the entire chain collapses to -1.", font_size=24).to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(2)
        self.play(FadeOut(narration3))

        # Fade out circles
        self.play(FadeOut(circles), FadeOut(final_circle))
        self.wait(0.5)

        # New part: Nested structure 5 ⊕ (0 ⊕ 8)
        expr_nested = MathTex("5 \\oplus (0 \\oplus 8)", font_size=40).to_edge(UP)
        self.play(Write(expr_nested))
        self.wait(1)

        # Highlight inner parentheses
        inner_group = SurroundingRectangle(MathTex("0 \\oplus 8"), color=YELLOW, buff=0.2)
        self.play(Create(inner_group))
        self.wait(1)

        # Narration: When parentheses exist, you must solve the inside group before applying the outside operation...
        narration4 = Text("When parentheses exist, you must solve the inside group before applying the outside operation, just like standard order of operations.", font_size=24).to_edge(DOWN)
        self.play(Write(narration4))
        self.wait(2)
        self.play(FadeOut(narration4))

        # Worked example: Evaluate inner term 0 ⊕ 8
        step1 = MathTex("0 \\oplus 8 = 8", font_size=36).to_edge(DOWN)
        self.play(Write(step1))
        self.wait(2)
        self.play(FadeOut(step1))

        # Substitute back into outer expression: 5 ⊕ 8
        expr_outer = MathTex("5 \\oplus 8", font_size=40).to_edge(UP)
        self.play(Transform(expr_nested, expr_outer))
        self.wait(1)

        # Calculate using definition a + b + a×b: 5 + 8 + (5 × 8) = 13 + 40 = 53
        step2 = MathTex("= 5 + 8 + (5 \\times 8)", font_size=36).to_edge(DOWN)
        self.play(Write(step2))
        self.wait(1)

        step3 = MathTex("= 13 + 40", font_size=36).next_to(step2, DOWN, buff=0.5)
        self.play(Write(step3))
        self.wait(1)

        step4 = MathTex("= 53", font_size=36).next_to(step3, DOWN, buff=0.5)
        self.play(Write(step4))
        self.wait(2)

        # Final fade out
        self.play(FadeOut(expr_nested), FadeOut(inner_group), FadeOut(step2), FadeOut(step3), FadeOut(step4))
        self.wait(0.5)
