from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Narrow Pulse", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Time axis
        time_axis = NumberLine(x_range=[-4, 4, 1], include_numbers=True, color=BLUE)
        time_axis.to_edge(DOWN)
        time_label = Text("Time", font_size=24).next_to(time_axis, DOWN)
        self.play(Create(time_axis), Write(time_label))
        self.wait(0.5)

        # Frequency axis
        freq_axis = NumberLine(x_range=[-8, 8, 2], include_numbers=True, color=GREEN)
        freq_axis.to_edge(DOWN)
        freq_label = Text("Frequency", font_size=24).next_to(freq_axis, DOWN)
        self.play(Create(freq_axis), Write(freq_label))
        self.wait(0.5)

        # Narrow Gaussian pulse in time domain
        gaussian_pulse = always_redraw(
            lambda: ParametricFunction(
                lambda t: [t, 2 * np.exp(-t**2 / 2), 0],
                t_range=[-2, 2],
                color=YELLOW
            )
        )
        self.play(Create(gaussian_pulse))
        self.wait(1)

        # Show the arrow from narrow pulse to wide spectrum
        arrow = Arrow(start=LEFT * 3, end=RIGHT * 3, color=RED)
        arrow.next_to(time_axis, UP, buff=0.5)
        arrow_label = Text("Narrow in Time", font_size=24).next_to(arrow, UP)
        self.play(GrowArrow(arrow), Write(arrow_label))
        self.wait(1)

        # Fourier Transform - wide bell curve
        fourier_transform = always_redraw(
            lambda: ParametricFunction(
                lambda t: [t, 0.5 * np.exp(-t**2 / 8), 0],
                t_range=[-6, 6],
                color=ORANGE
            )
        )
        self.play(Create(fourier_transform))
        self.wait(1)

        # Arrow from wide spectrum to broad frequency range
        arrow2 = Arrow(start=LEFT * 3, end=RIGHT * 3, color=RED)
        arrow2.next_to(freq_axis, UP, buff=0.5)
        arrow_label2 = Text("Wide in Frequency", font_size=24).next_to(arrow2, UP)
        self.play(GrowArrow(arrow2), Write(arrow_label2))
        self.wait(1)

        # Show Dirac delta function
        self.play(FadeOut(gaussian_pulse, arrow, arrow_label, fourier_transform, arrow2, arrow_label2))

        dirac = always_redraw(
            lambda: Line(start=[0, -2, 0], end=[0, 2, 0], color=PURPLE)
        )
        self.play(Create(dirac))
        self.wait(1)

        # Label for Dirac delta
        dirac_label = Text("Dirac Delta", font_size=24).next_to(dirac, LEFT)
        self.play(Write(dirac_label))
        self.wait(1)

        # Show its FT as a horizontal line
        ft_line = always_redraw(
            lambda: Line(start=[-6, 0, 0], end=[6, 0, 0], color=PURPLE)
        )
        self.play(Create(ft_line))
        self.wait(1)

        # Label for FT of Dirac
        ft_label = Text("Constant FT", font_size=24).next_to(ft_line, UP)
        self.play(Write(ft_label))
        self.wait(1)

        # Narration text
        narration = Text("A sharp click contains all frequencies.", font_size=24)
        narration.to_edge(UP)
        self.play(Write(narration))
        self.wait(2)

        self.play(FadeOut(title, time_axis, freq_axis, time_label, freq_label, dirac, dirac_label, ft_line, ft_label, narration))
        self.wait(0.5)
