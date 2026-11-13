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
        formula.move_to(ORIGIN)
        self.play(Write(formula))
        self.wait(1)

        # Prime pulses and connections
        primes = [2, 3, 5, 7, 11]
        dots = [Dot(point=[i, 0, 0], color=BLUE) for i in range(1, len(primes)+1)]
        lines = [Line(formula.get_left(), dot.get_right()) for dot in dots]

        for i, (dot, line) in enumerate(zip(dots, lines)):
            dot.shift(0.0 * RIGHT + 0.65 * UP)  # layout: separation vector
            self.play(
                Create(dot),
                Create(line),
                run_time=0.5
            )
            self.wait(0.3)

        # Prime counting function vs x/ln(x)
        prime_count = VGroup()
        for i in range(1, 21):
            if i > 1:
                y = int(i / np.log(i))
                prime_count.add(Dot(point=[i, y, 0], color=RED))
        prime_count.scale(0.5).shift(LEFT * 3 + DOWN * 1.5)
        approx_curve = ParametricFunction(
            lambda t: [t, t / np.log(t), 0],
            t_range=[2, 20],
            color=YELLOW
        ).scale(0.5).shift(LEFT * 3 + DOWN * 1.5)

        prime_count.shift(-0.58 * RIGHT + 0.0 * UP)  # layout: separation vector
        prime_count.shift(-0.5 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(prime_count), run_time=1)
        self.play(Create(approx_curve), run_time=1)
        self.wait(1)

        # Gaussian integers and prime splitting
        grid = NumberPlane(x_range=[-4, 5], y_range=[-4, 5], faded_line_ratio=1)
        grid.scale(0.7).shift(RIGHT * 3 + UP * 0.5)
        self.play(Create(grid))
        self.wait(0.5)

        # Prime 5 splits
        p5 = Dot(point=[1, 2, 0], color=GREEN)
        p5_conj = Dot(point=[1, -2, 0], color=GREEN)
        self.play(FadeIn(p5), FadeIn(p5_conj))
        self.wait(0.5)

        # Prime 7 stays inert
        p7 = Dot(point=[0, 7, 0], color=ORANGE)
        self.play(FadeIn(p7))
        self.wait(0.5)

        # Riemann Hypothesis line
        critical_line = Line(start=[0.5, -3.9, 0], end=[0.5, 3.9, 0], color=WHITE)
        self.play(Create(critical_line))
        self.wait(0.5)

        zeros = [Dot(point=[0.5, i*0.5, 0], color=PURPLE) for i in range(-5, 6)]
        for z in zeros:
            self.play(FadeIn(z), run_time=0.1)
        self.wait(1)

        # Modulus calculation
        golden = (1 + np.sqrt(5)) / 2
        mod_point = Dot(point=[golden, 0, 0], color=TEAL)
        self.play(FadeIn(mod_point))
        self.wait(0.5)

        # Dirichlet characters and progressions
        progression = [3, 7, 11, 15, 19]
        dots_progression = [Dot(point=[i, 0, 0], color=BLUE) for i in progression]
        self.play(Create(VGroup(*dots_progression)))
        self.wait(0.5)

        # Basel problem
        basel_sum = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}", font_size=32)
        basel_sum.to_edge(DOWN)
        self.play(Write(basel_sum))
        self.wait(1)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(prime_count),
            FadeOut(approx_curve),
            FadeOut(grid),
            FadeOut(p5),
            FadeOut(p5_conj),
            FadeOut(p7),
            FadeOut(critical_line),
            FadeOut(VGroup(*zeros)),
            FadeOut(mod_point),
            FadeOut(VGroup(*dots_progression)),
            FadeOut(basel_sum)
        )
        self.wait(0.5)
