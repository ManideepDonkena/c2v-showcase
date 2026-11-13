from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Rule 1: Total Preservation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Original list
        original_list = [1, 2, 3, 4]
        orig_nums = [Integer(n, font_size=32) for n in original_list]
        orig_group = Group(*orig_nums).arrange(RIGHT, buff=0.5)
        orig_group.to_edge(LEFT).shift(UP * 0.5)

        # Sum label
        orig_sum_label = Text("Sum =", font_size=24).next_to(orig_group, DOWN, buff=0.3)
        orig_sum_tex = MathTex("10", font_size=32).next_to(orig_sum_label, RIGHT, buff=0.2)
        orig_sum_group = Group(orig_sum_label, orig_sum_tex)

        # Folded list
        folded_list = [5, 5]
        fold_nums = [Integer(n, font_size=32) for n in folded_list]
        fold_group = Group(*fold_nums).arrange(RIGHT, buff=0.5)
        fold_group.to_edge(RIGHT).shift(UP * 0.5)
        
        # Folded sum label
        fold_sum_label = Text("Sum =", font_size=24).next_to(fold_group, DOWN, buff=0.3)
        fold_sum_tex = MathTex("10", font_size=32).next_to(fold_sum_label, RIGHT, buff=0.2)
        fold_sum_group = Group(fold_sum_label, fold_sum_tex)

        # Show original list and sum
        self.play(Write(orig_group))
        self.play(Write(orig_sum_group))
        self.wait(1)

        # Show folding process
        # Draw arrows from pairs
        arrow1 = Arrow(orig_nums[0].get_top(), fold_nums[0].get_bottom(), buff=0.1, color=YELLOW)
        arrow2 = Arrow(orig_nums[3].get_top(), fold_nums[0].get_bottom(), buff=0.1, color=YELLOW)
        arrow3 = Arrow(orig_nums[1].get_top(), fold_nums[1].get_bottom(), buff=0.1, color=YELLOW)
        arrow4 = Arrow(orig_nums[2].get_top(), fold_nums[1].get_bottom(), buff=0.1, color=YELLOW)

        self.play(Create(arrow1), Create(arrow2))
        self.wait(0.5)
        self.play(Create(arrow3), Create(arrow4))
        self.wait(0.5)

        # Show folded list
        self.play(Write(fold_group))
        self.play(Write(fold_sum_group))
        self.wait(1)

        # Checkmark
        check = Tex(r"$\checkmark$").scale(2).set_color(GREEN).next_to(fold_sum_label, LEFT)
        self.play(Write(check))
        self.wait(0.5)

        # Text overlay: "Total Preserved"
        total_preserved = Text("Total Preserved", font_size=24).to_edge(DOWN)
        self.play(Write(total_preserved))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(orig_group),
            FadeOut(orig_sum_group),
            FadeOut(fold_group),
            FadeOut(fold_sum_group),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(arrow3),
            FadeOut(arrow4),
            FadeOut(check),
            FadeOut(total_preserved)
        )
