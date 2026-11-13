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
        label_A = MathTex(f"({x}, {y})", font_size=24).next_to(A, UR, buff=0.2)
        self.play(FadeIn(A), Write(label_A))
        self.wait(0.5)

        # Step 1: from A to intermediate point
        step1 = Arrow(start=grid.coords_to_point(x, y),
                      end=grid.coords_to_point(y, x + 1),
                      buff=0.1,
                      color=BLUE)
        label_step1 = MathTex("Step\ 1", font_size=24).next_to(step1, UR, buff=0.2)
        label_step1.shift(0.0 * RIGHT + -0.48 * UP)  # layout: separation vector
        self.play(Create(step1), Write(label_step1))
        self.wait(0.5)

        # Intermediate point
        B_inter = Dot(grid.coords_to_point(y, x + 1), color=GREEN)
        label_B_inter = MathTex(f"({y}, {x+1})", font_size=24).next_to(B_inter, UR, buff=0.2)
        B_inter.shift(0.0 * RIGHT + -0.23 * UP)  # layout: separation vector
        label_B_inter.shift(0.0 * RIGHT + 0.37 * UP)  # layout: separation vector
        self.play(FadeIn(B_inter), Write(label_B_inter))
        self.wait(0.5)

        # Step 2: from intermediate to B
        step2 = Arrow(start=grid.coords_to_point(y, x + 1),
                      end=grid.coords_to_point(x + 1, y + 1),
                      buff=0.1,
                      color=RED)
        label_step2 = MathTex("Step\ 2", font_size=24).next_to(step2, DR, buff=0.2)
        self.play(Create(step2), Write(label_step2))
        self.wait(0.5)

        # Final point B
        B = Dot(grid.coords_to_point(x + 1, y + 1), color=YELLOW)
        label_B = MathTex(f"({x+1}, {y+1})", font_size=24).next_to(B, UR, buff=0.2)
        self.play(FadeIn(B), Write(label_B))
        self.wait(0.5)

        # Dashed arrow from A to B (net result)
        net_arrow = DashedLine(start=grid.coords_to_point(x, y),
                               end=grid.coords_to_point(x + 1, y + 1),
                               color=WHITE)
        label_net = MathTex("(+1,+1)", font_size=24).next_to(net_arrow, UR, buff=0.2)
        self.play(Create(net_arrow), Write(label_net))
        self.wait(1)

        # Narration text
        narration1 = Text("Two consecutive Krell steps", font_size=24).to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(1)
        self.play(FadeOut(narration1))

        # Specific numeric example from (0, 0)
        self.play(FadeOut(A), FadeOut(label_A), FadeOut(B_inter), FadeOut(label_B_inter),
                  FadeOut(step1), FadeOut(step2), FadeOut(label_step1), FadeOut(label_step2),
                  FadeOut(net_arrow), FadeOut(label_net))

        # Start from (0, 0)
        A_zero = Dot(grid.coords_to_point(0, 0), color=YELLOW)
        label_A_zero = MathTex("(0, 0)", font_size=24).next_to(A_zero, UR, buff=0.2)
        self.play(FadeIn(A_zero), Write(label_A_zero))
        self.wait(0.5)

        # First step from (0, 0)
        step1_zero = Arrow(start=grid.coords_to_point(0, 0),
                           end=grid.coords_to_point(0, 1),
                           buff=0.1,
                           color=BLUE)
        label_step1_zero = Text("Swap then add 1", font_size=24).next_to(step1_zero, UR, buff=0.2)
        self.play(Create(step1_zero), Write(label_step1_zero))
        self.wait(1)

        # Intermediate point (0, 1)
        B_inter_zero = Dot(grid.coords_to_point(0, 1), color=GREEN)
        label_B_inter_zero = MathTex("(0, 1)", font_size=24).next_to(B_inter_zero, UR, buff=0.2)
        self.play(FadeIn(B_inter_zero), Write(label_B_inter_zero))
        self.wait(0.5)

        # Second step from (0, 1)
        step2_zero = Arrow(start=grid.coords_to_point(0, 1),
                           end=grid.coords_to_point(1, 1),
                           buff=0.1,
                           color=RED)
        label_step2_zero = Text("Swap then add 1", font_size=24).next_to(step2_zero, DR, buff=0.2)
        self.play(Create(step2_zero), Write(label_step2_zero))
        self.wait(1)

        # Final point (1, 1)
        B_zero = Dot(grid.coords_to_point(1, 1), color=YELLOW)
        label_B_zero = MathTex("(1, 1)", font_size=24).next_to(B_zero, UR, buff=0.2)
        self.play(FadeIn(B_zero), Write(label_B_zero))
        self.wait(1)

        # Narration text
        narration2 = Text("From (0,0) to (1,1):", font_size=24).to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1)
        self.play(FadeOut(narration2))

        # Fade out everything
        self.play(FadeOut(title), FadeOut(grid), FadeOut(A_zero), FadeOut(label_A_zero),
                  FadeOut(B_inter_zero), FadeOut(label_B_inter_zero), FadeOut(step1_zero),
                  FadeOut(step2_zero), FadeOut(label_step1_zero), FadeOut(label_step2_zero),
                  FadeOut(B_zero), FadeOut(label_B_zero))
        self.wait(0.5)
