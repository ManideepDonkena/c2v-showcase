from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Orbit Words: Growth by Simultaneous Rewriting", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial word
        word1 = Text("XYY", font_size=40)
        word1.next_to(title, DOWN, buff=0.5)
        self.play(Write(word1))
        self.wait(1)

        # Transformation rules
        rule1 = MathTex("X \\to XYY", font_size=32)
        rule2 = MathTex("Y \\to YX", font_size=32)
        rules = VGroup(rule1, rule2).arrange(DOWN, buff=0.3)
        rules.next_to(word1, DOWN, buff=0.5)
        self.play(Write(rule1), Write(rule2))
        self.wait(1)

        # Show transformation of each letter
        xyy_parts = [Text("X", font_size=40), Text("Y", font_size=40), Text("Y", font_size=40)]
        xyy_parts[0].move_to(word1[0])
        xyy_parts[1].move_to(word1[1])
        xyy_parts[2].move_to(word1[2])

        # Transform each letter
        self.play(Transform(word1[0], xyy_parts[0]),
                  Transform(word1[1], xyy_parts[1]),
                  Transform(word1[2], xyy_parts[2]))
        self.wait(1)
        self.play(Transform(word1[0], xyy_parts[0]),
                  Transform(word1[1], xyy_parts[1]),
                  Transform(word1[2], xyy_parts[2]))
        self.wait(1)
        self.play(Transform(word1[0], xyy_parts[0]),
                  Transform(word1[1], xyy_parts[1]),
                  Transform(word1[2], xyy_parts[2]))
        self.wait(1)
        self.play(
            Transform(xyy_parts[0], Text("XYY", font_size=40)),
            Transform(xyy_parts[1], Text("YX", font_size=40)),
            Transform(xyy_parts[2], Text("YX", font_size=40)),
        )
        self.wait(1)

        # Concatenate
        new_word = Text("XYYYXYX", font_size=40)
        new_word.next_to(rules, DOWN, buff=0.5)
        self.play(Write(new_word))
        self.wait(1)

        # Highlight first letter transformation
        arrow = Arrow(start=new_word[0].get_left(), end=new_word[0].get_left() + LEFT * 0.5, buff=0.1)
        arrow_label = Text("X", font_size=24).next_to(arrow, LEFT)
        self.play(
            Create(arrow),
            Write(arrow_label)
        )
        self.wait(1)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(word1),
            FadeOut(rules),
            FadeOut(new_word),
            FadeOut(arrow),
            FadeOut(arrow_label)
        )
        self.wait(0.5)
