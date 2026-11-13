from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Equilateral Case", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Triangle
        triangle = Triangle().scale(1.5).move_to(UP * 1.2)
        triangle.set_stroke(width=8)
        side_label = MathTex("5").next_to(triangle, DOWN)
        self.play(Create(triangle), Write(side_label))
        self.wait(1)

        # Condition
        condition = MathTex("2 \\times 5 \\leq 3 \\times 5", font_size=40)
        condition.next_to(side_label, DOWN, buff=0.6)
        self.play(Write(condition))
        self.wait(1.5)

        # Check validity
        check = MathTex("10 \\leq 15").next_to(condition, DOWN, buff=0.4)
        self.play(Write(check))
        self.wait(1.5)

        # Animation: green and bounce
        self.play(
            triangle.animate.set_fill(GREEN, opacity=0.8).scale(1.05),
            run_time=0.3
        )
        self.play(triangle.animate.scale(1/1.05), run_time=0.3)
        self.wait(1)

        # Narration text
        narration = Text("Every equilateral triangle is mirthful", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        self.play(FadeOut(title, triangle, side_label, condition, check, narration))
        self.wait(0.5)
