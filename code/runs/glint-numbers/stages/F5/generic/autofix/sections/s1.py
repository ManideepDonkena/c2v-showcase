from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Glint Numbers", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Number 21 centered
        num = MathTex("21").scale(3).move_to(ORIGIN)
        self.play(Write(num))
        self.wait(0.5)

        # Highlight last digit '1' in green and fade rest
        num_copy = num.copy()
        num_copy[0][1].set_color(GREEN)  # '1' in 21
        num_copy[0][:1].set_opacity(0.3)  # '2' in 21
        self.play(Transform(num, num_copy))
        self.wait(0.5)

        # Definition text
        definition = Text("Glint Number: Last digit ≠ 0 AND Number ÷ Last Digit = Whole", font_size=24)
        definition.next_to(num, DOWN, buff=0.5)
        self.play(Write(definition))
        self.wait(0.5)

        # Checkmark animation
        check = Tex(r"$\checkmark$").scale(2).next_to(definition, RIGHT, buff=0.5)
        self.play(Write(check))
        self.wait(1)

        # Narration text (key words)
        narration = Text("We define a Glint number as a whole number ending in a non-zero digit that divides itself evenly.", font_size=20).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        # Fade out narration
        self.play(FadeOut(narration))

        # New narration text
        narration2 = Text("For instance, every number ending in 1 is automatically a Glint number.", font_size=20).to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(2)

        # Fade out narration and definition
        self.play(FadeOut(narration2, definition, check))

        # Show rule: "Every number ending in 1 is glint"
        rule = Text("Rule 1: Every number ending in 1 is glint", font_size=24).move_to(ORIGIN)
        rule.shift(0.0 * RIGHT + 0.82 * UP)  # layout: separation vector
        self.play(Write(rule))
        self.wait(1.5)

        # Fade out rule
        self.play(FadeOut(rule))

        # Show example: 24 is glint because 24 ÷ 4 = 6
        example = MathTex("24 \\div 4 = 6").scale(1.5).move_to(ORIGIN)
        example.shift(0.0 * RIGHT + 0.91 * UP)  # layout: separation vector
        self.play(Write(example))
        self.wait(1.5)

        # Fade out example
        self.play(FadeOut(example))

        # Show example: 26 is not glint because 26 ÷ 6 is not whole
        not_glint = MathTex("26 \\div 6 = 4.33...").scale(1.5).move_to(ORIGIN)
        not_glint.shift(0.0 * RIGHT + 0.91 * UP)  # layout: separation vector
        self.play(Write(not_glint))
        self.wait(1.5)

        # Fade out example
        self.play(FadeOut(not_glint))

        # Final fade out
        self.play(FadeOut(num, title))
        self.wait(0.5)
