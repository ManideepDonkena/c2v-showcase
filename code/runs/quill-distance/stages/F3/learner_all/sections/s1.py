from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Asymmetric Grid", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY}
        )
        grid.scale(0.8)
        grid.to_edge(DOWN)

        # Draw grid
        self.play(Create(grid), run_time=1)
        self.wait(0.5)

        # Points A and B
        A = Dot(color=YELLOW).move_to(grid.c2p(0, 0))
        B = Dot(color=RED).move_to(grid.c2p(1, 1))

        label_A = MathTex("A(0,0)", font_size=24).next_to(A, DOWN)
        label_B = MathTex("B(1,1)", font_size=24).next_to(B, UP)

        self.play(FadeIn(A), Write(label_A))
        self.wait(0.5)
        self.play(FadeIn(B), Write(label_B))
        self.wait(0.5)

        # Horizontal arrow from A to B
        arrow_h = Arrow(start=grid.c2p(0, 0), end=grid.c2p(1, 0), color=BLUE)
        label_h = MathTex("Cost: 1", font_size=24).next_to(arrow_h, DOWN, buff=0.1)
        self.play(GrowArrow(arrow_h), Write(label_h))
        self.wait(1)

        # Vertical arrow from A to B
        arrow_v = Arrow(start=grid.c2p(1, 0), end=grid.c2p(1, 1), color=GREEN)
        label_v = MathTex("Cost: 2", font_size=24).next_to(arrow_v, RIGHT, buff=0.1)
        self.play(GrowArrow(arrow_v), Write(label_v))
        self.wait(1)

        # Fade out arrows and labels
        self.play(FadeOut(arrow_h), FadeOut(label_h), FadeOut(arrow_v), FadeOut(label_v))

        # Formula at top
        formula = MathTex(r"\text{Quill Distance} = |x_1 - x_2| + 2 \cdot |y_1 - y_2|", font_size=30)
        formula.to_edge(UP, buff=0.2)
        self.play(FadeIn(formula))
        self.wait(1.5)

        # Show central point
        center = Dot(color=PURPLE).move_to(grid.c2p(0, 0))
        label_center = MathTex("C(0,0)", font_size=24).next_to(center, DOWN, buff=0.1)
        self.play(FadeIn(center), Write(label_center))
        self.wait(0.5)

        # Points at quill distance 4
        point1 = Dot(color=ORANGE).move_to(grid.c2p(4, 0))
        label1 = MathTex("4h", font_size=24).next_to(point1, DOWN, buff=0.1)
        self.play(FadeIn(point1), Write(label1))
        self.wait(0.5)

        point2 = Dot(color=ORANGE).move_to(grid.c2p(-4, 0))
        label2 = MathTex("4h", font_size=24).next_to(point2, DOWN, buff=0.1)
        self.play(FadeIn(point2), Write(label2))
        self.wait(0.5)

        point3 = Dot(color=ORANGE).move_to(grid.c2p(0, 2))
        label3 = MathTex("2v", font_size=24).next_to(point3, UP, buff=0.1)
        self.play(FadeIn(point3), Write(label3))
        self.wait(0.5)

        point4 = Dot(color=ORANGE).move_to(grid.c2p(0, -2))
        label4 = MathTex("2v", font_size=24).next_to(point4, DOWN, buff=0.1)
        self.play(FadeIn(point4), Write(label4))
        self.wait(1.5)

        # Fade out everything except grid and center
        self.play(
            FadeOut(point1), FadeOut(label1),
            FadeOut(point2), FadeOut(label2),
            FadeOut(point3), FadeOut(label3),
            FadeOut(point4), FadeOut(label4),
            FadeOut(center), FadeOut(label_center)
        )

        # Narration text
        narration = Text("Distance 2 requires 2 sideways or 1 vertical step.", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)

        self.play(FadeOut(narration))

        # Worked example
        example = MathTex(r"\text{From } (0,0) \text{ to } (3,2): 3 + 4 = 7", font_size=28)
        example.to_edge(DOWN)
        self.play(Write(example))
        self.wait(2)

        self.play(FadeOut(example), FadeOut(formula), FadeOut(title))
