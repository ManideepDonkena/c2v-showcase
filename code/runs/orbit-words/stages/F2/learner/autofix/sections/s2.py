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

        # Narration text: "Starting with X, we apply the rule."
        narration1 = Text("Starting with X,", font_size=24)
        narration1.next_to(x_word, DOWN, buff=0.5)
        self.play(Write(narration1))
        self.wait(1.5)

        # Rule explanation
        rule_text = Text("Rule: X → XYY", font_size=24)
        rule_text.next_to(narration1, DOWN, buff=0.3)
        self.play(Write(rule_text))
        self.wait(1.5)

        # Fade out narration and rule
        self.play(FadeOut(narration1), FadeOut(rule_text))

        # Show transformation: X becomes XYY
        xyy_word = Text("XYY", font_size=40)
        xyy_word.move_to(ORIGIN)
        self.play(ReplacementTransform(x_word, xyy_word))
        self.wait(1.5)

        # Narration text: "Since there is only one X, it becomes XYY."
        narration2 = Text("Since there is only one X,", font_size=24)
        narration2.next_to(xyy_word, DOWN, buff=0.5)
        self.play(Write(narration2))
        self.wait(1.5)

        # Narration text: "The word grows from length 1 to length 3."
        narration3 = Text("The word grows from length 1 to length 3.", font_size=24)
        narration3.next_to(narration2, DOWN, buff=0.3)
        self.play(Write(narration3))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(xyy_word), FadeOut(narration2), FadeOut(narration3))
        self.wait(0.5)
