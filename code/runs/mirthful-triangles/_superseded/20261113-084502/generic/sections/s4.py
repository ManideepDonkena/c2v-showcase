from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Worked Examples", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Triangle 1: 4, 5, 6 (green check)
        triangle1 = Polygon(
            [0, 0, 0], [4, 0, 0], [2, 3, 0],
            color=GREEN, fill_color=GREEN, fill_opacity=0.3
        ).scale(0.8).shift(LEFT * 2)
        label1 = Text("4, 5, 6", font_size=24).next_to(triangle1, DOWN)
        check1 = Text("✓", color=GREEN, font_size=40).next_to(label1, RIGHT)

        # Triangle 2: 3, 4, 5 (red X)
        triangle2 = Polygon(
            [0, 0, 0], [5, 0, 0], [2.5, 3, 0],
            color=RED, fill_color=RED, fill_opacity=0.3
        ).scale(0.8).shift(RIGHT * 2)
        label2 = Text("3, 4, 5", font_size=24).next_to(triangle2, DOWN)
        cross2 = Text("✗", color=RED, font_size=40).next_to(label2, RIGHT)

        # Show triangles
        self.play(Create(triangle1), Write(label1), Write(check1))
        self.wait(0.5)
        self.play(Create(triangle2), Write(label2), Write(cross2))
        self.wait(1)

        # Fade out labels and triangles
        self.play(FadeOut(label1), FadeOut(check1), FadeOut(label2), FadeOut(cross2))

        # Show calculations for triangle 1: 4,5,6
        calc1 = MathTex("2 \\times 6 = 12", "\\leq", "3 \\times 4 = 12").scale(0.8)
        calc1.arrange(RIGHT, buff=0.5)
        calc1.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(calc1))
        self.wait(1)

        # Fade out first calculation
        self.play(FadeOut(calc1))

        # Show calculations for triangle 2: 3,4,5
        calc2 = MathTex("2 \\times 5 = 10", ">", "3 \\times 3 = 9").scale(0.8)
        calc2.arrange(RIGHT, buff=0.5)
        calc2.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(calc2))
        self.wait(1.5)

        # Narration text
        narration = Text("Consider sides 4, 5, 6: twice the longest is 12, three times the shortest is 12, so it is mirthful.", font_size=24)
        narration.to_edge(UP).shift(DOWN * 3.5)
        self.play(Write(narration))
        self.wait(1)

        self.play(FadeOut(narration))

        narration2 = Text("But for 3, 4, 5: twice the longest is 10, which exceeds nine, so it is not mirthful.", font_size=24)
        narration2.to_edge(UP).shift(DOWN * 3.5)
        self.play(Write(narration2))
        self.wait(1.5)

        self.play(FadeOut(narration2), FadeOut(calc2))

        # Rule 3 reminder
        rule3 = Text("Rule 3: Middle side doesn't matter", font_size=24).to_edge(UP).shift(DOWN * 3.5)
        self.play(Write(rule3))
        self.wait(1.5)

        self.play(FadeOut(rule3), FadeOut(triangle1), FadeOut(triangle2))

        self.wait(0.5)
