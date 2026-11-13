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
            y_range=[-3.9, 3.9, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY, "stroke_opacity": 0.5}
        )
        grid.scale(0.55)
        grid.move_to(DOWN * 0.75)
        self.play(Create(grid))
        self.wait(0.5)

        # Point P at (3, 5)
        P = Dot(color=BLUE)
        P.move_to(grid.c2p(3, 5))
        label_P = MathTex("(3, 5)", font_size=24).next_to(P, UL, buff=0.15)
        self.play(FadeIn(P), Write(label_P))
        self.wait(1)

        # Arrow from P to Q
        arrow = Arrow(start=P.get_center(), end=grid.c2p(5, 4), color=YELLOW, buff=0.1)
        self.play(GrowArrow(arrow))
        self.wait(1)

        # Point Q at (5, 4)
        Q = Dot(color=RED)
        Q.move_to(grid.c2p(5, 4))
        label_Q = MathTex("(5, 4)", font_size=24).next_to(Q, UR, buff=0.2)
        self.play(FadeIn(Q), Write(label_Q))
        self.wait(1)

        # Swap label
        swap_label = Text("Swap", font_size=24).next_to(arrow, UP, buff=0.3)
        self.play(Write(swap_label))
        self.wait(1.5)

        # +1 label
        plus_label = Text("+1", font_size=24).next_to(arrow, DOWN, buff=0.3)
        self.play(Write(plus_label))
        self.wait(2)

        # Narration text
        narration = Text("A Krell step transforms any grid point (x, y) into a new location.", font_size=24)
        narration.to_edge(DOWN, buff=0.5)
        self.play(Write(narration))
        self.wait(2.5)

        # Clear narration and fade out
        self.play(FadeOut(narration))

        # Show transformation formula
        formula = MathTex("(x, y) \\rightarrow (y, x + 1)", font_size=32)
        formula.to_edge(DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(2)

        # Fade out everything except grid and points
        self.play(
            FadeOut(title),
            FadeOut(swap_label),
            FadeOut(plus_label),
            FadeOut(label_P),
            FadeOut(label_Q),
            FadeOut(formula)
        )
        self.wait(1)
