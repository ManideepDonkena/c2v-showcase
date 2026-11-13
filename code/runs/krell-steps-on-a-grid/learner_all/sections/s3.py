from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Staircase Path from Origin", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(x_range=[-1, 4], y_range=[-1, 4], 
                           axis_config={"stroke_color": GREY, "stroke_width": 1})
        grid.scale(0.8)
        grid.shift(DOWN * 0.5)
        self.play(Create(grid))
        self.wait(0.5)

        # Start point
        start_point = Dot(color=BLUE).move_to(grid.c2p(0, 0))
        start_label = MathTex("(0, 0)", font_size=24).next_to(start_point, DOWN)
        self.play(FadeIn(start_point), Write(start_label))
        self.wait(1)

        # Step 1: (0,0) -> (0,1)
        step1_arrow = Arrow(grid.c2p(0, 0), grid.c2p(0, 1), buff=0.1, color=YELLOW)
        step1_label = MathTex("(0, 1)", font_size=24).next_to(step1_arrow, UP)
        self.play(GrowArrow(step1_arrow), Write(step1_label))
        self.wait(1)

        # Step 2: (0,1) -> (1,1)
        step2_arrow = Arrow(grid.c2p(0, 1), grid.c2p(1, 1), buff=0.1, color=YELLOW)
        step2_label = MathTex("(1, 1)", font_size=24).next_to(step2_arrow, UP)
        self.play(GrowArrow(step2_arrow), Write(step2_label))
        self.wait(1)

        # Step 3: (1,1) -> (1,2)
        step3_arrow = Arrow(grid.c2p(1, 1), grid.c2p(1, 2), buff=0.1, color=YELLOW)
        step3_label = MathTex("(1, 2)", font_size=24).next_to(step3_arrow, UP)
        self.play(GrowArrow(step3_arrow), Write(step3_label))
        self.wait(1)

        # Step 4: (1,2) -> (2,2)
        step4_arrow = Arrow(grid.c2p(1, 2), grid.c2p(2, 2), buff=0.1, color=YELLOW)
        step4_label = MathTex("(2, 2)", font_size=24).next_to(step4_arrow, UP)
        self.play(GrowArrow(step4_arrow), Write(step4_label))
        self.wait(1.5)

        # Show formula
        formula = MathTex(r"(y, x + 1)", font_size=36).to_edge(UP).shift(DOWN * 0.8)
        arrow_label = Text("The new position is y for the first number and x plus one for the second", font_size=24)
        arrow_label.next_to(formula, DOWN)

        self.play(Write(formula))
        self.wait(1)
        self.play(Write(arrow_label))
        self.wait(2)
        self.play(FadeOut(arrow_label))

        # Show swap and increment: (2, 2) -> (2, 3)
        point_22 = Dot(color=RED).move_to(grid.c2p(2, 2))
        label_22 = MathTex("(2, 2)", font_size=24).next_to(point_22, UP)
        label_22.shift(0.25 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(FadeIn(point_22), Write(label_22))
        self.wait(1)

        # Swap visually
        swap_arrow = Arrow(grid.c2p(2, 2), grid.c2p(2, 2), color=GREEN, buff=0.1)
        swap_arrow.shift(RIGHT * 0.3)
        swap_text = Text("Swap", font_size=24).next_to(swap_arrow, UP)
        swap_text.shift(0.0 * RIGHT + -0.39 * UP)  # layout: separation vector
        swap_text.shift(0.34 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(GrowArrow(swap_arrow), Write(swap_text))
        self.wait(1)

        # Add 1 to second
        add_arrow = Arrow(grid.c2p(2, 2), grid.c2p(2, 3), color=ORANGE, buff=0.1)
        add_text = Text("Add 1", font_size=24).next_to(add_arrow, RIGHT)
        self.play(GrowArrow(add_arrow), Write(add_text))
        self.wait(1)

        result_label = MathTex("(2, 3)", font_size=24).next_to(add_arrow, UP)
        self.play(Write(result_label))
        self.wait(1.5)

        # Clear previous
        self.play(FadeOut(swap_arrow), FadeOut(swap_text), FadeOut(add_arrow), FadeOut(add_text))

        # Show another example: (-1, 4) -> (4, 0)
        point_neg14 = Dot(color=RED).move_to(grid.c2p(-1, 4))
        label_neg14 = MathTex("(-1, 4)", font_size=24).next_to(point_neg14, UP)
        self.play(FadeIn(point_neg14), Write(label_neg14))
        self.wait(1)

        # Swap
        swap_arrow2 = Arrow(grid.c2p(-1, 4), grid.c2p(4, -1), color=GREEN, buff=0.1)
        swap_text2 = Text("Swap", font_size=24).next_to(swap_arrow2, UP)
        self.play(GrowArrow(swap_arrow2), Write(swap_text2))
        self.wait(1)

        # Add 1 to second
        add_arrow2 = Arrow(grid.c2p(4, -1), grid.c2p(4, 0), color=ORANGE, buff=0.1)
        add_text2 = Text("Add 1", font_size=24).next_to(add_arrow2, RIGHT)
        self.play(GrowArrow(add_arrow2), Write(add_text2))
        self.wait(1)

        result_label2 = MathTex("(4, 0)", font_size=24).next_to(add_arrow2, UP)
        self.play(Write(result_label2))
        self.wait(1.5)

        # Clear
        self.play(FadeOut(swap_arrow2), FadeOut(swap_text2), FadeOut(add_arrow2), FadeOut(add_text2))

        # Show step 3 arrow from (2,2) to (2,3)
        step3_arrow_final = Arrow(grid.c2p(2, 2), grid.c2p(2, 3), buff=0.1, color=PURPLE)
        step3_label_final = Text("Step 3", font_size=24).next_to(step3_arrow_final, RIGHT)
        self.play(GrowArrow(step3_arrow_final), Write(step3_label_final))
        self.wait(1.5)

        # Show change in x vs y
        change_x = MathTex(r"\Delta x = 0", font_size=24).to_edge(LEFT).shift(DOWN * 2)
        change_y = MathTex(r"\Delta y = +1", font_size=24).next_to(change_x, DOWN)
        self.play(Write(change_x), Write(change_y))
        self.wait(2)
        self.play(FadeOut(change_x), FadeOut(change_y))

        # Continue path: (2, 2) -> (2, 3) -> (3, 3)
        step5_arrow = Arrow(grid.c2p(2, 3), grid.c2p(3, 3), buff=0.1, color=YELLOW)
        step5_label = MathTex("(3, 3)", font_size=24).next_to(step5_arrow, UP)
        self.play(GrowArrow(step5_arrow), Write(step5_label))
        self.wait(1)

        # Show Double Step Identity
        double_identity = Text("Double Krell Step: (+1, +1)", font_size=24).to_edge(DOWN)
        self.play(Write(double_identity))
        self.wait(1.5)
        self.play(FadeOut(double_identity))

        # Final step to reach (4, 4) via one more krell step
        final_arrow = Arrow(grid.c2p(3, 3), grid.c2p(3, 4), buff=0.1, color=PURPLE)
        final_label = Text("Step 5", font_size=24).next_to(final_arrow, RIGHT)
        self.play(GrowArrow(final_arrow), Write(final_label))
        self.wait(1)

        # Total steps
        total_text = Text("Total Steps: 5 (2 + 2 + 1)", font_size=24).to_edge(DOWN)
        self.play(Write(total_text))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(grid), FadeOut(start_point), FadeOut(start_label),
                  FadeOut(step1_arrow), FadeOut(step1_label),
                  FadeOut(step2_arrow), FadeOut(step2_label),
                  FadeOut(step3_arrow), FadeOut(step3_label),
                  FadeOut(step4_arrow), FadeOut(step4_label),
                  FadeOut(formula), FadeOut(point_22), FadeOut(label_22),
                  FadeOut(point_neg14), FadeOut(label_neg14),
                  FadeOut(result_label), FadeOut(result_label2),
                  FadeOut(step3_arrow_final), FadeOut(step3_label_final),
                  FadeOut(step5_arrow), FadeOut(step5_label),
                  FadeOut(final_arrow), FadeOut(final_label),
                  FadeOut(total_text))
