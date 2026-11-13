from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Krell Transformation Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
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
        P = Dot([3, 5, 0], color=BLUE)
        label_P = MathTex("(3, 5)", font_size=24).next_to(P, UR)
        P.shift(0.0 * RIGHT + -1.23 * UP)  # layout: separation vector
        self.play(FadeIn(P), Write(label_P))
        self.wait(0.5)

        # Arrow to (5, 3) - swap
        arrow1 = Arrow(P.get_center(), [5, 3, 0], color=YELLOW)
        label_swap = Text("Swap", font_size=24).next_to(arrow1, UP)
        self.play(GrowArrow(arrow1), Write(label_swap))
        self.wait(0.5)

        # Arrow to (5, 4) - add 1
        arrow2 = Arrow([5, 3, 0], [5, 4, 0], color=YELLOW)
        label_plus1 = Text("+1", font_size=24).next_to(arrow2, RIGHT)
        self.play(GrowArrow(arrow2), Write(label_plus1))
        self.wait(0.5)

        # Point Q at (5, 4)
        Q = Dot([5, 4, 0], color=RED)
        label_Q = MathTex("(5, 4)", font_size=24).next_to(Q, UR)
        self.play(FadeIn(Q), Write(label_Q))
        self.wait(0.5)

        # Formula
        formula = MathTex("(y, x + 1)", font_size=36).to_edge(DOWN)
        self.play(Write(formula))
        self.wait(0.5)

        # Voiceover: "The new position is y for the first number and x plus one for the second"
        self.wait(1)

        # Clear labels
        self.play(FadeOut(label_swap, label_plus1, arrow1, arrow2))

        # Show (2, 2) → (2, 3)
        point_A = Dot([2, 2, 0], color=BLUE)
        label_A = MathTex("(2, 2)", font_size=24).next_to(point_A, UR)
        self.play(FadeIn(point_A), Write(label_A))
        self.wait(0.5)

        arrow_A = Arrow(point_A.get_center(), [2, 3, 0], color=YELLOW)
        self.play(GrowArrow(arrow_A))
        self.wait(0.5)

        point_B = Dot([2, 3, 0], color=RED)
        label_B = MathTex("(2, 3)", font_size=24).next_to(point_B, UR)
        self.play(FadeIn(point_B), Write(label_B))
        self.wait(0.5)

        # Show (-1, 4) → (4, 0)
        point_C = Dot([-1, 4, 0], color=BLUE)
        label_C = MathTex("(-1, 4)", font_size=24).next_to(point_C, UR)
        self.play(FadeIn(point_C), Write(label_C))
        self.wait(0.5)

        arrow_C = Arrow(point_C.get_center(), [4, 0, 0], color=YELLOW)
        self.play(GrowArrow(arrow_C))
        self.wait(0.5)

        point_D = Dot([4, 0, 0], color=RED)
        label_D = MathTex("(4, 0)", font_size=24).next_to(point_D, UR)
        self.play(FadeIn(point_D), Write(label_D))
        self.wait(0.5)

        # Clear arrows and points
        self.play(FadeOut(arrow_A, arrow_C, point_A, point_B, point_C, point_D, label_A, label_B, label_C, label_D))

        # Staircase path from (0, 0)
        origin = Dot([0, 0, 0], color=BLUE)
        label_origin = MathTex("(0, 0)", font_size=24).next_to(origin, DL)
        self.play(FadeIn(origin), Write(label_origin))
        self.wait(0.5)

        step1 = Dot([0, 1, 0], color=RED)
        label_step1 = MathTex("(0, 1)", font_size=24).next_to(step1, UR)
        arrow_step1 = Arrow(origin.get_center(), step1.get_center(), color=YELLOW)
        self.play(GrowArrow(arrow_step1), FadeIn(step1), Write(label_step1))
        self.wait(0.5)

        # Show first few steps
        step2 = Dot([1, 1, 0], color=RED)
        label_step2 = MathTex("(1, 1)", font_size=24).next_to(step2, UR)
        arrow_step2 = Arrow(step1.get_center(), step2.get_center(), color=YELLOW)
        self.play(GrowArrow(arrow_step2), FadeIn(step2), Write(label_step2))
        self.wait(0.5)

        step3 = Dot([1, 2, 0], color=RED)
        label_step3 = MathTex("(1, 2)", font_size=24).next_to(step3, UR)
        arrow_step3 = Arrow(step2.get_center(), step3.get_center(), color=YELLOW)
        self.play(GrowArrow(arrow_step3), FadeIn(step3), Write(label_step3))
        self.wait(0.5)

        # Show (2, 2) → Step 3 → (2, 3)
        point_22 = Dot([2, 2, 0], color=BLUE)
        label_22 = MathTex("(2, 2)", font_size=24).next_to(point_22, UR)
        self.play(FadeIn(point_22), Write(label_22))
        self.wait(0.5)

        arrow_step3_label = Text("Step 3", font_size=24).next_to(arrow_step3, UP)
        self.play(Write(arrow_step3_label))
        self.wait(0.5)

        point_23 = Dot([2, 3, 0], color=RED)
        label_23 = MathTex("(2, 3)", font_size=24).next_to(point_23, UR)
        arrow_22to23 = Arrow(point_22.get_center(), point_23.get_center(), color=YELLOW)
        self.play(GrowArrow(arrow_22to23), FadeIn(point_23), Write(label_23))
        self.wait(0.5)

        # Show intermediate step
        inter_point = Dot([2, 3, 0], color=GREEN)
        label_inter = MathTex("(y, x + 1)", font_size=24).next_to(inter_point, DL)
        self.play(FadeIn(inter_point), Write(label_inter))
        self.wait(0.5)

        # Apply rule again to (2, 3) → (3, 3)
        arrow_23to33 = Arrow([2, 3, 0], [3, 3, 0], color=YELLOW)
        label_step4 = Text("Step 4", font_size=24).next_to(arrow_23to33, UP)
        self.play(GrowArrow(arrow_23to33), Write(label_step4))
        self.wait(0.5)

        point_33 = Dot([3, 3, 0], color=RED)
        label_33 = MathTex("(3, 3)", font_size=24).next_to(point_33, UR)
        self.play(FadeIn(point_33), Write(label_33))
        self.wait(0.5)

        # Show (x+1, y) and (x+1, y+1)
        final_point = Dot([3, 4, 0], color=GREEN)
        label_final = MathTex("(x + 1, y + 1)", font_size=24).next_to(final_point, UR)
        self.play(FadeIn(final_point), Write(label_final))
        self.wait(0.5)

        # Double Step Identity
        double_arrow = Arrow([0, 0, 0], [2, 2, 0], color=ORANGE)
        label_double = Text("Double Step", font_size=24).next_to(double_arrow, UP)
        self.play(GrowArrow(double_arrow), Write(label_double))
        self.wait(0.5)

        # One more step to reach (3, 3)
        final_arrow = Arrow([2, 2, 0], [3, 3, 0], color=YELLOW)
        label_final_step = Text("Final Step", font_size=24).next_to(final_arrow, UP)
        self.play(GrowArrow(final_arrow), Write(label_final_step))
        self.wait(0.5)

        # Final summary
        self.play(FadeOut(title, grid, P, Q, formula, arrow1, arrow2, label_swap, label_plus1, arrow_step1, arrow_step2, arrow_step3, arrow_22to23, arrow_23to33, double_arrow, final_arrow, label_origin, label_step1, label_step2, label_step3, label_22, label_23, label_inter, label_final, arrow_step3_label, label_step4, label_double, label_final_step))
        self.wait(0.5)
