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
            color=WHITE
        )
        number_line.move_to(DOWN * 0.5)
        number_line.set_width(12)
        self.play(Create(number_line))
        self.wait(0.5)

        # Numbers sliding in and turning green
        multiples = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        dapple_labels = []
        for num in multiples:
            num_obj = number_line.numbers[num // 10]
            num_obj_copy = num_obj.copy()
            self.play(
                ReplacementTransform(num_obj_copy, num_obj),
                run_time=0.3
            )
            self.play(
                num_obj.animate.set_color(GREEN),
                run_time=0.2
            )
            label = Text("Dapple", font_size=24).next_to(num_obj, UP)
            self.play(Write(label))
            dapple_labels.append(label)
            self.wait(0.3)

        # Show 0 separately with red X and label
        zero_label = number_line.numbers[0]
        self.play(
            zero_label.animate.set_color(RED),
            run_time=0.2
        )
        x_mark = Cross(zero_label, stroke_width=8)
        self.play(Create(x_mark))
        not_dapple_text = Text("Not Dapple (No Tens Digit)", font_size=24).next_to(zero_label, DOWN)
        not_dapple_text.shift(1.11 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(not_dapple_text))
        self.wait(1.0)

        # Example: 61 is dapple
        self.play(FadeOut(*dapple_labels), FadeOut(not_dapple_text), FadeOut(x_mark))
        example_61 = Text("61", font_size=40).move_to(UP * 1.5)
        self.play(Write(example_61))
        check = VMobject()  # Placeholder for Checkmark
        check = Circle().scale(0.2).set_stroke(GREEN, width=8)
        check.add(Cross(check, stroke_width=8))  # Simple checkmark using Cross and Circle
        check.next_to(example_61, RIGHT)
        self.play(Create(check))
        self.wait(0.5)

        # Example: 16 is not dapple
        example_16 = Text("16", font_size=40).move_to(UP * 1.5)
        self.play(Transform(example_61, example_16))
        self.wait(0.5)
        cross = Cross(example_16, stroke_width=8)
        self.play(Create(cross))
        self.wait(0.5)

        # Rule summary
        rule_text = Text("Every multiple of 10 from 10 to 90 is dapple.", font_size=24)
        rule_text.to_edge(DOWN)
        self.play(Write(rule_text))
        self.wait(1.0)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(number_line),
            FadeOut(example_61),
            FadeOut(check),
            FadeOut(cross),
            FadeOut(rule_text)
        )
        self.wait(0.5)
