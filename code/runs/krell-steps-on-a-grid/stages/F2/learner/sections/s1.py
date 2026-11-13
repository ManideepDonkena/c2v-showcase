from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Krell Transformation Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid
        grid = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_opacity": 0.3}
        )
        grid.set_stroke(width=0.5)
        self.play(Create(grid))
        self.wait(0.5)
        # Point P at (3, 5)
        P = Dot(point=[3, 5, 0], color=BLUE)
        label_P = MathTex("(3, 5)", font_size=24).next_to(P, UR, buff=0.2)
        P.shift(0.0 * RIGHT + -1.23 * UP)  # layout: separation vector
        self.play(FadeIn(P), Write(label_P))
        self.wait(0.5)

        # Arrow from P to Q
        arrow = Arrow(start=P.get_center(), end=[5, 4, 0], color=YELLOW, buff=0.1)
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Point Q at (5, 4)
        Q = Dot(point=[5, 4, 0], color=RED)
        label_Q = MathTex("(5, 4)", font_size=24).next_to(Q, DR, buff=0.2)
        self.play(FadeIn(Q), Write(label_Q))
        self.wait(0.5)

        # Labels above arrow
        swap_label = Text("Swap", font_size=24).next_to(arrow, UP, buff=0.2)
        plus1_label = Text("+1", font_size=24).next_to(arrow, UP, buff=0.2).shift(RIGHT * 0.5)

        self.play(Write(swap_label))
        self.wait(0.5)
        self.play(Transform(swap_label, plus1_label))
        self.wait(0.5)
        self.play(FadeOut(swap_label))

        # Formula label
        formula = MathTex("(y, x + 1)", font_size=32).next_to(arrow, UP, buff=0.5)
        self.play(Write(formula))
        self.wait(0.5)

        # Narration: "The new position is y for the first number and x plus one for the second"
        narration = Text("The new position is y for the first number and x plus one for the second", font_size=20)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        # Example 1: (2, 2) -> (2, 3)
        self.play(FadeOut(formula), FadeOut(P), FadeOut(Q), FadeOut(label_P), FadeOut(label_Q), FadeOut(arrow))
        self.wait(0.5)

        # Show swapping and incrementing
        x_val = MathTex("2", font_size=32).move_to([2, 1.5, 0])
        y_val = MathTex("2", font_size=32).move_to([3, 1.5, 0])
        self.play(Write(x_val), Write(y_val))
        self.wait(0.5)

        # Swap
        swapped_x = MathTex("2", font_size=32).move_to([3, 1.5, 0])
        swapped_y = MathTex("2", font_size=32).move_to([2, 1.5, 0])
        self.play(Transform(x_val, swapped_x), Transform(y_val, swapped_y))
        self.wait(0.5)

        # Add 1 to y
        new_y = MathTex("3", font_size=32).move_to([2, 1.5, 0])
        self.play(Transform(y_val, new_y))
        self.wait(0.5)

        result_label = Text("Result: (2, 3)", font_size=24).to_edge(DOWN)
        self.play(Write(result_label))
        self.wait(1.5)
        self.play(FadeOut(x_val), FadeOut(y_val), FadeOut(result_label))

        # Example 2: (-1, 4) -> (4, 0)
        self.wait(0.5)

        x_val2 = MathTex("-1", font_size=32).move_to([2, 1.5, 0])
        y_val2 = MathTex("4", font_size=32).move_to([3, 1.5, 0])
        self.play(Write(x_val2), Write(y_val2))
        self.wait(0.5)

        # Swap
        swapped_x2 = MathTex("4", font_size=32).move_to([3, 1.5, 0])
        swapped_y2 = MathTex("-1", font_size=32).move_to([2, 1.5, 0])
        self.play(Transform(x_val2, swapped_x2), Transform(y_val2, swapped_y2))
        self.wait(0.5)

        # Add 1 to y
        new_y2 = MathTex("0", font_size=32).move_to([2, 1.5, 0])
        self.play(Transform(y_val2, new_y2))
        self.wait(0.5)

        result_label2 = Text("Result: (4, 0)", font_size=24).to_edge(DOWN)
        self.play(Write(result_label2))
        self.wait(1.5)
        self.play(FadeOut(x_val2), FadeOut(y_val2), FadeOut(result_label2))

        # Final explanation
        final_explanation = Text("The new x is the old y.", font_size=24).to_edge(DOWN)
        self.play(Write(final_explanation))
        self.wait(1.5)
        self.play(FadeOut(final_explanation))

        self.play(FadeOut(title), FadeOut(grid))
        self.wait(0.5)
