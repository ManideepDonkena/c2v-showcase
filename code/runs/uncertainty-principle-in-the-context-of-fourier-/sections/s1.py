from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Narrow Pulse", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Time domain graph
        time_axis = NumberLine(x_range=[-4, 4, 1], include_numbers=True, color=BLUE)
        time_axis.to_edge(DOWN)
        time_label = Text("Time", font_size=24).next_to(time_axis, DOWN)
        
        # Frequency domain graph
        freq_axis = NumberLine(x_range=[-8, 8, 2], include_numbers=True, color=RED)
        freq_axis.to_edge(DOWN)
        freq_label = Text("Frequency", font_size=24).next_to(freq_axis, DOWN)
        
        # Gaussian pulse in time domain
        gaussian_pulse = always_redraw(
            lambda: ParametricFunction(
                lambda t: [t, 1.5 * np.exp(-t**2 / 2), 0],
                t_range=[-2, 2],
                color=BLUE,
                stroke_width=4
            )
        )
        
        # Fourier transform (frequency domain) - initially empty
        fourier_transform = always_redraw(
            lambda: ParametricFunction(
                lambda f: [f, 1.5 * np.exp(-f**2 / 8), 0],
                t_range=[-4, 4],
                color=RED,
                stroke_width=4
            )
        )
        
        # Initial setup
        self.play(Create(time_axis), Write(time_label))
        self.play(Create(gaussian_pulse))
        self.wait(1)
        
        # Show frequency domain
        self.play(Transform(gaussian_pulse, fourier_transform))
        self.play(Create(freq_axis), Write(freq_label))
        self.wait(0.5)
        
        # Arrows connecting narrow to wide
        arrow1 = Arrow(start=[-1.5, 1.5, 0], end=[-1.5, -1.5, 0], color=YELLOW)
        arrow2 = Arrow(start=[1.5, 1.5, 0], end=[1.5, -1.5, 0], color=YELLOW)
        
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait(1)
        
        # Key words
        word1 = Text("Narrow", font_size=24).next_to(arrow1, LEFT)
        word2 = Text("Wide", font_size=24).next_to(arrow2, RIGHT)
        self.play(Write(word1), Write(word2))
        self.wait(1.5)
        
        # Narration text
        narration = Text("Consider a sound that lasts only a split second—a sharp click.", font_size=24)
        narration.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(narration))
        self.wait(2)
        
        self.play(FadeOut(narration))
        
        narration2 = Text("Because it is so brief in time, it contains a vast range of frequencies.", font_size=24)
        narration2.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(narration2))
        self.wait(2)
        
        self.play(FadeOut(narration2))
        
        narration3 = Text("This wide spread in frequency is necessary to construct such a localized event.", font_size=24)
        narration3.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(narration3))
        self.wait(2)
        
        self.play(FadeOut(narration3), FadeOut(title), FadeOut(time_axis), FadeOut(freq_axis),
                  FadeOut(gaussian_pulse), FadeOut(fourier_transform), FadeOut(arrow1), FadeOut(arrow2),
                  FadeOut(time_label), FadeOut(freq_label), FadeOut(word1), FadeOut(word2))
        self.wait(0.5)
