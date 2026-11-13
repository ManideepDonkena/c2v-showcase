from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Swapping b and c", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grids side by side
        grid1 = Matrix([[2, 1], [2, 4]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid2 = Matrix([[2, 2], [1, 4]], bracket_h_buff=0.2, bracket_v_buff=0.2)

        # Labels
        label1 = Text("Grid 1", font_size=24).next_to(grid1, UP)
        label2 = Text("Grid 2", font_size=24).next_to(grid2, UP)

        # Position grids side by side
        grid1.shift(LEFT * 2)
        grid2.shift(RIGHT * 2)

        self.play(Write(grid1), Write(label1))
        label2.shift(0.0 * RIGHT + 0.41 * UP)  # layout: separation vector
        self.play(Write(grid2), Write(label2))
        self.wait(1)

        # Formula for both grids
        formula1 = MathTex("a \\times d - b - c", font_size=30).next_to(grid1, DOWN)
        formula2 = MathTex("a \\times d - b - c", font_size=30).next_to(grid2, DOWN)

        self.play(Write(formula1), Write(formula2))
        self.wait(1)

        # Highlight subtraction order
        highlight1 = SurroundingRectangle(formula1, color=YELLOW, buff=0.1)
        highlight2 = SurroundingRectangle(formula2, color=YELLOW, buff=0.1)

        self.play(Create(highlight1))
        self.wait(0.5)
        self.play(ReplacementTransform(highlight1, highlight2))
        self.wait(0.5)
        self.play(FadeOut(highlight2))

        # Show that order doesn't matter
        note = Text("Subtraction order does not change result", font_size=24).to_edge(DOWN)
        self.play(Write(note))
        self.wait(1)

        # Show equality of expressions
        eq = MathTex("a \\times d - b - c = a \\times d - c - b", font_size=30).next_to(note, UP)
        self.play(Write(eq))
        self.wait(1.5)

        # Checkmark
        check = Tex(r"$\checkmark$").scale(2).set_color(GREEN).to_edge(DOWN)
        check.shift(0.0 * RIGHT + 0.48 * UP)  # layout: separation vector
        check.shift(0.0 * RIGHT + 0.47 * UP)  # layout: separation vector
        self.play(Write(check))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(grid1),
            FadeOut(grid2),
            FadeOut(label1),
            FadeOut(label2),
            FadeOut(formula1),
            FadeOut(formula2),
            FadeOut(note),
            FadeOut(eq),
            FadeOut(check)
        )
        self.wait(0.5)
