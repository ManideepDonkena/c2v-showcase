from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Five Inclusion Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show number 75
        num_75 = MathTex("75", font_size=40)
        num_75.shift(UP * 1)
        self.play(Write(num_75))
        self.wait(1)

        # Pulse the '5'
        if len(num_75) > 1:
            pulse_5 = num_75[1].copy()
            pulse_5.set_color(GOLD)
            self.play(
                pulse_5.animate.scale(1.3).set_color(GOLD),
                run_time=0.5
            )
            self.play(
            pulse_5.animate.scale(1/1.3).set_color(WHITE),
            run_time=0.5
        )

        # Equation below
        equation = MathTex("75 \\div 5 = 15", font_size=32)
        equation.next_to(num_75, DOWN, buff=0.5)
        self.play(Write(equation))
        self.wait(1)

        # Green checkmark
        check = Tex(r"$\checkmark$", color=GREEN, font_size=40)
        check.next_to(equation, RIGHT, buff=0.3)
        self.play(Write(check))
        self.wait(1.5)

        # Rule text
        rule_text = Text("Rule: Ending in 5 is ALWAYS Glint", font_size=24)
        rule_text.to_edge(DOWN)
        self.play(Write(rule_text))
        self.wait(2)

        # Narration key words
        self.play(FadeOut(rule_text))

        narration_1 = Text("Similarly, any number ending in five", font_size=24)
        narration_1.to_edge(DOWN)
        self.play(Write(narration_1))
        self.wait(1.5)

        narration_2 = Text("is always a Glint number.", font_size=24)
        narration_2.next_to(narration_1, DOWN, aligned_edge=LEFT)
        narration_2.shift(0.0 * RIGHT + 0.23 * UP)  # layout: separation vector
        self.play(Write(narration_2))
        self.wait(1.5)

        self.play(FadeOut(narration_1), FadeOut(narration_2))

        # Definition and example
        definition = Text("A whole number is glint when:", font_size=24)
        definition.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(definition))
        self.wait(1)

        rule1 = Text("(1) Every number ending in 1 is glint.", font_size=24)
        rule1.next_to(definition, DOWN, aligned_edge=LEFT)
        self.play(Write(rule1))
        self.wait(1.5)

        rule2 = Text("(2) A number ending in 0 is never glint.", font_size=24)
        rule2.next_to(rule1, DOWN, aligned_edge=LEFT)
        self.play(Write(rule2))
        self.wait(1.5)

        rule3 = Text("(3) A number ending in 5 is always glint.", font_size=24)
        rule3.next_to(rule2, DOWN, aligned_edge=LEFT)
        rule3.shift(0.0 * RIGHT + 0.38 * UP)  # layout: separation vector
        self.play(Write(rule3))
        self.wait(1.5)

        example = Text("Worked example:", font_size=24)
        example.next_to(rule3, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(example))
        self.wait(1.5)

        ex_1 = MathTex("24 \\div 4 = 6", font_size=24)
        ex_1.next_to(example, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(ex_1))
        self.wait(1.5)

        ex_2 = MathTex("26 \\div 6 \\text{ is not whole}", font_size=24)
        ex_2.next_to(ex_1, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(ex_2))
        self.wait(2)

        # Final fade
        self.play(
            FadeOut(definition),
            FadeOut(rule1),
            FadeOut(rule2),
            FadeOut(rule3),
            FadeOut(example),
            FadeOut(ex_1),
            FadeOut(ex_2),
            FadeOut(num_75),
            FadeOut(equation),
            FadeOut(check),
            FadeOut(title)
        )
        self.wait(0.5)
