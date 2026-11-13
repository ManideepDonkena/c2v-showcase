from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Circle Constant", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Basel problem statement
        basel = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}", font_size=40)
        basel.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(basel))
        self.wait(1)

        # Show the sum visually
        dots = VGroup()
        for i in range(1, 6):
            dot = Dot().move_to(LEFT * (i - 3) * 0.8 + DOWN * 0.5)
            label = MathTex(f"\\frac{{1}}{{{i}^2}}", font_size=24).next_to(dot, UP, buff=0.1)
            dots.add(dot)
            self.play(Write(label), run_time=0.3)
            self.wait(0.2)

        # Show convergence to π²/6
        circle = Circle(radius=1.5, color=BLUE, fill_opacity=0.2).move_to(ORIGIN)
        self.play(Create(circle))
        self.wait(0.5)

        # Show area formula
        area_text = MathTex(r"\text{Area} = \frac{\pi^2}{6}", font_size=30).next_to(circle, DOWN)
        self.play(Write(area_text))
        self.wait(1.5)

        # Fade out and show prime connection
        self.play(FadeOut(basel), FadeOut(dots), FadeOut(area_text))
        self.wait(0.5)

        prime_conn = Text("Primes → π²/6 → Circle", font_size=24)
        prime_conn.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(prime_conn))
        self.wait(1.5)

        # Expand and contract circle
        self.play(
            circle.animate.scale(1.2),
            run_time=0.8
        )
        self.play(
            circle.animate.scale(0.833),
            run_time=0.8
        )

        self.wait(1)
        self.play(FadeOut(title), FadeOut(circle), FadeOut(prime_conn))
        self.wait(0.5)
