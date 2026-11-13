from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Double Step Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        # Setup grid and axes
        axes = Axes(x_range=[-7, 7], y_range=[-4, 4])
        axes.scale(0.5)
        self.play(Create(axes))
        self.wait(0.5)

        # Point A at (x, y)
        x, y = 2, 1
        point_A = Dot(axes.c2p(x, y), color=YELLOW)
        label_A = MathTex(f"({x}, {y})", font_size=24).next_to(point_A, UR, buff=0.2)
        self.play(FadeIn(point_A), Write(label_A))
        self.wait(0.5)

        # First Krell step: (x,y) -> (y, x+1)
        point_B_intermediate = Dot(axes.c2p(y, x + 1), color=GREEN)
        arrow1 = Arrow(axes.c2p(x, y), axes.c2p(y, x + 1), buff=0.1, color=BLUE)
        label_step1 = MathTex("Step\ 1", font_size=24).next_to(arrow1, UP, buff=0.1)
        self.play(Create(arrow1), Write(label_step1))
        self.wait(0.5)
        label_step1.shift(0.0 * RIGHT + 0.22 * UP)  # layout: separation vector
        label_step1.shift(0.0 * RIGHT + 0.29 * UP)  # layout: separation vector
        self.play(FadeIn(point_B_intermediate))

        # Second Krell step: (y, x+1) -> (x+1, y+1)
        point_B = Dot(axes.c2p(x + 1, y + 1), color=RED)
        arrow2 = Arrow(axes.c2p(y, x + 1), axes.c2p(x + 1, y + 1), buff=0.1, color=BLUE)
        label_step2 = MathTex("Step\ 2", font_size=24).next_to(arrow2, UP, buff=0.1)
        self.play(Create(arrow2), Write(label_step2))
        self.wait(0.5)
        point_B.shift(0.0 * RIGHT + -0.32 * UP)  # layout: separation vector
        self.play(FadeIn(point_B))

        # Dashed direct arrow from A to B
        direct_arrow = DashedLine(axes.c2p(x, y), axes.c2p(x + 1, y + 1), color=ORANGE)
        self.play(Create(direct_arrow))
        self.wait(0.5)

        # Label at point B: (x+1, y+1)
        label_B = MathTex(f"({x}+1, {y}+1)", font_size=24).next_to(point_B, DR, buff=0.2)
        self.play(Write(label_B))
        self.wait(0.5)

        # Narration text
        narration = Text("Two consecutive Krell steps move the point diagonally to (x + 1, y + 1).", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        # Fade out everything except title and grid
        self.play(
            FadeOut(point_A),
            FadeOut(label_A),
            FadeOut(point_B_intermediate),
            FadeOut(arrow1),
            FadeOut(label_step1),
            FadeOut(arrow2),
            FadeOut(label_step2),
            FadeOut(point_B),
            FadeOut(direct_arrow),
            FadeOut(label_B),
            FadeOut(narration)
        )
        self.wait(0.5)

        # Show example: (3, 5) -> (5, 4) -> (5+1, 4+1) = (6, 5)
        example_text = Text("Example:", font_size=24).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(example_text))
        self.wait(0.5)

        x_ex, y_ex = 3, 5
        point_ex_A = Dot(axes.c2p(x_ex, y_ex), color=YELLOW)
        label_ex_A = MathTex(f"({x_ex}, {y_ex})", font_size=24).next_to(point_ex_A, UR, buff=0.2)
        self.play(FadeIn(point_ex_A), Write(label_ex_A))
        self.wait(0.5)

        point_ex_B_intermediate = Dot(axes.c2p(y_ex, x_ex + 1), color=GREEN)
        arrow_ex1 = Arrow(axes.c2p(x_ex, y_ex), axes.c2p(y_ex, x_ex + 1), buff=0.1, color=BLUE)
        label_ex_step1 = MathTex("Step\ 1", font_size=24).next_to(arrow_ex1, UP, buff=0.1)
        self.play(Create(arrow_ex1), Write(label_ex_step1))
        self.wait(0.5)
        self.play(FadeIn(point_ex_B_intermediate))

        point_ex_B = Dot(axes.c2p(x_ex + 1, y_ex + 1), color=RED)
        arrow_ex2 = Arrow(axes.c2p(y_ex, x_ex + 1), axes.c2p(x_ex + 1, y_ex + 1), buff=0.1, color=BLUE)
        label_ex_step2 = MathTex("Step\ 2", font_size=24).next_to(arrow_ex2, UP, buff=0.1)
        self.play(Create(arrow_ex2), Write(label_ex_step2))
        self.wait(0.5)
        self.play(FadeIn(point_ex_B))

        label_ex_B = MathTex(f"({x_ex}+1, {y_ex}+1)", font_size=24).next_to(point_ex_B, DR, buff=0.2)
        self.play(Write(label_ex_B))
        self.wait(1.5)

        # Final fade out
        self.play(
            FadeOut(point_ex_A),
            FadeOut(label_ex_A),
            FadeOut(point_ex_B_intermediate),
            FadeOut(arrow_ex1),
            FadeOut(label_ex_step1),
            FadeOut(arrow_ex2),
            FadeOut(label_ex_step2),
            FadeOut(point_ex_B),
            FadeOut(label_ex_B),
            FadeOut(example_text),
            FadeOut(title),
            FadeOut(axes)
        )
        self.wait(0.5)
