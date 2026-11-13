from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Double Step Identity", font_size=36).to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Setup grid and axes
        axes = Axes(
            x_range=[-7, 7, 1],
            y_range=[-3.9, 3.9, 1],
            axis_config={"stroke_color": GREY},
            tips=False,
        )
        self.play(Create(axes), run_time=0.5)
        self.wait(0.5)

        # Point A at (x, y)
        x, y = 2, 1
        A = Dot(axes.c2p(x, y), color=YELLOW)
        label_A = MathTex(f"({x}, {y})").next_to(A, DOWN, buff=0.2)
        self.play(FadeIn(A), Write(label_A))
        self.wait(0.5)

        # First Krell step: (x, y) -> (y, x + 1)
        step1 = axes.c2p(y, x + 1)
        B_intermediate = Dot(step1, color=GREEN)
        arrow1 = Arrow(A.get_center(), B_intermediate.get_center(), buff=0.1, color=BLUE)
        label1 = MathTex("Step 1").next_to(arrow1, UP, buff=0.2)
        self.play(GrowArrow(arrow1), Write(label1))
        self.wait(0.5)

        # Second Krell step: (y, x + 1) -> (x + 1, y + 1)
        step2 = axes.c2p(x + 1, y + 1)
        B = Dot(step2, color=YELLOW)
        arrow2 = Arrow(B_intermediate.get_center(), B.get_center(), buff=0.1, color=BLUE)
        label2 = MathTex("Step 2").next_to(arrow2, UP, buff=0.2)
        label2.shift(0.0 * RIGHT + 0.55 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow2), Write(label2))
        self.wait(0.5)

        # Label at final point B
        label_B = MathTex(f"({x + 1}, {y + 1})").next_to(B, DOWN, buff=0.2)
        self.play(Write(label_B))
        self.wait(0.5)

        # Dashed arrow from A to B (net result)
        net_arrow = DashedLine(A.get_center(), B.get_center(), color=RED, dash_length=0.1)
        net_label = MathTex("(x+1, y+1)").next_to(net_arrow, UR, buff=0.2)
        self.play(Create(net_arrow), Write(net_label))
        self.wait(1)

        # Narration text
        narration = Text("Two consecutive Krell steps have a powerful simplification.", font_size=24).to_edge(DOWN, buff=0.3)
        self.play(Write(narration))
        self.wait(2)

        # Clear screen
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(A),
            FadeOut(B_intermediate),
            FadeOut(B),
            FadeOut(label_A),
            FadeOut(label_B),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(net_arrow),
            FadeOut(label1),
            FadeOut(label2),
            FadeOut(net_label),
            FadeOut(narration)
        )
        self.wait(0.5)


        # NEW: Show point (4, 6) and arrow to (6, 7)
        x_new, y_new = 4, 6
        point_start = Dot(axes.c2p(x_new, y_new), color=YELLOW)
        label_start = MathTex(f"({x_new}, {y_new})").next_to(point_start, DOWN, buff=0.2)
        self.play(FadeIn(point_start), Write(label_start))
        self.wait(0.5)

        # Arrow to (6, 7)
        point_end = Dot(axes.c2p(6, 7), color=YELLOW)
        arrow_new = Arrow(point_start.get_center(), point_end.get_center(), buff=0.1, color=BLUE)
        label_new = MathTex("Step 1").next_to(arrow_new, UP, buff=0.2)
        self.play(GrowArrow(arrow_new), Write(label_new))
        self.wait(0.5)

        # Label at (6, 7)
        label_end = MathTex(f"(6, 7)").next_to(point_end, DOWN, buff=0.2)
        self.play(Write(label_end))
        self.wait(0.5)

        # Narration for new step
        narration_new = Text("The first step takes us from (4, 6) to (6, 7)", font_size=24).to_edge(DOWN, buff=0.3)
        self.play(Write(narration_new))
        self.wait(2)

        # Fade out new elements
        self.play(
            FadeOut(point_start),
            FadeOut(label_start),
            FadeOut(point_end),
            FadeOut(label_end),
            FadeOut(arrow_new),
            FadeOut(label_new),
            FadeOut(narration_new)
        )
        self.wait(0.5)
