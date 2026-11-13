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
        number_line.move_to(ORIGIN)
        self.play(Create(number_line))
        self.wait(0.5)

        # Dissolve into complex plane
        plane = ComplexPlane()
        plane.add_coordinates()
        self.play(Transform(number_line, plane))
        self.wait(1)

        # Grid of points
        grid = VGroup()
        for x in range(-3, 4):
            for y in range(-2, 3):
                dot = Dot(plane.n2p(complex(x, y)), color=BLUE, radius=0.05)
                grid.add(dot)
        self.play(Write(grid))
        self.wait(1)

        # Zeta function surface
        def zeta_surface(u, v):
            s = complex(u, v)
            try:
                return 1 / (s - 1) + 1  # Simplified for visualization
            except:
                return 0

        surface = Surface(
            lambda u, v: plane.n2p(complex(u, v)) + UP * zeta_surface(u, v).real,
            u_range=[-2, 2],
            v_range=[-1.5, 1.5],
            resolution=(20, 20),
            fill_opacity=0.7,
            stroke_width=0,
            color=BLUE
        )
        self.play(Create(surface))
        self.wait(1.5)

        # Critical line Re(s) = 1/2
        critical_line = Line(
            plane.n2p(complex(0.5, -2)),
            plane.n2p(complex(0.5, 2)),
            color=YELLOW,
            stroke_width=3
        )
        self.play(Create(critical_line))
        self.wait(1)

        # Highlight zeros on critical line
        zero1 = Dot(plane.n2p(complex(0.5, 14.13)), color=RED, radius=0.1)
        zero2 = Dot(plane.n2p(complex(0.5, 21.02)), color=RED, radius=0.1)
        zero3 = Dot(plane.n2p(complex(0.5, 25.01)), color=RED, radius=0.1)
        
        self.play(FadeIn(zero1), FadeIn(zero2), FadeIn(zero3))
        self.wait(1.5)

        # Key words
        words = MathTex(r"\zeta(s)", font_size=40)
        words.to_edge(UP)
        self.play(Transform(title, words))
        self.wait(0.5)

        # Final text
        final_text = Text("Hidden zeros act as harmonics", font_size=24)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(plane), FadeOut(grid), FadeOut(surface),
                  FadeOut(critical_line), FadeOut(zero1), FadeOut(zero2), FadeOut(zero3),
                  FadeOut(final_text))
        self.wait(0.5)
