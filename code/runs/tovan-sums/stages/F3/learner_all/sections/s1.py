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

        formula = MathTex("a + b + (a \\times b)", font_size=40)
        formula.next_to(arrow, DOWN)
        self.play(Write(formula))
        self.wait(2)

        # Circles for a and b
        circle_a = Circle(radius=0.5, color=BLUE).move_to(LEFT * 2)
        label_a = MathTex("a", font_size=24).move_to(circle_a.get_center())
        circle_b = Circle(radius=0.5, color=GREEN).move_to(RIGHT * 2)
        label_b = MathTex("b", font_size=24).move_to(circle_b.get_center())

        self.play(Create(circle_a), Create(circle_b), Write(label_a), Write(label_b))
        self.wait(1)

        # Merge into one result circle
        result_circle = Circle(radius=0.8, color=YELLOW).move_to(ORIGIN)
        result_label = MathTex("Result", font_size=24).move_to(result_circle.get_center())
        self.play(
            Transform(circle_a, result_circle),
            Transform(circle_b, result_circle),
            Transform(label_a, result_label),
            Transform(label_b, result_label)
        )
        self.wait(1.5)

        # Narration: "We define the Tovan sum..."
        narration = Text("We define the Tovan sum of two whole numbers...", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)
        self.play(FadeOut(narration))

        # Chain example: 4 ⊕ (-1) ⊕ 2
        circle_4 = Circle(radius=0.4, color=RED).move_to(LEFT * 3)
        label_4 = MathTex("4", font_size=20).move_to(circle_4.get_center())
        circle_neg1 = Circle(radius=0.4, color=PURPLE).move_to(LEFT)
        label_neg1 = MathTex("-1", font_size=20).move_to(circle_neg1.get_center())
        circle_2 = Circle(radius=0.4, color=ORANGE).move_to(RIGHT * 2)
        label_2 = MathTex("2", font_size=20).move_to(circle_2.get_center())

        self.play(Create(circle_4), Create(circle_neg1), Create(circle_2))
        self.play(Write(label_4), Write(label_neg1), Write(label_2))
        self.wait(1)

        # Merge 4 and -1
        merged_circle = Circle(radius=0.6, color=DARK_BLUE).move_to(LEFT)
        label_merged = MathTex("-1", font_size=20).move_to(merged_circle.get_center())
        self.play(
            ReplacementTransform(circle_4, merged_circle),
            ReplacementTransform(label_4, label_merged),
            Transform(circle_neg1, merged_circle),
            Transform(label_neg1, label_merged)
        )
        self.wait(1)

        # Move merged circle to merge with 2
        self.play(
            merged_circle.animate.move_to(RIGHT * 2),
            label_merged.animate.move_to(RIGHT * 2)
        )
        self.wait(0.5)

        # Merge with 2
        final_circle = Circle(radius=0.6, color=DARK_BLUE).move_to(RIGHT * 2)
        final_label = MathTex("-1", font_size=20).move_to(final_circle.get_center())
        self.play(
            Transform(circle_2, final_circle),
            Transform(label_2, final_label)
        )
        self.wait(1.5)

        # Narration: "When chaining, we go left to right."
        narration2 = Text("When chaining, we go left to right.", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(2)
        self.play(FadeOut(narration2))

        # Narration: "Because -1 swallows everything..."
        narration3 = Text("Because -1 swallows everything it touches...", font_size=24)
        narration3.to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(2)
        self.play(FadeOut(narration3))

        # Formula expansion: (-1) + 5 + ((-1) × 5)
        formula_expanded = MathTex("(-1) + 5 + ((-1) \\times 5)", font_size=30)
        formula_expanded.move_to(ORIGIN)
        self.play(Transform(formula, formula_expanded))
        self.wait(2)

        # Step-by-step calculation
        step1 = MathTex("-1 + 5 - 5", font_size=30).move_to(ORIGIN)
        self.play(Transform(formula, step1))
        self.wait(1.5)

        step2 = MathTex("= -1", font_size=30).move_to(ORIGIN)
        self.play(Transform(formula, step2))
        self.wait(2)

        # Narration: "Even though 5 is added, the multiplication term..."
        narration4 = Text("Even though 5 is added, the multiplication term cancels it out...", font_size=24)
        narration4.to_edge(DOWN)
        self.play(Write(narration4))
        self.wait(2)
        self.play(FadeOut(narration4))

        # Nested structure: a ⊕ (b ⊕ c)
        nested = MathTex("a \\oplus (b \\oplus c)", font_size=36)
        nested.move_to(ORIGIN)
        self.play(Transform(formula, nested))
        self.wait(2)

        # Highlight inner parentheses
        highlight = SurroundingRectangle(MathTex("b \\oplus c", font_size=36), color=YELLOW, buff=0.1)
        self.play(Create(highlight))
        self.wait(1.5)

        # Narration: "When parentheses exist..."
        narration5 = Text("When parentheses exist, solve inside first.", font_size=24)
        narration5.to_edge(DOWN)
        self.play(Write(narration5))
        self.wait(2)
        self.play(FadeOut(narration5), FadeOut(highlight))

        # Final cleanup
        self.play(FadeOut(formula), FadeOut(title))
        self.wait(0.5)
