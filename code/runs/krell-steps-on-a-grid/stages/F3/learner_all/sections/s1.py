from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Krell Transformation Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid
        grid = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-3.9, 3.9, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY}
        )
        self.play(Create(grid))
        self.wait(0.5)

        # Axes labels
        x_label = MathTex("x").next_to(grid.get_x_axis(), UR, buff=0.2)
        y_label = MathTex("y").next_to(grid.get_y_axis(), UR, buff=0.2)
        x_label.shift(-0.49 * RIGHT + 0.0 * UP)  # layout: separation vector
        y_label.shift(0.0 * RIGHT + -0.57 * UP)  # layout: separation vector
        self.play(Write(x_label), Write(y_label))
        self.wait(0.5)

        # Point P at (3, 5)
        P = Dot(color=BLUE).move_to(grid.c2p(3, 5))
        label_P = MathTex("(3, 5)").next_to(P, UR, buff=0.2)
        P.shift(0.0 * RIGHT + -1.23 * UP)  # layout: separation vector
        self.play(FadeIn(P), Write(label_P))
        self.wait(0.5)

        # Arrow from P to Q
        arrow = Arrow(start=P.get_center(), end=grid.c2p(5, 4), color=YELLOW)
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Point Q at (5, 4)
        Q = Dot(color=RED).move_to(grid.c2p(5, 4))
        label_Q = MathTex("(5, 4)").next_to(Q, UR, buff=0.2)
        self.play(FadeIn(Q), Write(label_Q))
        self.wait(0.5)

        # Labels for transformation steps
        swap_label = Text("Swap", font_size=24).next_to(arrow, UP)
        plus1_label = Text("+1", font_size=24).next_to(arrow, DOWN)
        self.play(Write(swap_label))
        self.wait(0.5)
        self.play(Write(plus1_label))
        self.wait(1)

        # Fade out first example
        self.play(FadeOut(P), FadeOut(label_P), FadeOut(Q), FadeOut(label_Q), FadeOut(arrow), FadeOut(swap_label), FadeOut(plus1_label))

        # Example with (0, 0)
        origin = Dot(color=BLUE).move_to(grid.c2p(0, 0))
        label_origin = MathTex("(0, 0)").next_to(origin, UR, buff=0.2)
        self.play(FadeIn(origin), Write(label_origin))
        self.wait(0.5)

        # Step 1: (0, 0) -> (0, 1)
        arrow1 = Arrow(start=origin.get_center(), end=grid.c2p(0, 1), color=YELLOW)
        label_step1 = MathTex("(0, 1)").next_to(grid.c2p(0, 1), UR, buff=0.2)
        self.play(GrowArrow(arrow1))
        self.wait(0.5)
        self.play(Write(label_step1))
        self.wait(0.5)

        # Step 2: (0, 1) -> (1, 1)
        arrow2 = Arrow(start=grid.c2p(0, 1), end=grid.c2p(1, 1), color=YELLOW)
        label_step2 = MathTex("(1, 1)").next_to(grid.c2p(1, 1), UR, buff=0.2)
        self.play(GrowArrow(arrow2))
        self.wait(0.5)
        self.play(Write(label_step2))
        self.wait(0.5)

        # Fade out step-by-step
        self.play(FadeOut(origin), FadeOut(label_origin), FadeOut(arrow1), FadeOut(label_step1), FadeOut(arrow2), FadeOut(label_step2))

        # Third step from (1, 2) to (2, 3)
        point_12 = Dot(color=BLUE).move_to(grid.c2p(1, 2))
        label_12 = MathTex("(1, 2)").next_to(point_12, UR, buff=0.2)
        self.play(FadeIn(point_12), Write(label_12))
        self.wait(0.5)

        arrow3 = Arrow(start=point_12.get_center(), end=grid.c2p(2, 3), color=YELLOW)
        label_step3 = MathTex("(2, 3)").next_to(grid.c2p(2, 3), UR, buff=0.2)
        self.play(GrowArrow(arrow3))
        self.wait(0.5)
        self.play(Write(label_step3))
        self.wait(0.5)

        # Final fade out
        self.play(FadeOut(point_12), FadeOut(label_12), FadeOut(arrow3), FadeOut(label_step3))

        # Narration text at bottom
        narration = Text("A Krell step transforms any grid point (x, y) into a new location. First, we swap the coordinates to get (y, x), then we add 1 to the second number, resulting in (y, x + 1).", font_size=20)
        self.play(Write(narration))
        self.wait(3)

        self.play(FadeOut(narration), FadeOut(title), FadeOut(grid))
