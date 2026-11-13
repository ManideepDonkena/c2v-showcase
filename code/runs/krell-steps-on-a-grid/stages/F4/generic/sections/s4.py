from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Double Step Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Setup grid and axes
        axes = Axes(x_range=[-7, 7], y_range=[-4, 4], axis_config={"stroke_color": GREY})
        self.play(Create(axes))
        self.wait(0.5)

        # Point A at (x, y)
        x, y = 2, 1
        A = Dot(axes.c2p(x, y), color=BLUE)
        label_A = MathTex(f"({x}, {y})", font_size=24).next_to(A, DOWN)
        self.play(FadeIn(A), Write(label_A))
        self.wait(0.5)

        # First Krell step: (x, y) -> (y, x + 1)
        step1 = axes.c2p(y, x + 1)
        intermediate = Dot(step1, color=GREEN)
        label_intermediate = MathTex(f"({y}, {x+1})", font_size=24).next_to(intermediate, UP)
        arrow1 = Arrow(A.get_center(), intermediate.get_center(), buff=0.1, color=YELLOW)
        label1 = MathTex("Step 1", font_size=24).next_to(arrow1, UP)
        self.play(GrowArrow(arrow1), Write(label1))
        self.wait(0.5)
        self.play(FadeIn(intermediate), Write(label_intermediate))
        self.wait(0.5)

        # Second Krell step: (y, x + 1) -> (x + 1, y + 1)
        step2 = axes.c2p(x + 1, y + 1)
        B = Dot(step2, color=RED)
        label_B = MathTex(f"({x+1}, {y+1})", font_size=24).next_to(B, UR)
        arrow2 = Arrow(intermediate.get_center(), B.get_center(), buff=0.1, color=YELLOW)
        label2 = MathTex("Step 2", font_size=24).next_to(arrow2, UP)
        label2.shift(0.32 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow2), Write(label2))
        self.wait(0.5)
        self.play(FadeIn(B), Write(label_B))
        self.wait(0.5)

        # Dashed diagonal arrow from A to B
        dashed_arrow = DashedLine(A.get_center(), B.get_center(), color=ORANGE)
        label_net = MathTex("(x+1, y+1)", font_size=24).next_to(dashed_arrow, RIGHT)
        self.play(Create(dashed_arrow), Write(label_net))
        self.wait(0.5)

        # Narration text
        narration = Text("Two consecutive Krell steps have a powerful simplification.", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        # Clarify the new point
        clarify = Text("Regardless of starting position, two steps move to (x + 1, y + 1).", font_size=24).to_edge(DOWN)
        self.play(Write(clarify))
        self.wait(2.0)
        self.play(FadeOut(clarify))

        # Example: one krell step from (3,5) gives (5,4)
        example = MathTex("Example: (3, 5) \\xrightarrow{\\text{Krell}} (5, 4)", font_size=24).to_edge(DOWN)
        self.play(Write(example))
        self.wait(2.0)
        self.play(FadeOut(example))

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(A),
            FadeOut(label_A),
            FadeOut(intermediate),
            FadeOut(label_intermediate),
            FadeOut(B),
            FadeOut(label_B),
            FadeOut(arrow1),
            FadeOut(label1),
            FadeOut(arrow2),
            FadeOut(label2),
            FadeOut(dashed_arrow),
            FadeOut(label_net)
        )
        self.wait(0.5)
