from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Glint Numbers", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 21 as example
        num_21 = MathTex("21").scale(2).move_to(ORIGIN)
        self.play(Write(num_21))
        self.wait(0.5)

        # Highlight last digit '1' in green
        if len(num_21) > 1:
            digit_1 = num_21[1].copy()
            self.play(
                digit_1.animate.set_color(GREEN),
                num_21[0].animate.set_opacity(0.5)
            )
            self.wait(0.5)
        
        # Definition text
        definition = Text("Glint Number: Last digit ≠ 0 AND Number ÷ Last Digit = Whole", font_size=24).next_to(num_21, DOWN, buff=0.5)
        self.play(Write(definition))
        self.wait(0.5)

        # Checkmark
        check = Tex(r"$\checkmark$").scale(1.5).next_to(definition, RIGHT, buff=0.5)
        self.play(Write(check))
        self.wait(1)

        # Rule 1: Every number ending in 1 is glint
        rule1 = Text("Rule 1: Every number ending in 1 is a Glint number", font_size=24).to_edge(DOWN)
        self.play(Write(rule1))
        self.wait(1.5)

        # Fade out rule 1 and definition
        self.play(FadeOut(rule1), FadeOut(definition), FadeOut(check))

        # Show 30 is NOT glint
        num_30 = MathTex("30").scale(2).move_to(ORIGIN)
        self.play(ReplacementTransform(num_21, num_30))
        self.wait(0.5)

        if len(num_30) > 1:
            digit_0 = num_30[1].copy()
            self.play(
                digit_0.animate.set_color(RED),
                num_30[0].animate.set_opacity(0.5)
            )
            self.wait(0.5)

        rule2 = Text("Rule 2: A number ending in 0 is never a Glint number", font_size=24).next_to(num_30, DOWN, buff=0.5)
        self.play(Write(rule2))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(num_30), FadeOut(rule2))

        # Show 48 is glint
        num_48 = MathTex("48").scale(2).move_to(ORIGIN)
        self.play(Write(num_48))
        self.wait(0.5)

        if len(num_48) > 2:
            digit_8 = num_48[1].copy()
            self.play(
                digit_8.animate.set_color(GREEN),
                num_48[0].animate.set_opacity(0.5),
                num_48[1].animate.set_opacity(0.5)
            )
            self.wait(0.5)

        check2 = Tex(r"$\checkmark$").scale(1.5).next_to(num_48, RIGHT, buff=0.5)
        self.play(Write(check2))
        self.wait(0.5)

        # Show 49 is NOT glint
        num_49 = MathTex("49").scale(2).move_to(ORIGIN)
        self.play(ReplacementTransform(num_48, num_49))
        self.wait(0.5)

        if len(num_49) > 2:
            digit_9 = num_49[1].copy()
            self.play(
                digit_9.animate.set_color(RED),
                num_49[0].animate.set_opacity(0.5),
                num_49[1].animate.set_opacity(0.5)
            )
            self.wait(0.5)

        # Final rule: 5 is always glint
        rule3 = Text("Rule 3: A number ending in 5 is always a Glint number", font_size=24).next_to(num_49, DOWN, buff=0.5)
        self.play(Write(rule3))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(num_49), FadeOut(rule3), FadeOut(check2))

        # Final summary
        final = Text("Glint Number Rules:", font_size=24).to_edge(UP)
        final.shift(0.0 * RIGHT + 0.41 * UP)  # layout: separation vector
        self.play(Write(final))
        self.wait(0.5)

        rule_list = VGroup(
            Text("1. Every number ending in 1 is glint", font_size=20),
            Text("2. A number ending in 0 is never glint", font_size=20),
            Text("3. A number ending in 5 is always glint", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(final, DOWN, buff=0.5)

        rule_list.shift(0.0 * RIGHT + -0.19 * UP)  # layout: separation vector
        self.play(Write(rule_list))
        self.wait(1.5)

        self.play(FadeOut(final), FadeOut(rule_list))
        self.wait(0.5)
