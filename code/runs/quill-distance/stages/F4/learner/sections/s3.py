from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Shape of Distance 2", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Central point C(0,0)
        center = Dot(color=WHITE).move_to(ORIGIN)
        c_label = MathTex("C(0,0)", font_size=24).next_to(center, DOWN, buff=0.2)
        self.play(FadeIn(center), Write(c_label))
        self.wait(0.5)

        # First set of points at quill distance 2
        p1 = Dot(color=YELLOW).move_to(RIGHT * 2)
        p2 = Dot(color=YELLOW).move_to(LEFT * 2)
        p3 = Dot(color=YELLOW).move_to(UP)
        p4 = Dot(color=YELLOW).move_to(DOWN)

        # Labels for first set
        calc1 = MathTex("2 + 0 = 2", font_size=24).next_to(p1, DOWN, buff=0.3)
        calc2 = MathTex("2 + 0 = 2", font_size=24).next_to(p2, DOWN, buff=0.3)
        calc3 = MathTex("0 + 2 = 2", font_size=24).next_to(p3, RIGHT, buff=0.3)
        calc4 = MathTex("0 + 2 = 2", font_size=24).next_to(p4, RIGHT, buff=0.3)

        # Light up points one by one
        self.play(FadeIn(p1), Write(calc1))
        self.wait(0.5)
        self.play(FadeIn(p2), Write(calc2))
        self.wait(0.5)
        self.play(FadeIn(p3), Write(calc3))
        self.wait(0.5)
        self.play(FadeIn(p4), Write(calc4))
        self.wait(1)

        # Fade out first set
        self.play(FadeOut(p1), FadeOut(calc1), FadeOut(p2), FadeOut(calc2),
                  FadeOut(p3), FadeOut(calc3), FadeOut(p4), FadeOut(calc4))

        # Show second set of points at quill distance 6
        p5 = Dot(color=GREEN).move_to(RIGHT * 6)
        p6 = Dot(color=GREEN).move_to(LEFT * 6)
        p7 = Dot(color=GREEN).move_to(UP * 3)
        p8 = Dot(color=GREEN).move_to(DOWN * 3)

        # Labels for second set
        calc5 = MathTex("6 + 0 = 6", font_size=24).next_to(p5, DOWN, buff=0.3)
        calc6 = MathTex("6 + 0 = 6", font_size=24).next_to(p6, DOWN, buff=0.3)
        calc7 = MathTex("0 + 6 = 6", font_size=24).next_to(p7, RIGHT, buff=0.3)
        calc8 = MathTex("0 + 6 = 6", font_size=24).next_to(p8, RIGHT, buff=0.3)

        # Show explanation text
        explain = Text("Just as distance 2 required 2 sideways or 1 vertical step...", font_size=24)
        explain.to_edge(DOWN)
        self.play(Write(explain))
        self.wait(1)

        # Light up second set
        self.play(FadeIn(p5), Write(calc5))
        self.wait(0.5)
        self.play(FadeIn(p6), Write(calc6))
        self.wait(0.5)
        p7.shift(0.0 * RIGHT + -0.23 * UP)  # layout: separation vector
        calc7.shift(0.0 * RIGHT + -0.25 * UP)  # layout: separation vector
        self.play(FadeIn(p7), Write(calc7))
        self.wait(0.5)
        self.play(FadeIn(p8), Write(calc8))
        self.wait(1)

        # Fade out second set
        self.play(FadeOut(p5), FadeOut(calc5), FadeOut(p6), FadeOut(calc6),
                  FadeOut(p7), FadeOut(calc7), FadeOut(p8), FadeOut(calc8))

        # Final explanation
        final = Text("Distance 6 requires 6 sideways or 3 vertical steps.", font_size=24).to_edge(DOWN)
        self.play(ReplacementTransform(explain, final))
        self.wait(1.5)

        self.play(FadeOut(final), FadeOut(title))
