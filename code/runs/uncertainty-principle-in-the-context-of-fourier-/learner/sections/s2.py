from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Wide Pulse", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Time domain graph
        time_axis = NumberLine(x_range=[-5, 5, 1], include_numbers=True, color=BLUE)
        time_axis.to_edge(DOWN)
        time_label = Text("Time", font_size=24).next_to(time_axis, DOWN)
        
        # Gaussian pulse - wide
        pulse = ParametricFunction(
            lambda t: (t, 1.5 * np.exp(-t**2 / 2), 0),
            t_range=[-3, 3],
            color=YELLOW
        )
        pulse_label = Text("Wide Pulse", font_size=24).next_to(pulse, UP)
        
        self.play(Create(time_axis), Write(time_label))
        self.play(Create(pulse), Write(pulse_label))
        self.wait(1)

        # Show the frequency domain (Fourier Transform)
        freq_axis = NumberLine(x_range=[-3, 3, 1], include_numbers=True, color=RED)
        freq_axis.to_edge(DOWN)
        freq_label = Text("Frequency", font_size=24).next_to(freq_axis, DOWN)
        
        # Narrow spike (Fourier transform of wide pulse)
        spike = ParametricFunction(
            lambda t: (t, 3 * np.exp(-t**2 / 0.5), 0),
            t_range=[-1, 1],
            color=RED
        )
        spike_label = Text("Narrow Spectrum", font_size=24).next_to(spike, UP)
        
        self.play(Transform(time_axis, freq_axis), Transform(time_label, freq_label))
        self.play(Create(spike), Write(spike_label))
        self.wait(1)

        # Show the relationship
        words = Text("Long signal → Narrow spectrum", font_size=24).to_edge(UP)
        self.play(Write(words))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(title), FadeOut(pulse), FadeOut(spike), FadeOut(pulse_label), FadeOut(spike_label), FadeOut(time_axis), FadeOut(freq_axis), FadeOut(time_label), FadeOut(freq_label), FadeOut(words))
        self.wait(0.5)
