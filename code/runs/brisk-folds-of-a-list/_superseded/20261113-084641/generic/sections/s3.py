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
        orig_group = VGroup(*orig_nums).arrange(RIGHT, buff=0.5)
        orig_group.to_edge(LEFT).shift(UP * 0.5)

        # Sum label
        orig_sum_label = MathTex("1 + 2 + 3 + 4 =", font_size=24)
        orig_sum_label.next_to(orig_group, DOWN, buff=0.3)
        orig_sum_value = Integer(10, font_size=24)
        orig_sum_value.next_to(orig_sum_label, RIGHT, buff=0.2)

        self.play(Write(orig_group), run_time=1)
        self.play(Write(orig_sum_label), Write(orig_sum_value))
        self.wait(1)

        # Folding animation
        folded_nums = [5, 5]
        fold_group = VGroup(*[Integer(n, font_size=32) for n in folded_nums])
        fold_group.arrange(RIGHT, buff=0.5)
        fold_group.to_edge(RIGHT).shift(UP * 0.5)

        # Arrows showing pairing
        arrows = VGroup()
        for i in range(2):
            start = orig_group[i].get_center()
            end = fold_group[i].get_center()
            arrow = Arrow(start, end, buff=0.1, color=YELLOW)
            arrows.add(arrow)

        self.play(Create(arrows), run_time=1)
        self.wait(0.5)

        # Show folded result
        self.play(TransformMatchingShapes(VGroup(*orig_nums), fold_group))
        self.wait(1)

        # Folded sum label
        fold_sum_label = MathTex("5 + 5 =", font_size=24)
        fold_sum_label.next_to(fold_group, DOWN, buff=0.3)
        fold_sum_value = Integer(10, font_size=24)
        fold_sum_value.next_to(fold_sum_label, RIGHT, buff=0.2)

        self.play(Write(fold_sum_label), Write(fold_sum_value))
        self.wait(1.5)

        # Checkmark
        check = Tex(r"$\checkmark$", font_size=40).set_color(GREEN)
        check.next_to(fold_sum_label, RIGHT, buff=0.5)
        self.play(Write(check))
        self.wait(1)

        # Key phrase
        phrase = Text("Total Preserved", font_size=24).next_to(check, RIGHT, buff=0.5)
        self.play(Write(phrase))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(Group(title, orig_group, orig_sum_label, orig_sum_value,
                                arrows, fold_group, fold_sum_label, fold_sum_value, check, phrase)))
        self.wait(0.5)
