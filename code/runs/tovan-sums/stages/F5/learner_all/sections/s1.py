from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Definition and Formula", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Main expression: a ⊕ b
        a_op_b = MathTex("a \\oplus b", font_size=40)
        a_op_b.move_to(ORIGIN)
        self.play(Write(a_op_b))
        self.wait(1)

        # Arrow pointing down to formula
        arrow = Arrow(start=a_op_b.get_bottom(), end=a_op_b.get_bottom() + DOWN * 1.5, buff=0.2)
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Formula: a + b + (a × b)
        formula = MathTex("a + b + (a \\times b)", font_size=40)
        formula.next_to(arrow, DOWN, buff=0.3)
        self.play(Write(formula))
        self.wait(1.5)

        # Fade out formula and arrow
        self.play(FadeOut(formula), FadeOut(arrow))

        # Circles for a and b
        circle_a = Circle(radius=0.6, color=BLUE).move_to(LEFT * 2)
        circle_b = Circle(radius=0.6, color=GREEN).move_to(RIGHT * 2)
        label_a = Text("a", font_size=24).move_to(circle_a.get_center())
        label_b = Text("b", font_size=24).move_to(circle_b.get_center())

        self.play(Create(circle_a), Create(circle_b), Write(label_a), Write(label_b))
        self.wait(1)

        # Merge into one circle
        merged_circle = Circle(radius=1.2, color=YELLOW).move_to(ORIGIN)
        result_label = Text("Result", font_size=24).move_to(merged_circle.get_center())
        self.play(TransformFromCopy(circle_a, merged_circle), TransformFromCopy(circle_b, merged_circle))
        self.wait(0.5)
        result_label.shift(0.0 * RIGHT + 0.44 * UP)  # layout: separation vector
        self.play(Write(result_label))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(a_op_b), FadeOut(circle_a), FadeOut(circle_b), FadeOut(label_a), FadeOut(label_b), FadeOut(merged_circle), FadeOut(result_label), FadeOut(title))
        self.wait(0.5)

        # Chain example
        circle_3 = Circle(radius=0.6, color=BLUE).move_to(LEFT * 3)
        circle_neg1 = Circle(radius=0.6, color=RED).move_to(LEFT)
        circle_7 = Circle(radius=0.6, color=GREEN).move_to(RIGHT * 2)
        label_3 = Text("3", font_size=24).move_to(circle_3.get_center())
        label_neg1 = Text("(-1)", font_size=24).move_to(circle_neg1.get_center())
        label_7 = Text("7", font_size=24).move_to(circle_7.get_center())

        self.play(Create(circle_3), Create(circle_neg1), Create(circle_7), Write(label_3), Write(label_neg1), Write(label_7))
        self.wait(0.5)
        self.play(Write(Text("When chaining, we go left to right.", font_size=24).to_edge(DOWN)))
        self.wait(1)

        # Merge first two circles
        merged_chain = Circle(radius=1.2, color=DARK_BROWN).move_to(LEFT)
        merged_label = Text("-1", font_size=24).move_to(merged_chain.get_center())
        self.play(TransformFromCopy(circle_3, merged_chain), TransformFromCopy(circle_neg1, merged_chain))
        self.wait(0.5)
        merged_label.shift(0.0 * RIGHT + 0.42 * UP)  # layout: separation vector
        self.play(Write(merged_label))
        self.wait(1)

        # Move to merge with third circle
        self.play(merged_chain.animate.move_to(RIGHT * 2), merged_label.animate.move_to(merged_chain.get_center()))
        self.wait(0.5)
        self.play(TransformFromCopy(circle_7, merged_chain))
        self.wait(0.5)
        self.play(Write(Text("Because -1 swallows everything it touches, the entire chain collapses to -1.", font_size=24).to_edge(DOWN)))
        self.wait(2)

        # Fade out chain
        self.play(FadeOut(circle_3), FadeOut(circle_neg1), FadeOut(circle_7), FadeOut(label_3), FadeOut(label_neg1), FadeOut(label_7), FadeOut(merged_chain), FadeOut(merged_label))
        self.wait(0.5)

        # Nested structure example
        nested_expr = MathTex("5 \\oplus (0 \\oplus 8)", font_size=40)
        nested_expr.to_edge(UP)
        self.play(Write(nested_expr))
        self.wait(1)
        self.play(Write(Text("When parentheses exist, you must solve the inside group before applying the outside operation, just like standard order of operations.", font_size=24).to_edge(DOWN)))
        self.wait(2)

        # Highlight inner parentheses
        inner_parentheses = SurroundingRectangle(MathTex("0 \\oplus 8", font_size=40), color=YELLOW)
        self.play(Create(inner_parentheses))
        self.wait(1)
        self.play(FadeOut(inner_parentheses))

        # Worked example
        step1 = MathTex("0 \\oplus 8 = 8", font_size=36)
        step1.next_to(nested_expr, DOWN, buff=0.5)
        self.play(Write(step1))
        self.wait(1)

        step2 = MathTex("5 \\oplus 8 = 5 + 8 + (5 \\times 8) = 13 + 40 = 53", font_size=36)
        step2.next_to(step1, DOWN, buff=0.5)
        self.play(Write(step2))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(nested_expr), FadeOut(step1), FadeOut(step2))
        self.wait(0.5)
