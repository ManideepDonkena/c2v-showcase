from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Double Step Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Setup grid and axes
        axes = Axes(x_range=[-7, 7], y_range=[-4, 4], axis_config={"stroke_color": GREY})
        grid = always_redraw(lambda: NumberPlane(
            x_range=[-7, 7],
            y_range=[-4, 4],
            axis_config={"stroke_color": GREY}
        ))
        self.play(Create(grid), Create(axes))
        self.wait(0.5)
        
        # Start point A
        A = Dot(point=[0, 0, 0], color=BLUE)
        label_A = MathTex("(x, y)", font_size=24).next_to(A, DOWN, buff=0.2)
        self.play(FadeIn(A), Write(label_A))
        self.wait(0.5)

        # Step 1: from A to intermediate point
        step1_arrow = Arrow(start=A.get_center(), end=[0, 1, 0], color=YELLOW, buff=0.05)
        step1_label = MathTex("Step\ 1", font_size=24).next_to(step1_arrow, UP, buff=0.1)
        self.play(GrowArrow(step1_arrow), Write(step1_label))
        self.wait(0.5)

        # Intermediate point
        B_intermediate = Dot(point=[0, 1, 0], color=GREEN)
        label_B_int = MathTex("(y, x + 1)", font_size=24).next_to(B_intermediate, UP, buff=0.2)
        B_intermediate.shift(0.0 * RIGHT + -0.18 * UP)  # layout: separation vector
        self.play(FadeIn(B_intermediate), Write(label_B_int))
        self.wait(0.5)

        # Step 2: from intermediate to B
        step2_arrow = Arrow(start=B_intermediate.get_center(), end=[1, 1, 0], color=YELLOW, buff=0.05)
        step2_label = MathTex("Step\ 2", font_size=24).next_to(step2_arrow, RIGHT, buff=0.1)
        self.play(GrowArrow(step2_arrow), Write(step2_label))
        self.wait(0.5)

        # Final point B
        B = Dot(point=[1, 1, 0], color=RED)
        label_B = MathTex("(x + 1, y + 1)", font_size=24).next_to(B, UP, buff=0.2)
        label_B.shift(0.32 * RIGHT + 0.0 * UP)  # layout: separation vector
        B.shift(-0.18 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(FadeIn(B), Write(label_B))
        self.wait(0.5)

        # Dashed direct arrow from A to B
        direct_arrow = DashedLine(start=A.get_center(), end=B.get_center(), color=PURPLE)
        direct_label = MathTex("(+1, +1)", font_size=24).next_to(direct_arrow, UR, buff=0.1)
        self.play(Create(direct_arrow), Write(direct_label))
        self.wait(1)

        # Narration text
        narration = Text("Two consecutive Krell steps have a powerful simplification.", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        # Show double application of identity
        # First double step from (0, 0) to (1, 1)
        A2 = Dot(point=[0, 0, 0], color=BLUE)
        label_A2 = MathTex("(x, y)", font_size=24).next_to(A2, DOWN, buff=0.2)
        self.play(FadeIn(A2), Write(label_A2))
        self.wait(0.5)

        step1_arrow2 = Arrow(start=A2.get_center(), end=[0, 1, 0], color=YELLOW, buff=0.05)
        step1_label2 = MathTex("Step\ 1", font_size=24).next_to(step1_arrow2, UP, buff=0.1)
        self.play(GrowArrow(step1_arrow2), Write(step1_label2))
        self.wait(0.5)

        B_intermediate2 = Dot(point=[0, 1, 0], color=GREEN)
        label_B_int2 = MathTex("(y, x + 1)", font_size=24).next_to(B_intermediate2, UP, buff=0.2)
        self.play(FadeIn(B_intermediate2), Write(label_B_int2))
        self.wait(0.5)

        step2_arrow2 = Arrow(start=B_intermediate2.get_center(), end=[1, 1, 0], color=YELLOW, buff=0.05)
        step2_label2 = MathTex("Step\ 2", font_size=24).next_to(step2_arrow2, RIGHT, buff=0.1)
        self.play(GrowArrow(step2_arrow2), Write(step2_label2))
        self.wait(0.5)

        B2 = Dot(point=[1, 1, 0], color=RED)
        label_B2 = MathTex("(x + 1, y + 1)", font_size=24).next_to(B2, UP, buff=0.2)
        self.play(FadeIn(B2), Write(label_B2))
        self.wait(0.5)

        # Second double step from (1, 1) to (2, 2)
        A3 = Dot(point=[1, 1, 0], color=BLUE)
        label_A3 = MathTex("(x + 1, y + 1)", font_size=24).next_to(A3, DOWN, buff=0.2)
        self.play(FadeIn(A3), Write(label_A3))
        self.wait(0.5)

        step1_arrow3 = Arrow(start=A3.get_center(), end=[1, 2, 0], color=YELLOW, buff=0.05)
        step1_label3 = MathTex("Step\ 1", font_size=24).next_to(step1_arrow3, UP, buff=0.1)
        self.play(GrowArrow(step1_arrow3), Write(step1_label3))
        self.wait(0.5)

        B_intermediate3 = Dot(point=[1, 2, 0], color=GREEN)
        label_B_int3 = MathTex("(y, x + 1)", font_size=24).next_to(B_intermediate3, UP, buff=0.2)
        self.play(FadeIn(B_intermediate3), Write(label_B_int3))
        self.wait(0.5)

        step2_arrow3 = Arrow(start=B_intermediate3.get_center(), end=[2, 2, 0], color=YELLOW, buff=0.05)
        step2_label3 = MathTex("Step\ 2", font_size=24).next_to(step2_arrow3, RIGHT, buff=0.1)
        self.play(GrowArrow(step2_arrow3), Write(step2_label3))
        self.wait(0.5)

        B3 = Dot(point=[2, 2, 0], color=RED)
        label_B3 = MathTex("(x + 2, y + 2)", font_size=24).next_to(B3, UP, buff=0.2)
        self.play(FadeIn(B3), Write(label_B3))
        self.wait(0.5)

        # One more single step to (3, 3)
        A4 = Dot(point=[2, 2, 0], color=BLUE)
        label_A4 = MathTex("(x + 2, y + 2)", font_size=24).next_to(A4, DOWN, buff=0.2)
        self.play(FadeIn(A4), Write(label_A4))
        self.wait(0.5)

        step1_arrow4 = Arrow(start=A4.get_center(), end=[2, 3, 0], color=YELLOW, buff=0.05)
        step1_label4 = MathTex("Step\ 1", font_size=24).next_to(step1_arrow4, UP, buff=0.1)
        self.play(GrowArrow(step1_arrow4), Write(step1_label4))
        self.wait(0.5)

        B4 = Dot(point=[2, 3, 0], color=RED)
        label_B4 = MathTex("(x + 2, y + 3)", font_size=24).next_to(B4, UP, buff=0.2)
        self.play(FadeIn(B4), Write(label_B4))
        self.wait(0.5)

        # Final narration
        final_narration = Text("Total steps: 2 + 2 + 1 = 5", font_size=24).to_edge(DOWN)
        self.play(Write(final_narration))
        self.wait(1.5)
        self.play(FadeOut(final_narration))

        # Cleanup
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(axes),
            FadeOut(A), FadeOut(label_A),
            FadeOut(step1_arrow), FadeOut(step1_label),
            FadeOut(B_intermediate), FadeOut(label_B_int),
            FadeOut(step2_arrow), FadeOut(step2_label),
            FadeOut(B), FadeOut(label_B),
            FadeOut(direct_arrow), FadeOut(direct_label),
            FadeOut(A2), FadeOut(label_A2),
            FadeOut(step1_arrow2), FadeOut(step1_label2),
            FadeOut(B_intermediate2), FadeOut(label_B_int2),
            FadeOut(step2_arrow2), FadeOut(step2_label2),
            FadeOut(B2), FadeOut(label_B2),
            FadeOut(A3), FadeOut(label_A3),
            FadeOut(step1_arrow3), FadeOut(step1_label3),
            FadeOut(B_intermediate3), FadeOut(label_B_int3),
            FadeOut(step2_arrow3), FadeOut(step2_label3),
            FadeOut(B3), FadeOut(label_B3),
            FadeOut(A4), FadeOut(label_A4),
            FadeOut(step1_arrow4), FadeOut(step1_label4),
            FadeOut(B4), FadeOut(label_B4)
        )
