from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Multiple of Ten Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Number line
        number_line = NumberLine(
            x_range=[0, 100, 10],
            include_numbers=True,
            stroke_width=2
        ).move_to(DOWN * 0.5)
        number_line.width = 12
        self.play(Create(number_line))
        self.wait(0.5)

        # Dapple label
        dapple_label = Text("Dapple", font_size=24).set_color(GREEN)
        not_dapple_label = Text("Not Dapple", font_size=24).set_color(RED)

        # Show multiples of ten from 10 to 90
        for i in range(1, 10):
            num = i * 10
            # Ensure the number exists before accessing it
            if num < len(number_line.numbers):
                num_obj = number_line.numbers[num]
                num_obj_copy = num_obj.copy()
                number_line.shift(0.0 * RIGHT + -0.18 * UP)  # layout: separation vector
                number_line.shift(0.0 * RIGHT + -0.18 * UP)  # layout: separation vector
                number_line.shift(0.0 * RIGHT + -0.18 * UP)  # layout: separation vector
                self.play(
                    num_obj_copy.animate.move_to(number_line.n2p(num)),
                    run_time=0.3
                )
                self.wait(0.2)
                # Turn green and label
                self.play(
                    num_obj_copy.animate.set_color(GREEN),
                    run_time=0.2
                )
                dapple_text = dapple_label.copy().next_to(num_obj_copy, UP)
                self.play(Write(dapple_text))
                self.wait(0.3)

        # Show 0 separately
        if 0 < len(number_line.numbers):
            zero_obj = number_line.numbers[0]
            zero_copy = zero_obj.copy()
            self.play(
                zero_copy.animate.move_to(number_line.n2p(0)),
                run_time=0.3
            )
            self.wait(0.2)
            self.play(
                zero_copy.animate.set_color(RED),
                run_time=0.2
            )
            x_mark = Cross(zero_copy, stroke_width=8, color=RED)
            self.play(Create(x_mark))
            not_dapple_text = not_dapple_label.copy().next_to(zero_copy, UP)
            self.play(Write(not_dapple_text))
            self.wait(0.5)

        # Narration text
        narration = Text("Every multiple of ten from 10 to 90 is dapple.", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)

        # Clear narration and show definition
        self.play(FadeOut(narration))

        def_text = Text("A whole number is dapple when its tens digit > units digit.", font_size=24)
        self.play(Write(def_text))
        self.wait(1.5)
        self.play(FadeOut(def_text))

        # Show rule 1
        rule1 = Text("Rule 1: Every multiple of 10 from 10 to 90 is dapple.", font_size=24).to_edge(DOWN)
        self.play(Write(rule1))
        self.wait(2.0)

        # Example: 52 and 25
        example_text = Text("Example: 52 is dapple (5 > 2); 25 is not (2 < 5).", font_size=24)
        self.play(Write(example_text))
        self.wait(2.0)

        # Show 44 is not dapple
        example_44 = Text("44 is not (4 = 4).", font_size=24).next_to(example_text, DOWN)
        self.play(Write(example_44))
        self.wait(1.5)

        self.play(FadeOut(rule1, example_text, example_44))

        # Final summary
        final_text = Text("All multiples of 10 from 10 to 90 are dapple.", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2.0)

        self.play(FadeOut(final_text, title))
