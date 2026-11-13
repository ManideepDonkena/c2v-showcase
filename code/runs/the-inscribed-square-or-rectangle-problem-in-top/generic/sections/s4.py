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
            color=WHITE
        )
        self.play(Create(curve), run_time=2)
        self.wait(1)

        # Dissolve curve into dots
        dots = VGroup()
        for i in range(100):
            dot = Dot(
                point=curve.point_from_proportion(i/99),
                color=WHITE,
                radius=0.03
            )
            dots.add(dot)
        
        self.play(Transform(curve, dots), run_time=2)
        self.wait(1)

        # Form torus from dots
        torus = VGroup()
        for dot in dots:
            torus.add(dot)
        
        # Remap dots to torus shape
        torus_dots = VGroup()
        for i, dot in enumerate(dots):
            x, y, z = dot.get_center()
            # Map to torus coordinates
            angle1 = 2 * PI * (i / 100)
            angle2 = 2 * PI * (i % 10) / 10
            new_x = (2 + 0.5 * np.cos(angle2)) * np.cos(angle1)
            new_y = (2 + 0.5 * np.cos(angle2)) * np.sin(angle1)
            new_z = 0.5 * np.sin(angle2)
            dot.move_to(np.array([new_x, new_y, new_z]))
            torus_dots.add(dot)
        
        self.play(Transform(dots, torus_dots), run_time=2)
        self.wait(1)

        # Two paths on torus
        path1 = ParametricFunction(
            lambda t: np.array([
                (2 + 0.5 * np.cos(2 * PI * t)) * np.cos(2 * PI * t),
                (2 + 0.5 * np.cos(2 * PI * t)) * np.sin(2 * PI * t),
                0.5 * np.sin(2 * PI * t)
            ]),
            t_range=[0, 1],
            color=BLUE,
            stroke_width=3
        )
        
        path2 = ParametricFunction(
            lambda t: np.array([
                (2 + 0.5 * np.cos(2 * PI * t + PI/2)) * np.cos(2 * PI * t + PI/2),
                (2 + 0.5 * np.cos(2 * PI * t + PI/2)) * np.sin(2 * PI * t + PI/2),
                0.5 * np.sin(2 * PI * t + PI/2)
            ]),
            t_range=[0, 1],
            color=RED,
            stroke_width=3
        )
        
        self.play(Create(path1), run_time=1.5)
        self.play(Create(path2), run_time=1.5)
        self.wait(1)

        # Intersection point
        intersection = Dot(point=path1.point_from_proportion(0.25), color=YELLOW, radius=0.08)
        self.play(FadeIn(intersection))
        self.wait(0.5)

        # Glow effect
        glow = always_redraw(lambda: intersection.copy().set_color(GREEN).set_opacity(0.8).scale(1.5))
        self.add(glow)
        
        # Theorem text
        theorem = Text("Brouwer Fixed-Point Theorem", font_size=24).to_edge(DOWN)
        self.play(Write(theorem), run_time=1)
        self.wait(1)

        # Fade out
        self.play(
            FadeOut(curve),
            FadeOut(path1),
            FadeOut(path2),
            FadeOut(intersection),
            FadeOut(glow),
            FadeOut(theorem),
            FadeOut(title),
            run_time=1
        )
        self.wait(0.5)
