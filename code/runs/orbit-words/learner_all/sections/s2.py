from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Step 1: From X to XYY", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial word X
        x_word = Text("X", font_size=40).move_to(LEFT * 3 + UP * 0.5)
        self.play(Write(x_word))
        self.wait(0.5)

        # Splitting X into XYY
        xyy_group = VGroup(
            Text("X", font_size=40),
            Text("Y", font_size=40),
            Text("Y", font_size=40)
        ).arrange(RIGHT, buff=0.3).move_to(LEFT * 3 + UP * 0.5)

        self.play(Transform(x_word, xyy_group))
        self.wait(1)

        # Bracket highlighting
        bracket = Brace(xyy_group, direction=DOWN, buff=0.2)
        bracket_text = Text("X → XYY", font_size=24).next_to(bracket, DOWN)
        self.play(GrowFromCenter(bracket), Write(bracket_text))
        self.wait(1.5)

        # Rule explanation
        rule = MathTex(r"\text{Rule: } X \to XYY,\ Y \to YX", font_size=30).to_edge(DOWN)
        self.play(Write(rule))
        self.wait(1.5)

        # Comparison: one input letter → two output letters
        input_letter = Text("X", font_size=30).move_to(LEFT * 4 + DOWN * 1)
        arrow = Arrow(LEFT * 3.5 + DOWN * 1, LEFT * 2.5 + DOWN * 1, buff=0.2)
        output_letters = VGroup(
            Text("X", font_size=30),
            Text("Y", font_size=30)
        ).arrange(RIGHT, buff=0.2).move_to(LEFT * 2 + DOWN * 1)

        self.play(Write(input_letter), Write(arrow), Write(output_letters))
        self.wait(1.5)

        # Clear previous
        self.play(FadeOut(input_letter), FadeOut(arrow), FadeOut(output_letters))

        # Show X is the only start
        x_start = Text("X", font_size=40).move_to(LEFT * 3 + UP * 0.5)
        y_crossed = Text("Y", font_size=40).move_to(RIGHT * 3 + UP * 0.5)
        cross = Cross(y_crossed, color=RED)
        x_start.shift(0.0 * RIGHT + 0.55 * UP)  # layout: separation vector
        self.play(Write(x_start), Write(y_crossed), Create(cross))
        self.wait(1)

        # Show that process starts with X
        start_text = Text("Start from X", font_size=24).next_to(rule, UP)
        self.play(Write(start_text))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(x_start), FadeOut(y_crossed), FadeOut(cross), FadeOut(start_text))

        # Show first letter unchanged
        xyy_word = Text("XYY", font_size=40).move_to(LEFT * 3 + UP * 0.5)
        arrow_first = Arrow(LEFT * 3 + DOWN * 1, LEFT * 3 + DOWN * 0.2, buff=0.2)
        first_x = Text("X", font_size=40).move_to(LEFT * 3 + DOWN * 1)
        xyy_word.shift(0.0 * RIGHT + 0.55 * UP)  # layout: separation vector
        self.play(Write(xyy_word), Write(arrow_first), Write(first_x))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(xyy_word), FadeOut(arrow_first), FadeOut(first_x))

        # Show transformation of X in a longer word
        long_word = Text("XYYYXYX", font_size=30).move_to(LEFT * 4 + UP * 0.5)
        self.play(Write(long_word))
        self.wait(1)

        # Highlight first X and show it becomes XYY
        highlight_x = SurroundingRectangle(long_word[0], color=YELLOW, buff=0.1)
        xyy_transformed = Text("XYY", font_size=30).move_to(LEFT * 4 + DOWN * 0.5)
        arrow_transform = Arrow(LEFT * 4 + UP * 0.2, LEFT * 4 + DOWN * 0.2, buff=0.2)

        self.play(Create(highlight_x), Write(arrow_transform), Write(xyy_transformed))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(long_word), FadeOut(highlight_x), FadeOut(arrow_transform), FadeOut(xyy_transformed))

        # Show Ys appear from Step 0 to Step 1
        step0 = Text("Step 0: X", font_size=30).move_to(LEFT * 4 + UP * 0.5)
        step1 = Text("Step 1: XYY", font_size=30).move_to(RIGHT * 4 + UP * 0.5)

        self.play(Write(step0), Write(step1))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(step0), FadeOut(step1))

        # Final summary text
        final_text = Text("The process never begins with Y", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(rule), FadeOut(final_text))
