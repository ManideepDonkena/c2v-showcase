from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Trade-off", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        # Split screen
        time_pulse = always_redraw(
            lambda: self.get_time_pulse(width=2)
        )
        freq_spectrum = always_redraw(
            lambda: self.get_freq_spectrum(width=3)
        )

        # Left side - Time pulse
        time_label = Text("Time Domain", font_size=24).to_edge(UP).shift(DOWN*2.5)
        self.play(Write(time_label))
        # Right side - Frequency spectrum
        freq_label = Text("Frequency Domain", font_size=24).to_edge(UP).shift(DOWN*2.5).shift(RIGHT*3.5)
        self.play(Write(freq_label))

        # Slider
        self.slider = ValueTracker(1.0)
        slider_line = Line(LEFT*3, RIGHT*3, color=WHITE)
        slider_dot = always_redraw(
            lambda: Dot(slider_line.point_from_proportion(self.slider.get_value()/2 + 0.5), color=YELLOW)
        )
        slider_label = Text("Time Pulse Width", font_size=20).next_to(slider_line, DOWN)
        
        self.play(Create(slider_line), Create(slider_dot), Write(slider_label))
        self.wait(0.5)

        # Initial pulse and spectrum
        initial_pulse = self.get_time_pulse(width=1.0)
        initial_spectrum = self.get_freq_spectrum(width=1.0)
        
        initial_spectrum.shift(0.0 * RIGHT + -0.48 * UP)  # layout: separation vector
        initial_pulse.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        self.play(
            Create(initial_pulse),
            Create(initial_spectrum),
            run_time=1
        )
        self.wait(0.5)

        # Formula
        formula = MathTex(r"\Delta t \cdot \Delta \omega \geq \frac{1}{2}", font_size=36)
        formula.to_edge(UP).shift(DOWN*0.5)
        self.play(Write(formula))
        self.wait(0.5)

        # Animation
        self.play(
            self.slider.animate.set_value(0.2),
            run_time=3,
            rate_func=linear
        )
        self.wait(1)

        self.play(
            self.slider.animate.set_value(1.0),
            run_time=3,
            rate_func=linear
        )
        self.wait(1)

        # Final text overlay
        text = Text("You cannot simultaneously know both the exact time and frequency", font_size=24)
        text.to_edge(DOWN)
        self.play(Write(text))
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(time_label),
            FadeOut(freq_label),
            FadeOut(slider_line),
            FadeOut(slider_dot),
            FadeOut(slider_label),
            FadeOut(initial_pulse),
            FadeOut(initial_spectrum),
            FadeOut(formula),
            FadeOut(text)
        )
        self.wait(0.5)

    def get_time_pulse(self, width):
        pulse = Rectangle(width=width, height=1, color=BLUE, fill_opacity=0.5)
        pulse.move_to(ORIGIN)
        return pulse

    def get_freq_spectrum(self, width):
        # Create a simple frequency spectrum that widens as time pulse narrows
        # This is a simplified representation
        if width < 0.3:
            width = 0.3
        spectrum = Rectangle(width=1/width, height=2, color=RED, fill_opacity=0.5)
        spectrum.move_to(RIGHT*4)
        return spectrum
