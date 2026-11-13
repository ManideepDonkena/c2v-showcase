from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Hidden Harmony: Number Theory's Interconnections", font_size=24)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 1. Number line dissolves into complex plane
        number_line = NumberLine(x_range=[-5, 5, 1], include_numbers=True)
        number_line.shift(DOWN * 0.5)
        self.play(Create(number_line), run_time=1)
        self.wait(0.5)

        # Dissolve to 3D complex plane
        complex_plane = ComplexPlane(x_range=[-4, 4, 1], y_range=[-3, 3, 1])
        complex_plane.set_opacity(0.7)
        self.play(Transform(number_line, complex_plane), run_time=1.5)
        self.wait(0.5)
        # Grid of points
        grid = VGroup(*[Line(LEFT, RIGHT).set_color(BLUE).set_opacity(0.3).shift(i * RIGHT) for i in range(-10, 11)])
        grid += VGroup(*[Line(DOWN, UP).set_color(BLUE).set_opacity(0.3).shift(i * UP) for i in range(-10, 11)])
        self.play(Create(grid), run_time=1)
        self.wait(0.5)

        # Zeta function surface rising
        def zeta_func(x, y):
            s = complex(x, y)
            try:
                return 1 / (s - 1) + 1  # Simplified for visualization
            except ZeroDivisionError:
                return 0

        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                zeta_func(u, v).real if abs(zeta_func(u, v)) < 5 else 0
            ]),
            u_range=[-3, 3],
            v_range=[-2, 2],
            resolution=(20, 20),
            fill_opacity=0.6,
            stroke_width=0,
            color=BLUE
        )
        self.play(Create(surface), run_time=1.5)
        self.wait(0.5)

        # Zeros on critical line Re(s) = 1/2
        critical_line = Line(
            start=complex_plane.c2p(0.5, -3),
            end=complex_plane.c2p(0.5, 3),
            color=YELLOW,
            stroke_width=4
        )
        self.play(Create(critical_line), run_time=1)
        self.wait(0.5)

        # Glowing zeros on critical line
        zero_points = [
            complex_plane.c2p(0.5, 2),
            complex_plane.c2p(0.5, -2),
            complex_plane.c2p(0.5, 4),
            complex_plane.c2p(0.5, -4)
        ]
        dots = VGroup(*[Dot(p, color=RED, radius=0.1) for p in zero_points])
        dots.shift(0.0 * RIGHT + -0.25 * UP)  # layout: separation vector
        self.play(FadeIn(dots), run_time=1)
        self.wait(0.5)

        # Riemann Hypothesis statement
        rh_text = Text("Riemann Hypothesis", font_size=24).to_edge(UP)
        self.play(Transform(title, rh_text))
        self.wait(0.5)

        # Prime counting function vs x/ln(x)
        prime_count_func = VGroup(
            Dot(complex_plane.c2p(1, 1), color=GREEN),
            Dot(complex_plane.c2p(2, 2), color=GREEN),
            Dot(complex_plane.c2p(3, 3), color=GREEN),
            Dot(complex_plane.c2p(4, 4), color=GREEN),
            Dot(complex_plane.c2p(5, 5), color=GREEN)
        )
        self.play(FadeIn(prime_count_func))
        self.wait(0.5)

        x_ln_x = ParametricFunction(
            lambda t: complex_plane.c2p(t, t / np.log(t)),
            t_range=[2, 10],
            color=YELLOW
        )
        self.play(Create(x_ln_x), run_time=1)
        self.wait(0.5)

        # Gaussian integers grid
        gaussian_grid = VGroup()
        for i in range(-4, 5):
            for j in range(-3, 4):
                point = complex_plane.c2p(i, j)
                dot = Dot(point, color=WHITE, radius=0.05)
                gaussian_grid.add(dot)
        self.play(FadeIn(gaussian_grid), run_time=1)
        self.wait(0.5)

        # Prime factorization demonstration
        prime_5 = Text("5 = 1² + 2²", font_size=24).to_edge(DOWN)
        self.play(Write(prime_5))
        self.wait(0.5)

        prime_7 = Text("7 cannot be written as sum of two squares", font_size=24).next_to(prime_5, DOWN)
        self.play(Write(prime_7))
        self.wait(0.5)

        # Brick wall analogy
        brick_wall = VGroup(
            Rectangle(width=1, height=0.2, color=RED),
            Rectangle(width=1, height=0.2, color=RED),
            Rectangle(width=1, height=0.2, color=BLUE)
        )
        brick_wall.arrange(DOWN, buff=0.1)
        self.play(FadeIn(brick_wall))
        self.wait(0.5)

        # Critical line vs Re(s)=1
        critical_line = Line(
            start=complex_plane.c2p(0.5, -3),
            end=complex_plane.c2p(0.5, 3),
            color=YELLOW,
            stroke_width=4
        )
        self.play(Create(critical_line))
        self.wait(0.5)

        line_re1 = Line(
            start=complex_plane.c2p(1, -3),
            end=complex_plane.c2p(1, 3),
            color=ORANGE,
            stroke_width=4
        )
        self.play(Create(line_re1))
        self.wait(0.5)

        # Modulus calculation
        golden_ratio = (1 + np.sqrt(5)) / 2
        modulus_text = MathTex(r"\text{mod}(a + bi) = \sqrt{a^2 + b^2}", font_size=30)
        modulus_text.to_edge(UP)
        self.play(Write(modulus_text))
        self.wait(0.5)

        # Golden ratio example
        golden_point = complex_plane.c2p(golden_ratio, 0)
        dot_golden = Dot(golden_point, color=GREEN)
        self.play(FadeIn(dot_golden))
        self.wait(0.5)

        # Arithmetic progressions and Dirichlet characters
        progression = [3, 7, 11, 15, 19]
        wave = ParametricFunction(
            lambda t: complex_plane.c2p(t, np.sin(t)),
            t_range=[0, 10],
            color=BLUE
        )
        self.play(Create(wave))
        self.wait(0.5)

        # Gaussian integers and inert primes
        inert_prime = Text("Primes p ≡ 3 (mod 4) remain inert", font_size=24).to_edge(DOWN)
        self.play(Write(inert_prime))
        self.wait(0.5)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )
        self.wait(0.5)
