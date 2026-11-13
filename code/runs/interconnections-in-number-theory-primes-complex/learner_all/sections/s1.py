from manim import *

class S1(Scene):
    def construct(self):
        title = Text("The Prime Landscape", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Bar chart for primes 1 to 50
        bars = VGroup()
        prime_colors = []
        for i in range(1, 51):
            is_prime = i > 1 and all(i % j != 0 for j in range(2, int(i**0.5)+1))
            color = RED if is_prime else GRAY
            bar = Rectangle(height=0.2*i, width=0.4, fill_color=color, fill_opacity=1, stroke_width=0)
            bar.move_to([i*0.2 - 5, -1.5, 0], aligned_edge=DOWN)
            bars.add(bar)
            prime_colors.append(color)

        self.play(*[GrowFromEdge(bar, DOWN) for bar in bars], run_time=3)
        self.wait(1)

        # Overlay smooth curve x / ln(x)
        curve = always_redraw(lambda: ParametricFunction(
            lambda t: [t, t / np.log(t), 0],
            t_range=[2, 50],
            color=YELLOW,
            stroke_width=3
        ))
        self.play(Write(curve))
        self.wait(1.5)

        # Gaussian integers grid
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"stroke_color": GRAY},
            background_line_style={"stroke_color": GRAY}
        )
        self.play(Write(grid))
        self.wait(0.5)

        # Show inert prime (7) vs split prime (5)
        prime_5 = Dot([1, 2, 0], color=GREEN)
        prime_5_conj = Dot([1, -2, 0], color=GREEN)
        prime_7 = Dot([0, 7, 0], color=RED)

        self.play(FadeIn(prime_5), FadeIn(prime_5_conj))
        self.wait(0.5)
        self.play(FadeIn(prime_7))
        self.wait(1)

        # Critical line Re(s) = 1/2
        critical_line = Line(start=[0.5, -3.9, 0], end=[0.5, 3.9, 0], color=BLUE, stroke_width=3)
        self.play(Write(critical_line))
        self.wait(0.5)

        # Zeros clustering on critical line
        zeros = [Dot([0.5, 1.5, 0]), Dot([0.5, -2.3, 0]), Dot([0.5, 0.7, 0])]
        for z in zeros:
            self.play(FadeIn(z))
            self.wait(0.3)

        # Riemann Hypothesis text
        rh = Text("Riemann Hypothesis", font_size=24).next_to(critical_line, LEFT)
        self.play(Write(rh))
        self.wait(1.5)

        # Modulus calculation example
        mod_text = MathTex(r"\text{modulus} = \sqrt{a^2 + b^2}", font_size=30)
        mod_text.to_edge(DOWN)
        self.play(Write(mod_text))
        self.wait(1)

        # Basel problem
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}", font_size=30)
        basel.next_to(mod_text, UP)
        self.play(Write(basel))
        self.wait(1.5)

        # Prime counting vs Logarithmic integral
        count_func = always_redraw(lambda: ParametricFunction(
            lambda t: [t, 0.5*t / np.log(t), 0],
            t_range=[2, 50],
            color=RED,
            stroke_width=3
        ))
        self.play(Write(count_func))
        self.wait(1)

        # Arithmetic progressions and Dirichlet characters
        self.play(FadeOut(title), FadeOut(curve), FadeOut(grid), FadeOut(critical_line), FadeOut(rh),
                  FadeOut(mod_text), FadeOut(basel), FadeOut(count_func))

        # Final overlay: prime factorization in Gaussian integers
        self.wait(0.5)
        text1 = Text("Primes p ≡ 3 (mod 4) remain inert", font_size=24)
        self.play(Write(text1))
        self.wait(1)
        text2 = Text("Primes p ≡ 1 (mod 4) split into conjugates", font_size=24)
        self.play(ReplacementTransform(text1, text2))
        self.wait(1.5)

        self.play(FadeOut(*self.mobjects))
