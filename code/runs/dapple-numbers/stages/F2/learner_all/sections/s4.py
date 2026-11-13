from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Reversal Property", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 52 as Dapple, reverse to 25 as Not Dapple
        num52 = MathTex("52").set_color(GREEN).scale(1.5)
        num52.next_to(title, DOWN, buff=0.5)
        self.play(Write(num52))
        self.wait(0.5)

        # Split into digits
        digit5 = MathTex("5").set_color(GREEN).scale(1.5)
        digit2 = MathTex("2").set_color(GREEN).scale(1.5)
        digit5.next_to(num52, LEFT, buff=0.2)
        digit2.next_to(num52, RIGHT, buff=0.2)
        self.play(Write(digit5), Write(digit2))
        self.wait(0.5)

        # Swap positions
        num25 = MathTex("25").set_color(RED).scale(1.5)
        num25.next_to(title, DOWN, buff=0.5)
        self.play(Transform(num52, num25))
        self.wait(0.5)

        # Label as Not Dapple
        not_dapple = Text("Not Dapple", font_size=24).set_color(RED).next_to(num25, DOWN)
        self.play(Write(not_dapple))
        self.wait(0.5)

        # Arrow and text
        arrow = Arrow(start=num52.get_left(), end=num25.get_right(), buff=0.1)
        reversal_text = Text("Reversal", font_size=24).next_to(arrow, UP)
        self.play(GrowArrow(arrow), Write(reversal_text))
        self.wait(1)

        # Fade out
        self.play(FadeOut(num52), FadeOut(digit5), FadeOut(digit2), FadeOut(not_dapple), FadeOut(arrow), FadeOut(reversal_text))

        # Show 32, compare digits
        num32 = MathTex("32").scale(1.5)
        self.play(Write(num32))
        self.wait(0.5)

        digit3 = MathTex("3").set_color(YELLOW).scale(1.5)
        digit2 = MathTex("2").set_color(YELLOW).scale(1.5)
        digit3.next_to(num32, LEFT, buff=0.2)
        digit2.next_to(num32, RIGHT, buff=0.2)
        self.play(Write(digit3), Write(digit2))
        self.wait(0.5)

        greater = MathTex(">").set_color(GREEN).scale(1.5)
        greater.next_to(digit3, buff=0.2)
        self.play(Write(greater))
        self.wait(0.5)

        text_greater = Text("Tens > Units", font_size=24).next_to(greater, DOWN)
        self.play(Write(text_greater))
        self.wait(1)

        # Fade out
        self.play(FadeOut(num32), FadeOut(digit3), FadeOut(digit2), FadeOut(greater), FadeOut(text_greater))

        # Show 10 is Dapple
        num10 = MathTex("10").scale(1.5)
        self.play(Write(num10))
        self.wait(0.5)

        digit1 = MathTex("1").set_color(YELLOW).scale(1.5)
        digit0 = MathTex("0").set_color(YELLOW).scale(1.5)
        digit1.next_to(num10, LEFT, buff=0.2)
        digit0.next_to(num10, RIGHT, buff=0.2)
        self.play(Write(digit1), Write(digit0))
        self.wait(0.5)

        greater10 = MathTex(">").set_color(GREEN).scale(1.5)
        greater10.next_to(digit1, buff=0.2)
        self.play(Write(greater10))
        self.wait(0.5)

        text_10 = Text("1 > 0", font_size=24).next_to(greater10, DOWN)
        self.play(Write(text_10))
        self.wait(1)

        # Show 11 is Not Dapple
        num11 = MathTex("11").set_color(RED).scale(1.5)
        num11.next_to(num10, RIGHT, buff=1)
        self.play(Transform(num10, num11))
        self.wait(0.5)

        equal = MathTex("=").set_color(RED).scale(1.5)
        equal.next_to(digit1, buff=0.2)
        self.play(Write(equal))
        self.wait(0.5)

        not_dapple_11 = Text("Not Dapple (Tens = Units)", font_size=24).set_color(RED).next_to(num11, DOWN)
        self.play(Write(not_dapple_11))
        self.wait(1)

        # Fade out
        self.play(FadeOut(num10), FadeOut(digit1), FadeOut(digit0), FadeOut(greater10), FadeOut(text_10), FadeOut(equal), FadeOut(not_dapple_11))

        # Show 83 is Dapple
        num83 = MathTex("83").scale(1.5)
        self.play(Write(num83))
        self.wait(0.5)

        digit8 = MathTex("8").set_color(YELLOW).scale(1.5)
        digit3 = MathTex("3").set_color(YELLOW).scale(1.5)
        digit8.next_to(num83, LEFT, buff=0.2)
        digit3.next_to(num83, RIGHT, buff=0.2)
        self.play(Write(digit8), Write(digit3))
        self.wait(0.5)

        greater83 = MathTex(">").set_color(GREEN).scale(1.5)
        greater83.next_to(digit8, buff=0.2)
        self.play(Write(greater83))
        self.wait(0.5)

        text_83 = Text("Tens > Units", font_size=24).next_to(greater83, DOWN)
        self.play(Write(text_83))
        self.wait(1)

        # Fade out
        self.play(FadeOut(num83), FadeOut(digit8), FadeOut(digit3), FadeOut(greater83), FadeOut(text_83))

        # Show 7 is Not Dapple
        num7 = MathTex("7").scale(1.5)
        self.play(Write(num7))
        self.wait(0.5)

        zero = MathTex("0").set_color(YELLOW).scale(1.5)
        seven = MathTex("7").set_color(YELLOW).scale(1.5)
        zero.next_to(num7, LEFT, buff=0.2)
        seven.next_to(num7, RIGHT, buff=0.2)
        self.play(Write(zero), Write(seven))
        self.wait(0.5)

        less = MathTex("<").set_color(RED).scale(1.5)
        less.next_to(zero, buff=0.2)
        self.play(Write(less))
        self.wait(0.5)

        not_dapple_7 = Text("Not Dapple (0 < 7)", font_size=24).set_color(RED).next_to(num7, DOWN)
        self.play(Write(not_dapple_7))
        self.wait(1)

        # Fade out
        self.play(FadeOut(num7), FadeOut(zero), FadeOut(seven), FadeOut(less), FadeOut(not_dapple_7))

        # Show 98 is Dapple
        num98 = MathTex("98").scale(1.5)
        self.play(Write(num98))
        self.wait(0.5)

        digit9 = MathTex("9").set_color(YELLOW).scale(1.5)
        digit8 = MathTex("8").set_color(YELLOW).scale(1.5)
        digit9.next_to(num98, LEFT, buff=0.2)
        digit8.next_to(num98, RIGHT, buff=0.2)
        self.play(Write(digit9), Write(digit8))
        self.wait(0.5)

        greater98 = MathTex(">").set_color(GREEN).scale(1.5)
        greater98.next_to(digit9, buff=0.2)
        self.play(Write(greater98))
        self.wait(0.5)

        text_98 = Text("Tens > Units", font_size=24).next_to(greater98, DOWN)
        self.play(Write(text_98))
        self.wait(1)

        # Fade out
        self.play(FadeOut(num98), FadeOut(digit9), FadeOut(digit8), FadeOut(greater98), FadeOut(text_98))

        # Show 50 is Dapple
        num50 = MathTex("50").scale(1.5)
        self.play(Write(num50))
        self.wait(0.5)

        digit50 = MathTex("5").set_color(YELLOW).scale(1.5)
        digit00 = MathTex("0").set_color(YELLOW).scale(1.5)
        digit50.next_to(num50, LEFT, buff=0.2)
        digit00.next_to(num50, RIGHT, buff=0.2)
        self.play(Write(digit50), Write(digit00))
        self.wait(0.5)

        greater50 = MathTex(">").set_color(GREEN).scale(1.5)
        greater50.next_to(digit50, buff=0.2)
        self.play(Write(greater50))
        self.wait(0.5)

        text_50 = Text("5 > 0", font_size=24).next_to(greater50, DOWN)
        self.play(Write(text_50))
        self.wait(1)

        # Fade out
        self.play(FadeOut(num50), FadeOut(digit50), FadeOut(digit00), FadeOut(greater50), FadeOut(text_50))

        # Show 77 is Not Dapple
        num77 = MathTex("77").scale(1.5)
        self.play(Write(num77))
        self.wait(0.5)

        equal77 = MathTex("=").set_color(RED).scale(1.5)
        equal77.next_to(digit50, buff=0.2)
        self.play(Write(equal77))
        self.wait(0.5)

        not_dapple_77 = Text("Not Dapple (Tens = Units)", font_size=24).set_color(RED).next_to(num77, DOWN)
        self.play(Write(not_dapple_77))
        self.wait(1)

        # Fade out
        self.play(FadeOut(num77), FadeOut(equal77), FadeOut(not_dapple_77))

        # Show 44 is Not Dapple
        num44 = MathTex("44").scale(1.5)
        self.play(Write(num44))
        self.wait(0.5)

        equal44 = MathTex("=").set_color(RED).scale(1.5)
        equal44.next_to(digit50, buff=0.2)
        self.play(Write(equal44))
        self.wait(0.5)

        not_dapple_44 = Text("Not Dapple (Tens = Units)", font_size=24).set_color(RED).next_to(num44, DOWN)
        self.play(Write(not_dapple_44))
        self.wait(1)

        # Fade out
        self.play(FadeOut(num44), FadeOut(equal44), FadeOut(not_dapple_44))

        # Show 31 is Dapple and reverse to Not Dapple
        num31 = MathTex("31").set_color(GREEN).scale(1.5)
        self.play(Write(num31))
        self.wait(0.5)

        digit31 = MathTex("3").set_color(YELLOW).scale(1.5)
        digit11 = MathTex("1").set_color(YELLOW).scale(1.5)
        digit31.next_to(num31, LEFT, buff=0.2)
        digit11.next_to(num31, RIGHT, buff=0.2)
        self.play(Write(digit31), Write(digit11))
        self.wait(0.5)

        greater31 = MathTex(">").set_color(GREEN).scale(1.5)
        greater31.next_to(digit31, buff=0.2)
        self.play(Write(greater31))
        self.wait(0.5)

        text_31 = Text("Dapple", font_size=24).next_to(num31, DOWN)
        self.play(Write(text_31))
        self.wait(1)

        # Reverse
        num13 = MathTex("13").set_color(RED).scale(1.5)
        num13.next_to(num31, RIGHT, buff=1)
        self.play(Transform(num31, num13))
        self.wait(0.5)

        less13 = MathTex("<").set_color(RED).scale(1.5)
        less13.next_to(digit11, buff=0.2)
        self.play(Write(less13))
        self.wait(0.5)

        not_dapple_13 = Text("Not Dapple (1 < 3)", font_size=24).set_color(RED).next_to(num13, DOWN)
        self.play(Write(not_dapple_13))
        self.wait(1)

        # Fade out
        self.play(FadeOut(num31), FadeOut(digit31), FadeOut(digit11), FadeOut(greater31), FadeOut(text_31), FadeOut(less13), FadeOut(not_dapple_13))

        # Show 63 example
        num63 = MathTex("63").set_color(GREEN).scale(1.5)
        self.play(Write(num63))
        self.wait(0.5)

        digit6 = MathTex("6").set_color(YELLOW).scale(1.5)
        digit3 = MathTex("3").set_color(YELLOW).scale(1.5)
        digit6.next_to(num63, LEFT, buff=0.2)
        digit3.next_to(num63, RIGHT, buff=0.2)
        self.play(Write(digit6), Write(digit3))
        self.wait(0.5)

        greater63 = MathTex(">").set_color(GREEN).scale(1.5)
        greater63.next_to(digit6, buff=0.2)
        self.play(Write(greater63))
        self.wait(0.5)

        text_63 = Text("Tens > Units", font_size=24).next_to(greater63, DOWN)
        self.play(Write(text_63))
        self.wait(1)

        # Reverse to 36
        num36 = MathTex("36").set_color(RED).scale(1.5)
        num36.next_to(num63, RIGHT, buff=1)
        self.play(Transform(num63, num36))
        self.wait(0.5)

        less36 = MathTex("<").set_color(RED).scale(1.5)
        less36.next_to(digit3, buff=0.2)
        self.play(Write(less36))
        self.wait(0.5)

        text_conclude = Text("X > Y", font_size=24).next_to(num36, DOWN)
        self.play(Write(text_conclude))
        self.wait(1)

        # Fade out
        self.play(FadeOut(num63), FadeOut(digit6), FadeOut(digit3), FadeOut(greater63), FadeOut(text_63), FadeOut(less36), FadeOut(text_conclude))

        # Show 0 is Not Dapple
        num0 = MathTex("0").scale(1.5)
        self.play(Write(num0))
        self.wait(0.5)

        not_dapple_0 = Text("Not Dapple (no tens digit)", font_size=24).set_color(RED).next_to(num0, DOWN)
        self.play(Write(not_dapple_0))
        self.wait(1)

        # Fade out
        self.play(FadeOut(num0), FadeOut(not_dapple_0))

        self.wait(0.5)
