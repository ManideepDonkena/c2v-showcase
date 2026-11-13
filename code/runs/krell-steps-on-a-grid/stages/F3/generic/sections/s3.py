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

        # Start point
        start_point = Dot(color=YELLOW).move_to(grid.c2p(0, 0))
        start_label = MathTex("(0,0)", font_size=24).next_to(start_point, DOWN)
        self.play(FadeIn(start_point), Write(start_label))
        self.wait(1)

        # First step: (0,0) -> (0,1)
        step1 = Arrow(start_point.get_center(), grid.c2p(0, 1), buff=0, color=BLUE)
        point1 = Dot(color=YELLOW).move_to(grid.c2p(0, 1))
        label1 = MathTex("(0,1)", font_size=24).next_to(point1, UP)
        self.play(GrowArrow(step1), FadeIn(point1), Write(label1))
        self.wait(1)

        # Second step: (0,1) -> (1,1)
        step2 = Arrow(point1.get_center(), grid.c2p(1, 1), buff=0, color=BLUE)
        point2 = Dot(color=YELLOW).move_to(grid.c2p(1, 1))
        label2 = MathTex("(1,1)", font_size=24).next_to(point2, UP)
        self.play(GrowArrow(step2), FadeIn(point2), Write(label2))
        self.wait(1)

        # Third step: (1,1) -> (1,2)
        step3 = Arrow(point2.get_center(), grid.c2p(1, 2), buff=0, color=BLUE)
        point3 = Dot(color=YELLOW).move_to(grid.c2p(1, 2))
        label3 = MathTex("(1,2)", font_size=24).next_to(point3, UP)
        step3.shift(0.53 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(GrowArrow(step3), FadeIn(point3), Write(label3))
        self.wait(1)

        # Fourth step: (1,2) -> (2,2)
        step4 = Arrow(point3.get_center(), grid.c2p(2, 2), buff=0, color=BLUE)
        point4 = Dot(color=YELLOW).move_to(grid.c2p(2, 2))
        label4 = MathTex("(2,2)", font_size=24).next_to(point4, UP)
        self.play(GrowArrow(step4), FadeIn(point4), Write(label4))
        self.wait(1.5)

        # Show krell step definition
        rule1 = Text("A krell step moves (x, y) to (y, x + 1)", font_size=24)
        rule1.to_edge(DOWN)
        self.play(Write(rule1))
        self.wait(1.5)

        # Example: (3,5) -> (5,4)
        example = MathTex("(3,5) \\xrightarrow{\\text{krell}} (5,4)", font_size=30)
        example.next_to(rule1, UP)
        self.play(Write(example))
        self.wait(2)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(start_point),
            FadeOut(point1),
            FadeOut(point2),
            FadeOut(point3),
            FadeOut(point4),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            FadeOut(step4),
            FadeOut(start_label),
            FadeOut(label1),
            FadeOut(label2),
            FadeOut(label3),
            FadeOut(label4),
            FadeOut(rule1),
            FadeOut(example)
        )
        self.wait(0.5)
