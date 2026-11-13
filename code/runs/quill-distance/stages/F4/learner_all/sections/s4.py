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
            num = MathTex("1", font_size=24).move_to((start[0]+end[0])/2 * RIGHT + 0.3 * UP)
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
            num = MathTex("2", font_size=24).move_to((start[0], (start[1]+end[1])/2, 0) + 0.3 * LEFT)
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
        self.wait(0.5)

        # Show central point and four specific points lighting up
        center = Dot([0, 0, 0], color=WHITE)
        center_label = MathTex("(0,0)", font_size=24).next_to(center, DL)
        self.play(FadeIn(center), Write(center_label))
        self.wait(1)

        # Points at quill distance 6
        point1 = Dot([6, 0, 0], color=GREEN)
        point2 = Dot([-6, 0, 0], color=GREEN)
        point3 = Dot([0, 6, 0], color=GREEN)
        point4 = Dot([0, -6, 0], color=GREEN)

        # Animate lighting up in sequence
        self.play(FadeIn(point1))
        self.wait(0.5)
        self.play(FadeIn(point2))
        self.wait(0.5)
        point3.shift(0.0 * RIGHT + -2.23 * UP)  # layout: separation vector
        self.play(FadeIn(point3))
        self.wait(0.5)
        point4.shift(0.0 * RIGHT + 2.23 * UP)  # layout: separation vector
        self.play(FadeIn(point4))
        self.wait(1)

        # Narration text
        narration = Text("Just as distance 2 requires 2 sideways or 1 vertical step, distance 6 requires 6 sideways or 3 vertical steps.", font_size=24).to_edge(DOWN)
        narration.shift(1.36 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(narration))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(center), FadeOut(center_label),
            FadeOut(point1), FadeOut(point2), FadeOut(point3), FadeOut(point4),
            FadeOut(narration),
            FadeOut(title)
        )
        self.wait(0.5)
