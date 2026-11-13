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
            axis_config={"stroke_color": GREY},
        )
        self.play(Create(axes))
        self.wait(0.5)

        # Initial point A at (2, 2)
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
        B = Dot(axes.c2p(2, 3), color=GREEN)
        label_B = MathTex("(2, 3)", font_size=24).next_to(B, UR)
        self.play(FadeIn(B), Write(label_B))
        self.wait(0.5)

        # Step 2: Arrow from B to final point
        step2_arrow = Arrow(axes.c2p(2, 3), axes.c2p(3, 3), buff=0, color=YELLOW)
        label_step2 = MathTex("Step\ 2", font_size=24).next_to(step2_arrow, UP)
        label_step2.shift(0.0 * RIGHT + 0.27 * UP)  # layout: separation vector
        self.play(GrowArrow(step2_arrow), Write(label_step2))
        self.wait(0.5)

        # Final point C
        C = Dot(axes.c2p(3, 3), color=RED)
        label_C = MathTex("(3, 3)", font_size=24).next_to(C, UR)
        self.play(FadeIn(C), Write(label_C))
        self.wait(0.5)

        # Dashed direct arrow from A to C
        direct_arrow = DashedLine(axes.c2p(2, 2), axes.c2p(3, 3), color=ORANGE)
        label_direct = MathTex("(+1, +1)", font_size=24).next_to(direct_arrow, UR)
        self.play(Create(direct_arrow), Write(label_direct))
        self.wait(0.5)

        # Formula (y, x + 1) next to transformation arrow
        formula = MathTex("(y, x + 1)", font_size=30).next_to(step1_arrow, LEFT)
        self.play(Write(formula))
        self.wait(0.5)

        # Narration: "The new position is y for the first number and x plus one for the second"
        narration = Text("The new position is y for the first number and x plus one for the second", font_size=24)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        # Show specific example: (2, 2) -> swap -> add 1 to second
        swap_text = Text("Swap (2, 2) → (2, 2)", font_size=24).to_edge(DOWN)
        self.play(Write(swap_text))
        self.wait(0.5)

        add_one_text = Text("Add 1 to second → (2, 3)", font_size=24).next_to(swap_text, DOWN)
        self.play(Write(add_one_text))
        self.wait(0.5)

        result_text = Text("Result is (2, 3)", font_size=24).next_to(add_one_text, DOWN)
        self.play(Write(result_text))
        self.wait(1.0)
        self.play(FadeOut(swap_text), FadeOut(add_one_text), FadeOut(result_text))

        # Another example: (-1, 4) -> swap -> add 1 to second
        swap_text2 = Text("Swap (-1, 4) → (4, -1)", font_size=24).to_edge(DOWN)
        self.play(Write(swap_text2))
        self.wait(0.5)

        add_one_text2 = Text("Add 1 to second → (4, 0)", font_size=24).next_to(swap_text2, DOWN)
        self.play(Write(add_one_text2))
        self.wait(0.5)

        result_text2 = Text("Result is (4, 0)", font_size=24).next_to(add_one_text2, DOWN)
        self.play(Write(result_text2))
        self.wait(1.0)
        self.play(FadeOut(swap_text2), FadeOut(add_one_text2), FadeOut(result_text2))

        # Visual breakdown of transformation
        breakdown = Text("New x = original y", font_size=24).to_edge(DOWN)
        self.play(Write(breakdown))
        self.wait(0.5)

        breakdown2 = Text("New y = original x + 1", font_size=24).next_to(breakdown, DOWN)
        self.play(Write(breakdown2))
        self.wait(1.0)
        self.play(FadeOut(breakdown), FadeOut(breakdown2))

        # Apply rule again to (2, 2) → (2, 3)
        step3_arrow = Arrow(axes.c2p(2, 2), axes.c2p(2, 3), buff=0, color=PURPLE)
        label_step3 = MathTex("Step\ 3", font_size=24).next_to(step3_arrow, UP)
        self.play(GrowArrow(step3_arrow), Write(label_step3))
        self.wait(0.5)

        # Compare change in x vs y
        compare_text = Text("Change in x: 0; Change in y: +1", font_size=24).to_edge(DOWN)
        self.play(Write(compare_text))
        self.wait(1.0)
        self.play(FadeOut(compare_text))

        # Continue path from (2, 3) to (3, 3)
        step4_arrow = Arrow(axes.c2p(2, 3), axes.c2p(3, 3), buff=0, color=PURPLE)
        label_step4 = MathTex("Step\ 4", font_size=24).next_to(step4_arrow, UP)
        self.play(GrowArrow(step4_arrow), Write(label_step4))
        self.wait(0.5)

        # Show that two double steps give (+2, +2) and one more step gives total 5
        total_steps = Text("Two double steps = (+2, +2)", font_size=24).to_edge(DOWN)
        self.play(Write(total_steps))
        self.wait(1.0)

        final_step_arrow = Arrow(axes.c2p(3, 3), axes.c2p(4, 3), buff=0, color=PURPLE)
        label_final = MathTex("Step\ 5", font_size=24).next_to(final_step_arrow, UP)
        self.play(GrowArrow(final_step_arrow), Write(label_final))
        self.wait(1.0)

        final_point = Dot(axes.c2p(4, 3), color=RED)
        label_final_point = MathTex("(4, 3)", font_size=24).next_to(final_point, UR)
        self.play(FadeIn(final_point), Write(label_final_point))
        self.wait(0.5)

        # Final summary
        summary = Text("Total steps: 5", font_size=24).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(1.0)

        self.play(FadeOut(title), FadeOut(axes), FadeOut(A), FadeOut(B), FadeOut(C),
                  FadeOut(step1_arrow), FadeOut(step2_arrow), FadeOut(step3_arrow),
                  FadeOut(step4_arrow), FadeOut(direct_arrow), FadeOut(label_A),
                  FadeOut(label_B), FadeOut(label_C), FadeOut(label_step1),
                  FadeOut(label_step2), FadeOut(label_step3), FadeOut(label_step4),
                  FadeOut(label_direct), FadeOut(formula), FadeOut(summary))
