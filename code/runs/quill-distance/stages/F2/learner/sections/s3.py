from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Shape of Distance 2", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Central point C(0,0)
        C = Dot(color=WHITE).move_to(ORIGIN)
        label_C = MathTex("C(0,0)", font_size=24).next_to(C, DOWN, buff=0.2)
        self.play(FadeIn(C), Write(label_C))
        self.wait(0.5)

        # Points at distance 2: (2,0), (-2,0), (0,1), (0,-1)
        p1 = Dot(color=YELLOW).move_to(RIGHT * 2)
        calc1 = MathTex("2 + 0 = 2", font_size=24).next_to(p1, UP, buff=0.3)
        self.play(FadeIn(p1), Write(calc1))
        self.wait(1)

        p2 = Dot(color=YELLOW).move_to(LEFT * 2)
        calc2 = MathTex("0 + 2 = 2", font_size=24).next_to(p2, UP, buff=0.3)
        self.play(FadeIn(p2), Write(calc2))
        self.wait(1)

        p3 = Dot(color=YELLOW).move_to(UP)
        calc3 = MathTex("0 + 2 = 2", font_size=24).next_to(p3, UP, buff=0.3)
        self.play(FadeIn(p3), Write(calc3))
        self.wait(1)

        p4 = Dot(color=YELLOW).move_to(DOWN)
        calc4 = MathTex("0 + 2 = 2", font_size=24).next_to(p4, UP, buff=0.3)
        calc4.shift(0.0 * RIGHT + -0.25 * UP)  # layout: separation vector
        self.play(FadeIn(p4), Write(calc4))
        self.wait(1)

        # Dim point (1,1) with cost 3
        p5 = Dot(color=GRAY).move_to(UP + RIGHT)
        label_cost = MathTex("Cost: 3", font_size=24).next_to(p5, UP, buff=0.3)
        self.play(FadeIn(p5), Write(label_cost))
        self.wait(1)

        # Show point (4,0) with cost 4
        p6 = Dot(color=GREEN).move_to(RIGHT * 4)
        calc6 = MathTex("4 + 0 = 4", font_size=24).next_to(p6, UP, buff=0.3)
        self.play(FadeIn(p6), Write(calc6))
        self.wait(1)

        # Show point (2,1) with cost 4
        p7 = Dot(color=RED).move_to(UP + RIGHT * 2)
        calc7 = MathTex("2 + 2 = 4", font_size=24).next_to(p7, UP, buff=0.3)
        self.play(FadeIn(p7), Write(calc7))
        self.wait(1)

        # Show explanation text
        note = Text("Any point where horizontal distance = target cost (if vertical = 0)\nor vertical distance = target cost / 2 (if horizontal = 0)", font_size=24)
        note.to_edge(DOWN)
        self.play(Write(note))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(C), FadeOut(label_C),
            FadeOut(p1), FadeOut(calc1),
            FadeOut(p2), FadeOut(calc2),
            FadeOut(p3), FadeOut(calc3),
            FadeOut(p4), FadeOut(calc4),
            FadeOut(p5), FadeOut(label_cost),
            FadeOut(p6), FadeOut(calc6),
            FadeOut(p7), FadeOut(calc7),
            FadeOut(note),
            FadeOut(title)
        )
        self.wait(0.5)
