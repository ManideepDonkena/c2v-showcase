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
