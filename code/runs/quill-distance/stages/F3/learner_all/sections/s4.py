from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Understanding Quill Distance", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Points P and Q
        P = Dot([0, 0, 0], color=BLUE)
        Q = Dot([3, 2, 0], color=RED)
        P_label = MathTex("(0,0)", font_size=24).next_to(P, DOWN)
        Q_label = MathTex("(3,2)", font_size=24).next_to(Q, UR)

        self.play(FadeIn(P), FadeIn(Q), Write(P_label), Write(Q_label))
        self.wait(1)

        # Stepped path
        h_segments = []
        v_segments = []

        # Horizontal segments (3)
        for i in range(3):
            start = [i, 0, 0]
            end = [i+1, 0, 0]
            seg = Line(start, end, color=YELLOW)
            self.play(Create(seg))
            h_segments.append(seg)
            num = MathTex("1", font_size=24).move_to((start[0]+end[0])/2 * RIGHT + 0.3*UP)
            self.play(Write(num))
            self.wait(0.3)
            self.play(FadeOut(num))

        # Vertical segments (2)
        for i in range(2):
            start = [3, i, 0]
            end = [3, i+1, 0]
            seg = Line(start, end, color=YELLOW)
            self.play(Create(seg))
            v_segments.append(seg)
            num = MathTex("2", font_size=24).move_to((start[0], (start[1]+end[1])/2, 0) + 0.3*RIGHT)
            self.play(Write(num))
            self.wait(0.3)
            self.play(FadeOut(num))

        # Final equation
        eq = MathTex("3 + 4 = 7", font_size=40).to_edge(DOWN)
        self.play(Write(eq))
        self.wait(1.5)

        # Clear path and points
        self.play(
            *[FadeOut(seg) for seg in h_segments + v_segments],
            FadeOut(P), FadeOut(Q),
            FadeOut(P_label), FadeOut(Q_label),
            FadeOut(eq)
        )

        # Show central point and surrounding points lighting up
        center = Dot([0, 0, 0], color=WHITE)
        center_label = MathTex("(0,0)", font_size=24).next_to(center, DL)
        self.play(FadeIn(center), Write(center_label))
        self.wait(1)

        # Points at quill distance 4
        # Two points horizontally (cost 4+0=4)
        left_point = Dot([-4, 0, 0], color=GREEN)
        right_point = Dot([4, 0, 0], color=GREEN)
        self.play(FadeIn(left_point))
        self.wait(0.5)
        self.play(FadeIn(right_point))
        self.wait(0.5)

        # One point vertically up (cost 0+4=4)
        up_point = Dot([0, 4, 0], color=GREEN)
        up_point.shift(0.0 * RIGHT + -0.23 * UP)  # layout: separation vector
        self.play(FadeIn(up_point))
        self.wait(0.5)

        # One point vertically down (cost 0+4=4)
        down_point = Dot([0, -4, 0], color=GREEN)
        down_point.shift(0.0 * RIGHT + 0.23 * UP)  # layout: separation vector
        self.play(FadeIn(down_point))
        self.wait(1)

        # Narration text
        narration = Text("Distance 2 requires 2 sideways or 1 vertical step.", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)
        self.play(FadeOut(narration))

        # Show that distance 4 requires 4 sideways or 2 vertical steps
        narration2 = Text("Distance 4 requires 4 sideways or 2 vertical steps.", font_size=24).to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(2)
        self.play(FadeOut(narration2))

        # Final cleanup
        self.play(
            FadeOut(center), FadeOut(center_label),
            FadeOut(left_point), FadeOut(right_point),
            FadeOut(up_point), FadeOut(down_point),
            FadeOut(title)
        )
        self.wait(0.5)
