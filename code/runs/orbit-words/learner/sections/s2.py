from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Orbit Words: Growth by Simultaneous Rewriting", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Step 0: X
        step0_text = Text("Step 0:", font_size=24).to_corner(UL)
        x_word = Text("X", font_size=40)
        x_word.next_to(step0_text, RIGHT, buff=0.3)
        step0_text.shift(-0.32 * RIGHT + 0.0 * UP)  # layout: separation vector
        x_word.shift(0.0 * RIGHT + -0.69 * UP)  # layout: separation vector
        self.play(Write(step0_text), Write(x_word))
        self.wait(1)

        # Rule explanation
        rule = MathTex(r"\text{Rule: } X \to XYY,\quad Y \to YX", font_size=24)
        rule.next_to(title, DOWN, buff=0.3)
        self.play(Write(rule))
        self.wait(1)

        # Fade out step0_text and x_word
        self.play(FadeOut(step0_text), FadeOut(x_word))

        # Step 1: X -> XYY
        step1_text = Text("Step 1:", font_size=24).to_corner(UL)
        xyy_word = Text("XYY", font_size=40)
        xyy_word.next_to(step1_text, RIGHT, buff=0.3)
        step1_text.shift(-0.32 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(step1_text), Write(xyy_word))
        self.wait(1)

        # Bracket highlighting
        bracket = Brace(xyy_word, direction=DOWN, buff=0.1)
        bracket_label = Text("X becomes XYY", font_size=24)
        bracket_label.next_to(bracket, DOWN)
        self.play(GrowFromCenter(bracket), Write(bracket_label))
        self.wait(1.5)

        # Comparison: Step 0 vs Step 1
        self.play(FadeOut(bracket), FadeOut(bracket_label))

        # Show comparison side by side
        step0_comp = Text("Step 0: X", font_size=24)
        step1_comp = Text("Step 1: XYY", font_size=24)
        step0_comp.to_edge(LEFT).shift(DOWN * 1.5)
        step1_comp.to_edge(RIGHT).shift(DOWN * 1.5)
        self.play(Write(step0_comp), Write(step1_comp))
        self.wait(1)

        # Highlight Ys introduced
        y_highlight = SurroundingRectangle(xyy_word[1:], color=YELLOW, buff=0.1)
        y_text = Text("Ys appear in Step 1", font_size=24).next_to(y_highlight, DOWN)
        self.play(Create(y_highlight), Write(y_text))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(step0_comp),
            FadeOut(step1_comp),
            FadeOut(y_highlight),
            FadeOut(y_text),
            FadeOut(xyy_word),
            FadeOut(rule),
            FadeOut(title)
        )
        self.wait(0.5)
