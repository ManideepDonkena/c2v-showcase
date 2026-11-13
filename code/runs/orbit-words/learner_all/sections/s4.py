from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Verification and Growth", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Final word
        final_word = Text("XYYYXYX", font_size=40)
        length_text = MathTex(r"\text{Length: } 7", font_size=32)
        length_group = VGroup(length_text, final_word).arrange(DOWN, buff=0.5)
        length_group.to_edge(UP, buff=1.2)
        self.play(Write(final_word), Write(length_text))
        self.wait(1)

        # Arrow and text
        arrow = Arrow(start=DOWN, end=UP, color=YELLOW).next_to(final_word, DOWN, buff=0.5)
        rewrite_text = Text("Every rewrite makes the word longer", font_size=24)
        rewrite_text.next_to(arrow, DOWN, buff=0.3)
        self.play(GrowArrow(arrow), Write(rewrite_text))
        self.wait(1)

        # Checkmark
        checkmark = Tex(r"$\checkmark$", color=GREEN, font_size=40)
        checkmark.next_to(rewrite_text, RIGHT, buff=0.5)
        self.play(Write(checkmark))
        self.wait(1.5)

        # Show expansion of letters: X -> XYY, Y -> YX
        self.play(FadeOut(arrow, rewrite_text, checkmark))

        rule1 = MathTex(r"X \rightarrow XYY", font_size=32)
        rule2 = MathTex(r"Y \rightarrow YX", font_size=32)
        rules = VGroup(rule1, rule2).arrange(DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.play(Write(rules))
        self.wait(1)

        # Show visual expansion
        x_expansion = Text("X", font_size=36).set_color(BLUE)
        x_expanded = Text("XYY", font_size=36).set_color(BLUE)
        y_expansion = Text("Y", font_size=36).set_color(GREEN)
        y_expanded = Text("YX", font_size=36).set_color(GREEN)

        x_group = VGroup(x_expansion, Arrow(), x_expanded).arrange(RIGHT, buff=0.5)
        y_group = VGroup(y_expansion, Arrow(), y_expanded).arrange(RIGHT, buff=0.5)
        expansion_groups = VGroup(x_group, y_group).arrange(DOWN, buff=1).to_edge(RIGHT, buff=1)

        y_expansion.shift(0.0 * RIGHT + 0.31 * UP)  # layout: separation vector
        y_group.shift(0.0 * RIGHT + 0.29 * UP)  # layout: separation vector
        self.play(Write(expansion_groups))
        self.wait(2)

        # Show that process never begins with Y
        self.play(FadeOut(rules, expansion_groups))

        no_y_start = Text("The process never begins with Y; it always starts with X.", font_size=24)
        no_y_start.shift(0.0 * RIGHT + -0.71 * UP)  # layout: separation vector
        self.play(Write(no_y_start))
        self.wait(1.5)

        # Show red X through Y
        y_crossed = Text("Y", font_size=40).set_color(GREEN)
        cross = Line(start=LEFT, end=RIGHT, color=RED, stroke_width=8).scale(0.7).move_to(y_crossed)
        y_with_cross = VGroup(y_crossed, cross).arrange(DOWN, buff=0.1)
        self.play(Write(y_with_cross))
        self.wait(1)

        # Show that starting from Y is invalid
        self.play(FadeOut(no_y_start, y_with_cross))

        start_from_x = Text("Start from X", font_size=24).to_edge(LEFT, buff=1)
        self.play(Write(start_from_x))
        self.wait(0.5)

        # Show word starting with Y being crossed out
        y_word = Text("YXXX", font_size=36).set_color(GREEN)
        cross_y = Line(start=LEFT, end=RIGHT, color=RED, stroke_width=8).scale(0.7).move_to(y_word)
        y_crossed_out = VGroup(y_word, cross_y).arrange(DOWN, buff=0.1)
        self.play(Write(y_crossed_out))
        self.wait(1.5)

        # Show that the first letter remains unchanged
        self.play(FadeOut(start_from_x, y_crossed_out))

        word_before = Text("XYY", font_size=36).set_color(BLUE)
        word_after = Text("XYYYXYX", font_size=36).set_color(BLUE)
        arrow_first = Arrow(start=LEFT, end=RIGHT, color=YELLOW).next_to(word_before, DOWN, buff=0.5)
        first_letter_arrow = Arrow(start=word_before[0].get_left(), end=word_after[0].get_right(), color=RED)
        self.play(Write(word_before), Write(word_after))
        self.wait(0.5)

        # Highlight first letter
        self.play(Write(first_letter_arrow))
        self.wait(1.5)

        # Show transformation of first X to XYY
        self.play(FadeOut(word_before, word_after, first_letter_arrow))

        x_to_xyy = Text("X", font_size=36).set_color(BLUE)
        xyy_result = Text("XYY", font_size=36).set_color(BLUE)
        arrow_transform = Arrow(start=LEFT, end=RIGHT, color=YELLOW).next_to(x_to_xyy, DOWN, buff=0.5)
        self.play(Write(x_to_xyy), Write(xyy_result))
        self.wait(0.5)

        # Highlight new first character
        highlight = SurroundingRectangle(xyy_result[0], color=RED, buff=0.1)
        self.play(Create(highlight))
        self.wait(1.5)

        # Show that Y appears starting from Step 1
        self.play(FadeOut(x_to_xyy, xyy_result, arrow_transform, highlight))

        step_0 = Text("Step 0: X", font_size=24)
        step_1 = Text("Step 1: XYY", font_size=24)
        step_group = VGroup(step_0, step_1).arrange(DOWN, buff=0.5).to_edge(RIGHT, buff=1)
        self.play(Write(step_group))
        self.wait(1)

        # Show Y count
        y_count_0 = Text("0 Ys", font_size=24)
        y_count_1 = Text("2 Ys", font_size=24)
        y_counts = VGroup(y_count_0, y_count_1).arrange(DOWN, buff=0.5).next_to(step_group, LEFT, buff=0.5)
        self.play(Write(y_counts))
        self.wait(1.5)

        # Final cleanup
        self.play(FadeOut(step_group, y_counts, title))
        self.wait(0.5)
