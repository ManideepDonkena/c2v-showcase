from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Orbit Words: Growth by Simultaneous Rewriting", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Step 0: XYY
        step0 = Text("XYY", font_size=40)
        step0.next_to(title, DOWN, buff=0.5)
        self.play(Write(step0))
        self.wait(1)

        # Show transformation of each letter simultaneously
        x_text = Text("X", font_size=36).move_to(step0[0])
        y1_text = Text("Y", font_size=36).move_to(step0[1])
        y2_text = Text("Y", font_size=36).move_to(step0[2])

        # Show transformations
        x_transform = Text("XYY", font_size=36)
        y1_transform = Text("YX", font_size=36)
        y2_transform = Text("YX", font_size=36)

        self.play(Transform(x_text, x_transform), run_time=0.5)
        self.play(Transform(y1_text, y1_transform), run_time=0.5)
        self.play(Transform(y2_text, y2_transform), run_time=0.5)
        self.wait(1)

        # Concatenate to form new word
        result = Text("XYYYXYX", font_size=40)
        result.next_to(step0, DOWN, buff=0.5)
        self.play(Write(result))
        self.wait(1.5)

        # Show that each letter expands into two letters
        self.play(FadeOut(x_text), FadeOut(y1_text), FadeOut(y2_text))

        # Show visual comparison: input vs output per letter
        step0_letters = [Text("X", font_size=36), Text("Y", font_size=36), Text("Y", font_size=36)]
        step0_letters[0].move_to([-4, 1, 0])
        step0_letters[1].move_to([-2, 1, 0])
        step0_letters[2].move_to([0, 1, 0])

        step1_letters = [Text("XYY", font_size=36), Text("YX", font_size=36), Text("YX", font_size=36)]
        step1_letters[0].move_to([-4, -1, 0])
        step1_letters[1].move_to([-2, -1, 0])
        step1_letters[2].move_to([0, -1, 0])

        self.play(Write(VGroup(*step0_letters)))
        self.wait(0.5)
        self.play(Write(VGroup(*step1_letters)))
        self.wait(1)

        # Arrows showing expansion
        arrow1 = Arrow(step0_letters[0].get_bottom(), step1_letters[0].get_top(), buff=0.1)
        arrow2 = Arrow(step0_letters[1].get_bottom(), step1_letters[1].get_top(), buff=0.1)
        arrow3 = Arrow(step0_letters[2].get_bottom(), step1_letters[2].get_top(), buff=0.1)

        self.play(Create(arrow1), Create(arrow2), Create(arrow3))
        self.wait(1.5)

        # Show that process never begins with Y
        y_crossed = Text("Y", font_size=60).set_color(RED)
        x_on_y = Text("X", font_size=60).set_color(RED)
        y_crossed.next_to(step1_letters[0], LEFT, buff=1)
        x_on_y.next_to(y_crossed, RIGHT, buff=0.2)

        self.play(Write(y_crossed))
        self.wait(0.5)
        self.play(Write(x_on_y))
        self.wait(1)

        # Narration text
        narration = Text("The process never begins with Y; it always starts with X.", font_size=24)
        narration.next_to(y_crossed, DOWN, buff=0.5)
        self.play(Write(narration))
        self.wait(2)

        # Show invalid start from Y
        invalid_start = Text("Y", font_size=40).set_color(RED)
        invalid_start.next_to(step1_letters[0], LEFT, buff=1.5)
        invalid_arrow = Arrow(invalid_start.get_bottom(), step1_letters[0].get_top(), color=RED)

        self.play(Write(invalid_start))
        self.play(Create(invalid_arrow))
        self.wait(1.5)

        # Show rule text
        rule_text = Text("Start from X", font_size=24)
        rule_text.next_to(invalid_start, DOWN, buff=0.5)
        self.play(Write(rule_text))
        self.wait(1.5)

        # Highlight first letter transformation
        first_arrow = Arrow(step0[0].get_left(), step1_letters[0][0].get_right(), color=YELLOW)
        self.play(Create(first_arrow))
        self.wait(1)

        # Show that X stays at start of result
        highlight_result = Text("X", font_size=40).set_color(YELLOW)
        highlight_result.move_to(step1_letters[0][0])
        self.play(Transform(step1_letters[0][0], highlight_result))
        self.wait(1.5)

        # Show that Y appears from first rewrite
        step0_only_x = Text("X", font_size=36)
        step0_only_x.to_edge(LEFT).shift(DOWN * 2)
        step1_has_y = Text("XYY", font_size=36)
        step1_has_y.to_edge(RIGHT).shift(DOWN * 2)

        self.play(Write(step0_only_x))
        self.wait(0.5)
        self.play(Write(step1_has_y))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(VGroup(title, step0, result, step0_letters, step1_letters,
                                arrow1, arrow2, arrow3, y_crossed, x_on_y, narration,
                                invalid_start, invalid_arrow, rule_text, first_arrow,
                                highlight_result, step0_only_x, step1_has_y)))
        self.wait(0.5)
