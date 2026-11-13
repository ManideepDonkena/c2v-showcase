from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Non-Examples and Edge Cases", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 44
        num_44 = MathTex("44").scale(2)
        self.play(Write(num_44))
        self.wait(1)

        # Highlight digits and show equality
        if len(num_44) >= 2:
            highlight_44_1 = num_44[0].copy().set_color(RED)
            highlight_44_2 = num_44[1].copy().set_color(RED)
            self.play(
                Transform(num_44[0], highlight_44_1),
                Transform(num_44[1], highlight_44_2)
            )
        self.wait(0.5)
        equals = MathTex("=").scale(2).next_to(num_44, buff=0.3)
        self.play(Write(equals))
        self.wait(0.5)

        not_dapple_44 = Text("Not Dapple", font_size=24).next_to(equals, DOWN)
        self.play(Write(not_dapple_44))
        self.wait(1.5)

        # Fade out 44 and equals
        self.play(FadeOut(num_44), FadeOut(equals), FadeOut(not_dapple_44))

        # Show 25
        num_25 = MathTex("25").scale(2)
        self.play(Write(num_25))
        self.wait(1)

        # Highlight digits and show inequality
        if len(num_25) >= 2:
            highlight_25_1 = num_25[0].copy().set_color(RED)
            highlight_25_2 = num_25[1].copy().set_color(RED)
            self.play(
                Transform(num_25[0], highlight_25_1),
                Transform(num_25[1], highlight_25_2)
            )
        self.wait(0.5)

        less_than = MathTex("<").scale(2).next_to(num_25, buff=0.3)
        self.play(Write(less_than))
        self.wait(0.5)

        not_dapple_25 = Text("Not Dapple (2 < 5)", font_size=24).next_to(less_than, DOWN)
        self.play(Write(not_dapple_25))
        self.wait(1.5)

        # Fade out 25 and less than
        self.play(FadeOut(num_25), FadeOut(less_than), FadeOut(not_dapple_25))

        # Show 32
        num_32 = MathTex("32").scale(2)
        self.play(Write(num_32))
        self.wait(1)

        # Highlight digits and show inequality
        if len(num_32) >= 2:
            highlight_32_1 = num_32[0].copy().set_color(GREEN)
            highlight_32_2 = num_32[1].copy().set_color(GREEN)
            self.play(
                Transform(num_32[0], highlight_32_1),
                Transform(num_32[1], highlight_32_2)
            )
        self.wait(0.5)

        greater_than = MathTex(">").scale(2).next_to(num_32, buff=0.3)
        self.play(Write(greater_than))
        self.wait(0.5)

        dapple_check = Text("Dapple", font_size=24).next_to(greater_than, DOWN)
        self.play(Write(dapple_check))
        self.wait(1)

        # Add green checkmark or glow
        check = always_redraw(lambda: Circle(color=GREEN, radius=0.5, stroke_width=8).move_to(num_32.get_center()))
        self.play(Create(check))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(num_32), FadeOut(greater_than), FadeOut(dapple_check), FadeOut(check))
        self.wait(0.5)
