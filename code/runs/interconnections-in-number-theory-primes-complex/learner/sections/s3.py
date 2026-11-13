from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Hidden Harmony: Number Theory's Interconnections", font_size=24)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Euler's Product Formula
        formula = MathTex(r"\zeta(s) = \prod_{p} (1 - p^{-s})^{-1}", font_size=36)
        formula.move_to(UP * 0.5)
        self.play(Write(formula))
        self.wait(1)

        # Primes pulsing and connecting
        primes = [2, 3, 5, 7, 11]
        prime_circles = []
        lines = []

        for i, p in enumerate(primes):
            circle = Circle(radius=0.3, color=YELLOW).move_to(DOWN * 1.5 + RIGHT * (i - 2) * 1.5)
            prime_text = MathTex(f"{p}", font_size=24).move_to(circle.get_center())
            prime_circles.append(VGroup(circle, prime_text))
            self.play(GrowFromCenter(circle), Write(prime_text))
            self.wait(0.3)

            # Line from prime to zeta
            line = Line(circle.get_top(), formula.get_left(), color=BLUE)
            line.shift(-0.39 * RIGHT + 0.0 * UP)  # layout: separation vector
            line.shift(0.0 * RIGHT + -0.57 * UP)  # layout: separation vector
            self.play(Create(line))
            lines.append(line)
            self.wait(0.2)

        # Basel problem
        basel = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}", font_size=32)
        basel.next_to(formula, DOWN, buff=1.0)
        basel.shift(0.0 * RIGHT + 0.78 * UP)  # layout: separation vector
        self.play(Write(basel))
        self.wait(1.5)

        # Show connection
        connect_line = Line(formula.get_right(), basel.get_left(), color=GREEN)
        self.play(Create(connect_line))
        self.wait(1.5)

        # Key words
        reveal = Text("Euler revealed", font_size=24).to_corner(UL)
        self.play(Write(reveal))
        self.wait(0.5)
        self.play(FadeOut(reveal))

        isolated = Text("primes are not isolated", font_size=24).to_corner(UL)
        self.play(Write(isolated))
        self.wait(0.5)
        self.play(FadeOut(isolated))

        building = Text("fundamental building blocks", font_size=24).to_corner(UL)
        self.play(Write(building))
        self.wait(0.5)
        self.play(FadeOut(building))

        # Cleanup
        self.play(
            *[FadeOut(circle) for circle in prime_circles],
            *[FadeOut(line) for line in lines],
            FadeOut(formula),
            FadeOut(basel),
            FadeOut(connect_line),
            FadeOut(title)
        )
        self.wait(0.5)
