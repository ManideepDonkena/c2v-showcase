from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Krell Transformation Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY}
        )
        grid.set_opacity(0.5)
        self.play(Create(grid))
        self.wait(0.5)
        
        # Point P at (3, 5)
        P = Dot(point=[3, 5, 0], color=BLUE)
        label_P = MathTex("(3, 5)", font_size=24).next_to(P, UR, buff=0.2)
        P.shift(0.0 * RIGHT + -1.23 * UP)  # layout: separation vector
        self.play(FadeIn(P), Write(label_P))
        self.wait(0.5)

        # Arrow from P to Q
        arrow = Arrow(start=P.get_center(), end=[5, 4, 0], color=YELLOW)
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Labels 'Swap' and '+1'
        swap_label = Text("Swap", font_size=24).next_to(arrow, UP)
        plus1_label = Text("+1", font_size=24).next_to(arrow, DOWN)
        self.play(Write(swap_label))
        self.wait(0.5)
        self.play(Write(plus1_label))
        self.wait(0.5)

        # Point Q at (5, 4)
        Q = Dot(point=[5, 4, 0], color=RED)
        label_Q = MathTex("(5, 4)", font_size=24).next_to(Q, UR, buff=0.2)
        self.play(FadeIn(Q), Write(label_Q))
        self.wait(0.5)

        # Formula (y, x + 1)
        formula = MathTex("(y, x + 1)", font_size=32).to_edge(DOWN)
        self.play(Write(formula))
        self.wait(0.5)

        # Voiceover: "The new position is y for the first number and x plus one for the second"
        self.wait(1)

        # Example with (2, 2)
        self.play(FadeOut(swap_label), FadeOut(plus1_label), FadeOut(label_P), FadeOut(P))
        point_22 = Dot(point=[2, 2, 0], color=BLUE)
        label_22 = MathTex("(2, 2)", font_size=24).next_to(point_22, UR, buff=0.2)
        self.play(FadeIn(point_22), Write(label_22))
        self.wait(0.5)

        # Swap visually
        swap_arrow = Arrow(start=point_22.get_center(), end=[2, 2, 0], color=YELLOW)
        self.play(GrowArrow(swap_arrow))
        self.wait(0.5)

        # Add 1 to second coordinate
        new_point = Dot(point=[2, 3, 0], color=RED)
        label_new = MathTex("(2, 3)", font_size=24).next_to(new_point, UR, buff=0.2)
        self.play(TransformFromCopy(point_22, new_point), Write(label_new))
        self.wait(0.5)

        # Voiceover: "The result is (2, 3)"
        self.wait(1)

        # Example with (-1, 4)
        self.play(FadeOut(swap_arrow), FadeOut(label_22), FadeOut(point_22), FadeOut(new_point), FadeOut(label_new))
        point_neg14 = Dot(point=[-1, 4, 0], color=BLUE)
        label_neg14 = MathTex("(-1, 4)", font_size=24).next_to(point_neg14, UR, buff=0.2)
        self.play(FadeIn(point_neg14), Write(label_neg14))
        self.wait(0.5)

        # Swap visually
        swap_arrow2 = Arrow(start=point_neg14.get_center(), end=[4, -1, 0], color=YELLOW)
        self.play(GrowArrow(swap_arrow2))
        self.wait(0.5)

        # Add 1 to second coordinate
        new_point2 = Dot(point=[4, 0, 0], color=RED)
        label_new2 = MathTex("(4, 0)", font_size=24).next_to(new_point2, UR, buff=0.2)
        self.play(TransformFromCopy(point_neg14, new_point2), Write(label_new2))
        self.wait(0.5)

        # Voiceover: "The result is (4, 0)"
        self.wait(1)

        # Visual breakdown
        self.play(FadeOut(swap_arrow2), FadeOut(label_neg14), FadeOut(point_neg14), FadeOut(new_point2), FadeOut(label_new2))
        point_b = Dot(point=[2, 2, 0], color=BLUE)
        label_b = MathTex("(2, 2)", font_size=24).next_to(point_b, UR, buff=0.2)
        self.play(FadeIn(point_b), Write(label_b))
        self.wait(0.5)

        # Step 3 arrow
        step3_arrow = Arrow(start=point_b.get_center(), end=[2, 3, 0], color=YELLOW)
        step3_label = Text("Step 3", font_size=24).next_to(step3_arrow, UP)
        self.play(GrowArrow(step3_arrow), Write(step3_label))
        self.wait(0.5)

        # Voiceover: "Apply the rule again: swap the coordinates of (2, 2) to get (2, 2), then add 1 to the second number to get (2, 3)"
        self.wait(1)

        # Show path continuing
        self.play(FadeOut(step3_arrow), FadeOut(step3_label))
        point_22 = Dot(point=[2, 2, 0], color=BLUE)
        label_22 = MathTex("(2, 2)", font_size=24).next_to(point_22, UR, buff=0.2)
        self.play(FadeIn(point_22), Write(label_22))
        self.wait(0.5)

        # Step 3
        step3_arrow = Arrow(start=point_22.get_center(), end=[2, 3, 0], color=YELLOW)
        step3_label = Text("Step 3", font_size=24).next_to(step3_arrow, UP)
        self.play(GrowArrow(step3_arrow), Write(step3_label))
        self.wait(0.5)

        # Step 4
        point_23 = Dot(point=[2, 3, 0], color=RED)
        label_23 = MathTex("(2, 3)", font_size=24).next_to(point_23, UR, buff=0.2)
        self.play(TransformFromCopy(point_22, point_23), Write(label_23))
        step4_arrow = Arrow(start=point_23.get_center(), end=[3, 3, 0], color=YELLOW)
        step4_label = Text("Step 4", font_size=24).next_to(step4_arrow, UP)
        self.play(GrowArrow(step4_arrow), Write(step4_label))
        self.wait(0.5)

        # Show change in x vs y
        self.play(FadeOut(step3_arrow), FadeOut(step4_arrow), FadeOut(step3_label), FadeOut(step4_label))
        point_22 = Dot(point=[2, 2, 0], color=BLUE)
        label_22 = MathTex("(2, 2)", font_size=24).next_to(point_22, UR, buff=0.2)
        point_23 = Dot(point=[2, 3, 0], color=RED)
        label_23 = MathTex("(2, 3)", font_size=24).next_to(point_23, UR, buff=0.2)
        self.play(FadeIn(point_22), Write(label_22))
        self.wait(0.5)
        self.play(FadeIn(point_23), Write(label_23))
        self.wait(0.5)

        # Compare changes
        change_x = MathTex("\Delta x = 0", font_size=24).to_edge(LEFT).shift(DOWN * 1.5)
        change_y = MathTex("\Delta y = +1", font_size=24).to_edge(LEFT).shift(DOWN * 2)
        self.play(Write(change_x))
        self.wait(0.5)
        self.play(Write(change_y))
        self.wait(0.5)

        # Double Step Identity
        self.play(FadeOut(change_x), FadeOut(change_y), FadeOut(point_22), FadeOut(label_22), FadeOut(point_23), FadeOut(label_23))
        point_start = Dot(point=[0, 0, 0], color=BLUE)
        label_start = MathTex("(0, 0)", font_size=24).next_to(point_start, UR, buff=0.2)
        self.play(FadeIn(point_start), Write(label_start))
        self.wait(0.5)

        # Two steps
        step1_arrow = Arrow(start=point_start.get_center(), end=[0, 1, 0], color=YELLOW)
        step1_label = Text("Step 1", font_size=24).next_to(step1_arrow, UP)
        self.play(GrowArrow(step1_arrow), Write(step1_label))
        self.wait(0.5)

        point_01 = Dot(point=[0, 1, 0], color=RED)
        label_01 = MathTex("(0, 1)", font_size=24).next_to(point_01, UR, buff=0.2)
        self.play(TransformFromCopy(point_start, point_01), Write(label_01))
        step2_arrow = Arrow(start=point_01.get_center(), end=[1, 1, 0], color=YELLOW)
        step2_label = Text("Step 2", font_size=24).next_to(step2_arrow, UP)
        self.play(GrowArrow(step2_arrow), Write(step2_label))
        self.wait(0.5)

        point_11 = Dot(point=[1, 1, 0], color=RED)
        label_11 = MathTex("(1, 1)", font_size=24).next_to(point_11, UR, buff=0.2)
        self.play(TransformFromCopy(point_01, point_11), Write(label_11))
        self.wait(0.5)

        # One more step to reach final
        step3_arrow = Arrow(start=point_11.get_center(), end=[1, 2, 0], color=YELLOW)
        step3_label = Text("Step 3", font_size=24).next_to(step3_arrow, UP)
        self.play(GrowArrow(step3_arrow), Write(step3_label))
        self.wait(0.5)

        point_12 = Dot(point=[1, 2, 0], color=RED)
        label_12 = MathTex("(1, 2)", font_size=24).next_to(point_12, UR, buff=0.2)
        self.play(TransformFromCopy(point_11, point_12), Write(label_12))
        self.wait(0.5)

        # Final step to (2, 2)
        step4_arrow = Arrow(start=point_12.get_center(), end=[2, 2, 0], color=YELLOW)
        step4_label = Text("Step 4", font_size=24).next_to(step4_arrow, UP)
        self.play(GrowArrow(step4_arrow), Write(step4_label))
        self.wait(0.5)

        point_22_final = Dot(point=[2, 2, 0], color=RED)
        label_22_final = MathTex("(2, 2)", font_size=24).next_to(point_22_final, UR, buff=0.2)
        self.play(TransformFromCopy(point_12, point_22_final), Write(label_22_final))
        self.wait(0.5)

        # Total steps = 5
        total_steps = MathTex("Total Steps = 5", font_size=32).to_edge(DOWN)
        self.play(Write(total_steps))
        self.wait(1)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(P),
            FadeOut(Q),
            FadeOut(formula),
            FadeOut(point_22_final),
            FadeOut(label_22_final),
            FadeOut(total_steps)
        )
        self.wait(0.5)
