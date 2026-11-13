from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Circle Constant", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Basel problem sum converging to π²/6
        zeta_sum = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}", font_size=36)
        zeta_sum.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(zeta_sum))
        self.wait(1)

        # Circle expanding and contracting
        circle = Circle(color=BLUE, radius=0.5)
        circle.move_to(ORIGIN)
        self.play(Create(circle))
        self.wait(0.5)

        # Animate circle growing and shrinking to represent convergence
        self.play(
            circle.animate.scale(2),
            run_time=1,
            rate_func=there_and_back
        )
        self.wait(0.5)

        # Overlay of prime counting function vs x/ln(x)
        prime_count = VGroup()
        for i in range(1, 21):
            point = Dot(point=[i, i / np.log(i), 0], color=YELLOW)
            prime_count.add(point)
        prime_count.to_edge(DOWN).shift(LEFT * 3)

        smooth_curve = ParametricFunction(
            lambda t: [t, t / np.log(t), 0],
            t_range=[2, 20],
            color=GREEN
        )
        prime_count.shift(-1.12 * RIGHT + 0.0 * UP)  # layout: separation vector
        prime_count.shift(-1.0 * RIGHT + 0.0 * UP)  # layout: separation vector
        prime_count.shift(-1.0 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(prime_count), run_time=1)
        self.wait(0.5)
        self.play(Write(smooth_curve))
        self.wait(1)

        # Gaussian integers grid
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"stroke_color": GRAY},
            background_line_style={"stroke_color": GRAY}
        )
        self.play(Create(grid))
        self.wait(0.5)

        # Show inert prime (7) and split prime (5)
        prime_5 = Dot(point=[1, 2, 0], color=RED)
        prime_5_label = MathTex("5 = (1+2i)(1-2i)", font_size=24).next_to(prime_5, UP)
        self.play(FadeIn(prime_5), Write(prime_5_label))
        self.wait(0.5)

        prime_7 = Dot(point=[7, 0, 0], color=BLUE)
        prime_7_label = MathTex("7 \text{ remains inert}", font_size=24).next_to(prime_7, UP)
        self.play(FadeIn(prime_7), Write(prime_7_label))
        self.wait(1)

        # Critical Line
        critical_line = Line(start=[0.5, -3.9, 0], end=[0.5, 3.9, 0], color=ORANGE)
        self.play(Create(critical_line))
        self.wait(0.5)

        # Zeros clustering on critical line
        zeros = [Dot(point=[0.5, 1.5, 0], color=PURPLE), Dot(point=[0.5, -2.3, 0], color=PURPLE)]
        for z in zeros:
            self.play(FadeIn(z))
        self.wait(0.5)

        # Riemann Hypothesis statement
        rh = Text("Riemann Hypothesis", font_size=24).to_edge(UP).shift(DOWN * 1.5)
        self.play(Write(rh))
        self.wait(1)

        # Modulus of golden ratio
        golden = MathTex(r"\frac{1 + \sqrt{5}}{2}", font_size=30)
        golden.to_corner(UR)
        self.play(Write(golden))
        self.wait(0.5)

        # Dirichlet characters and arithmetic progressions
        progression = [3, 7, 11, 15, 19]
        dots = VGroup()
        for i, p in enumerate(progression):
            d = Dot(point=[p, 0, 0], color=TEAL)
            dots.add(d)
        self.play(FadeIn(dots))
        self.wait(0.5)

        # Prime factorization in Gaussian integers
        inert_prime = MathTex("3 \text{ remains prime}", font_size=24).to_edge(DOWN).shift(LEFT * 1)
        self.play(Write(inert_prime))
        self.wait(0.5)

        # Show that p ≡ 3 (mod 4) stays inert
        inert_text = Text("p ≡ 3 (mod 4) stays inert", font_size=24).to_edge(DOWN).shift(RIGHT * 1)
        self.play(Write(inert_text))
        self.wait(0.5)

        # Show that p ≡ 1 (mod 4) splits
        split_text = Text("p ≡ 1 (mod 4) splits", font_size=24).to_edge(DOWN).shift(RIGHT * 3)
        self.play(Write(split_text))
        self.wait(0.5)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )
        self.wait(0.5)
