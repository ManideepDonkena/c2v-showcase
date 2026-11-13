from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Krell Transformation Rule", font_size=36)
        title.to_edge(UP, buff=0.2)

        # Grid
        grid = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-3.9, 3.9, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY, "stroke_opacity": 0.5}
        )
        grid.scale(0.8)
        grid.to_edge(DOWN, buff=0.5)

        # Axes labels
        x_label = Text("x", font_size=24).next_to(grid.get_x_axis(), RIGHT)
        y_label = Text("y", font_size=24).next_to(grid.get_y_axis(), UP)

        # Point P at (3, 5)
        P = Dot(point=grid.c2p(3, 5), color=BLUE)
        label_P = Text("(3, 5)", font_size=24).next_to(P, UR, buff=0.2)

        # Arrow from P to Q
        arrow = Arrow(start=grid.c2p(3, 5), end=grid.c2p(5, 4), color=YELLOW)
        label_arrow = Text("Swap", font_size=24).next_to(arrow, UP, buff=0.1)

        # Point Q at (5, 4)
        Q = Dot(point=grid.c2p(5, 4), color=GREEN)
        label_Q = Text("(5, 4)", font_size=24).next_to(Q, UR, buff=0.2)

        # Show title
        self.play(Write(title))
        self.wait(0.5)

        # Show grid and axes
        self.play(Create(grid), run_time=1)
        self.play(Write(x_label), Write(y_label))
        self.wait(0.5)

        # Show P
        P.shift(0.0 * RIGHT + -0.44 * UP)  # layout: separation vector
        self.play(FadeIn(P), Write(label_P))
        self.wait(0.5)

        # Show arrow and label "Swap"
        self.play(Create(arrow), Write(label_arrow))
        self.wait(1)

        # Fade out arrow and "Swap" label
        self.play(FadeOut(arrow), FadeOut(label_arrow))

        # Show Q
        self.play(FadeIn(Q), Write(label_Q))
        self.wait(0.5)

        # Show "+1" label above Q
        plus_one = Text("+1", font_size=24).next_to(Q, UP, buff=0.1)
        self.play(Write(plus_one))
        self.wait(1.5)

        # Fade out everything except title and grid
        self.play(
            FadeOut(P),
            FadeOut(label_P),
            FadeOut(Q),
            FadeOut(label_Q),
            FadeOut(plus_one),
            run_time=0.5
        )

        # Narration text
        narration = Text("A Krell step transforms any grid point (x, y) into a new location.", font_size=24)
        narration.to_edge(DOWN, buff=0.3)
        self.play(Write(narration))
        self.wait(1.5)

        # Fade out narration
        self.play(FadeOut(narration))

        # Show transformation formula
        formula = MathTex("(x, y) \\rightarrow (y, x + 1)", font_size=32)
        formula.to_edge(DOWN, buff=0.3)
        self.play(Write(formula))
        self.wait(2)

        # Fade out everything except title and grid
        self.play(FadeOut(formula), run_time=0.5)
        self.wait(0.5)

        # Final narration text
        final_narration = Text("First, we swap the coordinates to get (y, x),", font_size=24)
        final_narration.to_edge(DOWN, buff=0.3)
        self.play(Write(final_narration))
        self.wait(1.5)

        self.play(FadeOut(final_narration))

        second_narration = Text("then we add 1 to the second number, resulting in (y, x + 1).", font_size=24)
        second_narration.to_edge(DOWN, buff=0.3)
        self.play(Write(second_narration))
        self.wait(2)

        self.play(FadeOut(second_narration))

        # End
        self.wait(0.5)
