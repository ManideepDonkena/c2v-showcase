from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Shape of Distance 2", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid and center point
        grid = NumberPlane(x_range=[-7, 7], y_range=[-4, 4], faded_line_ratio=1)
        self.play(Create(grid))
        self.wait(0.5)

        C = Dot([0, 0, 0], color=WHITE)
        c_label = MathTex("(0,0)", font_size=24).next_to(C, DOWN, buff=0.2)
        self.play(FadeIn(C), Write(c_label))
        self.wait(0.5)

        # First point: (2,0)
        p1 = Dot([2, 0, 0], color=YELLOW)
        p1_label = MathTex("(2,0)", font_size=24).next_to(p1, DOWN, buff=0.2)
        calc1 = MathTex("2 + 0 = 2", font_size=24).next_to(p1_label, DOWN, buff=0.2)
        self.play(FadeIn(p1), Write(p1_label))
        self.wait(0.5)
        self.play(Write(calc1))
        self.wait(1)

        # Second point: (-2,0)
        p2 = Dot([-2, 0, 0], color=YELLOW)
        p2_label = MathTex("(-2,0)", font_size=24).next_to(p2, DOWN, buff=0.2)
        calc2 = MathTex("2 + 0 = 2", font_size=24).next_to(p2_label, DOWN, buff=0.2)
        self.play(FadeIn(p2), Write(p2_label))
        self.wait(0.5)
        self.play(Write(calc2))
        self.wait(1)

        # Third point: (0,1)
        p3 = Dot([0, 1, 0], color=YELLOW)
        p3_label = MathTex("(0,1)", font_size=24).next_to(p3, UP, buff=0.2)
        calc3 = MathTex("0 + 1 = 2", font_size=24).next_to(p3_label, DOWN, buff=0.2)
        self.play(FadeIn(p3), Write(p3_label))
        self.wait(0.5)
        calc3.shift(0.0 * RIGHT + -0.31 * UP)  # layout: separation vector
        self.play(Write(calc3))
        self.wait(1)

        # Fourth point: (0,-1)
        p4 = Dot([0, -1, 0], color=YELLOW)
        p4_label = MathTex("(0,-1)", font_size=24).next_to(p4, DOWN, buff=0.2)
        calc4 = MathTex("0 + 1 = 2", font_size=24).next_to(p4_label, DOWN, buff=0.2)
        self.play(FadeIn(p4), Write(p4_label))
        self.wait(0.5)
        self.play(Write(calc4))
        self.wait(1)

        # Dim nearby point (1,1) with cost 3
        p5 = Dot([1, 1, 0], color=GRAY)
        p5_label = MathTex("(1,1)", font_size=24).next_to(p5, UP, buff=0.2)
        cost_label = MathTex("Cost: 3", font_size=24).next_to(p5_label, DOWN, buff=0.2)
        self.play(FadeIn(p5), Write(p5_label))
        self.wait(0.5)
        cost_label.shift(0.0 * RIGHT + -0.31 * UP)  # layout: separation vector
        self.play(Write(cost_label))
        self.wait(1.5)

        # Narration text
        narration = Text("Consider all points exactly at quill distance 2 from the center.", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        self.play(FadeOut(narration))

        narration2 = Text("These include two steps sideways, or just one step up or down.", font_size=24).to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(2)

        self.play(FadeOut(narration2))

        narration3 = Text("Points like (1,1) are further away because their cost is 3.", font_size=24).to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(2)

        self.play(FadeOut(narration3))

        # Final cleanup
        self.play(
            FadeOut(p1), FadeOut(p2), FadeOut(p3), FadeOut(p4), FadeOut(p5),
            FadeOut(p1_label), FadeOut(p2_label), FadeOut(p3_label), FadeOut(p4_label), FadeOut(p5_label),
            FadeOut(calc1), FadeOut(calc2), FadeOut(calc3), FadeOut(calc4), FadeOut(cost_label),
            FadeOut(C), FadeOut(c_label), FadeOut(grid), FadeOut(title)
        )
        self.wait(0.5)
