from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Non-Examples and Edge Cases", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 44 - Equal digits
        num_44 = MathTex("44").scale(2)
        self.play(Write(num_44))
        self.wait(0.5)
        if len(num_44) > 0:
            num_44[0].set_color(RED)
        if len(num_44) > 1:
            num_44[1].set_color(RED)
        eq_sign = MathTex("=").next_to(num_44, buff=0.3)
        self.play(Write(eq_sign))
        self.wait(0.5)
        not_dapple = Text("Not Dapple", font_size=24).next_to(eq_sign, DOWN)
        self.play(Write(not_dapple))
        self.wait(1)
        self.play(FadeOut(num_44), FadeOut(eq_sign), FadeOut(not_dapple))
        
        # 25 - Reversed digits
        num_25 = MathTex("25").scale(2)
        self.play(Write(num_25))
        self.wait(0.5)
        if len(num_25) > 0:
            num_25[0].set_color(RED)
        if len(num_25) > 1:
            num_25[1].set_color(RED)
        less_sign = MathTex("<").next_to(num_25, buff=0.3)
        self.play(Write(less_sign))
        self.wait(0.5)
        not_dapple_2 = Text("Not Dapple (2 < 5)", font_size=24).next_to(less_sign, DOWN)
        self.play(Write(not_dapple_2))
        self.wait(1)
        self.play(FadeOut(num_25), FadeOut(less_sign), FadeOut(not_dapple_2))

        # 32 - Valid case
        num_32 = MathTex("32").scale(2)
        self.play(Write(num_32))
        self.wait(0.5)
        if len(num_32) > 0:
            num_32[0].set_color(YELLOW)
        if len(num_32) > 1:
            num_32[1].set_color(GREEN)
        gt_sign = MathTex(">").next_to(num_32, buff=0.3)
        self.play(Write(gt_sign))
        self.wait(0.5)
        gt_sign.set_color(GREEN)
        valid_text = Text("Tens > Units", font_size=24).next_to(gt_sign, DOWN)
        self.play(Write(valid_text))
        self.wait(1)
        self.play(FadeOut(num_32), FadeOut(gt_sign), FadeOut(valid_text))

        # 10 - Smallest dapple
        num_10 = MathTex("10").scale(2)
        self.play(Write(num_10))
        self.wait(0.5)
        if len(num_10) > 0:
            num_10[0].set_color(YELLOW)
        if len(num_10) > 1:
            num_10[1].set_color(GREEN)
        gt_sign_10 = MathTex(">").next_to(num_10, buff=0.3)
        self.play(Write(gt_sign_10))
        self.wait(0.5)
        gt_sign_10.set_color(GREEN)
        valid_text_10 = Text("1 > 0", font_size=24).next_to(gt_sign_10, DOWN)
        self.play(Write(valid_text_10))
        self.wait(1)
        self.play(FadeOut(num_10), FadeOut(gt_sign_10), FadeOut(valid_text_10))

        # 11 - Not dapple
        num_11 = MathTex("11").scale(2)
        self.play(Write(num_11))
        self.wait(0.5)
        if len(num_11) > 0:
            num_11[0].set_color(RED)
        if len(num_11) > 1:
            num_11[1].set_color(RED)
        eq_sign_11 = MathTex("=").next_to(num_11, buff=0.3)
        self.play(Write(eq_sign_11))
        self.wait(0.5)
        not_dapple_11 = Text("Not Dapple (Tens = Units)", font_size=24).next_to(eq_sign_11, DOWN)
        self.play(Write(not_dapple_11))
        self.wait(1)
        self.play(FadeOut(num_11), FadeOut(eq_sign_11), FadeOut(not_dapple_11))

        # 83 - Valid case
        num_83 = MathTex("83").scale(2)
        self.play(Write(num_83))
        self.wait(0.5)
        if len(num_83) > 0:
            num_83[0].set_color(YELLOW)
        if len(num_83) > 1:
            num_83[1].set_color(GREEN)
        gt_sign_83 = MathTex(">").next_to(num_83, buff=0.3)
        self.play(Write(gt_sign_83))
        self.wait(0.5)
        gt_sign_83.set_color(GREEN)
        valid_text_83 = Text("Tens > Units", font_size=24).next_to(gt_sign_83, DOWN)
        self.play(Write(valid_text_83))
        self.wait(1)
        self.play(FadeOut(num_83), FadeOut(gt_sign_83), FadeOut(valid_text_83))

        # 7 - One-digit
        num_7 = MathTex("7").scale(2)
        self.play(Write(num_7))
        self.wait(0.5)
        zero = MathTex("0").next_to(num_7, LEFT, buff=0.3)
        zero.set_color(YELLOW)
        seven = MathTex("7").next_to(num_7, RIGHT, buff=0.3)
        seven.set_color(GREEN)
        gt_sign_7 = MathTex("<").next_to(zero, buff=0.3)
        gt_sign_7.shift(-0.45 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(gt_sign_7))
        self.wait(0.5)
        not_dapple_7 = Text("Not Dapple (0 > 7 is false)", font_size=24).next_to(gt_sign_7, DOWN)
        self.play(Write(not_dapple_7))
        self.wait(1)
        self.play(FadeOut(num_7), FadeOut(zero), FadeOut(seven), FadeOut(gt_sign_7), FadeOut(not_dapple_7))

        # 98 - Valid case
        num_98 = MathTex("98").scale(2)
        self.play(Write(num_98))
        self.wait(0.5)
        if len(num_98) > 0:
            num_98[0].set_color(YELLOW)
        if len(num_98) > 1:
            num_98[1].set_color(GREEN)
        gt_sign_98 = MathTex(">").next_to(num_98, buff=0.3)
        self.play(Write(gt_sign_98))
        self.wait(0.5)
        gt_sign_98.set_color(GREEN)
        valid_text_98 = Text("Tens > Units", font_size=24).next_to(gt_sign_98, DOWN)
        self.play(Write(valid_text_98))
        self.wait(1)
        self.play(FadeOut(num_98), FadeOut(gt_sign_98), FadeOut(valid_text_98))

        # 50 - Valid case
        num_50 = MathTex("50").scale(2)
        self.play(Write(num_50))
        self.wait(0.5)
        if len(num_50) > 0:
            num_50[0].set_color(YELLOW)
        if len(num_50) > 1:
            num_50[1].set_color(GREEN)
        gt_sign_50 = MathTex(">").next_to(num_50, buff=0.3)
        self.play(Write(gt_sign_50))
        self.wait(0.5)
        gt_sign_50.set_color(GREEN)
        valid_text_50 = Text("5 > 0", font_size=24).next_to(gt_sign_50, DOWN)
        self.play(Write(valid_text_50))
        self.wait(1)
        self.play(FadeOut(num_50), FadeOut(gt_sign_50), FadeOut(valid_text_50))

        # 77 - Equal digits
        num_77 = MathTex("77").scale(2)
        self.play(Write(num_77))
        self.wait(0.5)
        if len(num_77) > 0:
            num_77[0].set_color(RED)
        if len(num_77) > 1:
            num_77[1].set_color(RED)
        eq_sign_77 = MathTex("=").next_to(num_77, buff=0.3)
        self.play(Write(eq_sign_77))
        self.wait(0.5)
        not_dapple_77 = Text("Not Dapple (Tens = Units)", font_size=24).next_to(eq_sign_77, DOWN)
        self.play(Write(not_dapple_77))
        self.wait(1)
        self.play(FadeOut(num_77), FadeOut(eq_sign_77), FadeOut(not_dapple_77))

        # 44 again - Equal digits
        num_44_again = MathTex("44").scale(2)
        self.play(Write(num_44_again))
        self.wait(0.5)
        if len(num_44_again) > 0:
            num_44_again[0].set_color(RED)
        if len(num_44_again) > 1:
            num_44_again[1].set_color(RED)
        eq_sign_44 = MathTex("=").next_to(num_44_again, buff=0.3)
        self.play(Write(eq_sign_44))
        self.wait(0.5)
        not_dapple_44 = Text("Not Dapple (Tens = Units)", font_size=24).next_to(eq_sign_44, DOWN)
        self.play(Write(not_dapple_44))
        self.wait(1)
        self.play(FadeOut(num_44_again), FadeOut(eq_sign_44), FadeOut(not_dapple_44))

        # 44 and 10 - Not dapple
        num_44_final = MathTex("44").scale(1.5)
        num_10_final = MathTex("10").scale(1.5)
        group = VGroup(num_44_final, num_10_final).arrange(RIGHT, buff=1)
        self.play(Write(group))
        self.wait(0.5)
        eq_sign_final = MathTex("=").next_to(num_44_final, buff=0.3)
        less_sign_final = MathTex("<").next_to(num_10_final, buff=0.3)
        self.play(Write(eq_sign_final), Write(less_sign_final))
        self.wait(0.5)
        not_dapple_final = Text("Not Dapple", font_size=24).next_to(VGroup(eq_sign_final, less_sign_final), DOWN)
        self.play(Write(not_dapple_final))
        self.wait(1)
        self.play(FadeOut(group), FadeOut(eq_sign_final), FadeOut(less_sign_final), FadeOut(not_dapple_final))

        # 31 - Dapple
        num_31 = MathTex("31").scale(2)
        self.play(Write(num_31))
        self.wait(0.5)
        if len(num_31) > 0:
            num_31[0].set_color(GREEN)
        if len(num_31) > 1:
            num_31[1].set_color(YELLOW)
        valid_text_31 = Text("Dapple", font_size=24).next_to(num_31, DOWN)
        self.play(Write(valid_text_31))
        self.wait(1)
        self.play(FadeOut(num_31), FadeOut(valid_text_31))

        # 31 split and swap
        num_31_split = MathTex("3", "1").scale(2).arrange(RIGHT, buff=0.5)
        self.play(Write(num_31_split))
        self.wait(0.5)
        num_13 = MathTex("13").scale(2)
        self.play(Transform(num_31_split, num_13))
        self.wait(0.5)
        if len(num_13) > 0:
            num_13[0].set_color(RED)
        if len(num_13) > 1:
            num_13[1].set_color(RED)
        less_sign_swap = MathTex("<").next_to(num_13, buff=0.3)
        self.play(Write(less_sign_swap))
        self.wait(0.5)
        not_dapple_swap = Text("Not Dapple (1 < 3)", font_size=24).next_to(less_sign_swap, DOWN)
        self.play(Write(not_dapple_swap))
        self.wait(1)
        self.play(FadeOut(num_13), FadeOut(less_sign_swap), FadeOut(not_dapple_swap))

        # 63 - Demonstrate rule
        num_63 = MathTex("63").scale(2)
        num_63.shift(0.0 * RIGHT + 0.84 * UP)  # layout: separation vector
        self.play(Write(num_63))
        self.wait(0.5)
        if len(num_63) > 0:
            num_63[0].set_color(YELLOW)
        if len(num_63) > 1:
            num_63[1].set_color(GREEN)
        gt_sign_63 = MathTex(">").next_to(num_63, buff=0.3)
        self.play(Write(gt_sign_63))
        self.wait(0.5)
        gt_sign_63.set_color(GREEN)
        valid_text_63 = Text("Tens > Units", font_size=24).next_to(gt_sign_63, DOWN)
        self.play(Write(valid_text_63))
        self.wait(1)
        self.play(FadeOut(num_63), FadeOut(gt_sign_63), FadeOut(valid_text_63))

        # 0 - Not dapple
        num_zero = MathTex("0").scale(2)
        self.play(Write(num_zero))
        self.wait(0.5)
        not_dapple_zero = Text("Not Dapple (no tens digit)", font_size=24).next_to(num_zero, DOWN)
        self.play(Write(not_dapple_zero))
        self.wait(1)
        self.play(FadeOut(num_zero), FadeOut(not_dapple_zero))

        # End
        self.play(FadeOut(title))
        self.wait(0.5)
