from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Symmetry and Direction", font_size=36).to_edge(UP)
        title.set_z_index(2)
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
        cost_text_AB.add_background_rectangle(opacity=0.8)
        cost_text_AB.set_z_index(2)
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
        cost_text_BA.add_background_rectangle(opacity=0.8)
        cost_text_BA.set_z_index(2)
        self.play(Write(cost_text_BA))
        self.wait(1)

        # Symmetry statement
        symmetry = MathTex(r"d(A,B) = d(B,A)", font_size=40).to_edge(UP)
        symmetry.add_background_rectangle(opacity=0.8)
        self.play(Transform(title, symmetry))
        self.wait(1.5)

        # Narration text
        narration = Text("Despite the vertical cost, quill distance is symmetric.", font_size=24)
        narration.to_edge(DOWN)
        narration.add_background_rectangle(opacity=0.85, buff=0.1)
        narration.set_z_index(2)
        self.play(Write(narration))
        self.wait(1.5)

        # Clear narration and fade out
        self.play(FadeOut(narration))
        self.wait(0.5)

        # Final statement
        final = Text("The distance from A to B is exactly the same as from B back to A.", font_size=24)
        final.to_edge(DOWN)
        final.add_background_rectangle(opacity=0.85, buff=0.1)
        final.set_z_index(2)
        self.play(Write(final))
        self.wait(1.5)

        self.play(FadeOut(final), FadeOut(path_AB), FadeOut(path_BA),
                  FadeOut(cost_text_AB), FadeOut(cost_text_BA),
                  FadeOut(grid), FadeOut(title))
        self.wait(0.5)
