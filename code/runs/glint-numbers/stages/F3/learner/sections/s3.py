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
