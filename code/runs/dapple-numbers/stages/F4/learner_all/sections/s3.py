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
        self.wait(0.5)

        # Highlight digits
        highlight_44 = always_redraw(lambda: SurroundingRectangle(num_44, color=RED, buff=0.1))
        self.play(Create(highlight_44))
        self.wait(0.5)

        # Equals sign
        eq = MathTex("=").scale(2)
        eq.next_to(num_44, RIGHT, buff=0.5)
        self.play(Write(eq))
        self.wait(0.5)

        # Not Dapple label
        not_dapple = Text("Not Dapple", font_size=24, color=RED).next_to(eq, RIGHT, buff=0.5)
        self.play(Write(not_dapple))
        self.wait(1)

        # Narration: If digits are equal
        narration1 = Text("If the digits are equal", font_size=24).to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(1.5)
        self.play(FadeOut(narration1))

        # Fade out 44 and related
        self.play(FadeOut(num_44, highlight_44, eq, not_dapple))
        self.wait(0.5)

        # Show 25
        num_25 = MathTex("25").scale(2)
        self.play(Write(num_25))
        self.wait(0.5)

        # Turn red
        num_25.set_color(RED)
        self.wait(0.5)

        # Not Dapple label with condition
        not_dapple_25 = Text("Not Dapple (2 < 5)", font_size=24, color=RED).next_to(num_25, RIGHT, buff=0.5)
        self.play(Write(not_dapple_25))
        self.wait(1)

        # Narration: If tens digit is smaller
        narration2 = Text("If tens digit < units digit", font_size=24).to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1.5)
        self.play(FadeOut(narration2))

        # Fade out 25 and related
        self.play(FadeOut(num_25, not_dapple_25))
        self.wait(0.5)

        # Show definition
        definition = Text("A whole number is dapple if its tens digit > units digit", font_size=24).to_edge(UP)
        definition.shift(0.0 * RIGHT + 0.49 * UP)  # layout: separation vector
        self.play(Write(definition))
        self.wait(1)

        # Example: 61 is dapple
        example_61 = MathTex("61").scale(2)
        self.play(Write(example_61))
        self.wait(0.5)

        check = always_redraw(lambda: Circle(color=GREEN, radius=0.4).move_to(example_61.get_center() + 0.89 * UP))
        self.play(Create(check))
        self.wait(0.5)

        # Label 6 > 1
        condition_61 = Text("6 > 1", font_size=24).next_to(example_61, DOWN, buff=0.3)
        self.play(Write(condition_61))
        self.wait(1)

        # Fade out 61 and related
        self.play(FadeOut(example_61, check, condition_61))
        self.wait(0.5)

        # Counter-example: 16 is not dapple
        example_16 = MathTex("16").scale(2)
        self.play(Write(example_16))
        self.wait(0.5)

        example_16.set_color(RED)
        self.wait(0.5)

        # Label 1 < 6
        condition_16 = Text("1 < 6", font_size=24, color=RED).next_to(example_16, DOWN, buff=0.3)
        self.play(Write(condition_16))
        self.wait(1)

        # Fade out everything
        self.play(FadeOut(example_16, condition_16, definition))
        self.wait(0.5)
