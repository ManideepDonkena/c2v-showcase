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

        # Dissolve into grid of dots (torus representation)
        dots = VGroup()
        for i in range(20):
            for j in range(20):
                x = 2 * np.cos(2 * PI * i / 20) + 3
                y = 2 * np.sin(2 * PI * i / 20)
                z = 2 * np.cos(2 * PI * j / 20)
                dot = Dot(point=[x, y, z], color=WHITE, radius=0.05)
                dots.add(dot)
        self.play(Transform(curve, dots), run_time=2)
        self.wait(1)

        # Two paths on torus
        path1 = ParametricFunction(
            lambda t: np.array([
                2 * np.cos(2 * PI * t) + 3,
                2 * np.sin(2 * PI * t),
                0
            ]),
            t_range=[0, 1],
            color=BLUE
        )
        path2 = ParametricFunction(
            lambda t: np.array([
                3,
                0,
                2 * np.sin(2 * PI * t)
            ]),
            t_range=[0, 1],
            color=RED
        )

        self.play(Create(path1), run_time=1)
        self.play(Create(path2), run_time=1)
        self.wait(1)

        # Intersection point with glow
        intersection = Dot(point=[3, 0, 0], color=GREEN, radius=0.1)
        glow = Circle(color=GREEN, radius=0.2).set_stroke(width=5)
        self.play(FadeIn(intersection), run_time=0.5)
        self.play(Write(glow))
        self.wait(0.5)

        # Theorem text
        theorem_text = Text("Brouwer Fixed-Point Theorem", font_size=24).next_to(intersection, DOWN)
        theorem_text.shift(0.0 * RIGHT + -1.85 * UP)  # layout: separation vector
        self.play(Write(theorem_text), run_time=1)
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(title, curve, path1, path2, intersection, glow, theorem_text))
        self.wait(0.5)

        # Visual metaphor: stationary point
        metaphor = Text("Search for inscribed square = Find a stationary point", font_size=24).to_edge(DOWN)
        self.play(Write(metaphor), run_time=1.5)
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(metaphor))
        self.wait(0.5)

        # Fixed point theorem mention
        fixed_point = Text("Fixed Point Theorems (e.g., Vaughan Jones)", font_size=24).to_edge(DOWN)
        self.play(Write(fixed_point), run_time=1.5)
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(fixed_point))
        self.wait(0.5)

        # Packing circles metaphor
        circle1 = Circle(radius=0.3, color=BLUE).move_to([-2, 0, 0])
        circle2 = Circle(radius=0.3, color=BLUE).move_to([0, 0, 0])
        circle3 = Circle(radius=0.3, color=BLUE).move_to([2, 0, 0])
        circles = VGroup(circle1, circle2, circle3)

        self.play(Write(circles), run_time=1)
        self.wait(1)

        # Explanation
        explanation = Text("Packing circles to approximate shape", font_size=24).next_to(circles, DOWN)
        explanation.shift(0.0 * RIGHT + -1.65 * UP)  # layout: separation vector
        explanation.shift(0.0 * RIGHT + -0.41 * UP)  # layout: separation vector
        self.play(Write(explanation), run_time=1.5)
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(circles, explanation))
        self.wait(0.5)
