from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Euler's Identity", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Main equation
        zeta_eq = MathTex(r"\zeta(s) = \prod_{p} (1 - p^{-s})^{-1}", font_size=40)
        zeta_eq.move_to(ORIGIN)
        self.play(Write(zeta_eq))
        self.wait(1)

        # Primes list
        primes = [2, 3, 5, 7, 11]
        prime_texts = [MathTex(f"p={p}", font_size=24) for p in primes]
        for i, pt in enumerate(prime_texts):
            pt.to_edge(DOWN).shift(RIGHT * (i - 2) * 1.5)
        self.play(*[Write(pt) for pt in prime_texts])
        self.wait(0.5)
        
        # Connect each prime to the equation
        lines = []
        for i, pt in enumerate(prime_texts):
            line = Line(pt.get_top(), zeta_eq.get_center() + LEFT * 2)
            line.set_color(YELLOW)
            self.play(GrowArrow(line))
            lines.append(line)
            self.wait(0.3)

        # Fade out primes and lines
        self.play(*[FadeOut(pt) for pt in prime_texts], *[FadeOut(line) for line in lines])
        self.wait(0.5)

        # Key words
        reveal = Text("Euler revealed", font_size=24)
        reveal.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(reveal))
        self.wait(1)

        # Fade out reveal text
        self.play(FadeOut(reveal))

        # More key words
        fundamental = Text("fundamental building blocks", font_size=24)
        fundamental.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(fundamental))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(zeta_eq), FadeOut(fundamental), FadeOut(title))
        self.wait(0.5)
