from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Five Inclusion Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Number 75 appears
        num = MathTex("75", font_size=40)
        num.move_to(ORIGIN)
        self.play(Write(num))
        self.wait(1)
        # Pulse the '5'
        pulse = None
        if len(num) > 1:
            pulse = num[1].copy()
            pulse.set_color(GOLD)
            self.play(pulse.animate.scale(1.2).set_color(GOLD))
        if pulse is not None:
            self.play(pulse.animate.scale(1/1.2).set_color(WHITE))
        self.wait(0.5)

        # Equation appears
        equation = MathTex("75 \\div 5 = 15", font_size=32)
        equation.next_to(num, DOWN, buff=0.5)
        self.play(Write(equation))
        self.wait(1.5)

        # Green checkmark
        check = Tex("$\\checkmark$", color=GREEN, font_size=40)
        check.next_to(equation, RIGHT, buff=0.3)
        self.play(Write(check))
        self.wait(1.5)

        # Rule text
        rule = Text("Rule: Ending in 5 is ALWAYS Glint", font_size=24)
        rule.next_to(check, DOWN, buff=0.5)
        self.play(Write(rule))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(num),
            FadeOut(equation),
            FadeOut(check),
            FadeOut(rule)
        )
        self.wait(0.5)

        # New rule 2
        rule2 = Text("Rule 2: A number ending in 0 is never a Glint number.", font_size=24)
        rule2.to_edge(UP)
        self.play(Write(rule2))
        self.wait(1.5)

        example_30 = MathTex("30", font_size=36)
        example_30.next_to(rule2, DOWN, buff=0.5)
        self.play(Write(example_30))
        self.wait(1.5)

        explanation_30 = Text("For example, the number 30 ends in 0, so it is NOT a Glint number.", font_size=24)
        explanation_30.next_to(example_30, DOWN, buff=0.5)
        self.play(Write(explanation_30))
        self.wait(2)

        # Fade out previous content
        self.play(
            FadeOut(rule2),
            FadeOut(example_30),
            FadeOut(explanation_30)
        )
        self.wait(0.5)

        # New rule about 3
        rule3 = Text("A number ending in 3 is always a Glint number.", font_size=24)
        rule3.to_edge(UP)
        self.play(Write(rule3))
        self.wait(1.5)

        example_13 = MathTex("13", font_size=36)
        example_13.next_to(rule3, DOWN, buff=0.5)
        self.play(Write(example_13))
        self.wait(1.5)

        explanation_13 = Text("Its last digit is 3 (not zero). 13 ÷ 3 is not whole, so 13 is NOT a Glint number.", font_size=24)
        explanation_13.next_to(example_13, DOWN, buff=0.5)
        self.play(Write(explanation_13))
        self.wait(2)

        # Fade out previous content
        self.play(
            FadeOut(rule3),
            FadeOut(example_13),
            FadeOut(explanation_13)
        )
        self.wait(0.5)

        # New worked example with 48 and 49
        example_48 = MathTex("48", font_size=36)
        example_48.to_edge(UP)
        self.play(Write(example_48))
        self.wait(1.5)

        explanation_48 = Text("Consider the number 48. Its last digit is 8.", font_size=24)
        explanation_48.next_to(example_48, DOWN, buff=0.5)
        self.play(Write(explanation_48))
        self.wait(1.5)

        equation_48 = MathTex("48 \\div 8 = 6", font_size=32)
        equation_48.next_to(explanation_48, DOWN, buff=0.5)
        self.play(Write(equation_48))
        self.wait(1.5)

        check_48 = Tex("$\\checkmark$", color=GREEN, font_size=40)
        check_48.next_to(equation_48, RIGHT, buff=0.3)
        self.play(Write(check_48))
        self.wait(1.5)

        conclusion_48 = Text("Therefore, 48 is a Glint number.", font_size=24)
        conclusion_48.next_to(check_48, DOWN, buff=0.5)
        self.play(Write(conclusion_48))
        self.wait(2)

        # Contrast with 49
        example_49 = MathTex("49", font_size=36)
        example_49.next_to(conclusion_48, DOWN, buff=0.5)
        self.play(Write(example_49))
        self.wait(1.5)

        explanation_49 = Text("Contrast this with 49. Its last digit is 9.", font_size=24)
        explanation_49.next_to(example_49, DOWN, buff=0.5)
        self.play(Write(explanation_49))
        self.wait(1.5)

        equation_49 = MathTex("49 \\div 9 = 5.44...", font_size=32)
        equation_49.next_to(explanation_49, DOWN, buff=0.5)
        self.play(Write(equation_49))
        self.wait(1.5)

        cross_49 = Tex("$\\times$", color=RED, font_size=40)
        cross_49.next_to(equation_49, RIGHT, buff=0.3)
        self.play(Write(cross_49))
        self.wait(1.5)

        conclusion_49 = Text("Therefore, 49 is not a Glint number.", font_size=24)
        conclusion_49.next_to(cross_49, DOWN, buff=0.5)
        self.play(Write(conclusion_49))
        self.wait(2)

        # Final fade out
        self.play(
            FadeOut(example_48),
            FadeOut(explanation_48),
            FadeOut(equation_48),
            FadeOut(check_48),
            FadeOut(conclusion_48),
            FadeOut(example_49),
            FadeOut(explanation_49),
            FadeOut(equation_49),
            FadeOut(cross_49),
            FadeOut(conclusion_49)
        )
        self.wait(0.5)
