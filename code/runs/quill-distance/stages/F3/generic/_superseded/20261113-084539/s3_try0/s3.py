from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Shape of Distance 2", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid and center point
        grid = NumberPlane(x_range=[-7, 7], y_range=[-4, 4], faded_line_ratio=1)
        grid.set_opacity(0.3)
        self.play(Create(grid))

        C = Dot([0, 0, 0], color=YELLOW)
        c_label = Tex("C", font_size=24).next_to(C, DL, buff=0.1)
        self.play(FadeIn(C), Write(c_label))
        self.wait(0.5)

        # Point (2,0) with calculation
        p1 = Dot([2, 0], color=GREEN)
        p1_label = Tex("(2,0)", font_size=24).next_to(p1, UR, buff=0.1)
        calc1 = MathTex("2 + 0 = 2", font_size=30).to_edge(DOWN)
        self.play(FadeIn(p1), Write(p1_label))
        self.wait(0.5)
        self.play(Write(calc1))
        self.wait(1)

        # Point (-2,0) with calculation
        p2 = Dot([-2, 0], color=GREEN)
        p2_label = Tex("(-2,0)", font_size=24).next_to(p2, UL, buff=0.1)
        self.play(FadeIn(p2), Write(p2_label))
        self.wait(0.5)
        self.play(Transform(calc1, MathTex("0 + 2 = 2", font_size=30).to_edge(DOWN)))
        self.wait(1)

        # Point (0,1) with calculation
        p3 = Dot([0, 1], color=GREEN)
        p3_label = Tex("(0,1)", font_size=24).next_to(p3, UP, buff=0.1)
        self.play(FadeIn(p3), Write(p3_label))
        self.wait(0.5)
        self.play(Transform(calc1, MathTex("0 + 2 = 2", font_size=30).to_edge(DOWN)))
        self.wait(1)

        # Point (0,-1) with calculation
        p4 = Dot([0, -1], color=GREEN)
        p4_label = Tex("(0,-1)", font_size=24).next_to(p4, DOWN, buff=0.1)
        self.play(FadeIn(p4), Write(p4_label))
        self.wait(0.5)
        self.play(Transform(calc1, MathTex("0 + 2 = 2", font_size=30).to_edge(DOWN)))
        self.wait(1)

        # Dim point (1,1) with cost
        p5 = Dot([1, 1], color=GRAY)
        p5_label = Tex("(1,1)", font_size=24).next_to(p5, UR, buff=0.1)
        cost_label = Tex("Cost: 3", font_size=24).next_to(p5_label, DOWN, buff=0.1)
        self.play(FadeIn(p5), Write(p5_label))
        self.wait(0.5)
        self.play(Write(cost_label))
        self.wait(1.5)

        # Narration text
        narration = Text("Consider all points exactly at quill distance 2 from the center.", font_size=24)
        narration.to_edge(UP, buff=0.5)
        self.play(Transform(title, narration))
        self.wait(1.5)

        # Final narration
        final_narration = Text("These include two steps sideways, or just one step up or down.", font_size=24)
        final_narration.to_edge(UP, buff=0.5)
        self.play(Transform(title, final_narration))
        self.wait(1.5)

        # Final note
        note = Text("Points like (1,1) are further away because their cost is 3.", font_size=24)
        note.to_edge(UP, buff=0.5)
        self.play(Transform(title, note))
        self.wait(1.5)

        self.play(FadeOut(title, p1, p2, p3, p4, p5, c_label, p1_label, p2_label, p3_label, p4_label, p5_label, cost_label, calc1, grid))
