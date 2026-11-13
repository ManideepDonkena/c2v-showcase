from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Orbit Words: Growth by Simultaneous Rewriting", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial word X
        x_word = Text("X", font_size=40)
        x_word.move_to(ORIGIN)
        self.play(Write(x_word))
        self.wait(1)

        # Rule explanation
        rule_text = Text("Rule: X → XYY, Y → YX", font_size=24)
        rule_text.next_to(x_word, DOWN, buff=0.5)
        self.play(Write(rule_text))
        self.wait(1.5)

        # Fade out rule text
        self.play(FadeOut(rule_text))

        # Split X into XYY
        xyy_group = VGroup(
            Text("X", font_size=40),
            Text("Y", font_size=40),
            Text("Y", font_size=40)
        )
        xyy_group.arrange(RIGHT, buff=0.3)
        xyy_group.move_to(ORIGIN)

        # Animation: X splits into XYY
        self.play(
            Transform(x_word, xyy_group),
            run_time=1.5
        )
        self.wait(1)

        # Bracket highlighting
        bracket = Brace(xyy_group, direction=UP)
        bracket_text = Text("X → XYY", font_size=24)
        bracket_text.next_to(bracket, UP)

        self.play(
            GrowFromCenter(bracket),
            Write(bracket_text)
        )
        self.wait(1.5)

        # Fade out bracket and text
        self.play(FadeOut(bracket), FadeOut(bracket_text))

        # Show word length growth
        length_text = Text("Length: 1 → 3", font_size=24)
        length_text.next_to(xyy_group, DOWN, buff=0.5)
        self.play(Write(length_text))
        self.wait(1.5)

        # Fade out everything except final word
        self.play(
            FadeOut(title),
            FadeOut(length_text),
            xyy_group.animate.move_to(ORIGIN)
        )
        self.wait(0.5)
