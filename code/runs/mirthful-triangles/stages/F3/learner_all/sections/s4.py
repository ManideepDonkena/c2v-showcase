from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Worked Examples", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Left triangle: 4, 5, 6 (green check)
        left_tri = Triangle().scale(1.2).shift(LEFT * 3)
        left_tri.set_stroke(color=GREEN, width=8)
        left_labels = VGroup(
            MathTex("4").next_to(left_tri, DOWN, buff=0.2),
            MathTex("5").next_to(left_tri, LEFT, buff=0.2),
            MathTex("6").next_to(left_tri, RIGHT, buff=0.2)
        )
        left_group = VGroup(left_tri, left_labels)

        # Right triangle: 3, 4, 5 (red X)
        right_tri = Triangle().scale(1.2).shift(RIGHT * 3)
        right_tri.set_stroke(color=RED, width=8)
        right_labels = VGroup(
            MathTex("3").next_to(right_tri, DOWN, buff=0.2),
            MathTex("4").next_to(right_tri, LEFT, buff=0.2),
            MathTex("5").next_to(right_tri, RIGHT, buff=0.2)
        )
        right_group = VGroup(right_tri, right_labels)

        # Show triangles
        self.play(Create(left_tri), Create(right_tri))
        self.play(Write(left_labels), Write(right_labels))
        self.wait(1)

        # Calculations for left triangle: 12 ≤ 12
        calc1 = MathTex("2 \\times 6 =", "12", "\\leq", "3 \\times 4 =", "12").scale(1.2)
        calc1.next_to(left_tri, DOWN, buff=0.8)
        self.play(Write(calc1))
        self.wait(1)

        # Calculations for right triangle: 10 > 9
        calc2 = MathTex("2 \\times 5 =", "10", ">", "3 \\times 3 =", "9").scale(1.2)
        calc2.next_to(right_tri, DOWN, buff=0.8)
        self.play(Write(calc2))
        self.wait(1.5)

        # Narration text
        narration1 = Text("Consider sides 4, 5, 6:", font_size=24).to_edge(DOWN).shift(UP * 0.5)
        narration2 = Text("twice the longest is 12, three times the shortest is 12", font_size=24).next_to(narration1, DOWN)
        self.play(Write(narration1), Write(narration2))
        self.wait(2)

        self.play(FadeOut(narration1), FadeOut(narration2))

        # New triangle: 2, 3, 4
        new_tri = Triangle().scale(1.2).shift(LEFT * 3)
        new_tri.set_stroke(color=WHITE, width=8)
        new_labels = VGroup(
            MathTex("2").next_to(new_tri, DOWN, buff=0.2),
            MathTex("3").next_to(new_tri, LEFT, buff=0.2),
            MathTex("4").next_to(new_tri, RIGHT, buff=0.2)
        )
        new_group = VGroup(new_tri, new_labels)

        self.play(Transform(left_group, new_group))
        self.wait(0.5)

        # Show rule question
        rule_text = Text("Check the rule:", font_size=24).to_edge(DOWN).shift(UP * 0.5)
        rule_question = Text("Is twice the longest side at most three times the shortest?", font_size=24).next_to(rule_text, DOWN)
        self.play(Write(rule_text), Write(rule_question))
        self.wait(2)

        # Show calculation: 2×4 ≤ 3×2 → 8 ≤ 6
        calc3 = MathTex("2 \\times 4 =", "8", "\\leq", "3 \\times 2 =", "6").scale(1.2)
        calc3.next_to(new_tri, DOWN, buff=0.8)
        calc1.shift(0.0 * RIGHT + 0.64 * UP)  # layout: separation vector
        self.play(Write(calc3))
        self.wait(1)

        # Red X or pulse to indicate failure
        red_x = Cross(calc3, color=RED, stroke_width=10)
        self.play(Create(red_x))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(left_tri),
            FadeOut(right_tri),
            FadeOut(left_labels),
            FadeOut(right_labels),
            FadeOut(calc1),
            FadeOut(calc2),
            FadeOut(calc3),
            FadeOut(red_x),
            FadeOut(rule_text),
            FadeOut(rule_question)
        )
        self.wait(0.5)
