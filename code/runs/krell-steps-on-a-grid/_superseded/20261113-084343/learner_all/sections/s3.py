from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Staircase Path from Origin", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(x_range=[-1, 4], y_range=[-1, 4], 
                           axis_config={"stroke_color": GREY, "stroke_width": 1})
        grid.set_opacity(0.5)
        self.play(Create(grid))
        self.wait(0.5)
        
        # Start point
        origin = Dot([0, 0, 0], color=RED)
        orig_label = MathTex("(0, 0)", font_size=24).next_to(origin, DOWN)
        self.play(FadeIn(origin), Write(orig_label))
        self.wait(0.5)

        # Step 1: (0,0) -> (0,1)
        step1_arrow = Arrow([0, 0, 0], [0, 1, 0], buff=0, color=YELLOW)
        step1_label = MathTex("(0, 1)", font_size=24).next_to(step1_arrow.get_end(), UP)
        self.play(GrowArrow(step1_arrow), Write(step1_label))
        self.wait(0.5)

        # Step 2: (0,1) -> (1,1)
        step2_arrow = Arrow([0, 1, 0], [1, 1, 0], buff=0, color=YELLOW)
        step2_label = MathTex("(1, 1)", font_size=24).next_to(step2_arrow.get_end(), UP)
        self.play(GrowArrow(step2_arrow), Write(step2_label))
        self.wait(0.5)

        # Step 3: (1,1) -> (1,2)
        step3_arrow = Arrow([1, 1, 0], [1, 2, 0], buff=0, color=YELLOW)
        step3_label = MathTex("(1, 2)", font_size=24).next_to(step3_arrow.get_end(), UP)
        step3_arrow.shift(0.53 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(GrowArrow(step3_arrow), Write(step3_label))
        self.wait(0.5)

        # Step 4: (1,2) -> (2,2)
        step4_arrow = Arrow([1, 2, 0], [2, 2, 0], buff=0, color=YELLOW)
        step4_label = MathTex("(2, 2)", font_size=24).next_to(step4_arrow.get_end(), UP)
        self.play(GrowArrow(step4_arrow), Write(step4_label))
        self.wait(0.5)

        # Show formula
        formula = MathTex(r"(y, x + 1)", font_size=30).to_edge(UP).shift(DOWN * 1.2)
        self.play(Write(formula))
        self.wait(0.5)

        # Show transformation of (2,2) to (2,3)
        point_22 = Dot([2, 2, 0], color=GREEN)
        label_22 = MathTex("(2, 2)", font_size=24).next_to(point_22, DOWN)
        self.play(FadeIn(point_22), Write(label_22))
        self.wait(0.5)

        # Swap and add
        swap_arrow = Arrow([2, 2, 0], [2, 3, 0], buff=0, color=BLUE)
        swap_label = MathTex("(2, 3)", font_size=24).next_to(swap_arrow.get_end(), UP)
        swap_label.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        swap_arrow.shift(0.53 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(GrowArrow(swap_arrow), Write(swap_label))
        self.wait(0.5)

        # Show (−1, 4) transformation
        point_neg14 = Dot([-1, 4, 0], color=GREEN)
        label_neg14 = MathTex("(-1, 4)", font_size=24).next_to(point_neg14, DOWN)
        self.play(FadeIn(point_neg14), Write(label_neg14))
        self.wait(0.5)

        # Swap and add
        swap_arrow2 = Arrow([-1, 4, 0], [4, 0, 0], buff=0, color=BLUE)
        swap_label2 = MathTex("(4, 0)", font_size=24).next_to(swap_arrow2.get_end(), UP)
        self.play(GrowArrow(swap_arrow2), Write(swap_label2))
        self.wait(0.5)

        # Show the pattern
        pattern_text = Text("x stays same, y increases", font_size=24).to_edge(DOWN)
        self.play(Write(pattern_text))
        self.wait(1)

        # Show next step from (2, 2) to (2, 3)
        self.play(FadeOut(pattern_text))
        step5_arrow = Arrow([2, 2, 0], [2, 3, 0], buff=0, color=YELLOW)
        step5_label = MathTex("(2, 3)", font_size=24).next_to(step5_arrow.get_end(), UP)
        self.play(GrowArrow(step5_arrow), Write(step5_label))
        self.wait(0.5)

        # Next step from (2, 3) to (3, 3)
        step6_arrow = Arrow([2, 3, 0], [3, 3, 0], buff=0, color=YELLOW)
        step6_label = MathTex("(3, 3)", font_size=24).next_to(step6_arrow.get_end(), UP)
        self.play(GrowArrow(step6_arrow), Write(step6_label))
        self.wait(0.5)

        # Show intermediate (y, x+1) then apply rule again
        inter_point = Dot([2, 3, 0], color=ORANGE)
        inter_label = MathTex("(2, 3)", font_size=24).next_to(inter_point, DOWN)
        self.play(FadeIn(inter_point), Write(inter_label))
        self.wait(0.5)

        # Apply rule again: (2,3) -> swap to (3,2) then add 1 to second -> (3,3)
        final_arrow = Arrow([2, 3, 0], [3, 3, 0], buff=0, color=BLUE)
        final_label = MathTex("(3, 3)", font_size=24).next_to(final_arrow.get_end(), UP)
        self.play(GrowArrow(final_arrow), Write(final_label))
        self.wait(0.5)

        # Show Double Step Identity
        identity_text = Text("Double Krell Step = (+1,+1)", font_size=24).to_edge(DOWN)
        self.play(Write(identity_text))
        self.wait(1)

        # Total steps: 2 + 2 + 1 = 5
        total_text = Text("Total Steps: 5", font_size=24).next_to(identity_text, DOWN)
        self.play(Write(total_text))
        self.wait(1)

        self.play(FadeOut(title), FadeOut(grid), FadeOut(origin), FadeOut(orig_label),
                  FadeOut(step1_arrow), FadeOut(step1_label),
                  FadeOut(step2_arrow), FadeOut(step2_label),
                  FadeOut(step3_arrow), FadeOut(step3_label),
                  FadeOut(step4_arrow), FadeOut(step4_label),
                  FadeOut(formula),
                  FadeOut(point_22), FadeOut(label_22),
                  FadeOut(swap_arrow), FadeOut(swap_label),
                  FadeOut(point_neg14), FadeOut(label_neg14),
                  FadeOut(swap_arrow2), FadeOut(swap_label2),
                  FadeOut(inter_point), FadeOut(inter_label),
                  FadeOut(final_arrow), FadeOut(final_label),
                  FadeOut(identity_text), FadeOut(total_text))
