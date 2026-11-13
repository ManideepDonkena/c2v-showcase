from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Worked Examples: Success vs Failure", font_size=36)
        title.to_edge(UP, buff=0.2)

        # Left side: 24 is Glint
        num_24 = Text("24", font_size=40)
        num_24.shift(LEFT * 3 + UP * 1.5)

        highlight_4 = Rectangle(width=0.6, height=0.8, color=YELLOW, fill_opacity=0.3)
        highlight_4.move_to(num_24.get_center() + RIGHT * 0.3)

        div_24_by_4 = MathTex("24 \\div 4 = 6", font_size=32)
        div_24_by_4.shift(LEFT * 3 + DOWN * 1)

        check = Text("✓", font_size=40, color=GREEN)
        check.next_to(div_24_by_4, RIGHT, buff=0.3)

        # Right side: 26 is not Glint
        num_26 = Text("26", font_size=40)
        num_26.shift(RIGHT * 3 + UP * 1.5)

        highlight_6 = Rectangle(width=0.6, height=0.8, color=YELLOW, fill_opacity=0.3)
        highlight_6.move_to(num_26.get_center() + RIGHT * 0.3)

        div_26_by_6 = MathTex("26 \\div 6 = 4.33...", font_size=32)
        div_26_by_6.shift(RIGHT * 3 + DOWN * 1)

        x_mark = Text("✗", font_size=40, color=RED)
        x_mark.next_to(div_26_by_6, RIGHT, buff=0.3)

        # Narration text
        narration1 = Text("Let's test two examples.", font_size=24)
        narration1.to_edge(DOWN, buff=0.5)

        # Rule 2 text
        rule2 = Text("Rule 2: A number ending in 0 is never a Glint number.", font_size=24)
        rule2.shift(UP * 2)

        example_30 = Text("For example, the number 30 ends in 0, so it is NOT a Glint number.", font_size=24)
        example_30.next_to(rule2, DOWN, buff=0.2)

        # New worked examples
        num_48 = Text("48", font_size=40)
        num_48.shift(LEFT * 3 + UP * 0.5)

        highlight_8 = Rectangle(width=0.6, height=0.8, color=YELLOW, fill_opacity=0.3)
        highlight_8.move_to(num_48.get_center() + RIGHT * 0.3)

        div_48_by_8 = MathTex("48 \\div 8 = 6", font_size=32)
        div_48_by_8.shift(LEFT * 3 + DOWN * 0.5)

        check_48 = Text("✓", font_size=40, color=GREEN)
        check_48.next_to(div_48_by_8, RIGHT, buff=0.3)

        num_49 = Text("49", font_size=40)
        num_49.shift(RIGHT * 3 + UP * 0.5)

        highlight_9 = Rectangle(width=0.6, height=0.8, color=YELLOW, fill_opacity=0.3)
        highlight_9.move_to(num_49.get_center() + RIGHT * 0.3)

        div_49_by_9 = MathTex("49 \\div 9 = 5.44...", font_size=32)
        div_49_by_9.shift(RIGHT * 3 + DOWN * 0.5)

        x_mark_49 = Text("✗", font_size=40, color=RED)
        x_mark_49.next_to(div_49_by_9, RIGHT, buff=0.3)

        # Show title
        self.play(Write(title))
        self.wait(0.5)

        # Show first example: 24 is Glint
        self.play(Write(num_24), run_time=0.5)
        highlight_4.shift(0.44 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(highlight_4), run_time=0.3)
        self.wait(0.5)
        self.play(Write(div_24_by_4), run_time=0.5)
        self.play(Write(check), run_time=0.3)
        self.wait(1)

        # Show second example: 26 is not Glint
        self.play(Write(num_26), run_time=0.5)
        highlight_6.shift(0.43 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(highlight_6), run_time=0.3)
        self.wait(0.5)
        self.play(Write(div_26_by_6), run_time=0.5)
        self.play(Write(x_mark), run_time=0.3)
        self.wait(1)

        # Narration text
        self.play(Write(narration1))
        self.wait(2)

        # Fade out all
        self.play(
            FadeOut(title),
            FadeOut(num_24),
            FadeOut(highlight_4),
            FadeOut(div_24_by_4),
            FadeOut(check),
            FadeOut(num_26),
            FadeOut(highlight_6),
            FadeOut(div_26_by_6),
            FadeOut(x_mark),
            FadeOut(narration1)
        )
        self.wait(0.5)

        # Add Rule 2
        self.play(Write(rule2))
        self.wait(1)
        self.play(Write(example_30))
        self.wait(2)

        # Show new examples
        self.play(Write(num_48), run_time=0.5)
        highlight_8.shift(0.44 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(highlight_8), run_time=0.3)
        self.wait(0.5)
        self.play(Write(div_48_by_8), run_time=0.5)
        self.play(Write(check_48), run_time=0.3)
        self.wait(1)

        self.play(Write(num_49), run_time=0.5)
        highlight_9.shift(0.43 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(highlight_9), run_time=0.3)
        self.wait(0.5)
        self.play(Write(div_49_by_9), run_time=0.5)
        self.play(Write(x_mark_49), run_time=0.3)
        self.wait(1)

        # Fade out new examples
        self.play(
            FadeOut(num_48),
            FadeOut(highlight_8),
            FadeOut(div_48_by_8),
            FadeOut(check_48),
            FadeOut(num_49),
            FadeOut(highlight_9),
            FadeOut(div_49_by_9),
            FadeOut(x_mark_49),
            FadeOut(rule2),
            FadeOut(example_30)
        )
        self.wait(0.5)
