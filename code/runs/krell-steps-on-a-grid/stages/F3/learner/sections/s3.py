from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Staircase Path from Origin", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(x_range=[-7, 7], y_range=[-3.9, 3.9], faded_line_ratio=1)
        grid.set_opacity(0.5)
        self.play(Create(grid))
        self.wait(0.5)

        # Start point (0,0)
        start_point = Dot(color=YELLOW).move_to(grid.c2p(0, 0))
        start_label = MathTex("(0,0)", font_size=24).next_to(start_point, DOWN, buff=0.2)
        self.play(FadeIn(start_point), Write(start_label))
        self.wait(1)

        # First step: (0,0) -> (0,1)
        step1 = Arrow(start_point, grid.c2p(0, 1), color=BLUE, buff=0.1)
        step1_label = MathTex("(0,1)", font_size=24).next_to(grid.c2p(0, 1), UP, buff=0.2)
        self.play(GrowArrow(step1), Write(step1_label))
        self.wait(1)

        # Second step: (0,1) -> (1,1)
        step2 = Arrow(grid.c2p(0, 1), grid.c2p(1, 1), color=BLUE, buff=0.1)
        step2_label = MathTex("(1,1)", font_size=24).next_to(grid.c2p(1, 1), UP, buff=0.2)
        self.play(GrowArrow(step2), Write(step2_label))
        self.wait(1)

        # Third step: (1,1) -> (1,2)
        step3 = Arrow(grid.c2p(1, 1), grid.c2p(1, 2), color=BLUE, buff=0.1)
        step3_label = MathTex("(1,2)", font_size=24).next_to(grid.c2p(1, 2), UP, buff=0.2)
        step3.shift(0.0 * RIGHT + 0.35 * UP)  # layout: separation vector
        self.play(GrowArrow(step3), Write(step3_label))
        self.wait(1)
        # Fourth step: (1,2) -> (2,2)
        step4 = Arrow(grid.c2p(1, 2), grid.c2p(2, 2), color=BLUE, buff=0.1)
        step4_label = MathTex("(2,2)", font_size=24).next_to(grid.c2p(2, 2), UP, buff=0.2)
        self.play(GrowArrow(step4), Write(step4_label))
        self.wait(1)

        # Show the third step arrow from (1,2) to (2,3)
        third_step_arrow = Arrow(grid.c2p(1, 2), grid.c2p(2, 3), color=RED, buff=0.1)
        third_step_label = MathTex("(2,3)", font_size=24).next_to(grid.c2p(2, 3), UP, buff=0.2)
        step3_text = Text("Step 3", font_size=24).next_to(third_step_arrow, RIGHT, buff=0.2)

        third_step_label.shift(0.0 * RIGHT + 0.45 * UP)  # layout: separation vector
        self.play(GrowArrow(third_step_arrow), Write(step3_text), Write(third_step_label))
        self.wait(1.5)

        # Fade out everything except title
        self.play(
            FadeOut(start_point),
            FadeOut(start_label),
            FadeOut(step1),
            FadeOut(step1_label),
            FadeOut(step2),
            FadeOut(step2_label),
            FadeOut(step3),
            FadeOut(step3_label),
            FadeOut(step4),
            FadeOut(step4_label),
            FadeOut(third_step_arrow),
            FadeOut(step3_text),
            FadeOut(third_step_label),
            FadeOut(grid),
            FadeOut(title)
        )
