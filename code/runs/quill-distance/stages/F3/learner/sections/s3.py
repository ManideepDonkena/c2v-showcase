from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Shape of Distance 2", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            axis_config={"stroke_color": GREY_A},
            background_line_style={"stroke_color": GREY_D}
        )
        self.play(Create(grid))
        self.wait(0.5)
        # Center point C
        C = Dot([0, 0, 0], color=WHITE)
        c_label = MathTex("C(0,0)", font_size=24).next_to(C, DOWN, buff=0.2)
        self.play(FadeIn(C), Write(c_label))
        self.wait(0.5)

        # Points at distance 2
        p1 = Dot([2, 0, 0], color=YELLOW)
        p1_label = MathTex("(2,0)", font_size=24).next_to(p1, DOWN, buff=0.2)
        calc1 = MathTex("2 + 0 = 2", font_size=24).next_to(p1_label, DOWN, buff=0.2)
        self.play(FadeIn(p1), Write(p1_label), Write(calc1))
        self.wait(1)

        p2 = Dot([-2, 0, 0], color=YELLOW)
        p2_label = MathTex("(-2,0)", font_size=24).next_to(p2, DOWN, buff=0.2)
        calc2 = MathTex("2 + 0 = 2", font_size=24).next_to(p2_label, DOWN, buff=0.2)
        self.play(FadeIn(p2), Write(p2_label), Write(calc2))
        self.wait(1)

        p3 = Dot([0, 1, 0], color=YELLOW)
        p3_label = MathTex("(0,1)", font_size=24).next_to(p3, UP, buff=0.2)
        calc3 = MathTex("0 + 2 = 2", font_size=24).next_to(p3_label, DOWN, buff=0.2)
        calc3.shift(0.0 * RIGHT + -0.31 * UP)  # layout: separation vector
        self.play(FadeIn(p3), Write(p3_label), Write(calc3))
        self.wait(1)

        p4 = Dot([0, -1, 0], color=YELLOW)
        p4_label = MathTex("(0,-1)", font_size=24).next_to(p4, DOWN, buff=0.2)
        calc4 = MathTex("0 + 2 = 2", font_size=24).next_to(p4_label, DOWN, buff=0.2)
        self.play(FadeIn(p4), Write(p4_label), Write(calc4))
        self.wait(1)

        # Fade out distance 2 points
        self.play(
            FadeOut(p1), FadeOut(p2), FadeOut(p3), FadeOut(p4),
            FadeOut(p1_label), FadeOut(p2_label), FadeOut(p3_label), FadeOut(p4_label),
            FadeOut(calc1), FadeOut(calc2), FadeOut(calc3), FadeOut(calc4)
        )
        self.wait(0.5)

        # Show points at distance 4
        p5 = Dot([4, 0, 0], color=GREEN)
        p5_label = MathTex("(4,0)", font_size=24).next_to(p5, DOWN, buff=0.2)
        calc5 = MathTex("4 + 0 = 4", font_size=24).next_to(p5_label, DOWN, buff=0.2)
        self.play(FadeIn(p5), Write(p5_label), Write(calc5))
        self.wait(1)

        p6 = Dot([-4, 0, 0], color=GREEN)
        p6_label = MathTex("(-4,0)", font_size=24).next_to(p6, DOWN, buff=0.2)
        calc6 = MathTex("4 + 0 = 4", font_size=24).next_to(p6_label, DOWN, buff=0.2)
        self.play(FadeIn(p6), Write(p6_label), Write(calc6))
        self.wait(1)

        p7 = Dot([0, 2, 0], color=GREEN)
        p7_label = MathTex("(0,2)", font_size=24).next_to(p7, UP, buff=0.2)
        calc7 = MathTex("0 + 4 = 4", font_size=24).next_to(p7_label, DOWN, buff=0.2)
        calc7.shift(0.0 * RIGHT + -0.31 * UP)  # layout: separation vector
        self.play(FadeIn(p7), Write(p7_label), Write(calc7))
        self.wait(1)

        p8 = Dot([0, -2, 0], color=GREEN)
        p8_label = MathTex("(0,-2)", font_size=24).next_to(p8, DOWN, buff=0.2)
        calc8 = MathTex("0 + 4 = 4", font_size=24).next_to(p8_label, DOWN, buff=0.2)
        self.play(FadeIn(p8), Write(p8_label), Write(calc8))
        self.wait(1)

        # Fade out distance 4 points
        self.play(
            FadeOut(p5), FadeOut(p6), FadeOut(p7), FadeOut(p8),
            FadeOut(p5_label), FadeOut(p6_label), FadeOut(p7_label), FadeOut(p8_label),
            FadeOut(calc5), FadeOut(calc6), FadeOut(calc7), FadeOut(calc8)
        )
        self.wait(0.5)

        # Explanation text
        explanation = Text("Distance 2: 2 sideways or 1 vertical", font_size=24).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(1.5)

        explanation2 = Text("Distance 4: 4 sideways or 2 vertical", font_size=24).next_to(explanation, UP, buff=0.3)
        self.play(Write(explanation2))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(C),
            FadeOut(c_label),
            FadeOut(explanation),
            FadeOut(explanation2)
        )
        self.wait(0.5)
