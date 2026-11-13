from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Equilateral Case", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Triangle
        triangle = Triangle().scale(1.5).move_to(ORIGIN)
        triangle.set_stroke(width=8)
        side_label = MathTex("5").next_to(triangle, DOWN)
        self.play(Create(triangle), Write(side_label))
        self.wait(1)

        # Condition
        condition = MathTex("2 \\times 5 \\leq 3 \\times 5", font_size=40)
        condition.next_to(triangle, DOWN, buff=1.2)
        self.play(Write(condition))
        self.wait(1.5)

        # Check validity
        check = MathTex("10 \\leq 15").next_to(condition, DOWN, buff=0.5)
        self.play(Write(check))
        self.wait(1.5)

        # Animation: green and bounce
        self.play(
            triangle.animate.set_fill(GREEN, opacity=0.8),
            triangle.animate.scale(1.05),
            run_time=0.3
        )
        self.play(triangle.animate.scale(1/1.05), run_time=0.3)
        self.wait(1)

        # Narration text
        narration = Text("Every equilateral triangle is mirthful", font_size=24).to_edge(DOWN)
        narration.shift(0.0 * RIGHT + 0.49 * UP)  # layout: separation vector
        self.play(Write(narration))
        self.wait(2)

        # Fade out existing objects
        self.play(FadeOut(title, triangle, side_label, condition, check, narration))
        self.wait(0.5)

        # New triangle with sides 5, 7, 8
        new_triangle = Triangle().scale(1.5).move_to(ORIGIN)
        new_triangle.set_stroke(width=8)
        label_5 = MathTex("5").next_to(new_triangle, DOWN)
        label_7 = MathTex("7").next_to(new_triangle, LEFT)
        label_8 = MathTex("8").next_to(new_triangle, RIGHT)
        self.play(Create(new_triangle), Write(label_5), Write(label_7), Write(label_8))
        self.wait(1)

        # Say the rule
        rule_text = Text("Check the rule: Is twice the longest side at most three times the shortest?", font_size=24).to_edge(DOWN)
        self.play(Write(rule_text))
        self.wait(2)

        # Show calculation
        calc = MathTex("2 \\times 8 \\leq 3 \\times 5", font_size=40).move_to(UP * 1.5)
        self.play(Write(calc))
        self.wait(1.5)

        # Resolve the inequality
        result = MathTex("16 \\leq 15", font_size=40).next_to(calc, DOWN, buff=0.5)
        self.play(Write(result))
        self.wait(1.5)

        # Red X or pulse to indicate failure
        cross = Cross(result, color=RED, stroke_width=10)
        self.play(Create(cross))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(new_triangle, label_5, label_7, label_8, calc, result, cross, rule_text))
        self.wait(0.5)
