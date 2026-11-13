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
        
        # Point A at (2, 1)
        A = Dot([2, 1, 0], color=BLUE)
        label_A = MathTex("(x, y)", font_size=24).next_to(A, DOWN)
        self.play(FadeIn(A), Write(label_A))
        self.wait(0.5)

        # Step 1: Krell step from A to intermediate point
        step1_arrow = Arrow(A.get_center(), [1, 2, 0], color=YELLOW, buff=0.1)
        step1_label = MathTex("Step\ 1", font_size=24).next_to(step1_arrow, UP)
        self.play(GrowArrow(step1_arrow), Write(step1_label))
        self.wait(0.5)

        # Intermediate point
        B_inter = Dot([1, 2, 0], color=GREEN)
        label_B_inter = MathTex("(y, x+1)", font_size=24).next_to(B_inter, UP)
        label_B_inter.shift(0.0 * RIGHT + 0.22 * UP)  # layout: separation vector
        self.play(FadeIn(B_inter), Write(label_B_inter))
        self.wait(0.5)

        # Step 2: Krell step from intermediate to B
        step2_arrow = Arrow(B_inter.get_center(), [2, 3, 0], color=YELLOW, buff=0.1)
        step2_label = MathTex("Step\ 2", font_size=24).next_to(step2_arrow, UP)
        step2_label.shift(0.0 * RIGHT + 0.47 * UP)  # layout: separation vector
        step2_arrow.shift(0.0 * RIGHT + -0.53 * UP)  # layout: separation vector
        self.play(GrowArrow(step2_arrow), Write(step2_label))
        self.wait(0.5)

        # Final point B
        B = Dot([2, 3, 0], color=BLUE)
        label_B = MathTex("(x+1, y+1)", font_size=24).next_to(B, UP)
        self.play(FadeIn(B), Write(label_B))
        self.wait(0.5)

        # Dashed direct arrow from A to B
        direct_arrow = DashedLine(A.get_center(), B.get_center(), color=RED)
        direct_label = MathTex("(+1,+1)", font_size=24).next_to(direct_arrow, RIGHT)
        self.play(Create(direct_arrow), Write(direct_label))
        self.wait(0.5)

        # Narration text
        narration = Text("Two consecutive Krell steps have a powerful simplification.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        # Show applying Double Step Identity twice
        narration2 = Text("Applying it twice gives (+2, +2).", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1.5)
        self.play(FadeOut(narration2))

        # Show one more single step to reach (3, 3)
        final_arrow = Arrow(B.get_center(), [3, 4, 0], color=PURPLE, buff=0.1)
        final_label = MathTex("Step\ 3", font_size=24).next_to(final_arrow, UP)
        self.play(GrowArrow(final_arrow), Write(final_label))
        self.wait(0.5)

        # Final point
        C = Dot([3, 4, 0], color=BLUE)
        label_C = MathTex("(x+2, y+2)", font_size=24).next_to(C, UP)
        self.play(FadeIn(C), Write(label_C))
        self.wait(0.5)

        # Total steps text
        total_text = Text("Total: 5 steps (2 + 2 + 1)", font_size=24).to_edge(DOWN)
        self.play(Write(total_text))
        self.wait(2.0)

        # Cleanup
        self.play(FadeOut(title, grid, A, B_inter, B, C, step1_arrow, step2_arrow, final_arrow,
                          label_A, label_B_inter, label_B, label_C, step1_label, step2_label,
                          final_label, direct_arrow, direct_label, narration, narration2, total_text))
        self.wait(0.5)
