from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Unit Circle Boundary", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Unit circle
        unit_circle = Circle(radius=1, color=BLUE, stroke_width=3)
        unit_circle.shift(LEFT*2)
        self.play(Create(unit_circle))
        self.wait(0.5)

        # Labels
        origin = Dot(color=WHITE).shift(LEFT*2)
        origin_label = MathTex("0", font_size=24).next_to(origin, DOWN)
        self.play(FadeIn(origin_label))
        self.wait(0.5)

        # Inside points (green)
        z1 = Dot(color=GREEN).shift(LEFT*2 + UP*0.5)
        z1_label = MathTex("z_1", font_size=24).next_to(z1, UR)
        self.play(FadeIn(z1), FadeIn(z1_label))
        self.wait(0.5)

        # Outside points (red)
        z2 = Dot(color=RED).shift(LEFT*2 + DOWN*1.5)
        z2_label = MathTex("z_2", font_size=24).next_to(z2, DR)
        self.play(FadeIn(z2), FadeIn(z2_label))
        self.wait(0.5)

        # Boundary point (white)
        z3 = Dot(color=WHITE).shift(LEFT*2 + RIGHT*1)
        z3_label = MathTex("z_3", font_size=24).next_to(z3, UP)
        z3_label.shift(0.25 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(FadeIn(z3), FadeIn(z3_label))
        self.wait(0.5)

        # Text explanations
        explanation1 = Text("If |z₀| < 1, orbit converges to zero", font_size=24)
        explanation1.to_edge(DOWN).shift(LEFT*2)
        self.play(Write(explanation1))
        self.wait(1.0)

        explanation2 = Text("If |z₀| > 1, orbit diverges to infinity", font_size=24)
        explanation2.to_edge(DOWN).shift(RIGHT*2)
        self.play(Transform(explanation1, explanation2))
        self.wait(1.0)

        explanation3 = Text("The unit circle separates behaviors", font_size=24)
        explanation3.to_edge(DOWN)
        self.play(Transform(explanation1, explanation3))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(unit_circle),
            FadeOut(origin_label),
            FadeOut(z1), FadeOut(z1_label),
            FadeOut(z2), FadeOut(z2_label),
            FadeOut(z3), FadeOut(z3_label),
            FadeOut(explanation1)
        )
        self.wait(0.5)
