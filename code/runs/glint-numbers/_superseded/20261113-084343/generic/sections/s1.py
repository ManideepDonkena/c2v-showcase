from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Glint Numbers", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Number 21 appears center screen
        num_21 = Integer(21, font_size=60).move_to(ORIGIN)
        self.play(Write(num_21))
        self.wait(0.5)

        # Highlight last digit '1' in green
        last_digit = num_21[-1]
        self.play(last_digit.animate.set_color(GREEN), run_time=0.5)
        self.wait(0.5)

        # Fade rest of number slightly
        rest_of_num = VGroup(*[num_21[i] for i in range(len(num_21)-1)])
        self.play(rest_of_num.animate.set_opacity(0.5), run_time=0.5)
        self.wait(0.5)

        # Definition text below
        definition = Text("Glint Number: Last digit ≠ 0 AND Number ÷ Last Digit = Whole", font_size=24).next_to(num_21, DOWN, buff=0.5)
        self.play(Write(definition))
        self.wait(0.5)

        # Checkmark animation
        checkmark = Tex(r"$\checkmark$").scale(1.5).next_to(num_21, RIGHT, buff=0.5)
        self.play(Write(checkmark))
        self.wait(1)

        # Narration key words
        narration1 = Text("Glint number", font_size=24).to_edge(DOWN).shift(UP * 0.5)
        narration2 = Text("ending in 1", font_size=24).next_to(narration1, RIGHT, buff=0.5)
        self.play(Write(narration1))
        self.wait(0.5)
        self.play(Write(narration2))
        self.wait(1)

        # Clear narration
        self.play(FadeOut(narration1), FadeOut(narration2))

        # Show rules
        rule1 = Text("Rule 1: Every number ending in 1 is glint", font_size=24).to_edge(DOWN)
        self.play(Write(rule1))
        self.wait(1.5)

        # Clear rule 1
        self.play(FadeOut(rule1))

        # Show worked example
        example = Text("Example: 24 ÷ 4 = 6 → Glint", font_size=24).to_edge(DOWN)
        self.play(Write(example))
        self.wait(1.5)

        # Clear example
        self.play(FadeOut(example))

        # Show another example (not glint)
        not_glint = Text("Example: 26 ÷ 6 ≠ Whole → Not Glint", font_size=24).to_edge(DOWN)
        self.play(Write(not_glint))
        self.wait(1.5)

        # Clear
        self.play(FadeOut(not_glint))

        # Final rule summary
        final_rules = VGroup(
            Text("Rules:", font_size=24),
            Text("(1) Every number ending in 1 is glint", font_size=20),
            Text("(2) A number ending in 0 is never glint", font_size=20),
            Text("(3) A number ending in 5 is always glint", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT).shift(UP * 0.5)

        self.play(Write(final_rules))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(final_rules), FadeOut(num_21), FadeOut(last_digit), FadeOut(definition), FadeOut(checkmark), FadeOut(title))
        self.wait(0.5)
