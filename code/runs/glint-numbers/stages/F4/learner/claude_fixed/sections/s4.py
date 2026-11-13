from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Worked Examples: Success vs Failure", font_size=36)
        title.to_edge(UP, buff=0.2)

        # Left side: 24 is Glint
        num_24 = Text("24", font_size=40)
        num_24.shift(LEFT * 3 + UP * 1.5)
        num_24.set_z_index(2)

        highlight_4 = Rectangle(width=0.4, height=0.8, color=YELLOW, fill_opacity=0.3)
        highlight_4.move_to(num_24[1].get_center())
        highlight_4.set_z_index(1)

        div_24_by_4 = MathTex("24 \\div 4 = 6", font_size=32)
        div_24_by_4.shift(LEFT * 3 + DOWN * 1)

        check = Text("✓", font_size=40, color=GREEN)
        check.next_to(div_24_by_4, RIGHT, buff=0.3)

        # Right side: 26 is not Glint
        num_26 = Text("26", font_size=40)
        num_26.shift(RIGHT * 3 + UP * 1.5)
        num_26.set_z_index(2)

        highlight_6 = Rectangle(width=0.4, height=0.8, color=YELLOW, fill_opacity=0.3)
        highlight_6.move_to(num_26[1].get_center())
        highlight_6.set_z_index(1)

        div_26_by_6 = MathTex("26 \\div 6 = 4.33...", font_size=32)
        div_26_by_6.shift(RIGHT * 3 + DOWN * 1)

        x_mark = Text("✗", font_size=40, color=RED)
        x_mark.next_to(div_26_by_6, RIGHT, buff=0.3)

        # Narration text
        narration1 = Text("Let's test two examples.", font_size=24)
        narration1.to_edge(DOWN, buff=0.5)

        # Show title
        self.play(Write(title))
        self.wait(0.5)

        # Show first example: 24 is Glint
        self.play(Write(num_24), run_time=0.5)
        self.play(Create(highlight_4), run_time=0.3)
        self.wait(0.5)
        self.play(Write(div_24_by_4), run_time=0.5)
        self.play(Write(check), run_time=0.3)
        self.wait(1)

        # Show second example: 26 is not Glint
        self.play(Write(num_26), run_time=0.5)
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
