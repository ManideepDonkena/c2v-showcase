from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Staircase Path from Origin", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(x_range=[-1, 4], y_range=[-1, 4], 
                           axis_config={"stroke_color": GREY, "stroke_width": 1})
        grid.set_opacity(0.5)
        self.play(Create(grid))
        self.wait(0.5)

        # Start point
        start_point = Dot(color=YELLOW).move_to(grid.c2p(0, 0))
        start_label = MathTex("(0,0)", font_size=24).next_to(start_point, DOWN, buff=0.2)
        self.play(FadeIn(start_point), Write(start_label))
        self.wait(1)

        # First step: (0,0) -> (0,1)
        step1 = Arrow(start_point.get_center(), grid.c2p(0, 1), color=BLUE, buff=0)
        point1 = Dot(color=YELLOW).move_to(grid.c2p(0, 1))
        label1 = MathTex("(0,1)", font_size=24).next_to(point1, UP, buff=0.2)
        self.play(GrowArrow(step1), FadeIn(point1), Write(label1))
        self.wait(1)

        # Second step: (0,1) -> (1,1)
        step2 = Arrow(point1.get_center(), grid.c2p(1, 1), color=BLUE, buff=0)
        point2 = Dot(color=YELLOW).move_to(grid.c2p(1, 1))
        label2 = MathTex("(1,1)", font_size=24).next_to(point2, DOWN, buff=0.2)
        self.play(GrowArrow(step2), FadeIn(point2), Write(label2))
        self.wait(1)

        # Third step: (1,1) -> (1,2)
        step3 = Arrow(point2.get_center(), grid.c2p(1, 2), color=BLUE, buff=0)
        point3 = Dot(color=YELLOW).move_to(grid.c2p(1, 2))
        label3 = MathTex("(1,2)", font_size=24).next_to(point3, UP, buff=0.2)
        self.play(GrowArrow(step3), FadeIn(point3), Write(label3))
        self.wait(1)

        # Fourth step: (1,2) -> (2,2)
        step4 = Arrow(point3.get_center(), grid.c2p(2, 2), color=BLUE, buff=0)
        point4 = Dot(color=YELLOW).move_to(grid.c2p(2, 2))
        label4 = MathTex("(2,2)", font_size=24).next_to(point4, DOWN, buff=0.2)
        self.play(GrowArrow(step4), FadeIn(point4), Write(label4))
        self.wait(1.5)

        # Narration text
        narration = Text("Repeating Krell steps from the origin creates a distinct staircase pattern.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        # Clear narration and show path summary
        self.play(FadeOut(narration))
        summary = Text("Path: (0,0) → (0,1) → (1,1) → (1,2) → (2,2)", font_size=24)
        summary.to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)

        # Fade out summary
        self.play(FadeOut(summary))

        # Show point (4, 6) and arrow labeled 'Step 1' leading to new point
        point_46 = Dot(color=YELLOW).move_to(grid.c2p(4, 6))
        label_46 = MathTex("(4,6)", font_size=24).next_to(point_46, UP, buff=0.2)
        point_46.shift(0.0 * RIGHT + -0.73 * UP)  # layout: separation vector
        self.play(FadeIn(point_46), Write(label_46))
        self.wait(1)

        # Arrow from (4,6) to (6,7)
        step_new = Arrow(point_46.get_center(), grid.c2p(6, 7), color=BLUE, buff=0)
        point_new = Dot(color=YELLOW).move_to(grid.c2p(6, 7))
        label_new = MathTex("(6,7)", font_size=24).next_to(point_new, DOWN, buff=0.2)
        self.play(GrowArrow(step_new), FadeIn(point_new), Write(label_new))
        self.wait(1)

        # Say the narration
        narration_2 = Text("The first step takes us from (4, 6) to (6, 7)", font_size=24)
        narration_2.to_edge(DOWN)
        self.play(Write(narration_2))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(title, grid, point_46, point_new, step_new, label_46, label_new, narration_2))
