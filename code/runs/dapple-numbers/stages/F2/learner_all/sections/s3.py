from manim import *

class S3(Scene):
    def construct(self):
        title = Text("Non-Examples and Edge Cases", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 44 - equal digits
        num44 = MathTex("44").scale(2)
        self.play(Write(num44))
        self.wait(0.5)
        if len(num44) > 0:
            num44[0].set_color(RED)
        if len(num44) > 1:
            num44[1].set_color(RED)
        eq = MathTex("=").next_to(num44, RIGHT)
        self.play(Write(eq))
        self.wait(0.5)
        not_dapple = Text("Not Dapple", font_size=24).next_to(eq, RIGHT)
        self.play(Write(not_dapple))
        self.wait(1)
        self.play(FadeOut(num44), FadeOut(eq), FadeOut(not_dapple))
        
        # 25 - reversed
        num25 = MathTex("25").scale(2)
        self.play(Write(num25))
        self.wait(0.5)
        if len(num25) > 0:
            num25[0].set_color(RED)
        if len(num25) > 1:
            num25[1].set_color(RED)
        less = MathTex("<").next_to(num25, RIGHT)
        self.play(Write(less))
        self.wait(0.5)
        not_dapple2 = Text("Not Dapple (2 < 5)", font_size=24).next_to(less, RIGHT)
        self.play(Write(not_dapple2))
        self.wait(1)
        self.play(FadeOut(num25), FadeOut(less), FadeOut(not_dapple2))

        # 32 - valid case
        num32 = MathTex("32").scale(2)
        self.play(Write(num32))
        self.wait(0.5)
        if len(num32) > 0:
            num32[0].set_color(YELLOW)
        if len(num32) > 1:
            num32[1].set_color(GREEN)
        gt = MathTex(">").next_to(num32, RIGHT).set_color(GREEN)
        self.play(Write(gt))
        self.wait(0.5)
        text32 = Text("Tens > Units", font_size=24).next_to(gt, RIGHT)
        self.play(Write(text32))
        self.wait(1)
        self.play(FadeOut(num32), FadeOut(gt), FadeOut(text32))

        # 10 - valid case
        num10 = MathTex("10").scale(2)
        self.play(Write(num10))
        self.wait(0.5)
        if len(num10) > 0:
            num10[0].set_color(YELLOW)
        if len(num10) > 1:
            num10[1].set_color(GREEN)
        gt10 = MathTex(">").next_to(num10, RIGHT).set_color(GREEN)
        self.play(Write(gt10))
        self.wait(0.5)
        text10 = Text("1 > 0", font_size=24).next_to(gt10, RIGHT)
        self.play(Write(text10))
        self.wait(1)
        self.play(FadeOut(num10), FadeOut(gt10), FadeOut(text10))

        # 11 - not dapple
        num11 = MathTex("11").scale(2)
        self.play(Write(num11))
        self.wait(0.5)
        if len(num11) > 0:
            num11[0].set_color(RED)
        if len(num11) > 1:
            num11[1].set_color(RED)
        eq11 = MathTex("=").next_to(num11, RIGHT)
        self.play(Write(eq11))
        self.wait(0.5)
        not_dapple11 = Text("Not Dapple (Tens = Units)", font_size=24).next_to(eq11, RIGHT)
        self.play(Write(not_dapple11))
        self.wait(1)
        self.play(FadeOut(num11), FadeOut(eq11), FadeOut(not_dapple11))

        # 83 - valid
        num83 = MathTex("83").scale(2)
        self.play(Write(num83))
        self.wait(0.5)
        if len(num83) > 0:
            num83[0].set_color(YELLOW)
        if len(num83) > 1:
            num83[1].set_color(GREEN)
        gt83 = MathTex(">").next_to(num83, RIGHT).set_color(GREEN)
        self.play(Write(gt83))
        self.wait(0.5)
        text83 = Text("Tens > Units", font_size=24).next_to(gt83, RIGHT)
        self.play(Write(text83))
        self.wait(1)
        self.play(FadeOut(num83), FadeOut(gt83), FadeOut(text83))

        # 7 - one digit
        num7 = MathTex("7").scale(2)
        self.play(Write(num7))
        self.wait(0.5)
        tens7 = MathTex("0").set_color(YELLOW).next_to(num7, LEFT)
        units7 = MathTex("7").set_color(GREEN).next_to(num7, RIGHT)
        gt7 = MathTex(">").next_to(tens7, RIGHT).set_color(RED).shift(RIGHT * 0.45)
        self.play(Write(tens7), Write(units7), Write(gt7))
        self.wait(0.5)
        not_dapple7 = Text("Not Dapple (0 > 7 is false)", font_size=24).next_to(gt7, RIGHT)
        self.play(Write(not_dapple7))
        self.wait(1)
        self.play(FadeOut(num7), FadeOut(tens7), FadeOut(units7), FadeOut(gt7), FadeOut(not_dapple7))

        # 98 - valid
        num98 = MathTex("98").scale(2)
        self.play(Write(num98))
        self.wait(0.5)
        if len(num98) > 0:
            num98[0].set_color(YELLOW)
        if len(num98) > 1:
            num98[1].set_color(GREEN)
        gt98 = MathTex(">").next_to(num98, RIGHT).set_color(GREEN)
        self.play(Write(gt98))
        self.wait(0.5)
        text98 = Text("Tens > Units", font_size=24).next_to(gt98, RIGHT)
        self.play(Write(text98))
        self.wait(1)
        self.play(FadeOut(num98), FadeOut(gt98), FadeOut(text98))

        # 50 - valid
        num50 = MathTex("50").scale(2)
        self.play(Write(num50))
        self.wait(0.5)
        if len(num50) > 0:
            num50[0].set_color(YELLOW)
        if len(num50) > 1:
            num50[1].set_color(GREEN)
        gt50 = MathTex(">").next_to(num50, RIGHT).set_color(GREEN)
        self.play(Write(gt50))
        self.wait(0.5)
        text50 = Text("5 > 0", font_size=24).next_to(gt50, RIGHT)
        self.play(Write(text50))
        self.wait(1)
        self.play(FadeOut(num50), FadeOut(gt50), FadeOut(text50))

        # 77 - equal
        num77 = MathTex("77").scale(2)
        self.play(Write(num77))
        self.wait(0.5)
        if len(num77) > 0:
            num77[0].set_color(RED)
        if len(num77) > 1:
            num77[1].set_color(RED)
        eq77 = MathTex("=").next_to(num77, RIGHT)
        self.play(Write(eq77))
        self.wait(0.5)
        not_dapple77 = Text("Not Dapple (Tens = Units)", font_size=24).next_to(eq77, RIGHT)
        self.play(Write(not_dapple77))
        self.wait(1)
        self.play(FadeOut(num77), FadeOut(eq77), FadeOut(not_dapple77))

        # 44 again - equal
        num44again = MathTex("44").scale(2)
        self.play(Write(num44again))
        self.wait(0.5)
        if len(num44again) > 0:
            num44again[0].set_color(RED)
        if len(num44again) > 1:
            num44again[1].set_color(RED)
        eq44 = MathTex("=").next_to(num44again, RIGHT)
        self.play(Write(eq44))
        self.wait(0.5)
        not_dapple44 = Text("Not Dapple (Tens = Units)", font_size=24).next_to(eq44, RIGHT)
        self.play(Write(not_dapple44))
        self.wait(1)
        self.play(FadeOut(num44again), FadeOut(eq44), FadeOut(not_dapple44))

        # 44 and 10 - not dapple
        num44final = MathTex("44").scale(1.5)
        num10final = MathTex("10").scale(1.5)
        group = VGroup(num44final, num10final).arrange(RIGHT, buff=2)
        self.play(Write(group))
        self.wait(0.5)
        eq_final = MathTex("=").next_to(num44final, RIGHT)
        less_final = MathTex("<").next_to(num10final, RIGHT)
        self.play(Write(eq_final), Write(less_final))
        self.wait(0.5)
        not_dapple_final = Text("Not Dapple", font_size=24).next_to(eq_final, RIGHT)
        not_dapple_final2 = Text("Not Dapple", font_size=24).next_to(less_final, RIGHT)
        self.play(Write(not_dapple_final), Write(not_dapple_final2))
        self.wait(1)
        self.play(FadeOut(group), FadeOut(eq_final), FadeOut(less_final), FadeOut(not_dapple_final), FadeOut(not_dapple_final2))

        # 31 - dapple
        num31 = MathTex("31").scale(2)
        self.play(Write(num31))
        self.wait(0.5)
        if len(num31) > 0:
            num31[0].set_color(GREEN)
        if len(num31) > 1:
            num31[1].set_color(YELLOW)
        gt31 = MathTex(">").next_to(num31, RIGHT).set_color(GREEN)
        self.play(Write(gt31))
        self.wait(0.5)
        text31 = Text("Dapple", font_size=24).next_to(gt31, RIGHT)
        self.play(Write(text31))
        self.wait(1)
        self.play(FadeOut(num31), FadeOut(gt31), FadeOut(text31))

        # 31 -> 13 - not dapple
        num31split = MathTex("31").scale(2)
        num13 = MathTex("13").scale(2)
        self.play(Write(num31split))
        self.wait(0.5)
        self.play(ReplacementTransform(num31split, num13))
        self.wait(0.5)
        if len(num13) > 0:
            num13[0].set_color(RED)
        if len(num13) > 1:
            num13[1].set_color(RED)
        less13 = MathTex("<").next_to(num13, RIGHT)
        self.play(Write(less13))
        self.wait(0.5)
        not_dapple13 = Text("Not Dapple (1 < 3)", font_size=24).next_to(less13, RIGHT)
        self.play(Write(not_dapple13))
        self.wait(1)
        self.play(FadeOut(num13), FadeOut(less13), FadeOut(not_dapple13))

        # 63 - dapple example
        num63 = MathTex("63").scale(2)
        self.play(Write(num63))
        self.wait(0.5)
        if len(num63) > 0:
            num63[0].set_color(YELLOW)
        if len(num63) > 1:
            num63[1].set_color(GREEN)
        gt63 = MathTex(">").next_to(num63, RIGHT).set_color(GREEN)
        self.play(Write(gt63))
        self.wait(0.5)
        text63 = Text("Tens > Units", font_size=24).next_to(gt63, RIGHT)
        self.play(Write(text63))
        self.wait(1)
        self.play(FadeOut(num63), FadeOut(gt63), FadeOut(text63))

        # 0 - not dapple
        num0 = MathTex("0").scale(2)
        self.play(Write(num0))
        self.wait(0.5)
        not_dapple0 = Text("Not Dapple (no tens digit)", font_size=24).next_to(num0, RIGHT)
        self.play(Write(not_dapple0))
        self.wait(1)
        self.play(FadeOut(num0), FadeOut(not_dapple0))

        self.play(FadeOut(title))
        self.wait(0.5)
