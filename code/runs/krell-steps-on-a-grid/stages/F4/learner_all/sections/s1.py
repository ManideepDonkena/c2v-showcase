from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Krell Transformation Rule", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid
        grid = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY}
        )
        grid.scale(0.8)
        grid.to_edge(DOWN, buff=0.5)
        self.play(Create(grid))
        self.wait(0.5)

        # Point P at (3, 5)
        P = Dot(color=BLUE)
        P.move_to(grid.c2p(3, 5))
        label_P = MathTex("(3, 5)", font_size=24).next_to(P, UR, buff=0.2)
        label_P.shift(0.0 * RIGHT + -0.38 * UP)  # layout: separation vector
        self.play(FadeIn(P), Write(label_P))
        self.wait(0.5)

        # Arrow from P to Q
        arrow = Arrow(start=P.get_center(), end=grid.c2p(5, 4), color=YELLOW)
        arrow.shift(0.0 * RIGHT + -0.63 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Point Q at (5, 4)
        Q = Dot(color=RED)
        Q.move_to(grid.c2p(5, 4))
        label_Q = MathTex("(5, 4)", font_size=24).next_to(Q, UR, buff=0.2)
        self.play(FadeIn(Q), Write(label_Q))
        self.wait(0.5)

        # Labels for transformation steps
        swap_label = Text("Swap", font_size=24).next_to(arrow, UP)
        plus1_label = Text("+1", font_size=24).next_to(arrow, UP)
        self.play(Write(swap_label))
        self.wait(0.5)
        self.play(Transform(swap_label, plus1_label))
        self.wait(0.5)
        self.play(FadeOut(swap_label))

        # Narration text
        narration = Text("A Krell step transforms any grid point (x, y) into a new location.", font_size=24)
        narration.to_edge(DOWN, buff=0.5)
        self.play(Write(narration))
        self.wait(1)

        # Clear narration and show example
        self.play(FadeOut(narration))

        # Show (4, 6) -> (6, 7)
        point_46 = Dot(color=GREEN)
        point_46.move_to(grid.c2p(4, 6))
        label_46 = MathTex("(4, 6)", font_size=24).next_to(point_46, UR, buff=0.2)
        self.play(FadeIn(point_46), Write(label_46))
        self.wait(0.5)

        arrow_step1 = Arrow(start=point_46.get_center(), end=grid.c2p(6, 7), color=YELLOW)
        step1_label = Text("Step 1", font_size=24).next_to(arrow_step1, UP)
        self.play(GrowArrow(arrow_step1), Write(step1_label))
        self.wait(0.5)

        point_67 = Dot(color=ORANGE)
        point_67.move_to(grid.c2p(6, 7))
        label_67 = MathTex("(6, 7)", font_size=24).next_to(point_67, UR, buff=0.2)
        self.play(FadeIn(point_67), Write(label_67))
        self.wait(1)

        # Final narration
        final_narration = Text("The first step takes us from (4, 6) to (6, 7)", font_size=24)
        final_narration.to_edge(DOWN, buff=0.5)
        self.play(Write(final_narration))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(P), FadeOut(label_P),
            FadeOut(Q), FadeOut(label_Q),
            FadeOut(arrow),
            FadeOut(point_46), FadeOut(label_46),
            FadeOut(point_67), FadeOut(label_67),
            FadeOut(arrow_step1), FadeOut(step1_label),
            FadeOut(final_narration)
        )
