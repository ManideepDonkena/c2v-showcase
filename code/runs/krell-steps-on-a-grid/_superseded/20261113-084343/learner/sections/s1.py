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
            background_line_style={"stroke_color": GREY}
        )
        grid.set_opacity(0.5)
        self.play(Create(grid))
        self.wait(0.5)
        
        # Point P at (3, 5)
        P = Dot(point=[3, 5, 0], color=BLUE)
        label_P = Tex("(3, 5)", font_size=24).next_to(P, UR, buff=0.2)
        self.play(FadeIn(P), Write(label_P))
        self.wait(0.5)

        # Arrow from P to Q
        arrow = Arrow(start=P.get_center(), end=[5, 4, 0], color=YELLOW, buff=0.1)
        self.play(Create(arrow))
        self.wait(0.5)

        # Swap label
        swap_label = Text("Swap", font_size=24).next_to(arrow, UP)
        self.play(Write(swap_label))
        self.wait(0.5)

        # +1 label
        plus_label = Text("+1", font_size=24).next_to(arrow, UP)
        self.play(Transform(swap_label, plus_label))
        self.wait(0.5)

        # Fade out labels
        self.play(FadeOut(swap_label))

        # Point Q at (5, 4)
        Q = Dot(point=[5, 4, 0], color=RED)
        label_Q = Tex("(5, 4)", font_size=24).next_to(Q, DR, buff=0.2)
        self.play(FadeIn(Q), Write(label_Q))
        self.wait(0.5)

        # Formula
        formula = MathTex("(y, x + 1)", font_size=40).next_to(arrow, DOWN)
        self.play(Write(formula))
        self.wait(0.5)

        # Narration: "The new position is y for the first number and x plus one for the second"
        narration = Text("The new position is y for the first number and x plus one for the second", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        # Example 1: (2, 2) -> (2, 3)
        self.play(FadeOut(formula), FadeOut(P), FadeOut(label_P), FadeOut(Q), FadeOut(label_Q), FadeOut(arrow))
        self.wait(0.5)

        # Show swapping (2, 2)
        x_val = Tex("2", font_size=30).move_to([2, 1.5, 0])
        y_val = Tex("2", font_size=30).move_to([3, 1.5, 0])
        self.play(Write(x_val), Write(y_val))
        self.wait(0.5)

        # Swap visually
        swap_arrow = Arrow(start=[2, 1.5, 0], end=[3, 1.5, 0], color=YELLOW)
        self.play(Create(swap_arrow))
        self.wait(0.5)

        # Show new positions after swap
        x_new = Tex("2", font_size=30).move_to([3, 1.5, 0])
        y_new = Tex("2", font_size=30).move_to([2, 1.5, 0])
        self.play(Transform(x_val, x_new), Transform(y_val, y_new))
        self.wait(0.5)

        # Add 1 to new y
        plus_one = Tex("+1", font_size=24).next_to(y_new, UP)
        self.play(Write(plus_one))
        self.wait(0.5)

        # Final result (2, 3)
        final_result = Tex("(2, 3)", font_size=30).to_edge(DOWN)
        self.play(Write(final_result))
        self.wait(1.5)
        self.play(FadeOut(x_val), FadeOut(y_val), FadeOut(swap_arrow), FadeOut(plus_one), FadeOut(final_result))

        # Example 2: (-1, 4) -> (4, 0)
        self.wait(0.5)

        x_val_2 = Tex("-1", font_size=30).move_to([2, 1.5, 0])
        y_val_2 = Tex("4", font_size=30).move_to([3, 1.5, 0])
        self.play(Write(x_val_2), Write(y_val_2))
        self.wait(0.5)

        # Swap visually
        swap_arrow_2 = Arrow(start=[2, 1.5, 0], end=[3, 1.5, 0], color=YELLOW)
        self.play(Create(swap_arrow_2))
        self.wait(0.5)

        x_new_2 = Tex("4", font_size=30).move_to([3, 1.5, 0])
        y_new_2 = Tex("-1", font_size=30).move_to([2, 1.5, 0])
        self.play(Transform(x_val_2, x_new_2), Transform(y_val_2, y_new_2))
        self.wait(0.5)

        # Add 1 to new y
        plus_one_2 = Tex("+1", font_size=24).next_to(y_new_2, UP)
        self.play(Write(plus_one_2))
        self.wait(0.5)

        # Final result (4, 0)
        final_result_2 = Tex("(4, 0)", font_size=30).to_edge(DOWN)
        self.play(Write(final_result_2))
        self.wait(1.5)
        self.play(FadeOut(x_val_2), FadeOut(y_val_2), FadeOut(swap_arrow_2), FadeOut(plus_one_2), FadeOut(final_result_2))

        # Show visual breakdown
        self.wait(0.5)

        # Original point (x, y) = (3, 5)
        orig_x = Tex("3", font_size=24).move_to([1, 2, 0])
        orig_y = Tex("5", font_size=24).move_to([2, 2, 0])
        self.play(Write(orig_x), Write(orig_y))
        self.wait(0.5)

        # New x is old y
        new_x = Tex("5", font_size=24).move_to([1, 1, 0])
        arrow_new_x = Arrow(start=[2, 2, 0], end=[1, 1, 0], color=GREEN)
        self.play(Create(arrow_new_x), Transform(orig_y, new_x))
        self.wait(0.5)

        # New y is old x + 1
        new_y = Tex("3 + 1 = 4", font_size=24).move_to([2, 1, 0])
        arrow_new_y = Arrow(start=[1, 2, 0], end=[2, 1, 0], color=GREEN)
        self.play(Create(arrow_new_y), Transform(orig_x, new_y))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(orig_x), FadeOut(orig_y), FadeOut(arrow_new_x), FadeOut(arrow_new_y), FadeOut(new_x), FadeOut(new_y))

        # Final title fade
        self.play(FadeOut(title))
        self.wait(0.5)
