from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Staircase Path from Origin", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(x_range=[-7, 7], y_range=[-4, 4], faded_line_ratio=1)
        grid.set_opacity(0.5)
        self.play(Create(grid))
        self.wait(0.5)

        # Start point (0, 0)
        start_point = Dot(color=YELLOW).move_to(grid.c2p(0, 0))
        start_label = MathTex("(0,0)", font_size=24).next_to(start_point, DOWN)
        self.play(FadeIn(start_point), Write(start_label))
        self.wait(0.5)

        # First step: (0, 0) -> (0, 1)
        step1 = Line(grid.c2p(0, 0), grid.c2p(0, 1), color=BLUE)
        self.play(Create(step1))
        self.wait(0.5)

        point1 = Dot(color=YELLOW).move_to(grid.c2p(0, 1))
        label1 = MathTex("(0,1)", font_size=24).next_to(point1, UP)
        self.play(FadeIn(point1), Write(label1))
        self.wait(0.5)

        # Second step: (0, 1) -> (1, 1)
        step2 = Line(grid.c2p(0, 1), grid.c2p(1, 1), color=BLUE)
        self.play(Create(step2))
        self.wait(0.5)

        point2 = Dot(color=YELLOW).move_to(grid.c2p(1, 1))
        label2 = MathTex("(1,1)", font_size=24).next_to(point2, UP)
        self.play(FadeIn(point2), Write(label2))
        self.wait(0.5)

        # Third step: (1, 1) -> (1, 2)
        step3 = Line(grid.c2p(1, 1), grid.c2p(1, 2), color=BLUE)
        self.play(Create(step3))
        self.wait(0.5)

        point3 = Dot(color=YELLOW).move_to(grid.c2p(1, 2))
        label3 = MathTex("(1,2)", font_size=24).next_to(point3, UP)
        self.play(FadeIn(point3), Write(label3))
        self.wait(0.5)

        # Fourth step: (1, 2) -> (2, 2)
        step4 = Line(grid.c2p(1, 2), grid.c2p(2, 2), color=BLUE)
        self.play(Create(step4))
        self.wait(0.5)

        point4 = Dot(color=YELLOW).move_to(grid.c2p(2, 2))
        label4 = MathTex("(2,2)", font_size=24).next_to(point4, UP)
        self.play(FadeIn(point4), Write(label4))
        self.wait(1.0)

        # Fade out staircase
        self.play(
            FadeOut(step1), FadeOut(step2), FadeOut(step3), FadeOut(step4),
            FadeOut(point1), FadeOut(point2), FadeOut(point3), FadeOut(point4),
            FadeOut(label1), FadeOut(label2), FadeOut(label3), FadeOut(label4),
            FadeOut(start_point), FadeOut(start_label)
        )
        self.wait(0.5)

        # Show new example: (4, 6) -> (6, 7)
        point_46 = Dot(color=GREEN).move_to(grid.c2p(4, 6))
        label_46 = MathTex("(4,6)", font_size=24).next_to(point_46, DOWN)
        point_46.shift(0.0 * RIGHT + -2.23 * UP)  # layout: separation vector
        self.play(FadeIn(point_46), Write(label_46))
        self.wait(0.5)

        # Arrow from (4, 6) to (6, 7)
        arrow = Arrow(grid.c2p(4, 6), grid.c2p(6, 7), color=RED, buff=0.1)
        step_label = MathTex("Step\ 1", font_size=24).next_to(arrow, UP)
        self.play(Create(arrow), Write(step_label))
        self.wait(0.5)

        point_67 = Dot(color=GREEN).move_to(grid.c2p(6, 7))
        label_67 = MathTex("(6,7)", font_size=24).next_to(point_67, UP)
        self.play(FadeIn(point_67), Write(label_67))
        self.wait(1.0)

        # Final cleanup
        self.play(
            FadeOut(point_46), FadeOut(label_46),
            FadeOut(arrow), FadeOut(step_label),
            FadeOut(point_67), FadeOut(label_67),
            FadeOut(title)
        )
        self.wait(0.5)
