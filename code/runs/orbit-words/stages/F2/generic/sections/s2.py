from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Orbit Words: Growth by Simultaneous Rewriting", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial word X
        x_word = Text("X", font_size=40)
        x_word.move_to(ORIGIN)
        self.play(Write(x_word))
        self.wait(1)

        # Rule explanation
        rule_text = Text("Rule: X → XYY, Y → YX", font_size=28)
        rule_text.next_to(x_word, DOWN, buff=0.5)
        self.play(Write(rule_text))
        self.wait(1.5)

        # Fade out rule text
        self.play(FadeOut(rule_text))

        # Split X into XYY
        x1 = Text("X", font_size=40).move_to(x_word.get_center())
        y1 = Text("Y", font_size=40).next_to(x1, RIGHT)
        y2 = Text("Y", font_size=40).next_to(y1, RIGHT)

        self.play(Transform(x_word, x1), run_time=0.5)
        self.wait(0.5)
        self.play(Write(y1), run_time=0.5)
        self.wait(0.5)
        self.play(Write(y2), run_time=0.5)
        self.wait(0.5)

        # Final XYY word
        xyy_word = VGroup(x1, y1, y2)
        xyy_word.move_to(ORIGIN)
        self.play(ReplacementTransform(x_word, xyy_word))
        self.wait(1)

        # Bracket highlighting
        bracket_left = Line(start=UP * 0.3, end=DOWN * 0.3, color=YELLOW)
        bracket_right = Line(start=UP * 0.3, end=DOWN * 0.3, color=YELLOW)
        bracket_left.next_to(x1, DOWN)
        bracket_right.next_to(y2, DOWN)
        bracket_group = VGroup(bracket_left, bracket_right)

        self.play(Write(bracket_group))
        self.wait(1)

        # Length explanation
        length_text = Text("Length 1 → 3", font_size=30)
        length_text.next_to(xyy_word, DOWN, buff=0.5)
        self.play(Write(length_text))
        self.wait(2)

        # Fade out everything except title and final word
        self.play(
            FadeOut(bracket_group),
            FadeOut(length_text),
            FadeOut(title)
        )
        self.wait(0.5)
