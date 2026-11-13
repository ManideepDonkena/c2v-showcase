from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Vector Addition", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Vector A (red)
        A = Arrow(start=[-4, -1, 0], end=[0, 1, 0], color=RED, stroke_width=8)
        A_label = MathTex("\\vec{A}", color=RED).next_to(A.get_end(), UR, buff=0.2)
        self.play(Create(A), Write(A_label))
        self.wait(1)

        # Vector B (blue) starting at origin
        B = Arrow(start=[-4, -1, 0], end=[-2, 2, 0], color=BLUE, stroke_width=8)
        B_label = MathTex("\\vec{B}", color=BLUE).next_to(B.get_end(), UR, buff=0.2)
        self.play(Create(B), Write(B_label))
        self.wait(1)

        # Move B to tail of A
        self.play(B.animate.shift(A.get_start() - B.get_start()),
                  B_label.animate.shift(A.get_start() - B.get_start()))
        self.play(B.animate.shift(A.get_start() - B.get_start()),
                  B_label.animate.shift(A.get_start() - B.get_start()))
        self.play(B.animate.shift(A.get_start() - B.get_start()),
                  B_label.animate.shift(A.get_start() - B.get_start()))
        B_copy = B.copy()
        self.play(
            Transform(B, B_copy),
            B.animate.shift(A.get_end() - B.get_start()),
            run_time=2
        )
        self.wait(1)

        # Resultant vector C (green)
        C = Arrow(start=[-4, -1, 0], end=[-2, 2, 0], color=GREEN, stroke_width=8)
        C_label = MathTex("\\vec{A} + \\vec{B}", color=GREEN).next_to(C.get_end(), DL, buff=0.2)
        self.play(Create(C), Write(C_label))
        self.wait(1)

        # Clear explanation text
        head_to_tail = Text("Head-to-tail method", font_size=24).to_edge(DOWN)
        self.play(Write(head_to_tail))
        self.wait(1.5)

        # Fade out all objects
        self.play(
            FadeOut(A), FadeOut(B), FadeOut(C),
            FadeOut(A_label), FadeOut(B_label), FadeOut(C_label),
            FadeOut(head_to_tail), FadeOut(title)
        )
        self.wait(0.5)
