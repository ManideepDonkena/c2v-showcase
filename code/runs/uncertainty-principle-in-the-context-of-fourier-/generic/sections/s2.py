from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Wide Pulse", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Time domain pulse
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
        
        # Frequency domain (Fourier transform)
        freq_axis = NumberLine(x_range=[-3, 3, 1], include_numbers=True, color=RED)
        freq_axis.to_edge(DOWN)
        freq_label = Text("Frequency", font_size=24).next_to(freq_axis, DOWN)
        
        # Narrow spike
        spike = Line(start=(0, -1.5, 0), end=(0, 1.5, 0), color=RED, stroke_width=8)
        spike_label = Text("Narrow Spectrum", font_size=24).next_to(spike, UP)
        
        # Initial setup
        self.play(Write(time_axis), Write(time_label))
        self.play(Create(pulse), Write(pulse_label))
        self.wait(1)
        
        # Show the transform
        self.play(Write(freq_axis), Write(freq_label))
        self.wait(0.5)
        self.play(Create(spike), Write(spike_label))
        self.wait(1.5)
        
        # Key words on screen
        word1 = Text("Long", font_size=24).to_corner(UL)
        self.play(Write(word1))
        self.wait(0.5)
        self.play(FadeOut(word1))
        
        word2 = Text("Precise", font_size=24).to_corner(UL)
        self.play(Write(word2))
        self.wait(0.5)
        self.play(FadeOut(word2))
        
        word3 = Text("Defined", font_size=24).to_corner(UL)
        self.play(Write(word3))
        self.wait(0.5)
        self.play(FadeOut(word3))
        
        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(time_axis),
            FadeOut(time_label),
            FadeOut(pulse),
            FadeOut(pulse_label),
            FadeOut(freq_axis),
            FadeOut(freq_label),
            FadeOut(spike),
            FadeOut(spike_label)
        )
        self.wait(0.5)
