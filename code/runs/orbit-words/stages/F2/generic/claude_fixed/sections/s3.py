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
        word1.next_to(title, DOWN, buff=0.5)
        self.play(Write(word1))
        self.wait(1)

        # Show transformation rules
        rule1 = MathTex("X \\to XYY", font_size=36)
        rule2 = MathTex("Y \\to YX", font_size=36)
        rules = VGroup(rule1, rule2).arrange(DOWN, buff=0.3)
        rules.next_to(word1, DOWN, buff=0.8)
        self.play(Write(rule1), Write(rule2))
        self.wait(1.5)

        # Show each letter transformation
        x_part = Text("X", font_size=40).set_color(BLUE)
        y1_part = Text("Y", font_size=40).set_color(GREEN)
        y2_part = Text("Y", font_size=40).set_color(GREEN)

        parts = VGroup(x_part, y1_part, y2_part)
        parts.arrange(RIGHT, buff=0.5)
        parts.move_to(word1)

        # Fade out original word
        self.play(FadeOut(word1), FadeIn(parts))

        # Transform each letter
        x_new = Text("XYY", font_size=40).set_color(BLUE)
        y1_new = Text("YX", font_size=40).set_color(GREEN)
        y2_new = Text("YX", font_size=40).set_color(GREEN)
        new_parts = VGroup(x_new, y1_new, y2_new).arrange(RIGHT, buff=0.5)
        new_parts.next_to(rules, DOWN, buff=0.6)

        # Animate transformations
        self.play(ReplacementTransform(x_part, x_new))
        self.play(ReplacementTransform(y1_part, y1_new))
        self.play(ReplacementTransform(y2_part, y2_new))

        # Combine into new word
        final_word = Text("XYYYXYX", font_size=40)
        final_word.next_to(new_parts, DOWN, buff=0.6)
        self.play(Write(final_word))
        self.wait(1.5)

        # Narration text
        narration = Text("Now rewrite every letter in XYY at once.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)

        narration2 = Text("The X becomes XYY, and each Y becomes YX.", font_size=24)
        narration2.to_edge(DOWN)
        self.play(ReplacementTransform(narration, narration2))
        self.wait(1.5)

        narration3 = Text("Concatenating these gives us the new orbit word: XYYYXYX.", font_size=24)
        narration3.to_edge(DOWN)
        self.play(ReplacementTransform(narration2, narration3))
        self.wait(2)
        self.play(FadeOut(narration3))

        # Clean up
        self.play(FadeOut(title), FadeOut(rules), FadeOut(new_parts), FadeOut(final_word))
        self.wait(0.5)
