from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Brisk Folds: Halving Lists with Sum Preservation", font_size=30)
        title.to_edge(UP, buff=0.2)

        # Original list
        original_list = [1, 2, 3, 4]
        original_mobs = [Integer(x, font_size=36) for x in original_list]
        original_group = VGroup(*original_mobs).arrange(RIGHT, buff=0.5)
        original_group.move_to(DOWN * 1)

        # Sum label
        sum_label = Text("Sum = ", font_size=24)
        sum_value = Integer(10, font_size=24)
        sum_group = VGroup(sum_label, sum_value).arrange(RIGHT, buff=0.2)
        sum_group.next_to(original_group, DOWN, buff=0.3)

        # Folded list
        folded_list = [5, 5]
        folded_mobs = [Integer(x, font_size=36) for x in folded_list]
        folded_group = VGroup(*folded_mobs).arrange(RIGHT, buff=0.5)
        folded_group.move_to(UP * 1)

        # Folded sum label
        folded_sum_label = Text("Sum = ", font_size=24)
        folded_sum_value = Integer(10, font_size=24)
        folded_sum_group = VGroup(folded_sum_label, folded_sum_value).arrange(RIGHT, buff=0.2)
        folded_sum_group.next_to(folded_group, DOWN, buff=0.3)

        # Arrows showing pairing
        arrows = []
        for i in range(2):
            start = original_mobs[i].get_center()
            end = original_mobs[3-i].get_center()
            arrow = Arrow(start, end, color=YELLOW, tip_length=0.2)
            arrows.append(arrow)

        # Animation
        self.play(Write(title))
        self.wait(0.5)

        self.play(Write(original_group), Write(sum_group))
        self.wait(1)

        self.play(Write(folded_group), Write(folded_sum_group))
        self.wait(1)

        self.play(*[Create(a) for a in arrows])
        self.wait(1)
        
        # Show sum counters
        original_sum_counter = always_redraw(lambda: Integer(10, font_size=24).next_to(sum_value, RIGHT, buff=0.2))
        folded_sum_counter = always_redraw(lambda: Integer(10, font_size=24).next_to(folded_sum_value, RIGHT, buff=0.2))

        self.play(Write(original_sum_counter), Write(folded_sum_counter))
        self.wait(1)

        # Checkmark
        check = Tex(r"$\checkmark$").scale(2)
        check.next_to(folded_sum_group, RIGHT, buff=0.5)
        self.play(Write(check))
        self.wait(1.5)

        # Narration text
        narration = Text("Total Preserved", font_size=24)
        narration.to_edge(DOWN, buff=0.3)
        self.play(Write(narration))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(original_group), FadeOut(folded_group),
                  FadeOut(sum_group), FadeOut(folded_sum_group),
                  FadeOut(arrows), FadeOut(original_sum_counter),
                  FadeOut(folded_sum_counter), FadeOut(check), FadeOut(narration))
        self.wait(0.5)
