from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Multiple of Ten Rule", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Number line
        number_line = NumberLine(
            x_range=[0, 100, 10],
            include_numbers=True,
            stroke_width=2,
            tick_size=0.05,
            unit_size=0.7
        )
        number_line.move_to(DOWN * 0.5)
        # Set numbers_to_show after object creation
        number_line.numbers_to_show = range(0, 100, 10)
        number_line.shift(28.21 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(number_line))
        self.wait(0.5)

        # Dapple label
        dapple_label = Text("Dapple", font_size=24, color=GREEN)
        not_dapple_label = Text("Not Dapple", font_size=24, color=RED)

        # Numbers 10 to 90 slide in and turn green
        for i in range(1, 10):
            num = i * 10
            num_mob = Integer(num, font_size=30)
            num_mob.move_to(number_line.n2p(num))
            self.play(
                FadeIn(num_mob),
                run_time=0.3
            )
            # Label as Dapple
            dapple_copy = dapple_label.copy()
            dapple_copy.next_to(num_mob, UP)
            self.play(
                Transform(num_mob, num_mob.set_color(GREEN)),
                FadeIn(dapple_copy),
                run_time=0.2
            )
            self.wait(0.3)

        # Show 0 separately
        zero = Integer(0, font_size=40)
        zero.move_to(number_line.n2p(0))
        self.play(FadeIn(zero), run_time=0.5)
        self.wait(0.5)

        # Label for 0
        not_dapple_zero = not_dapple_label.copy()
        not_dapple_zero.next_to(zero, UP)
        self.play(FadeIn(not_dapple_zero), run_time=0.5)
        self.wait(0.5)

        # Explanation text
        explanation = Text("No tens digit → Not Dapple", font_size=24, color=RED)
        explanation.next_to(zero, DOWN)
        self.play(Write(explanation))
        self.wait(1.0)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(number_line),
            FadeOut(zero),
            FadeOut(not_dapple_zero),
            FadeOut(explanation),
            run_time=0.5
        )
        self.wait(0.5)
