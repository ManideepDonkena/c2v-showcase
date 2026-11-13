from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Symmetry and Direction", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid points A and B
        A = Dot([0, 0, 0], color=BLUE)
        B = Dot([2, 1, 0], color=RED)
        label_A = Tex("A").next_to(A, DOWN)
        label_B = Tex("B").next_to(B, UP)

        self.play(FadeIn(A), FadeIn(B), Write(label_A), Write(label_B))
        self.wait(0.5)

        # Path from A to B
        path1 = Line(A.get_center(), B.get_center(), color=YELLOW)
        self.play(Create(path1))
        self.wait(0.5)

        # Cost calculation for A to B: 2 horizontal + 2 vertical = 4
        cost_text1 = MathTex("2 + 2 = 4", font_size=30).next_to(path1, UP)
        self.play(Write(cost_text1))
        self.wait(1)

        # Reverse path from B to A
        path2 = Line(B.get_center(), A.get_center(), color=YELLOW)
        self.play(Create(path2))
        self.wait(0.5)

        # Cost calculation for B to A: 2 horizontal + 2 vertical = 4
        cost_text2 = MathTex("2 + 2 = 4", font_size=30).next_to(path2, DOWN)
        self.play(Write(cost_text2))
        self.wait(1)

        # Symmetry statement
        symmetry = MathTex(r"d(A,B) = d(B,A)", font_size=40).to_edge(UP).shift(DOWN * 0.5)
        self.play(ReplacementTransform(cost_text1, symmetry))
        self.wait(1)

        # Narration text
        narration1 = Text("Despite the vertical cost,", font_size=24).to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(narration1))
        self.wait(1.5)

        narration2 = Text("quill distance is symmetric.", font_size=24).to_edge(DOWN).shift(UP * 0.5)
        self.play(ReplacementTransform(narration1, narration2))
        self.wait(1.5)

        narration3 = Text("Direction does not change the total cost.", font_size=24).to_edge(DOWN).shift(UP * 0.5)
        self.play(ReplacementTransform(narration2, narration3))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(symmetry), FadeOut(narration3), FadeOut(path1), FadeOut(path2), FadeOut(A), FadeOut(B), FadeOut(label_A), FadeOut(label_B), FadeOut(cost_text1), FadeOut(cost_text2), FadeOut(title))
        self.wait(0.5)
