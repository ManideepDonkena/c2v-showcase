from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Five Inclusion Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First number: 75
        num_75 = MathTex("75", font_size=40)
        num_75.shift(UP * 1)
        self.play(Write(num_75))
        self.wait(0.5)
        # Pulse '5' in 75
        if len(num_75) > 1:
            pulse_75 = num_75[1].copy()
            pulse_75.set_color(GOLD)
            self.play(pulse_75.animate.scale(1.2).set_color(GOLD), run_time=0.5)
            self.play(pulse_75.animate.scale(1/1.2).set_color(WHITE), run_time=0.5)

        # Equation for 75
        eq_75 = MathTex("75 \div 5 = 15", font_size=32)
        eq_75.next_to(num_75, DOWN, buff=0.5)
        self.play(Write(eq_75))
        self.wait(0.5)

        # Green checkmark
        check_75 = Tex("\\checkmark", color=GREEN, font_size=40)
        check_75.next_to(eq_75, RIGHT, buff=0.3)
        self.play(Write(check_75))
        self.wait(1)

        # Fade out first example
        self.play(FadeOut(num_75), FadeOut(eq_75), FadeOut(check_75))

        # Second number: 45
        num_45 = MathTex("45", font_size=40)
        num_45.shift(UP * 1)
        self.play(Write(num_45))
        self.wait(0.5)

        # Pulse '5' in 45
        if len(num_45) > 1:
            pulse_45 = num_45[1].copy()
            pulse_45.set_color(GOLD)
            self.play(pulse_45.animate.scale(1.2).set_color(GOLD), run_time=0.5)
            self.play(pulse_45.animate.scale(1/1.2).set_color(WHITE), run_time=0.5)

        # Equation for 45
        eq_45 = MathTex("45 \\div 5 = 9", font_size=32)
        eq_45.next_to(num_45, DOWN, buff=0.5)
        self.play(Write(eq_45))
        self.wait(0.5)

        # Green checkmark
        check_45 = Tex("\\checkmark", color=GREEN, font_size=40)
        check_45.next_to(eq_45, RIGHT, buff=0.3)
        self.play(Write(check_45))
        self.wait(1)

        # Rule text
        rule_text = Text("Rule: Ending in 5 is ALWAYS Glint", font_size=28)
        rule_text.to_edge(DOWN)
        self.play(Write(rule_text))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(num_45), FadeOut(eq_45), FadeOut(check_45), FadeOut(rule_text))
