from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Origin and the Rule", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial 'X'
        x_symbol = Tex(r"$X$", font_size=72)
        x_symbol.move_to(ORIGIN)
        self.play(FadeIn(x_symbol))
        self.wait(1)

        # Arrows and labels
        arrow1 = Arrow(start=DOWN*0.5, end=UP*0.5, color=BLUE)
        arrow1.next_to(x_symbol, UP)
        rule1_label = Text("X → XYY", font_size=24, color=BLUE)
        rule1_label.next_to(arrow1, UP)

        arrow2 = Arrow(start=DOWN*0.5, end=UP*0.5, color=GREEN)
        arrow2.next_to(x_symbol, DOWN)
        rule2_label = Text("Y → YX", font_size=24, color=GREEN)
        rule2_label.next_to(arrow2, DOWN)

        self.play(GrowArrow(arrow1), Write(rule1_label))
        self.wait(1)
        self.play(GrowArrow(arrow2), Write(rule2_label))
        self.wait(1.5)

        # Simultaneous Rewrite pulse
        simultaneous = Text("Simultaneous Rewrite", font_size=30)
        simultaneous.to_edge(UP)
        simultaneous.shift(DOWN * 0.5)
        self.play(FadeIn(simultaneous))
        self.play(simultaneous.animate.scale(1.2).set_color(YELLOW))
        self.wait(0.5)
        self.play(FadeOut(simultaneous))

        # Example growth
        example_text = Text("X → XYY → XYYYXYX", font_size=24)
        example_text.to_edge(DOWN)
        self.play(Write(example_text))
        self.wait(2)

        # Clear screen and show rules
        self.play(FadeOut(x_symbol, arrow1, rule1_label, arrow2, rule2_label, example_text))

        rule1 = Text("1. Every orbit word starts with X.", font_size=24)
        rule2 = Text("2. Each rewrite makes the word longer.", font_size=24)
        rule3 = Text("Rules: X → XYY, Y → YX", font_size=24)

        rule1.to_edge(UP).shift(DOWN * 0.5)
        rule2.next_to(rule1, DOWN)
        rule3.next_to(rule2, DOWN)

        self.play(Write(rule1))
        self.wait(1)
        self.play(Write(rule2))
        self.wait(1)
        self.play(Write(rule3))
        self.wait(2)

        # Fade out
        self.play(FadeOut(rule1, rule2, rule3))
        self.wait(0.5)
