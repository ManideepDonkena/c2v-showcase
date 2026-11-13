from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Euler's Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Main equation
        zeta_eq = MathTex(r"\zeta(s) = \prod_{p} (1 - p^{-s})^{-1}", font_size=40)
        zeta_eq.to_edge(UP, buff=1.2)
        self.play(Write(zeta_eq))
        self.wait(1)

        # Primes list
        primes = [2, 3, 5, 7, 11]
        prime_texts = [MathTex(f"p={p}", font_size=24) for p in primes]
        for i, pt in enumerate(prime_texts):
            pt.to_edge(LEFT, buff=1).shift(DOWN * (i - 2))
        self.play(*[Write(pt) for pt in prime_texts])
        self.wait(0.5)

        # Connect lines
        lines = []
        for i, pt in enumerate(prime_texts):
            line = Line(pt.get_right(), zeta_eq.get_left(), color=YELLOW)
            line.set_opacity(0.7)
            self.play(Create(line), run_time=0.5)
            lines.append(line)
            self.wait(0.3)

        # Highlight key idea
        idea = Text("Primes are building blocks", font_size=24).to_edge(DOWN)
        self.play(Write(idea))
        self.wait(1.5)

        # Fade out
        self.play(
            *[FadeOut(line) for line in lines],
            *[FadeOut(pt) for pt in prime_texts],
            FadeOut(idea),
            run_time=1
        )
        self.wait(0.5)
