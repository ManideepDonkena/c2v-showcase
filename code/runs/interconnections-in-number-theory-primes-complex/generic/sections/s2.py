from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Hidden Harmony: Number Theory's Interconnections", font_size=24)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Number line
        number_line = NumberLine(x_range=[-5, 5, 1], include_numbers=True, stroke_width=2)
        number_line.move_to(DOWN * 0.5)
        self.play(Create(number_line))
        self.wait(0.5)

        # Dissolve into complex plane
        self.play(FadeOut(number_line))
        self.wait(0.5)

        # Complex plane grid
        complex_plane = ComplexPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            axis_config={"stroke_width": 2},
            background_line_style={"stroke_opacity": 0.5}
        )
        complex_plane.move_to(ORIGIN)
        self.play(Create(complex_plane))
        self.wait(0.5)

        # Zeta function surface
        def zeta_func(x, y):
            s = complex(x, y)
            try:
                return 1 / (s - 1) + 1  # Simplified version for visualization
            except:
                return 0

        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                zeta_func(u, v) * 0.5  # Scale down for visibility
            ]),
            u_range=[-3, 3],
            v_range=[-2, 2],
            resolution=(20, 20),
            fill_opacity=0.7,
            stroke_width=0.5,
            color=BLUE
        )
        self.play(Create(surface))
        self.wait(1)

        # Critical line Re(s) = 1/2
        critical_line = Line(
            start=np.array([-4, 0, 0]),
            end=np.array([4, 0, 0]),
            color=YELLOW,
            stroke_width=3
        )
        self.play(Create(critical_line))
        self.wait(0.5)

        # Zeros on critical line
        zeros = [
            complex(0.5, 14.13),
            complex(0.5, 21.02),
            complex(0.5, 25.01),
            complex(0.5, 30.42),
            complex(0.5, 32.93)
        ]

        zero_dots = VGroup()
        for z in zeros:
            dot = Dot(point=[z.real, z.imag, 0], color=RED, radius=0.1)
            zero_dots.add(dot)

        # Adjust position to avoid layout issues
        zero_dots.shift(0.0 * RIGHT + -5.0 * UP)  # Move up to fit in frame
        self.play(FadeIn(zero_dots))
        self.wait(1)

        # Highlight key words
        keywords = MathTex(r"\text{Riemann Zeta function}", font_size=32)
        keywords.to_edge(UP)
        # Shift up slightly to avoid overlap with title
        keywords.shift(0.4 * UP)
        self.play(Write(keywords))
        self.wait(0.5)

        self.play(FadeOut(keywords))

        # Show the encoding message
        message = Text("Its hidden zeros act as harmonics", font_size=28)
        message.move_to(DOWN * 1.5)
        # Shift up slightly to avoid overlap with surface
        message.shift(0.8 * UP)
        self.play(Write(message))
        self.wait(1)

        self.play(FadeOut(message))

        # Final fade out
        self.play(
            FadeOut(complex_plane),
            FadeOut(surface),
            FadeOut(critical_line),
            FadeOut(zero_dots),
            FadeOut(title)
        )
        self.wait(0.5)
