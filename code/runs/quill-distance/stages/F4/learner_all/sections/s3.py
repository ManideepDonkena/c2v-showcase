from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Shape of Distance 2", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid and center point
        grid = NumberPlane(x_range=[-7, 7], y_range=[-4, 4], faded_line_ratio=1)
        self.play(Create(grid))
        self.wait(0.5)
        C = Dot([0, 0, 0], color=WHITE)
        self.play(FadeIn(C))
        self.wait(0.5)

        # Distance 2 points
        p1 = Dot([2, 0, 0], color=YELLOW)
        p2 = Dot([-2, 0, 0], color=YELLOW)
        p3 = Dot([0, 1, 0], color=YELLOW)
        p4 = Dot([0, -1, 0], color=YELLOW)

        # Labels for distance 2
        calc1 = MathTex("2 + 0 = 2", font_size=24).next_to(p1, DOWN)
        calc2 = MathTex("0 + 2 = 2", font_size=24).next_to(p2, DOWN)
        calc3 = MathTex("0 + 2 = 2", font_size=24).next_to(p3, RIGHT)
        calc4 = MathTex("0 + 2 = 2", font_size=24).next_to(p4, RIGHT)

        self.play(FadeIn(p1), Write(calc1))
        self.wait(1)
        self.play(FadeIn(p2), Write(calc2))
        self.wait(1)
        self.play(FadeIn(p3), Write(calc3))
        self.wait(1)
        self.play(FadeIn(p4), Write(calc4))
        self.wait(1)

        # Fade out distance 2 points and labels
        self.play(FadeOut(p1), FadeOut(calc1), FadeOut(p2), FadeOut(calc2),
                  FadeOut(p3), FadeOut(calc3), FadeOut(p4), FadeOut(calc4))

        # Distance 6 points
        p5 = Dot([6, 0, 0], color=YELLOW)
        p6 = Dot([-6, 0, 0], color=YELLOW)
        p7 = Dot([0, 3, 0], color=YELLOW)
        p8 = Dot([0, -3, 0], color=YELLOW)

        calc5 = MathTex("6 + 0 = 6", font_size=24).next_to(p5, DOWN)
        calc6 = MathTex("0 + 6 = 6", font_size=24).next_to(p6, DOWN)
        calc7 = MathTex("0 + 6 = 6", font_size=24).next_to(p7, RIGHT)
        calc8 = MathTex("0 + 6 = 6", font_size=24).next_to(p8, RIGHT)

        self.play(FadeIn(p5), Write(calc5))
        self.wait(1)
        self.play(FadeIn(p6), Write(calc6))
        self.wait(1)
        p7.shift(0.0 * RIGHT + -0.23 * UP)  # layout: separation vector
        calc7.shift(0.0 * RIGHT + -0.25 * UP)  # layout: separation vector
        self.play(FadeIn(p7), Write(calc7))
        self.wait(1)
        self.play(FadeIn(p8), Write(calc8))
        self.wait(1)

        # Fade out all points
        self.play(FadeOut(p5), FadeOut(calc5), FadeOut(p6), FadeOut(calc6),
                  FadeOut(p7), FadeOut(calc7), FadeOut(p8), FadeOut(calc8))

        # Narration text
        text1 = Text("Distance 2: 2 sideways or 1 vertical", font_size=24).to_edge(DOWN)
        self.play(Write(text1))
        self.wait(1.5)
        self.play(FadeOut(text1))

        text2 = Text("Distance 6: 6 sideways or 3 vertical", font_size=24).to_edge(DOWN)
        self.play(Write(text2))
        self.wait(1.5)
        self.play(FadeOut(text2))

        # Final fade out
        self.play(FadeOut(title), FadeOut(grid), FadeOut(C))
        self.wait(0.5)
