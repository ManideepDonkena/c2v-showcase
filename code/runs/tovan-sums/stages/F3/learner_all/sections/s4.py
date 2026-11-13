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

        step2 = MathTex("= 2 + 3 + (2 \\times 3)", font_size=40)
        step2.next_to(step1, DOWN, buff=0.5)
        self.play(Transform(step1, step2))
        self.wait(1.5)

        step3 = MathTex("= 2 + 3 + 6", font_size=40)
        step3.next_to(step1, DOWN, buff=0.5)
        self.play(Transform(step1, step3))
        self.wait(1.5)

        step4 = MathTex("= 11", font_size=40)
        step4.next_to(step1, DOWN, buff=0.5)
        self.play(Transform(step1, step4))
        self.wait(2)

        # Left to right chaining
        self.play(FadeOut(step1))

        text1 = Text("When chaining, we go left to right.", font_size=24)
        text1.to_edge(DOWN)
        self.play(Write(text1))
        self.wait(1.5)

        # Three circles: 4, -1, 2
        c1 = Circle(radius=0.6, color=BLUE).shift(LEFT * 2)
        t1 = Text("4", font_size=24).move_to(c1.get_center())
        c2 = Circle(radius=0.6, color=RED).shift(LEFT)
        t2 = Text("-1", font_size=24).move_to(c2.get_center())
        c3 = Circle(radius=0.6, color=GREEN).shift(RIGHT)
        t3 = Text("2", font_size=24).move_to(c3.get_center())

        self.play(Create(c1), Write(t1))
        self.wait(0.5)
        self.play(Create(c2), Write(t2))
        self.wait(0.5)
        self.play(Create(c3), Write(t3))
        self.wait(1)

        # Merge first two circles into one dark circle labeled -1
        merge_circle = Circle(radius=0.6, color=DARK_BROWN).shift(LEFT)
        merge_text = Text("-1", font_size=24).move_to(merge_circle.get_center())
        self.play(
            ReplacementTransform(c1, merge_circle),
            ReplacementTransform(t1, merge_text),
            FadeOut(c2),
            FadeOut(t2)
        )
        self.wait(1.5)

        # Move merged circle to merge with third
        self.play(
            merge_circle.animate.shift(RIGHT),
            merge_text.animate.shift(RIGHT),
            FadeOut(c3),
            FadeOut(t3)
        )
        self.wait(1.5)

        final_circle = Circle(radius=0.6, color=DARK_BROWN).shift(RIGHT)
        final_text = Text("-1", font_size=24).move_to(final_circle.get_center())
        self.play(Transform(merge_circle, final_circle), Transform(merge_text, final_text))
        self.wait(2)

        # Formula: (-1) + 5 + ((-1) × 5)
        self.play(FadeOut(text1), FadeOut(merge_circle), FadeOut(merge_text))

        formula = MathTex("(-1) + 5 + ((-1) \\times 5)", font_size=40)
        formula.to_edge(UP)
        formula.shift(0.0 * RIGHT + -0.53 * UP)  # layout: separation vector
        self.play(Write(formula))
        self.wait(1.5)

        step_a = MathTex("= -1 + 5 + (-5)", font_size=40)
        step_a.next_to(formula, DOWN, buff=0.5)
        self.play(Transform(formula, step_a))
        self.wait(1.5)

        step_b = MathTex("= -1 + (5 - 5)", font_size=40)
        step_b.next_to(formula, DOWN, buff=0.5)
        self.play(Transform(formula, step_b))
        self.wait(1.5)

        step_c = MathTex("= -1", font_size=40)
        step_c.next_to(formula, DOWN, buff=0.5)
        self.play(Transform(formula, step_c))
        self.wait(2)

        # Nested structure
        self.play(FadeOut(formula))

        text2 = Text("Even though 5 is added, the multiplication term (-1 × 5) cancels it out completely, leaving only the absorbing element.", font_size=24)
        text2.to_edge(DOWN)
        self.play(Write(text2))
        self.wait(2)

        # Show nested structure
        nested = MathTex("a \\oplus (b \\oplus c)", font_size=40)
        nested.to_edge(UP)
        self.play(Write(nested))
        self.wait(1.5)

        inner = SurroundingRectangle(MathTex("b \\oplus c", font_size=40), color=YELLOW, buff=0.2)
        self.play(Create(inner))
        self.wait(1.5)

        text3 = Text("When parentheses exist, you must solve the inside group before applying the outside operation, just like standard order of operations.", font_size=24)
        text3.to_edge(DOWN)
        self.play(Transform(text2, text3))
        self.wait(2)

        # Final cleanup
        self.play(FadeOut(nested), FadeOut(inner), FadeOut(text2))
        self.wait(0.5)
