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
        c_label = Tex("C").next_to(C, DOWN, buff=0.2)
        self.play(FadeIn(C), Write(c_label))
        self.wait(0.5)

        # Points at quill distance 2
        p1 = Dot([2, 0, 0], color=YELLOW)
        p1_label = Tex("(2, 0)").next_to(p1, DOWN, buff=0.2)
        calc1 = MathTex("2 + 0 = 2").move_to(UP * 2)
        self.play(FadeIn(p1), Write(p1_label))
        self.wait(0.5)
        self.play(Write(calc1))
        self.wait(1.0)
        self.play(FadeOut(calc1))

        p2 = Dot([-2, 0, 0], color=YELLOW)
        p2_label = Tex("(-2, 0)").next_to(p2, DOWN, buff=0.2)
        calc2 = MathTex("2 + 0 = 2").move_to(UP * 2)
        self.play(FadeIn(p2), Write(p2_label))
        self.wait(0.5)
        self.play(Write(calc2))
        self.wait(1.0)
        self.play(FadeOut(calc2))

        p3 = Dot([0, 1, 0], color=YELLOW)
        p3_label = Tex("(0, 1)").next_to(p3, RIGHT, buff=0.2)
        calc3 = MathTex("0 + 2 = 2").move_to(UP * 2)
        self.play(FadeIn(p3), Write(p3_label))
        self.wait(0.5)
        self.play(Write(calc3))
        self.wait(1.0)
        self.play(FadeOut(calc3))

        p4 = Dot([0, -1, 0], color=YELLOW)
        p4_label = Tex("(0, -1)").next_to(p4, LEFT, buff=0.2)
        calc4 = MathTex("0 + 2 = 2").move_to(UP * 2)
        self.play(FadeIn(p4), Write(p4_label))
        self.wait(0.5)
        self.play(Write(calc4))
        self.wait(1.0)
        self.play(FadeOut(calc4))

        # Show nearby point (1,1) as dim
        p5 = Dot([1, 1, 0], color=GREY)
        p5_label = Tex("(1, 1)").next_to(p5, UR, buff=0.2)
        cost_label = Tex("Cost: 3").next_to(p5_label, DOWN, buff=0.2)
        p5.shift(0.0 * RIGHT + 0.48 * UP)  # layout: separation vector
        self.play(FadeIn(p5), Write(p5_label))
        self.wait(0.5)
        cost_label.shift(0.47 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(cost_label))
        self.wait(1.5)
        self.play(FadeOut(cost_label))

        # Narration text
        narration = Text("Consider all points exactly at quill distance 2 from the center.", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2.0)
        self.play(FadeOut(narration))

        narration2 = Text("These include two steps sideways, or just one step up or down.", font_size=24).to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(2.0)
        self.play(FadeOut(narration2))

        narration3 = Text("Points like (1,1) are further away because their cost is 3.", font_size=24).to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(2.0)
        self.play(FadeOut(narration3))

        # Final cleanup
        self.play(
            FadeOut(p1), FadeOut(p2), FadeOut(p3), FadeOut(p4), FadeOut(p5),
            FadeOut(p1_label), FadeOut(p2_label), FadeOut(p3_label), FadeOut(p4_label), FadeOut(p5_label),
            FadeOut(C), FadeOut(c_label), FadeOut(grid), FadeOut(title)
        )
        self.wait(0.5)
