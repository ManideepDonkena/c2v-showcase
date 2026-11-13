from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Double Step Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(x_range=[-7, 7], y_range=[-4, 4], faded_line_ratio=1)
        grid.set_opacity(0.5)
        self.play(Create(grid))
        self.wait(0.5)

        # Point A at (x, y)
        x, y = 2, 1
        A = Dot(grid.coords_to_point(x, y), color=YELLOW)
        label_A = MathTex(f"({x}, {y})", font_size=24).next_to(A, DOWN, buff=0.2)
        self.play(FadeIn(A), Write(label_A))
        self.wait(0.5)

        # Step 1: Krell step from A
        step1 = Arrow(start=grid.coords_to_point(x, y),
                      end=grid.coords_to_point(y, x + 1),
                      buff=0.05,
                      color=BLUE)
        label_step1 = MathTex("Step\ 1", font_size=24).next_to(step1, UP, buff=0.1)
        self.play(GrowArrow(step1), Write(label_step1))
        self.wait(0.5)

        # Intermediate point
        B_intermediate = Dot(grid.coords_to_point(y, x + 1), color=GREEN)
        label_B_intermediate = MathTex(f"({y}, {x+1})", font_size=24).next_to(B_intermediate, UP, buff=0.2)
        self.play(FadeIn(B_intermediate), Write(label_B_intermediate))
        self.wait(0.5)

        # Step 2: Krell step from intermediate point
        step2 = Arrow(start=grid.coords_to_point(y, x + 1),
                      end=grid.coords_to_point(x + 1, y + 1),
                      buff=0.05,
                      color=BLUE)
        label_step2 = MathTex("Step\ 2", font_size=24).next_to(step2, UP, buff=0.1)
        self.play(GrowArrow(step2), Write(label_step2))
        self.wait(0.5)

        # Final point B
        B = Dot(grid.coords_to_point(x + 1, y + 1), color=YELLOW)
        label_B = MathTex(f"({x+1}, {y+1})", font_size=24).next_to(B, DOWN, buff=0.2)
        self.play(FadeIn(B), Write(label_B))
        self.wait(0.5)

        # Direct diagonal arrow from A to B
        direct_arrow = DashedLine(start=grid.coords_to_point(x, y),
                                 end=grid.coords_to_point(x + 1, y + 1))
        label_direct = MathTex("Direct\ Path", font_size=24).next_to(direct_arrow, UR, buff=0.1)
        self.play(GrowArrow(direct_arrow), Write(label_direct))
        self.wait(1)
        
        # Narration text
        narration = Text("Two consecutive Krell steps have a powerful simplification.", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        self.play(FadeOut(narration))

        # Final narration
        final_narration = Text("Regardless of the starting position, two steps always move the point diagonally to (x + 1, y + 1).", font_size=24).to_edge(DOWN)
        self.play(Write(final_narration))
        self.wait(3)

        self.play(FadeOut(final_narration), FadeOut(title), FadeOut(grid), FadeOut(A), FadeOut(label_A),
                  FadeOut(step1), FadeOut(label_step1), FadeOut(B_intermediate), FadeOut(label_B_intermediate),
                  FadeOut(step2), FadeOut(label_step2), FadeOut(B), FadeOut(label_B), FadeOut(direct_arrow), FadeOut(label_direct))
