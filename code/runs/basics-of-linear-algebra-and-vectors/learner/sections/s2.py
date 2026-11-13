from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Vector Addition", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Vector A (red)
        A = Arrow(start=[-3, -1, 0], end=[0, 2, 0], color=RED, buff=0)
        A_label = MathTex("A", color=RED).next_to(A.get_end(), UR, buff=0.1)
        self.play(Create(A), Write(A_label))
        self.wait(0.5)

        # Vector B (blue) starting at tail of A
        B = Arrow(start=[0, 2, 0], end=[3, 5, 0], color=BLUE, buff=0)
        B_label = MathTex("B", color=BLUE).next_to(B.get_end(), UR, buff=0.1)
        B.shift(0.0 * RIGHT + -2.03 * UP)  # layout: separation vector
        B_label.shift(0.0 * RIGHT + -1.59 * UP)  # layout: separation vector
        self.play(Create(B), Write(B_label))
        self.wait(0.5)

        # Show head-to-tail method
        C = Arrow(start=[-3, -1, 0], end=[3, 5, 0], color=GREEN, buff=0)
        C_label = MathTex("A + B", color=GREEN).next_to(C.get_end(), DR, buff=0.1)
        C.shift(0.0 * RIGHT + -1.15 * UP)  # layout: separation vector
        self.play(Create(C), Write(C_label))
        self.wait(1)

        # Show text: head-to-tail method
        method_text = Text("Head-to-Tail Method", font_size=24)
        method_text.to_edge(DOWN)
        self.play(Write(method_text))
        self.wait(1.5)
        self.play(FadeOut(method_text))

        # Show perpendicular vectors (90 degrees)
        A_perp = Arrow(start=[-2, -1, 0], end=[1, 2, 0], color=RED, buff=0)
        B_perp = Arrow(start=[1, 2, 0], end=[1, -1, 0], color=BLUE, buff=0)
        perp_label = Text("Perpendicular (90°)", font_size=24)
        perp_label.to_edge(DOWN)
        self.play(Transform(A, A_perp), Transform(B, B_perp))
        self.wait(0.5)

        # Show right angle marker
        right_angle = Square(side_length=0.3, color=WHITE).move_to([1, 2, 0])
        self.play(Create(right_angle))
        self.wait(0.5)
        self.play(Write(perp_label))
        self.wait(1.5)
        self.play(FadeOut(perp_label), FadeOut(right_angle))

        # Show parallel vectors (0 or 180 degrees)
        A_par = Arrow(start=[-2, -1, 0], end=[1, 2, 0], color=RED, buff=0)
        B_par = Arrow(start=[1, 2, 0], end=[4, 5, 0], color=BLUE, buff=0)
        parallel_label = Text("Parallel (0° or 180°)", font_size=24)
        parallel_label.to_edge(DOWN)
        self.play(Transform(A, A_par), Transform(B, B_par))
        self.wait(0.5)

        # Show angle 0 degrees
        self.play(Write(parallel_label))
        self.wait(1.5)
        self.play(FadeOut(parallel_label))

        # Show vectors overlapping (parallel)
        A_over = Arrow(start=[-2, -1, 0], end=[4, 5, 0], color=RED, buff=0)
        B_over = Arrow(start=[-2, -1, 0], end=[4, 5, 0], color=BLUE, buff=0)
        self.play(Transform(A, A_over), Transform(B, B_over))
        self.wait(1.5)

        # Fade out all
        self.play(FadeOut(A), FadeOut(B), FadeOut(C), FadeOut(A_label), FadeOut(B_label), FadeOut(C_label), FadeOut(title))
        self.wait(0.5)
