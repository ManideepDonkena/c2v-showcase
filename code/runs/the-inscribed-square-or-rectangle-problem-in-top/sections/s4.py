from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Topological Insight", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial curve
        curve = ParametricFunction(
            lambda t: np.array([
                2 * np.cos(t) + 0.5 * np.cos(3 * t),
                2 * np.sin(t) + 0.5 * np.sin(3 * t),
                0
            ]),
            t_range=[0, TAU],
            color=WHITE,
            stroke_width=3
        )
        self.play(Create(curve))
        self.wait(1)

        # Dissolve curve into dots
        dots = VGroup()
        for i in range(100):
            point = curve.point_from_proportion(i/99)
            dot = Dot(point, color=WHITE, radius=0.03)
            dots.add(dot)
        
        self.play(Transform(curve, dots), run_time=2)
        self.wait(1)

        # Create torus grid
        torus_grid = VGroup()
        for i in range(20):
            for j in range(20):
                x = (i / 19) * 4 - 2
                y = (j / 19) * 4 - 2
                dot = Dot(
                    point=np.array([x, y, 0]),
                    color=WHITE,
                    radius=0.05
                )
                torus_grid.add(dot)
        
        self.play(Transform(dots, torus_grid), run_time=2)
        self.wait(1)

        # Two paths on torus
        path1 = Line(
            start=np.array([-2, -2, 0]),
            end=np.array([2, 2, 0]),
            color=YELLOW,
            stroke_width=3
        )
        path2 = Line(
            start=np.array([-2, 2, 0]),
            end=np.array([2, -2, 0]),
            color=BLUE,
            stroke_width=3
        )

        self.play(Create(path1), Create(path2), run_time=1.5)
        self.wait(1)

        # Intersection point
        intersection = Dot(point=np.array([0, 0, 0]), color=GREEN, radius=0.1)
        self.play(FadeIn(intersection))
        self.wait(0.5)

        # Glow effect on intersection
        glow = Circle(color=GREEN, radius=0.15, stroke_width=5).move_to(intersection.get_center())
        self.play(Create(glow), run_time=0.5)
        self.play(FadeOut(glow), run_time=0.5)
        # Theorem text
        theorem = Text("Brouwer Fixed-Point Theorem", font_size=24).to_edge(DOWN)
        self.play(Write(theorem))
        self.wait(1)
        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(dots),
            FadeOut(path1),
            FadeOut(path2),
            FadeOut(intersection),
            FadeOut(theorem),
            run_time=1
        )
        self.wait(0.5)
