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
            y_range=[-3.9, 3.9, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY}
        )
        grid.set_opacity(0.5)
        self.play(Create(grid))
        self.wait(0.5)
        
        # Point P at (3, 5)
        P = Dot(point=[3, 5, 0], color=BLUE)
        label_P = MathTex("(3, 5)", font_size=24).next_to(P, UR, buff=0.2)
        self.play(FadeIn(P), Write(label_P))
        self.wait(0.5)

        # Arrow from P to Q
        arrow = Arrow(start=P.get_center(), end=[5, 4, 0], color=YELLOW)
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Labels 'Swap' and '+1'
        swap_label = Text("Swap", font_size=24).next_to(arrow, UP)
        self.play(Write(swap_label))
        self.wait(0.5)
        self.play(FadeOut(swap_label))

        plus_one_label = Text("+1", font_size=24).next_to(arrow, UP)
        self.play(Write(plus_one_label))
        self.wait(0.5)
        self.play(FadeOut(plus_one_label))

        # Point Q at (5, 4)
        Q = Dot(point=[5, 4, 0], color=RED)
        label_Q = MathTex("(5, 4)", font_size=24).next_to(Q, DR, buff=0.2)
        self.play(FadeIn(Q), Write(label_Q))
        self.wait(0.5)

        # Formula
        formula = MathTex(r"(y, x + 1)", font_size=32).next_to(arrow, DOWN)
        self.play(Write(formula))
        self.wait(0.5)

        # Narration: "The new position is y for the first number and x plus one for the second"
        narration = Text("The new position is y for the first number and x plus one for the second", font_size=20)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        # Show example with (2, 2)
        self.play(FadeOut(formula), FadeOut(P), FadeOut(label_P), FadeOut(Q), FadeOut(label_Q), FadeOut(arrow))
        self.wait(0.5)

        # Show (2, 2) → swap → (2, 2) → +1 → (2, 3)
        start_point = MathTex("2", "2").arrange(RIGHT, buff=0.5).to_edge(UP)
        self.play(Write(start_point))
        self.wait(0.5)

        # Swap visually
        swapped = MathTex("2", "2").arrange(RIGHT, buff=0.5).to_edge(UP)
        self.play(Transform(start_point, swapped))
        self.wait(0.5)

        # Add 1 to second
        result = MathTex("2", "3").arrange(RIGHT, buff=0.5).to_edge(UP)
        self.play(Transform(start_point, result))
        self.wait(0.5)

        final_label = Text("Result is (2, 3)", font_size=24).next_to(result, DOWN)
        self.play(Write(final_label))
        self.wait(1.0)
        self.play(FadeOut(start_point), FadeOut(final_label))

        # Show example with (-1, 4)
        self.wait(0.5)

        start_point2 = MathTex("-1", "4").arrange(RIGHT, buff=0.5).to_edge(UP)
        self.play(Write(start_point2))
        self.wait(0.5)

        # Swap
        swapped2 = MathTex("4", "-1").arrange(RIGHT, buff=0.5).to_edge(UP)
        self.play(Transform(start_point2, swapped2))
        self.wait(0.5)

        # Add 1 to second
        result2 = MathTex("4", "0").arrange(RIGHT, buff=0.5).to_edge(UP)
        self.play(Transform(start_point2, result2))
        self.wait(0.5)

        final_label2 = Text("Result is (4, 0)", font_size=24).next_to(result2, DOWN)
        self.play(Write(final_label2))
        self.wait(1.0)
        self.play(FadeOut(start_point2), FadeOut(final_label2))

        # Show visual breakdown
        self.wait(0.5)

        # Original point (x, y) = (3, 5)
        orig_point = MathTex("x=3", "y=5").arrange(DOWN, buff=0.5).to_edge(LEFT)
        self.play(Write(orig_point))
        self.wait(0.5)

        # After swap: x becomes y, y becomes x
        swap_text = Text("Swap", font_size=24).next_to(orig_point, RIGHT, buff=1)
        self.play(Write(swap_text))
        self.wait(0.5)

        swapped_point = MathTex("y=5", "x=3").arrange(DOWN, buff=0.5).to_edge(RIGHT)
        self.play(Write(swapped_point))
        self.wait(0.5)

        # Add 1 to new y (which was x)
        plus_one_text = Text("+1", font_size=24).next_to(swapped_point, RIGHT, buff=1)
        self.play(Write(plus_one_text))
        self.wait(0.5)

        final_result = MathTex("y=5", "x+1=4").arrange(DOWN, buff=0.5).to_edge(RIGHT)
        self.play(Transform(swapped_point, final_result))
        self.wait(0.5)

        # Fade out
        self.play(FadeOut(orig_point), FadeOut(swap_text), FadeOut(swapped_point), FadeOut(plus_one_text), FadeOut(title))
        self.wait(0.5)
