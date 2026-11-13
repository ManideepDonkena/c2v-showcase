from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Five Inclusion Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 75 example
        num_75 = MathTex("75").scale(2)
        self.play(Write(num_75))
        self.wait(0.5)
        
        digit_5 = num_75[0][1]
        self.play(Flash(digit_5, color=GOLD, flash_radius=0.3))
        self.wait(0.5)

        eq_75 = MathTex("75 \\div 5 = 15").next_to(num_75, DOWN, buff=0.5)
        self.play(Write(eq_75))
        self.wait(0.5)

        check_75 = Tex("\checkmark", color=GREEN).scale(2).next_to(eq_75, RIGHT)
        self.play(Write(check_75))
        self.wait(1)

        # 45 example
        num_45 = MathTex("45").scale(2).shift(DOWN * 1.5 + RIGHT * 0.84)
        self.play(Transform(num_75, num_45))
        self.wait(0.5)

        digit_5_45 = num_45[0][1]
        self.play(Flash(digit_5_45, color=GOLD, flash_radius=0.3))
        self.wait(0.5)

        eq_45 = MathTex("45 \\div 5 = 9").next_to(num_45, DOWN, buff=0.5)
        self.play(Write(eq_45))
        self.wait(0.5)

        check_45 = Tex("\\checkmark", color=GREEN).scale(2).next_to(eq_45, RIGHT)
        self.play(Write(check_45))
        self.wait(1)
        
        # 30 example
        num_30 = MathTex("30").scale(2).shift(DOWN * 1.5)
        self.play(Transform(num_45, num_30))
        self.wait(0.5)
        
        digit_0 = num_30[0][1]
        self.play(Flash(digit_0, color=RED, flash_radius=0.3))
        digit_0.shift(-0.23 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(digit_0.animate.set_color(RED))
        self.wait(0.5)

        x_30 = Tex("X", color=RED).scale(4).next_to(num_30, DOWN, buff=0.5)
        self.play(Write(x_30))
        self.wait(1)

        # 10 example
        num_10 = MathTex("10").scale(2).shift(DOWN * 1.5)
        self.play(Transform(num_30, num_10))
        self.wait(0.5)

        digit_0_10 = num_10[0][1]
        self.play(Flash(digit_0_10, color=RED, flash_radius=0.3))
        self.play(digit_0_10.animate.set_color(RED))
        self.wait(0.5)

        x_10 = Tex("Division by Zero is Impossible", color=RED).scale(0.7).next_to(num_10, DOWN, buff=0.5)
        self.play(Write(x_10))
        self.wait(1.5)

        # 31 example
        num_31 = MathTex("31").scale(2).shift(DOWN * 1.5)
        self.play(Transform(num_10, num_31))
        self.wait(0.5)

        digit_1 = num_31[0][1]
        self.play(Flash(digit_1, color=GREEN, flash_radius=0.3))
        self.wait(0.5)

        text_31 = Tex("Ends in 1 = Always Glint").scale(0.6).next_to(num_31, DOWN, buff=0.5)
        self.play(Write(text_31))
        self.wait(1)

        # 27 example
        num_27 = MathTex("27").scale(2).shift(DOWN * 1.5)
        self.play(Transform(num_31, num_27))
        self.wait(0.5)

        digit_7 = num_27[0][1]
        self.play(Flash(digit_7, color=GREEN, flash_radius=0.3))
        self.wait(0.5)

        eq_27 = MathTex("27 \\div 7 = 3.85...").next_to(num_27, DOWN, buff=0.5)
        self.play(Write(eq_27))
        self.wait(0.5)

        x_27 = Tex("X", color=RED).scale(2).next_to(eq_27, RIGHT)
        self.play(Write(x_27))
        self.wait(0.5)

        text_27 = Tex("Ends in 7 is NOT always Glint").scale(0.6).next_to(eq_27, DOWN, buff=0.3)
        self.play(Write(text_27))
        self.wait(1.5)

        # 22 example
        num_22 = MathTex("22").scale(2).shift(DOWN * 1.5)
        self.play(Transform(num_27, num_22))
        self.wait(0.5)

        digit_2 = num_22[0][1]
        self.play(Flash(digit_2, color=GREEN, flash_radius=0.3))
        self.wait(0.5)

        eq_22 = MathTex("22 \\div 2 = 11").next_to(num_22, DOWN, buff=0.5)
        self.play(Write(eq_22))
        self.wait(0.5)

        check_22 = Tex("\\checkmark", color=GREEN).scale(2).next_to(eq_22, RIGHT)
        self.play(Write(check_22))
        self.wait(1)

        # 21 and 24 examples
        num_21 = MathTex("21").scale(1.5).shift(DOWN * 1.5)
        num_24 = MathTex("24").scale(1.5).next_to(num_21, RIGHT, buff=1)
        self.play(Transform(num_22, num_21), Transform(eq_22, num_24))
        self.wait(0.5)

        digit_1_21 = num_21[0][1]
        self.play(Flash(digit_1_21, color=GREEN, flash_radius=0.3))
        self.wait(0.5)

        digit_4_24 = num_24[0][1]
        self.play(Flash(digit_4_24, color=GREEN, flash_radius=0.3))
        self.wait(0.5)

        eq_21 = MathTex("21 \\div 1 = 21").next_to(num_21, DOWN, buff=0.5)
        self.play(Write(eq_21))
        self.wait(0.5)

        check_21 = Tex("\\checkmark", color=GREEN).scale(1.5).next_to(eq_21, RIGHT)
        self.play(Write(check_21))

        eq_24 = MathTex("24 \\div 4 = 6").next_to(num_24, DOWN, buff=0.5)
        self.play(Write(eq_24))
        self.wait(0.5)

        check_24 = Tex("\\checkmark", color=GREEN).scale(1.5).next_to(eq_24, RIGHT)
        self.play(Write(check_24))
        self.wait(1.5)

        # 26 vs 24
        num_26 = MathTex("26").scale(1.5).shift(DOWN * 1.5)
        self.play(Transform(num_21, num_26))
        self.wait(0.5)

        digit_6 = num_26[0][1]
        self.play(Flash(digit_6, color=GREEN, flash_radius=0.3))
        self.wait(0.5)

        eq_26 = MathTex("26 \\div 6 = 4.33...").next_to(num_26, DOWN, buff=0.5)
        self.play(Write(eq_26))
        self.wait(0.5)

        x_26 = Tex("X", color=RED).scale(2).next_to(eq_26, RIGHT)
        self.play(Write(x_26))
        self.wait(1.5)

        # Final Rule Summary
        rule_text = Text("Rule: Ending in 5 is ALWAYS Glint", font_size=24).to_edge(DOWN)
        self.play(Write(rule_text))
        self.wait(1.5)

        self.play(FadeOut(title, num_26, eq_26, x_26, rule_text))
