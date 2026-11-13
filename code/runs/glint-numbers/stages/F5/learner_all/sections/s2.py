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

        # Add Rule 2
        rule2 = Text("Rule 2: A number ending in 0 is never a Glint number.", font_size=24)
        rule2.to_edge(UP, buff=0.3)
        rule2.shift(0.0 * RIGHT + -0.43 * UP)  # layout: separation vector
        self.play(Write(rule2))
        self.wait(1.5)

        # Example with 30
        example30 = MathTex("30", font_size=36)
        example30.move_to(ORIGIN)
        self.play(ReplacementTransform(num, example30))
        self.wait(1)

        # Highlight the '0' in red and shake it
        if len(example30) > 1:
            zero = example30[1]
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
        cross2 = Cross(stroke_color=RED, stroke_width=15, scale_factor=2)
        cross2.move_to(ORIGIN)
        self.play(Create(cross2), run_time=0.7)
        self.wait(0.5)

        # Show explanation for 30
        explanation30 = Text("For example, the number 30 ends in 0, so it is NOT a Glint number.", font_size=24)
        explanation30.next_to(example30, DOWN, buff=0.5)
        explanation30.shift(0.0 * RIGHT + -1.52 * UP)  # layout: separation vector
        self.play(Write(explanation30))
        self.wait(2)

        self.play(FadeOut(explanation30), FadeOut(cross2), FadeOut(example30))

        # Show Rule 3
        rule3 = Text("A number ending in 3 is always a Glint number", font_size=24)
        rule3.to_edge(UP, buff=0.3)
        rule3.shift(0.0 * RIGHT + -0.43 * UP)  # layout: separation vector
        self.play(Write(rule3))
        self.wait(1.5)

        # Example with 13
        example13 = MathTex("13", font_size=36)
        example13.move_to(ORIGIN)
        self.play(Write(example13))
        self.wait(1)

        # Show division and explanation
        div13 = MathTex("13 \\div 3 = 4.33...", font_size=30)
        div13.next_to(example13, DOWN, buff=0.5)
        self.play(Write(div13))
        self.wait(2)

        # Show that it's not a Glint number
        not_glint = Text("So 13 is NOT a Glint number.", font_size=24)
        not_glint.next_to(div13, DOWN, buff=0.5)
        self.play(Write(not_glint))
        self.wait(2)

        self.play(FadeOut(not_glint), FadeOut(div13), FadeOut(example13))

        # Show Rule 4
        rule4 = Text("However, we define Glint numbers based on divisibility by the last digit.", font_size=24)
        rule4.to_edge(UP, buff=0.3)
        self.play(Write(rule4))
        self.wait(1.5)

        # Example with 48
        example48 = MathTex("48", font_size=36)
        example48.move_to(ORIGIN)
        self.play(Write(example48))
        self.wait(1)

        div48 = MathTex("48 \\div 8 = 6", font_size=30)
        div48.next_to(example48, DOWN, buff=0.5)
        self.play(Write(div48))
        self.wait(2)

        glint48 = Text("Therefore, 48 IS a Glint number.", font_size=24)
        glint48.next_to(div48, DOWN, buff=0.5)
        self.play(Write(glint48))
        self.wait(2)

        self.play(FadeOut(glint48), FadeOut(div48), FadeOut(example48))

        # Example with 49
        example49 = MathTex("49", font_size=36)
        example49.move_to(ORIGIN)
        self.play(Write(example49))
        self.wait(1)

        div49 = MathTex("49 \\div 9 = 5.44...", font_size=30)
        div49.next_to(example49, DOWN, buff=0.5)
        self.play(Write(div49))
        self.wait(2)

        not_glint49 = Text("Therefore, 49 is NOT a Glint number.", font_size=24)
        not_glint49.next_to(div49, DOWN, buff=0.5)
        self.play(Write(not_glint49))
        self.wait(2)

        self.play(FadeOut(not_glint49), FadeOut(div49), FadeOut(example49))

        # Clean up
        self.play(FadeOut(rule2), FadeOut(rule3), FadeOut(rule4))
        self.wait(0.5)
        self.play(FadeOut(title))
        self.wait(0.5)
