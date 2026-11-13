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
        unit_circle.shift(ORIGIN)
        self.play(Create(unit_circle))
        self.wait(0.5)

        # Labels
        origin = Dot(color=WHITE).shift(ORIGIN)
        origin_label = MathTex("0", font_size=24).next_to(origin, DOWN)
        self.play(FadeIn(origin_label))
        self.wait(0.5)

        # Inside points (green)
        z1 = Dot(color=GREEN).shift(0.5 * RIGHT)
        z1_label = MathTex("z_0", font_size=24).next_to(z1, UR)
        z1_label.shift(0.32 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(FadeIn(z1), FadeIn(z1_label))
        self.wait(0.5)

        # Outside points (red)
        z2 = Dot(color=RED).shift(2 * RIGHT)
        z2_label = MathTex("z_0", font_size=24).next_to(z2, UR)
        self.play(FadeIn(z2), FadeIn(z2_label))
        self.wait(0.5)

        # Show orbit behavior
        # Green orbit shrinking to zero
        green_orbit = VGroup()
        point = z1.copy()
        for i in range(5):
            next_point = point.copy().shift((point.get_center()[0] * 0.5) * LEFT)
            line = Line(point.get_center(), next_point.get_center(), color=GREEN, stroke_width=2)
            green_orbit.add(line)
            point = next_point
        self.play(Create(green_orbit))
        self.wait(1)

        # Red orbit exploding to infinity
        red_orbit = VGroup()
        point = z2.copy()
        for i in range(5):
            next_point = point.copy().shift((point.get_center()[0] * 1.5) * RIGHT)
            line = Line(point.get_center(), next_point.get_center(), color=RED, stroke_width=2)
            red_orbit.add(line)
            point = next_point
        self.play(Create(red_orbit))
        self.wait(1)

        # Text overlay
        notice_text = Text("Notice how the magnitude of z determines its fate.", font_size=24)
        notice_text.to_edge(DOWN)
        self.play(Write(notice_text))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(notice_text))

        # Show threshold effect
        threshold_text = Text("If |z_0| < 1, orbit converges to zero.", font_size=24)
        threshold_text.to_edge(DOWN)
        self.play(Write(threshold_text))
        self.wait(1.5)

        self.play(FadeOut(threshold_text))

        # Show divergence
        diverge_text = Text("If |z_0| > 1, orbit diverges to infinity.", font_size=24)
        diverge_text.to_edge(DOWN)
        self.play(Write(diverge_text))
        self.wait(1.5)

        self.play(FadeOut(diverge_text))

        # Final boundary text
        boundary_text = Text("The unit circle acts as a critical boundary separating these two behaviors.", font_size=24)
        boundary_text.to_edge(DOWN)
        self.play(Write(boundary_text))
        self.wait(1.5)

        self.play(FadeOut(boundary_text), FadeOut(title), FadeOut(unit_circle), FadeOut(z1), FadeOut(z2), FadeOut(green_orbit), FadeOut(red_orbit), FadeOut(origin_label), FadeOut(z1_label), FadeOut(z2_label))
        self.wait(0.5)
