from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Trade-off", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Formula display
        formula = MathTex(r"\Delta t \cdot \Delta \omega \geq \frac{1}{2}", font_size=40)
        formula.to_corner(UR)
        self.play(Write(formula))
        self.wait(0.5)

        # Left side: Time pulse
        time_axis = NumberLine(x_range=[-4, 4, 1], include_numbers=False, length=6)
        time_axis.to_edge(LEFT).shift(DOWN*1.5)
        time_label = Text("Time", font_size=24).next_to(time_axis, DOWN)
        
        # Initial pulse
        pulse_width = 0.0
        pulse = always_redraw(
            lambda: Rectangle(
                width=0.5 + 1.5 * pulse_width,
                height=1,
                color=BLUE,
            ).set_fill(opacity=0.7)
            .move_to(time_axis.n2p(0))
        )
        
        # Slider
        slider = always_redraw(
            lambda: Line(
                start=time_axis.n2p(-3),
                end=time_axis.n2p(3),
                color=GRAY
            )
        )
        slider_handle = always_redraw(
            lambda: Dot(
                point=slider.point_from_proportion(pulse_width),
                color=YELLOW
            )
        )

        # Right side: Frequency spectrum
        freq_axis = NumberLine(x_range=[-6, 6, 1], include_numbers=False, length=6)
        freq_axis.to_edge(RIGHT).shift(DOWN*1.5)
        freq_label = Text("Frequency", font_size=24).next_to(freq_axis, DOWN)
        
        # Initial spectrum
        spectrum = always_redraw(
            lambda: parametric_surface(
                lambda u, v: np.array([
                    v,
                    0.5 * np.exp(-0.5 * (v)**2 / (0.5 + 1.5 * pulse_width)**2) * np.sin(3*v),
                    0
                ]),
                u_range=[-6, 6],
                v_range=[-6, 6],
                resolution=(20, 20),
                fill_opacity=0.7,
                color=RED
            ).shift(RIGHT*4)
        )

        # Add all elements to scene
        self.play(
            Create(time_axis),
            Write(time_label),
            Create(freq_axis),
            Write(freq_label),
            Create(slider),
            Create(slider_handle),
            Create(pulse),
            Create(spectrum),
            run_time=1
        )
        self.wait(0.5)

        # Animation loop
        self.play(
            UpdateFromFunc(
                slider_handle,
                lambda m: m.move_to(slider.point_from_proportion(pulse_width))
            ),
            UpdateFromFunc(
                pulse,
                lambda m: m.become(
                    Rectangle(
                        width=0.5 + 1.5 * pulse_width,
                        height=1,
                        color=BLUE,
                        fill_opacity=0.7
                    ).move_to(time_axis.n2p(0))
                )
            ),
            UpdateFromFunc(
                spectrum,
                lambda m: m.become(
                    parametric_surface(
                        lambda u, v: np.array([
                            v,
                            0.5 * np.exp(-0.5 * (v)**2 / (0.5 + 1.5 * pulse_width)**2) * np.sin(3*v),
                            0
                        ]),
                        u_range=[-6, 6],
                        v_range=[-6, 6],
                        resolution=(20, 20),
                        fill_opacity=0.7,
                        color=RED
                    ).shift(RIGHT*4)
                )
            ),
            run_time=3,
            rate_func=linear
        )

        self.wait(1)

        # Show key message
        msg = Text("Compressing in time blurs frequency", font_size=24).to_edge(DOWN)
        self.play(Write(msg))
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(time_axis),
            FadeOut(time_label),
            FadeOut(freq_axis),
            FadeOut(freq_label),
            FadeOut(slider),
            FadeOut(slider_handle),
            FadeOut(pulse),
            FadeOut(spectrum),
            FadeOut(msg)
        )
        self.wait(0.5)
