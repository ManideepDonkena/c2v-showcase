from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Staircase Path from Origin", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(x_range=[-7, 7], y_range=[-4, 4], faded_line_ratio=1)
        grid.set_opacity(0.5)
        self.play(Create(grid))
        self.wait(0.5)

        # Start point (0, 0)
        origin = Dot([0, 0, 0], color=YELLOW)
        origin_label = MathTex("(0, 0)", font_size=24).next_to(origin, DOWN, buff=0.2)
        self.play(FadeIn(origin), Write(origin_label))
        self.wait(0.5)

        # First step: (0, 0) -> (0, 1)
        step1 = Arrow(start=[0, 0, 0], end=[0, 1, 0], buff=0, color=BLUE)
        point1 = Dot([0, 1, 0], color=YELLOW)
        label1 = MathTex("(0, 1)", font_size=24).next_to(point1, UP, buff=0.2)
        self.play(GrowArrow(step1), FadeIn(point1), Write(label1))
        self.wait(0.5)

        # Second step: (0, 1) -> (1, 1)
        step2 = Arrow(start=[0, 1, 0], end=[1, 1, 0], buff=0, color=BLUE)
        point2 = Dot([1, 1, 0], color=YELLOW)
        label2 = MathTex("(1, 1)", font_size=24).next_to(point2, UP, buff=0.2)
        self.play(GrowArrow(step2), FadeIn(point2), Write(label2))
        self.wait(0.5)

        # Third step: (1, 1) -> (1, 2)
        step3 = Arrow(start=[1, 1, 0], end=[1, 2, 0], buff=0, color=BLUE)
        point3 = Dot([1, 2, 0], color=YELLOW)
        label3 = MathTex("(1, 2)", font_size=24).next_to(point3, UP, buff=0.2)
        step3.shift(0.53 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(GrowArrow(step3), FadeIn(point3), Write(label3))
        self.wait(0.5)

        # Fourth step: (1, 2) -> (2, 2)
        step4 = Arrow(start=[1, 2, 0], end=[2, 2, 0], buff=0, color=BLUE)
        point4 = Dot([2, 2, 0], color=YELLOW)
        label4 = MathTex("(2, 2)", font_size=24).next_to(point4, UP, buff=0.2)
        self.play(GrowArrow(step4), FadeIn(point4), Write(label4))
        self.wait(1)

        # Show Step 3 arrow from (2, 2) to (2, 3)
        step_arrow = Arrow(start=[2, 2, 0], end=[2, 3, 0], buff=0, color=RED).shift(RIGHT * 0.53)
        step_label = MathTex("Step 3", font_size=24).next_to(step_arrow, RIGHT, buff=0.2)
        self.play(GrowArrow(step_arrow), Write(step_label))
        self.wait(1)

        # Narration text
        narration = Text("Apply the rule again: swap (2, 2) → (2, 2), add 1 to second → (2, 3)", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)

        # Show point (2, 2) and next step to (2, 3)
        point_22 = Dot([2, 2, 0], color=YELLOW)
        point_23 = Dot([2, 3, 0], color=YELLOW)
        arrow_22to23 = Arrow(start=[2, 2, 0], end=[2, 3, 0], buff=0, color=GREEN)
        label_23 = MathTex("(2, 3)", font_size=24).next_to(point_23, UP, buff=0.2)
        point_23.shift(0.0 * RIGHT + -0.23 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow_22to23), FadeIn(point_23), Write(label_23))
        self.wait(1)

        # Show change in x vs y
        dx = MathTex("\Delta x = 0", font_size=24).to_corner(UL)
        dy = MathTex("\Delta y = +1", font_size=24).next_to(dx, DOWN)
        self.play(Write(dx), Write(dy))
        self.wait(1.5)

        # Fade out narration and dx/dy
        self.play(FadeOut(narration), FadeOut(dx), FadeOut(dy))

        # Continue path from (2, 2) to (2, 3) to (3, 3)
        step_23 = Arrow(start=[2, 2, 0], end=[2, 3, 0], buff=0, color=GREEN)
        point_23_final = Dot([2, 3, 0], color=YELLOW)
        label_23_final = MathTex("(2, 3)", font_size=24).next_to(point_23_final, UP, buff=0.2)
        self.play(GrowArrow(step_23), FadeIn(point_23_final), Write(label_23_final))
        self.wait(1)

        # Apply rule to (2, 3): swap → (3, 2), add 1 to second → (3, 3)
        step_arrow2 = Arrow(start=[2, 3, 0], end=[3, 3, 0], buff=0, color=RED)
        label_step2 = MathTex("Step 4", font_size=24).next_to(step_arrow2, RIGHT, buff=0.2)
        point_33 = Dot([3, 3, 0], color=YELLOW)
        label_33 = MathTex("(3, 3)", font_size=24).next_to(point_33, UP, buff=0.2)
        self.play(GrowArrow(step_arrow2), Write(label_step2), FadeIn(point_33), Write(label_33))
        self.wait(1.5)

        # Final cleanup
        self.play(FadeOut(title), FadeOut(grid), FadeOut(origin), FadeOut(origin_label),
                  FadeOut(step1), FadeOut(label1), FadeOut(step2), FadeOut(label2),
                  FadeOut(step3), FadeOut(label3), FadeOut(step4), FadeOut(label4),
                  FadeOut(step_arrow), FadeOut(step_label), FadeOut(point_22),
                  FadeOut(arrow_22to23), FadeOut(point_23_final), FadeOut(label_23_final),
                  FadeOut(step_23), FadeOut(point_33), FadeOut(label_33), FadeOut(label_step2))
        self.wait(0.5)
