from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Double Step Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Setup grid and axes
        axes = Axes(
            x_range=[-7, 7, 1],
            y_range=[-3.9, 3.9, 1],
            axis_config={"color": WHITE},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        axes_labels.shift(0.0 * RIGHT + -0.52 * UP)  # layout: separation vector
        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)

        # Start point A at (2, 2)
        A = Dot(axes.c2p(2, 2), color=BLUE)
        label_A = MathTex("(2, 2)", font_size=24).next_to(A, UR)
        self.play(FadeIn(A), Write(label_A))
        self.wait(0.5)

        # Step 1: Arrow from A to intermediate point
        step1_arrow = Arrow(axes.c2p(2, 2), axes.c2p(2, 3), buff=0, color=YELLOW)
        label_step1 = MathTex("Step\ 1", font_size=24).next_to(step1_arrow, UP)
        self.play(GrowArrow(step1_arrow), Write(label_step1))
        self.wait(0.5)

        # Intermediate point
        B = Dot(axes.c2p(2, 3), color=BLUE)
        label_B = MathTex("(2, 3)", font_size=24).next_to(B, UR)
        self.play(FadeIn(B), Write(label_B))
        self.wait(0.5)

        # Step 2: Arrow from intermediate to final point
        step2_arrow = Arrow(axes.c2p(2, 3), axes.c2p(3, 3), buff=0, color=YELLOW)
        label_step2 = MathTex("Step\ 2", font_size=24).next_to(step2_arrow, UP)
        label_step2.shift(0.0 * RIGHT + 0.27 * UP)  # layout: separation vector
        self.play(GrowArrow(step2_arrow), Write(label_step2))
        self.wait(0.5)

        # Final point C
        C = Dot(axes.c2p(3, 3), color=BLUE)
        label_C = MathTex("(3, 3)", font_size=24).next_to(C, UR)
        self.play(FadeIn(C), Write(label_C))
        self.wait(0.5)

        # Dashed direct arrow from A to C
        direct_arrow = DashedLine(axes.c2p(2, 2), axes.c2p(3, 3), color=GREEN)
        label_direct = MathTex("(x+1, y+1)", font_size=24).next_to(direct_arrow, DR)
        self.play(Create(direct_arrow), Write(label_direct))
        self.wait(0.5)

        # Show formula (y, x + 1) next to transformation arrow
        formula = MathTex("(y, x + 1)", font_size=30).next_to(step1_arrow, LEFT)
        self.play(Write(formula))
        self.wait(0.5)

        # Narration text
        narration = Text("Two consecutive Krell steps have a powerful simplification.", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.0)
        self.play(FadeOut(narration))

        # Show specific example: (2, 2) → swap → (2, 2) → add 1 to second → (2, 3)
        swap_text = Text("Swap coordinates", font_size=24).to_edge(LEFT).shift(DOWN * 1.5)
        self.play(Write(swap_text))
        self.wait(0.5)

        # Show swapping visually
        swap_arrow = Arrow(axes.c2p(2, 2), axes.c2p(2, 2), buff=0, color=RED)
        self.play(GrowArrow(swap_arrow))
        self.wait(0.5)

        add_one_text = Text("Add 1 to second", font_size=24).to_edge(LEFT).shift(DOWN * 1.0)
        self.play(Write(add_one_text))
        self.wait(0.5)

        result_text = Text("Result: (2, 3)", font_size=24).to_edge(LEFT).shift(DOWN * 0.5)
        self.play(Write(result_text))
        self.wait(1.0)

        # Clear previous
        self.play(FadeOut(swap_arrow), FadeOut(swap_text), FadeOut(add_one_text), FadeOut(result_text))

        # Show second example: (-1, 4) → swap → (4, -1) → add 1 to second → (4, 0)
        A2 = Dot(axes.c2p(-1, 4), color=BLUE)
        label_A2 = MathTex("(-1, 4)", font_size=24).next_to(A2, UR)
        self.play(FadeIn(A2), Write(label_A2))
        self.wait(0.5)

        swap_text2 = Text("Swap coordinates", font_size=24).to_edge(LEFT).shift(DOWN * 1.5)
        self.play(Write(swap_text2))
        self.wait(0.5)

        # Visual swap
        swap_arrow2 = Arrow(axes.c2p(-1, 4), axes.c2p(4, -1), buff=0, color=RED)
        self.play(GrowArrow(swap_arrow2))
        self.wait(0.5)

        add_one_text2 = Text("Add 1 to second", font_size=24).to_edge(LEFT).shift(DOWN * 1.0)
        self.play(Write(add_one_text2))
        self.wait(0.5)

        result_text2 = Text("Result: (4, 0)", font_size=24).to_edge(LEFT).shift(DOWN * 0.5)
        self.play(Write(result_text2))
        self.wait(1.0)

        # Clear
        self.play(FadeOut(swap_arrow2), FadeOut(swap_text2), FadeOut(add_one_text2), FadeOut(result_text2))

        # Show visual breakdown of x and y roles
        breakdown = Text("New x = old y", font_size=24).to_edge(LEFT).shift(DOWN * 1.5)
        self.play(Write(breakdown))
        self.wait(0.5)

        breakdown2 = Text("New y = old x + 1", font_size=24).to_edge(LEFT).shift(DOWN * 1.0)
        self.play(Write(breakdown2))
        self.wait(1.0)

        # Clear
        self.play(FadeOut(breakdown), FadeOut(breakdown2))

        # Apply rule again to (2, 2) → (2, 3)
        step3_arrow = Arrow(axes.c2p(2, 2), axes.c2p(2, 3), buff=0, color=YELLOW)
        label_step3 = MathTex("Step\ 3", font_size=24).next_to(step3_arrow, UP)
        self.play(GrowArrow(step3_arrow), Write(label_step3))
        self.wait(0.5)

        # Compare change in x vs y
        change_x = Text("Change in x: 0", font_size=24).to_edge(LEFT).shift(DOWN * 1.5)
        change_y = Text("Change in y: +1", font_size=24).to_edge(LEFT).shift(DOWN * 1.0)
        self.play(Write(change_x))
        self.wait(0.5)
        self.play(Write(change_y))
        self.wait(1.0)

        # Clear
        self.play(FadeOut(step3_arrow), FadeOut(label_step3), FadeOut(change_x), FadeOut(change_y))

        # Continue path from (2, 2) to (2, 3) to (3, 3)
        step4_arrow = Arrow(axes.c2p(2, 3), axes.c2p(3, 3), buff=0, color=YELLOW)
        label_step4 = MathTex("Step\ 4", font_size=24).next_to(step4_arrow, UP)
        self.play(GrowArrow(step4_arrow), Write(label_step4))
        self.wait(0.5)

        # Show total steps
        total_steps = Text("Total: 2 + 2 + 1 = 5 steps", font_size=24).to_edge(DOWN)
        self.play(Write(total_steps))
        self.wait(1.0)

        # Final cleanup
        self.play(FadeOut(title), FadeOut(axes), FadeOut(axes_labels), FadeOut(A), FadeOut(label_A),
                  FadeOut(B), FadeOut(label_B), FadeOut(C), FadeOut(label_C), FadeOut(step1_arrow),
                  FadeOut(label_step1), FadeOut(step2_arrow), FadeOut(label_step2), FadeOut(direct_arrow),
                  FadeOut(label_direct), FadeOut(formula), FadeOut(total_steps))
        self.wait(0.5)
