from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Orbit Words: Growth by Simultaneous Rewriting", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Step 0: X
        step0 = Text("Step 0", font_size=24).to_corner(UL)
        x_word = Text("X", font_size=40)
        x_word.next_to(step0, DOWN, buff=0.5)
        self.play(Write(step0), Write(x_word))
        self.wait(1)

        # Rule display
        rule = MathTex(r"\text{Rule: } X \to XYY,\quad Y \to YX", font_size=32)
        rule.to_edge(UP, buff=0.5)
        self.play(Transform(title, rule))
        self.wait(1)

        # Show transformation of X to XYY
        xyy = Text("XYY", font_size=40)
        xyy.next_to(x_word, RIGHT, buff=1)
        arrow = Arrow(x_word.get_right(), xyy.get_left(), buff=0.2)
        self.play(GrowArrow(arrow), Write(xyy))
        self.wait(1)

        # Highlight that X becomes XYY
        bracket = BraceBetweenPoints(x_word.get_left(), x_word.get_right(), direction=DOWN)
        bracket_text = Text("X", font_size=24).next_to(bracket, DOWN)
        self.play(GrowFromCenter(bracket), Write(bracket_text))
        self.wait(1)

        # Show that no Ys exist yet
        no_y = Text("No Ys yet", font_size=24).next_to(x_word, DOWN)
        self.play(Write(no_y))
        self.wait(1.5)

        # Comparison: one input letter → two output letters
        input_letter = Text("X", font_size=30).to_edge(LEFT, buff=1)
        output_letters = Text("XYY", font_size=30).next_to(input_letter, RIGHT, buff=2)
        arrow2 = Arrow(input_letter.get_right(), output_letters.get_left(), buff=0.2)
        self.play(Write(input_letter), Write(output_letters), GrowArrow(arrow2))
        self.wait(1.5)

        # Show that process never starts with Y
        y_crossed = Text("Y", font_size=60).set_color(RED)
        x_on_y = Cross(y_crossed, color=RED)
        y_crossed_group = VGroup(y_crossed, x_on_y).arrange(DOWN, buff=0.5)
        y_crossed_group.to_edge(RIGHT, buff=1)
        self.play(Write(y_crossed_group))
        self.wait(1)

        # Show that it starts from X
        start_from_x = Text("Start from X", font_size=24).next_to(y_crossed_group, DOWN)
        self.play(Write(start_from_x))
        self.wait(1.5)

        # Show invalid starting with Y
        y_word = Text("Y", font_size=40).to_edge(LEFT, buff=1)
        cross_y = Cross(y_word, color=RED)
        self.play(Write(y_word), Create(cross_y))
        self.wait(1)

        # Show first letter remains unchanged in this case
        xyy_group = Text("XYY", font_size=40).to_edge(RIGHT, buff=1)
        arrow3 = Arrow(x_word.get_left(), xyy_group.get_left(), buff=0.2)
        self.play(Write(xyy_group), GrowArrow(arrow3))
        self.wait(1)

        # Show transformation of first letter in longer word
        long_word = Text("XYYYXYX", font_size=30).to_edge(DOWN, buff=0.5)
        self.play(Write(long_word))
        self.wait(1)

        # Highlight first X and show it becomes XYY
        first_x = long_word[0]
        first_x_copy = first_x.copy()
        first_x_copy.move_to(xyy_group.get_left())
        self.play(Transform(first_x, first_x_copy))
        self.wait(1)

        # Show that Ys appear in Step 1
        step1 = Text("Step 1", font_size=24).to_corner(UL)
        self.play(Write(step1))
        self.wait(0.5)

        # Show that Step 0 has only X, Step 1 introduces Ys
        step0_y_count = Text("0 Ys", font_size=24).next_to(x_word, DOWN)
        step1_y_count = Text("2 Ys", font_size=24).next_to(xyy, DOWN)
        self.play(Write(step0_y_count), Write(step1_y_count))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(VGroup(title, step0, x_word, xyy, arrow, bracket, bracket_text, no_y,
                                 input_letter, output_letters, arrow2, y_crossed_group, start_from_x,
                                 y_word, cross_y, long_word, first_x_copy, step1, step0_y_count, step1_y_count)))
        self.wait(0.5)
