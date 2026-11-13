from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Symmetry and Direction", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(x_range=[-7, 7], y_range=[-4, 4], faded_line_ratio=1)
        grid.set_opacity(0.5)
        self.play(Create(grid))
        self.wait(0.5)
        
        # Points A and B
        A = Dot([0, 0, 0], color=BLUE)
        B = Dot([2, 1, 0], color=RED)
        label_A = Tex("A").next_to(A, DOWN)
        label_B = Tex("B").next_to(B, UP)
        
        # Path from A to B
        path_AB = VGroup(
            Line(A.get_center(), [2, 0, 0], color=YELLOW),
            Line([2, 0, 0], [2, 1, 0], color=YELLOW)
        )
        self.play(Create(path_AB))
        self.wait(0.5)

        # Cost calculation for A to B
        cost_text_AB = MathTex("2 + 2 = 4", font_size=30).next_to(B, UR)
        self.play(Write(cost_text_AB))
        self.wait(1)

        # Reverse path from B to A
        path_BA = VGroup(
            Line(B.get_center(), [0, 1, 0], color=GREEN),
            Line([0, 1, 0], [0, 0, 0], color=GREEN)
        )
        self.play(Create(path_BA))
        self.wait(0.5)

        # Cost calculation for B to A
        cost_text_BA = MathTex("2 + 2 = 4", font_size=30).next_to(A, DL)
        self.play(Write(cost_text_BA))
        self.wait(1)

        # Symmetry statement
        symmetry = MathTex(r"d(A,B) = d(B,A)", font_size=40).to_edge(UP)
        self.play(Transform(title, symmetry))
        self.wait(1.5)

        # Narration text
        narration = Text("Despite the vertical cost, quill distance is symmetric.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)

        # Clear narration and fade out
        self.play(FadeOut(narration))
        self.wait(0.5)

        # Central point and four specific points lighting up in sequence
        center = Dot([0, 0, 0], color=WHITE)
        self.play(FadeIn(center))
        self.wait(0.5)

        # Point 6 units right
        point1 = Dot([6, 0, 0], color=YELLOW)
        self.play(FadeIn(point1))
        self.wait(0.5)
        
        # Point 6 units left
        point2 = Dot([-6, 0, 0], color=YELLOW)
        self.play(FadeIn(point2))
        self.wait(0.5)
        
        # Point 3 units up
        point3 = Dot([0, 3, 0], color=YELLOW)
        self.play(FadeIn(point3))
        self.wait(0.5)
        
        # Point 3 units down
        point4 = Dot([0, -3, 0], color=YELLOW)
        self.play(FadeIn(point4))
        self.wait(0.5)

        # Explanation text
        explanation = Text("Just as distance 2 required 2 sideways or 1 vertical step, distance 6 requires 6 sideways steps or 3 vertical steps.", font_size=24)
        explanation.to_edge(DOWN)
        explanation.shift(1.83 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(explanation))
        self.wait(1.5)

        # Final statement
        final = Text("The distance from A to B is exactly the same as from B back to A.", font_size=24)
        final.to_edge(DOWN)
        self.play(Write(final))
        self.wait(1.5)

        self.play(FadeOut(final), FadeOut(explanation), FadeOut(path_AB), FadeOut(path_BA),
                  FadeOut(cost_text_AB), FadeOut(cost_text_BA),
                  FadeOut(A), FadeOut(B), FadeOut(label_A), FadeOut(label_B),
                  FadeOut(grid), FadeOut(title), FadeOut(center), FadeOut(point1),
                  FadeOut(point2), FadeOut(point3), FadeOut(point4))
        self.wait(0.5)
