from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Vector Addition", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Vector A (red)
        A = Arrow(start=[-4, -1, 0], end=[0, 1, 0], color=RED, stroke_width=8)
        A_label = MathTex("\\vec{A}", font_size=30).next_to(A, UR, buff=0.2)
        self.play(Create(A), Write(A_label))
        self.wait(1)

        # Vector B (blue) starting at origin
        B = Arrow(start=[0, 0, 0], end=[2, 2, 0], color=BLUE, stroke_width=8)
        B_label = MathTex("\\vec{B}", font_size=30).next_to(B, UR, buff=0.2)
        B.shift(0.19 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(B), Write(B_label))
        self.wait(1)

        # Move B to tail of A
        B_copy = B.copy()
        self.play(B_copy.animate.shift(A.get_end() - B.get_start()))
        self.wait(1)

        # Resultant vector C (green)
        C = Arrow(start=A.get_start(), end=B_copy.get_end(), color=GREEN, stroke_width=8)
        C_label = MathTex("\\vec{A} + \\vec{B}", font_size=30).next_to(C, UR, buff=0.2)
        self.play(Create(C), Write(C_label))
        self.wait(1)

        # Narration text
        method_text = Text("Head-to-tail method", font_size=24).to_edge(DOWN)
        self.play(Write(method_text))
        self.wait(1)
        
        self.play(FadeOut(method_text))
        
        result_text = Text("Resultant vector", font_size=24).to_edge(DOWN)
        self.play(Write(result_text))
        self.wait(1)
        
        self.play(FadeOut(result_text))
        
        # Final wait
        self.wait(1)
