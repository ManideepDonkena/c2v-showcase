from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Reversal Property", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 52 as Dapple, reverse to 25 as Not Dapple
        num52 = MathTex("52").set_color(GREEN).scale(1.5)
        self.play(Write(num52))
        self.wait(0.5)

        # Split into digits
        digit5 = MathTex("5").move_to(num52.get_center()).scale(1.5)
        digit2 = MathTex("2").move_to(num52.get_center()).scale(1.5)
        self.play(Transform(num52, VGroup(digit5, digit2)))

        # Swap positions
        self.play(
            digit5.animate.move_to(RIGHT * 0.5 + UP * 0.5),
            digit2.animate.move_to(LEFT * 0.5 + UP * 0.5)
        )
        num25 = MathTex("25").set_color(RED).scale(1.5).move_to(ORIGIN)
        num25.shift(0.64 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(num25))
        self.wait(0.5)

        # Label reversal
        arrow = Arrow(LEFT, RIGHT, buff=0.2).next_to(num52, DOWN)
        rev_text = Text("Reversal", font_size=24).next_to(arrow, DOWN)
        self.play(GrowArrow(arrow), Write(rev_text))
        self.wait(1)

        # Show 32 with comparison
        num32 = MathTex("32").scale(1.5).to_edge(LEFT)
        self.play(Write(num32))
        self.wait(0.5)

        digit3 = MathTex("3").set_color(YELLOW).next_to(num32, LEFT)
        digit2 = MathTex("2").set_color(YELLOW).next_to(num32, RIGHT)
        self.play(Write(digit3), Write(digit2))
        self.wait(0.5)

        comp_gt = MathTex(">").set_color(GREEN).scale(1.5).move_to(ORIGIN)
        comp_gt.shift(0.53 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(comp_gt))
        self.wait(0.5)

        text_gt = Text("Tens > Units", font_size=24).next_to(comp_gt, DOWN)
        self.play(Write(text_gt))
        self.wait(1)

        # Show 10 as Dapple
        num10 = MathTex("10").scale(1.5).to_edge(RIGHT)
        self.play(Write(num10))
        self.wait(0.5)

        digit1 = MathTex("1").set_color(YELLOW).next_to(num10, LEFT)
        digit0 = MathTex("0").set_color(YELLOW).next_to(num10, RIGHT)
        self.play(Write(digit1), Write(digit0))
        self.wait(0.5)

        comp_gt_10 = MathTex(">").set_color(GREEN).scale(1.5).move_to(ORIGIN)
        self.play(Write(comp_gt_10))
        self.wait(0.5)

        text_10 = Text("1 > 0", font_size=24).next_to(comp_gt_10, DOWN)
        self.play(Write(text_10))
        self.wait(1)

        # Show 11 as Not Dapple
        num11 = MathTex("11").set_color(RED).scale(1.5).move_to(ORIGIN)
        self.play(Transform(num10, num11))
        self.wait(0.5)

        eq_sign = MathTex("=").set_color(RED).scale(1.5).move_to(ORIGIN)
        self.play(Write(eq_sign))
        self.wait(0.5)

        text_not_dapple_eq = Text("Not Dapple (Tens = Units)", font_size=24).next_to(eq_sign, DOWN)
        self.play(Write(text_not_dapple_eq))
        self.wait(1)

        # Show 83 as Dapple
        num83 = MathTex("83").scale(1.5).to_edge(LEFT)
        self.play(Write(num83))
        self.wait(0.5)

        digit8 = MathTex("8").set_color(YELLOW).next_to(num83, LEFT)
        digit3 = MathTex("3").set_color(YELLOW).next_to(num83, RIGHT)
        self.play(Write(digit8), Write(digit3))
        self.wait(0.5)

        comp_gt_83 = MathTex(">").set_color(GREEN).scale(1.5).move_to(ORIGIN)
        self.play(Write(comp_gt_83))
        self.wait(0.5)

        text_83 = Text("Tens > Units", font_size=24).next_to(comp_gt_83, DOWN)
        self.play(Write(text_83))
        self.wait(1)

        # Show 7 (one-digit)
        num7 = MathTex("7").scale(1.5).to_edge(RIGHT)
        self.play(Write(num7))
        self.wait(0.5)

        comp_false = MathTex("0 > 7").set_color(RED).scale(1.5).move_to(ORIGIN)
        self.play(Write(comp_false))
        self.wait(0.5)

        text_not_dapple_7 = Text("Not Dapple", font_size=24).next_to(comp_false, DOWN)
        self.play(Write(text_not_dapple_7))
        self.wait(1)

        # Show 98 as Dapple
        num98 = MathTex("98").scale(1.5).to_edge(LEFT)
        self.play(Write(num98))
        self.wait(0.5)

        digit9 = MathTex("9").set_color(YELLOW).next_to(num98, LEFT)
        digit8 = MathTex("8").set_color(YELLOW).next_to(num98, RIGHT)
        self.play(Write(digit9), Write(digit8))
        self.wait(0.5)

        comp_gt_98 = MathTex(">").set_color(GREEN).scale(1.5).move_to(ORIGIN)
        self.play(Write(comp_gt_98))
        self.wait(0.5)

        text_98 = Text("Tens > Units", font_size=24).next_to(comp_gt_98, DOWN)
        self.play(Write(text_98))
        self.wait(1)

        # Show 50 as Dapple
        num50 = MathTex("50").scale(1.5).to_edge(RIGHT)
        self.play(Write(num50))
        self.wait(0.5)

        digit5_50 = MathTex("5").set_color(YELLOW).next_to(num50, LEFT)
        digit0_50 = MathTex("0").set_color(YELLOW).next_to(num50, RIGHT)
        self.play(Write(digit5_50), Write(digit0_50))
        self.wait(0.5)

        comp_gt_50 = MathTex(">").set_color(GREEN).scale(1.5).move_to(ORIGIN)
        self.play(Write(comp_gt_50))
        self.wait(0.5)

        text_50 = Text("5 > 0", font_size=24).next_to(comp_gt_50, DOWN)
        self.play(Write(text_50))
        self.wait(1)

        # Show 77 as Not Dapple
        num77 = MathTex("77").scale(1.5).to_edge(LEFT)
        self.play(Write(num77))
        self.wait(0.5)

        eq_sign_77 = MathTex("=").set_color(RED).scale(1.5).move_to(ORIGIN)
        self.play(Write(eq_sign_77))
        self.wait(0.5)

        text_not_dapple_eq_77 = Text("Not Dapple (Tens = Units)", font_size=24).next_to(eq_sign_77, DOWN)
        self.play(Write(text_not_dapple_eq_77))
        self.wait(1)

        # Show 44 as Not Dapple
        num44 = MathTex("44").scale(1.5).to_edge(RIGHT)
        self.play(Write(num44))
        self.wait(0.5)

        eq_sign_44 = MathTex("=").set_color(RED).scale(1.5).move_to(ORIGIN)
        self.play(Write(eq_sign_44))
        self.wait(0.5)

        text_not_dapple_eq_44 = Text("Not Dapple (Tens = Units)", font_size=24).next_to(eq_sign_44, DOWN)
        self.play(Write(text_not_dapple_eq_44))
        self.wait(1)

        # Show 31 as Dapple, reverse to Not Dapple
        num31 = MathTex("31").set_color(GREEN).scale(1.5).to_edge(LEFT)
        self.play(Write(num31))
        self.wait(0.5)

        digit3_31 = MathTex("3").set_color(YELLOW).next_to(num31, LEFT)
        digit1_31 = MathTex("1").set_color(YELLOW).next_to(num31, RIGHT)
        self.play(Write(digit3_31), Write(digit1_31))
        self.wait(0.5)

        comp_gt_31 = MathTex(">").set_color(GREEN).scale(1.5).move_to(ORIGIN)
        self.play(Write(comp_gt_31))
        self.wait(0.5)

        text_31 = Text("Tens > Units", font_size=24).next_to(comp_gt_31, DOWN)
        self.play(Write(text_31))
        self.wait(1)

        # Reverse 31 to 13
        num13 = MathTex("13").set_color(RED).scale(1.5).move_to(ORIGIN)
        self.play(Transform(num31, num13))
        self.wait(0.5)

        digit1_13 = MathTex("1").set_color(YELLOW).next_to(num13, LEFT)
        digit3_13 = MathTex("3").set_color(YELLOW).next_to(num13, RIGHT)
        self.play(Write(digit1_13), Write(digit3_13))
        self.wait(0.5)

        comp_lt_13 = MathTex("<").set_color(RED).scale(1.5).move_to(ORIGIN)
        self.play(Write(comp_lt_13))
        self.wait(0.5)

        text_not_dapple_13 = Text("Not Dapple (1 < 3)", font_size=24).next_to(comp_lt_13, DOWN)
        self.play(Write(text_not_dapple_13))
        self.wait(1)

        # Show 63 example
        num63 = MathTex("63").scale(1.5).to_edge(LEFT)
        self.play(Write(num63))
        self.wait(0.5)

        digit6 = MathTex("6").set_color(YELLOW).next_to(num63, LEFT)
        digit3 = MathTex("3").set_color(YELLOW).next_to(num63, RIGHT)
        self.play(Write(digit6), Write(digit3))
        self.wait(0.5)

        comp_gt_63 = MathTex(">").set_color(GREEN).scale(1.5).move_to(ORIGIN)
        self.play(Write(comp_gt_63))
        self.wait(0.5)

        text_63 = Text("Tens > Units", font_size=24).next_to(comp_gt_63, DOWN)
        self.play(Write(text_63))
        self.wait(1)

        # Show 36 (reversed)
        num36 = MathTex("36").scale(1.5).move_to(ORIGIN)
        self.play(Transform(num63, num36))
        self.wait(0.5)

        digit3_36 = MathTex("3").set_color(YELLOW).next_to(num36, LEFT)
        digit6_36 = MathTex("6").set_color(YELLOW).next_to(num36, RIGHT)
        self.play(Write(digit3_36), Write(digit6_36))
        self.wait(0.5)

        comp_lt_36 = MathTex("<").set_color(RED).scale(1.5).move_to(ORIGIN)
        self.play(Write(comp_lt_36))
        self.wait(0.5)

        text_conclusion = Text("X > Y", font_size=24).next_to(comp_lt_36, DOWN)
        self.play(Write(text_conclusion))
        self.wait(1)

        # Show 0
        num0 = MathTex("0").scale(1.5).to_edge(RIGHT)
        self.play(Write(num0))
        self.wait(0.5)

        text_not_dapple_0 = Text("Not Dapple", font_size=24).next_to(num0, DOWN)
        self.play(Write(text_not_dapple_0))
        self.wait(1)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(num52), FadeOut(num25), FadeOut(arrow), FadeOut(rev_text),
                  FadeOut(num32), FadeOut(digit3), FadeOut(digit2), FadeOut(comp_gt), FadeOut(text_gt),
                  FadeOut(num10), FadeOut(digit1), FadeOut(digit0), FadeOut(comp_gt_10), FadeOut(text_10),
                  FadeOut(num11), FadeOut(eq_sign), FadeOut(text_not_dapple_eq),
                  FadeOut(num83), FadeOut(digit8), FadeOut(digit3), FadeOut(comp_gt_83), FadeOut(text_83),
                  FadeOut(num7), FadeOut(comp_false), FadeOut(text_not_dapple_7),
                  FadeOut(num98), FadeOut(digit9), FadeOut(digit8), FadeOut(comp_gt_98), FadeOut(text_98),
                  FadeOut(num50), FadeOut(digit5_50), FadeOut(digit0_50), FadeOut(comp_gt_50), FadeOut(text_50),
                  FadeOut(num77), FadeOut(eq_sign_77), FadeOut(num44), FadeOut(eq_sign_44),
                  FadeOut(num31), FadeOut(digit3_31), FadeOut(digit1_31), FadeOut(comp_gt_31), FadeOut(text_31),
                  FadeOut(num13), FadeOut(digit1_13), FadeOut(digit3_13), FadeOut(comp_lt_13), FadeOut(text_not_dapple_13),
                  FadeOut(num63), FadeOut(digit6), FadeOut(digit3), FadeOut(comp_gt_63), FadeOut(text_63),
                  FadeOut(num36), FadeOut(digit3_36), FadeOut(digit6_36), FadeOut(comp_lt_36), FadeOut(text_conclusion),
                  FadeOut(num0), FadeOut(text_not_dapple_0))
        self.wait(0.5)
