from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Peano Curve Construction", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial line segment
        line = Line(start=[-3, 0, 0], end=[3, 0, 0], color=BLUE)
        self.play(Create(line))
        self.wait(1)

        # First iteration: U shape
        u_shape = VGroup(
            Line(start=[-3, 0, 0], end=[-3, 2, 0], color=BLUE),
            Line(start=[-3, 2, 0], end=[0, 2, 0], color=BLUE),
            Line(start=[0, 2, 0], end=[0, 0, 0], color=BLUE),
            Line(start=[0, 0, 0], end=[3, 0, 0], color=BLUE),
        )
        self.play(Transform(line, u_shape))
        self.wait(1)

        # Second iteration
        u_shape2 = VGroup(
            Line(start=[-3, 0, 0], end=[-3, 2, 0], color=BLUE),
            Line(start=[-3, 2, 0], end=[-1, 2, 0], color=BLUE),
            Line(start=[-1, 2, 0], end=[-1, 0, 0], color=BLUE),
            Line(start=[-1, 0, 0], end=[0, 0, 0], color=BLUE),
            Line(start=[0, 0, 0], end=[0, 2, 0], color=BLUE),
            Line(start=[0, 2, 0], end=[1, 2, 0], color=BLUE),
            Line(start=[1, 2, 0], end=[1, 0, 0], color=BLUE),
            Line(start=[1, 0, 0], end=[3, 0, 0], color=BLUE),
        )
        self.play(Transform(line, u_shape2))
        self.wait(1)

        # Third iteration
        u_shape3 = VGroup(
            Line(start=[-3, 0, 0], end=[-3, 2, 0], color=BLUE),
            Line(start=[-3, 2, 0], end=[-2.5, 2, 0], color=BLUE),
            Line(start=[-2.5, 2, 0], end=[-2.5, 0, 0], color=BLUE),
            Line(start=[-2.5, 0, 0], end=[-2, 0, 0], color=BLUE),
            Line(start=[-2, 0, 0], end=[-2, 2, 0], color=BLUE),
            Line(start=[-2, 2, 0], end=[-1.5, 2, 0], color=BLUE),
            Line(start=[-1.5, 2, 0], end=[-1.5, 0, 0], color=BLUE),
            Line(start=[-1.5, 0, 0], end=[-1, 0, 0], color=BLUE),
            Line(start=[-1, 0, 0], end=[-1, 2, 0], color=BLUE),
            Line(start=[-1, 2, 0], end=[-0.5, 2, 0], color=BLUE),
            Line(start=[-0.5, 2, 0], end=[-0.5, 0, 0], color=BLUE),
            Line(start=[-0.5, 0, 0], end=[0, 0, 0], color=BLUE),
            Line(start=[0, 0, 0], end=[0, 2, 0], color=BLUE),
            Line(start=[0, 2, 0], end=[0.5, 2, 0], color=BLUE),
            Line(start=[0.5, 2, 0], end=[0.5, 0, 0], color=BLUE),
            Line(start=[0.5, 0, 0], end=[1, 0, 0], color=BLUE),
            Line(start=[1, 0, 0], end=[1, 2, 0], color=BLUE),
            Line(start=[1, 2, 0], end=[1.5, 2, 0], color=BLUE),
            Line(start=[1.5, 2, 0], end=[1.5, 0, 0], color=BLUE),
            Line(start=[1.5, 0, 0], end=[2, 0, 0], color=BLUE),
            Line(start=[2, 0, 0], end=[2, 2, 0], color=BLUE),
            Line(start=[2, 2, 0], end=[2.5, 2, 0], color=BLUE),
            Line(start=[2.5, 2, 0], end=[2.5, 0, 0], color=BLUE),
            Line(start=[2.5, 0, 0], end=[3, 0, 0], color=BLUE),
        )
        self.play(Transform(line, u_shape3))
        self.wait(1)

        # Show two points mapping to same location
        point_a = Dot([-2.75, 1, 0], color=YELLOW)
        point_b = Dot([-2.25, 1, 0], color=GREEN)
        label = MathTex(r"f(a) = f(b)", font_size=30).next_to(point_a, UP)
        self.play(FadeIn(point_a), FadeIn(point_b))
        label.shift(0.0 * RIGHT + 0.82 * UP)  # layout: separation vector
        self.play(Write(label))
        self.wait(1.5)

        # Show that it's not injective
        self.play(FadeOut(label), FadeOut(point_a), FadeOut(point_b))

        # Show two adjacent points in square with distant pre-images
        point1 = Dot([-2.7, 0.9, 0], color=RED)
        point2 = Dot([-2.65, 0.9, 0], color=ORANGE)
        self.play(FadeIn(point1), FadeIn(point2))
        self.wait(1)

        # Show counter for length
        length_counter = ValueTracker(3)
        length_text = always_redraw(
            lambda: MathTex(r"\text{Length} = " + str(int(length_counter.get_value())), font_size=24).to_corner(UL)
        )
        self.add(length_text)
        self.play(length_counter.animate.set_value(9), run_time=0.5)
        self.wait(0.5)
        self.play(length_counter.animate.set_value(27), run_time=0.5)
        self.wait(0.5)
        self.play(length_counter.animate.set_value(81), run_time=0.5)
        self.wait(1)

        # Show finite area vs infinite length
        square = Square(side_length=6, color=GREEN, fill_opacity=0.2)
        self.play(Create(square))
        self.wait(1)

        # Unit interval and square with equal measure
        unit_interval = Line(start=[-3, -2, 0], end=[3, -2, 0], color=BLUE)
        self.play(Create(unit_interval))
        self.wait(0.5)

        measure_label = MathTex(r"\text{Lebesgue measure } 1", font_size=24).next_to(unit_interval, DOWN)
        self.play(Write(measure_label))
        self.wait(1)

        # Hilbert curve scaling
        hilbert_text = Text("Hilbert Curve: N=4, r=1/2", font_size=24).to_edge(DOWN)
        self.play(Write(hilbert_text))
        self.wait(1)

        # Show geometric transformation rule
        self.play(FadeOut(hilbert_text), FadeOut(measure_label))

        # Final text
        final_text = Text("Infinite length, finite area", font_size=30).to_edge(UP)
        final_text.shift(0.0 * RIGHT + -0.53 * UP)  # layout: separation vector
        self.play(Write(final_text))
        self.wait(1)

        self.play(FadeOut(title), FadeOut(line), FadeOut(square), FadeOut(unit_interval), FadeOut(length_text), FadeOut(final_text))
