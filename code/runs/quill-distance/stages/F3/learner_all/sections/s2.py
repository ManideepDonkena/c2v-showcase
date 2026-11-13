from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Symmetry and Direction", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Points A and B
        A = Dot([0, 0, 0], color=BLUE)
        B = Dot([2, 1, 0], color=RED)
        A_label = Tex("A").next_to(A, DOWN)
        B_label = Tex("B").next_to(B, UP)

        self.play(FadeIn(A), FadeIn(B), Write(A_label), Write(B_label))
        self.wait(0.5)

        # Path from A to B
        path1 = Line(A.get_center(), B.get_center(), color=YELLOW)
        self.play(Create(path1))
        self.wait(0.5)

        # Cost calculation for A to B
        cost_text1 = MathTex("2 + 2 = 4", font_size=30).next_to(path1, UP)
        self.play(Write(cost_text1))
        self.wait(1)

        # Reverse path from B to A
        path2 = Line(B.get_center(), A.get_center(), color=YELLOW)
        self.play(Create(path2))
        self.wait(0.5)

        # Cost calculation for B to A
        cost_text2 = MathTex("2 + 2 = 4", font_size=30).next_to(path2, UP)
        cost_text1.shift(0.0 * RIGHT + 0.39 * UP)  # layout: separation vector
        self.play(Write(cost_text2))
        self.wait(1)

        # Symmetry statement
        symmetry = MathTex(r"d(A,B) = d(B,A)", font_size=40).to_edge(UP)
        self.play(Transform(title, symmetry))
        self.wait(1.5)

        # Clear previous elements
        self.play(FadeOut(path1), FadeOut(path2), FadeOut(cost_text1), FadeOut(cost_text2))

        # Central point
        center = Dot([0, 0, 0], color=GREEN)
        center_label = Tex("Center").next_to(center, DOWN)
        center_label.shift(0.0 * RIGHT + -0.51 * UP)  # layout: separation vector
        self.play(FadeIn(center), Write(center_label))
        self.wait(0.5)

        # Four points at quill distance 4
        point1 = Dot([4, 0, 0], color=YELLOW)
        point2 = Dot([-4, 0, 0], color=YELLOW)
        point3 = Dot([0, 2, 0], color=YELLOW)
        point4 = Dot([0, -2, 0], color=YELLOW)

        # Light up points in sequence
        self.play(FadeIn(point1))
        self.wait(0.5)
        self.play(FadeIn(point2))
        self.wait(0.5)
        self.play(FadeIn(point3))
        self.wait(0.5)
        self.play(FadeIn(point4))
        self.wait(1)

        # Explanation text
        explanation = Text("Distance 4: 4 sideways or 2 vertical steps", font_size=24).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(center), FadeOut(center_label), FadeOut(point1), FadeOut(point2),
                  FadeOut(point3), FadeOut(point4), FadeOut(explanation), FadeOut(title))
        self.wait(0.5)
