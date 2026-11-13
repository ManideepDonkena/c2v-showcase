from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Origin and the Rule", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial 'X'
        x_letter = Text("X", font_size=120)
        x_letter.move_to(ORIGIN)
        self.play(FadeIn(x_letter))
        self.wait(1)

        # Arrows and rules
        blue_arrow = Arrow(start=LEFT, end=RIGHT, color=BLUE, buff=0.5)
        green_arrow = Arrow(start=LEFT, end=RIGHT, color=GREEN, buff=0.5)
        
        blue_label = MathTex("X \\rightarrow XYY", color=BLUE, font_size=36)
        green_label = MathTex("Y \\rightarrow YX", color=GREEN, font_size=36)

        # Position arrows and labels
        blue_arrow.next_to(x_letter, UP, buff=0.5)
        blue_label.next_to(blue_arrow, UP, buff=0.2)
        
        green_arrow.next_to(x_letter, DOWN, buff=0.5)
        green_label.next_to(green_arrow, DOWN, buff=0.2)

        self.play(GrowArrow(blue_arrow), Write(blue_label))
        self.wait(1)
        self.play(GrowArrow(green_arrow), Write(green_label))
        self.wait(1.5)

        # Simultaneous Rewrite pulse
        simultaneous = Text("Simultaneous Rewrite", font_size=32)
        simultaneous.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(simultaneous))
        self.play(simultaneous.animate.set_opacity(0.5))
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

        # Example: X -> XYY
        example1 = Text("X → XYY", font_size=30)
        example1.to_edge(DOWN, buff=0.8)
        self.play(Write(example1))
        self.wait(1.5)
        self.play(FadeOut(example1))

        # Example: XYY -> XYYYXYX
        example2 = Text("XYY → XYYYXYX", font_size=30)
        example2.to_edge(DOWN, buff=0.8)
        self.play(Write(example2))
        self.wait(2)
        self.play(FadeOut(example2))

        # Fade out everything except title and initial 'X'
        self.play(
            FadeOut(blue_arrow),
            FadeOut(green_arrow),
            FadeOut(blue_label),
            FadeOut(green_label),
            FadeOut(x_letter),
            FadeOut(title)
        )
