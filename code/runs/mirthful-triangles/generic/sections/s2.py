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
        triangle_group = VGroup(triangle, side_label)

        # Show triangle
        self.play(Create(triangle), Write(side_label))
        self.wait(1)

        # Condition
        condition = MathTex("2 \\times 5 \\leq 3 \\times 5", font_size=40)
        condition.to_edge(DOWN)
        self.play(Write(condition))
        self.wait(1)

        # Evaluate
        eval_text = MathTex("10 \\leq 15", font_size=40)
        eval_text.next_to(condition, DOWN, buff=0.3)
        eval_text.shift(0.0 * RIGHT + 0.28 * UP)  # layout: separation vector
        self.play(Write(eval_text))
        self.wait(1)

        # Green and bounce
        self.play(triangle.animate.set_fill(GREEN, opacity=0.8), run_time=0.5)
        triangle_copy = triangle.copy()
        self.play(
            triangle.animate.shift(DOWN * 0.2),
            triangle_copy.animate.shift(UP * 0.2),
            run_time=0.3
        )
        self.play(
            triangle.animate.shift(UP * 0.2),
            triangle_copy.animate.shift(DOWN * 0.2),
            run_time=0.3
        )
        self.wait(1)

        # Narration text
        narration1 = Text("Every equilateral triangle is mirthful", font_size=24).to_edge(UP, buff=0.5)
        narration1.shift(0.0 * RIGHT + 0.49 * UP)  # layout: separation vector
        self.play(Write(narration1))
        self.wait(1)
        self.play(FadeOut(narration1))

        narration2 = Text("because longest = shortest", font_size=24).to_edge(UP, buff=0.5)
        narration2.shift(0.0 * RIGHT + 0.48 * UP)  # layout: separation vector
        self.play(Write(narration2))
        self.wait(1)
        self.play(FadeOut(narration2))

        # Fade out
        self.play(
            FadeOut(triangle_group),
            FadeOut(condition),
            FadeOut(eval_text),
            FadeOut(title)
        )
        self.wait(0.5)
