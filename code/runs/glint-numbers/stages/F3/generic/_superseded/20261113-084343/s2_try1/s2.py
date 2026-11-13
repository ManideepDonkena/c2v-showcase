from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Glint Numbers", font_size=36)
        title.to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Show number 50
        num = MathTex("50", font_size=40)
        num.move_to(ORIGIN)
        self.play(Write(num))
        self.wait(1)
        
        # Highlight the '0' in red and shake it
        if len(num) > 1:
            zero = num[1]
            zero_copy = zero.copy()
            self.play(
                zero.animate.set_color(RED),
                run_time=0.5
            )
            self.play(
                zero_copy.animate.shift(RIGHT * 0.2).shift(LEFT * 0.4).shift(RIGHT * 0.2),
                run_time=0.5
            )
            self.wait(0.5)

        # Add large red X
        cross = Cross(stroke_color=RED, stroke_width=15, scale_factor=2)
        cross.move_to(ORIGIN)
        self.play(Create(cross), run_time=0.7)
        self.wait(0.5)

        # Show rule text
        rule_text = Text("Rule: Ending in 0 is NEVER Glint", font_size=24)
        rule_text.next_to(num, DOWN, buff=0.5)
        rule_text.shift(0.0 * RIGHT + -1.51 * UP)  # layout: separation vector
        self.play(Write(rule_text))
        self.wait(1.5)

        # Narration key words
        self.play(FadeOut(rule_text))
        self.wait(0.3)

        narration1 = Text("However,", font_size=24)
        narration1.to_edge(DOWN, buff=0.3)
        self.play(Write(narration1))
        self.wait(1)

        self.play(FadeOut(narration1))
        narration2 = Text("there is a strict exclusion rule:", font_size=24)
        narration2.to_edge(DOWN, buff=0.3)
        self.play(Write(narration2))
        self.wait(1.5)

        self.play(FadeOut(narration2))
        narration3 = Text("any number ending in zero", font_size=24)
        narration3.to_edge(DOWN, buff=0.3)
        self.play(Write(narration3))
        self.wait(1.5)

        self.play(FadeOut(narration3))
        narration4 = Text("can never be a Glint number.", font_size=24)
        narration4.to_edge(DOWN, buff=0.3)
        self.play(Write(narration4))
        self.wait(1.5)

        self.play(FadeOut(narration4))
        narration5 = Text("This is because division by zero", font_size=24)
        narration5.to_edge(DOWN, buff=0.3)
        self.play(Write(narration5))
        self.wait(1.5)

        self.play(FadeOut(narration5))
        narration6 = Text("is undefined.", font_size=24)
        narration6.to_edge(DOWN, buff=0.3)
        self.play(Write(narration6))
        self.wait(1.5)

        self.play(FadeOut(narration6))

        # Clean up
        self.play(FadeOut(num), FadeOut(cross), FadeOut(title))
        self.wait(0.5)
