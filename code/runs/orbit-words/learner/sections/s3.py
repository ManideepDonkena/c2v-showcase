from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Orbit Words: Growth by Simultaneous Rewriting", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial word
        word1 = Text("XYY", font_size=40)
        word1.move_to(ORIGIN)
        self.play(Write(word1))
        self.wait(1)

        # Arrows and transformations
        # X -> XYY
        x_arrow = Arrow(start=word1[0].get_left(), end=word1[0].get_left() + LEFT * 1.5, buff=0.1)
        x_text = Text("X", font_size=24).next_to(x_arrow, DOWN)

        # Y -> YX
        y1_arrow = Arrow(start=word1[1].get_right(), end=word1[1].get_right() + RIGHT * 1.5, buff=0.1)
        y1_text = Text("Y", font_size=24).next_to(y1_arrow, DOWN)

        y2_arrow = Arrow(start=word1[2].get_right(), end=word1[2].get_right() + RIGHT * 1.5, buff=0.1)
        y2_text = Text("Y", font_size=24).next_to(y2_arrow, DOWN)

        self.play(GrowArrow(x_arrow), Write(x_text))
        self.wait(0.5)
        self.play(GrowArrow(y1_arrow), Write(y1_text))
        self.wait(0.5)
        self.play(GrowArrow(y2_arrow), Write(y2_text))
        self.wait(0.5)

        # Show transformations
        xyy = Text("XYY", font_size=30).next_to(word1, DOWN, buff=0.5)
        yx1 = Text("YX", font_size=30).next_to(xyy, RIGHT, buff=0.2)
        yx2 = Text("YX", font_size=30).next_to(yx1, RIGHT, buff=0.2)

        self.play(Write(xyy))
        self.wait(0.5)
        self.play(Write(yx1))
        self.wait(0.5)
        self.play(Write(yx2))
        self.wait(0.5)

        # Concatenate
        final_word = Text("XYYYXYX", font_size=40)
        final_word.next_to(word1, DOWN, buff=1.5)
        self.play(Write(final_word))
        self.wait(1)

        # Highlight first character of result
        highlight = SurroundingRectangle(final_word[0], color=YELLOW, buff=0.1)
        self.play(Create(highlight))
        self.wait(0.5)
        self.play(FadeOut(highlight))

        # Show arrow from original X to new X
        arrow_from_start = Arrow(
            start=word1[0].get_top(),
            end=final_word[0].get_top(),
            color=GREEN,
            buff=0.1
        )
        self.play(GrowArrow(arrow_from_start))
        self.wait(1)

        # Narration text
        narration = Text("Now rewrite every letter in XYY at once.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        narration2 = Text("The X becomes XYY, and each Y becomes YX.", font_size=24)
        narration2.to_edge(DOWN)
        self.play(ReplacementTransform(narration, narration2))
        self.wait(1.5)
        self.play(FadeOut(narration2))

        narration3 = Text("Concatenating gives us: XYYYXYX", font_size=24)
        narration3.to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(1.5)
        self.play(FadeOut(narration3))

        # Cleanup
        self.play(
            FadeOut(word1),
            FadeOut(x_arrow),
            FadeOut(y1_arrow),
            FadeOut(y2_arrow),
            FadeOut(x_text),
            FadeOut(y1_text),
            FadeOut(y2_text),
            FadeOut(xyy),
            FadeOut(yx1),
            FadeOut(yx2),
            FadeOut(final_word),
            FadeOut(arrow_from_start),
            FadeOut(title)
        )
        self.wait(0.5)
