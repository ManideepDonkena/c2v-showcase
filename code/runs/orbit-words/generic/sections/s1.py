from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Origin and the Rule", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial X
        x_letter = Tex(r"$X$", font_size=120)
        x_letter.move_to(ORIGIN)
        self.play(FadeIn(x_letter))
        self.wait(1)

        # Arrows and labels
        arrow1 = Arrow(start=DOWN*0.5, end=UP*0.5, color=BLUE)
        arrow1.next_to(x_letter, UP)
        rule1 = MathTex(r"X \rightarrow XYY", color=BLUE, font_size=36)
        rule1.next_to(arrow1, UP)

        arrow2 = Arrow(start=DOWN*0.5, end=UP*0.5, color=GREEN)
        arrow2.next_to(x_letter, DOWN)
        rule2 = MathTex(r"Y \rightarrow YX", color=GREEN, font_size=36)
        rule2.next_to(arrow2, DOWN)

        self.play(GrowArrow(arrow1), Write(rule1))
        self.wait(1)
        self.play(GrowArrow(arrow2), Write(rule2))
        self.wait(1.5)

        # Simultaneous Rewrite pulse
        simultaneous = Text("Simultaneous Rewrite", font_size=36, color=YELLOW)
        simultaneous.to_edge(UP)
        simultaneous.shift(0.0 * RIGHT + -0.65 * UP)  # layout: separation vector
        self.play(FadeIn(simultaneous))
        self.wait(0.5)
        self.play(FadeOut(simultaneous))

        # Narration text
        narration1 = Text("An orbit word begins with a single letter, X.", font_size=24)
        narration1.to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(2)

        self.play(FadeOut(narration1))

        narration2 = Text("To grow, we rewrite every letter at the same time:", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(2)

        self.play(FadeOut(narration2))

        narration3 = Text("replace each X with XYY, and each Y with YX.", font_size=24)
        narration3.to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(2.5)

        self.play(FadeOut(narration3))

        # Show the rules clearly
        rule_text = Text("Rules:", font_size=30)
        rule_text.to_corner(UL)
        self.play(Write(rule_text))
        self.wait(1)

        rule1_text = Text("1. Every orbit word starts with X.", font_size=24)
        rule1_text.next_to(rule_text, DOWN, aligned_edge=LEFT)
        self.play(Write(rule1_text))
        self.wait(1.5)

        rule2_text = Text("2. Each rewrite makes the word longer.", font_size=24)
        rule2_text.next_to(rule1_text, DOWN, aligned_edge=LEFT)
        self.play(Write(rule2_text))
        self.wait(1.5)

        # Worked example
        example = MathTex(r"X \rightarrow XYY \rightarrow XYYYXYX", font_size=36)
        example.to_edge(DOWN)
        self.play(Write(example))
        self.wait(2.5)

        # Fade out everything
        self.play(
            FadeOut(x_letter),
            FadeOut(arrow1),
            FadeOut(rule1),
            FadeOut(arrow2),
            FadeOut(rule2),
            FadeOut(rule_text),
            FadeOut(rule1_text),
            FadeOut(rule2_text),
            FadeOut(example),
            FadeOut(title)
        )
        self.wait(0.5)
