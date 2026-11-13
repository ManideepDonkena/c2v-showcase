from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Brisk Folds: Halving Lists with Sum Preservation", font_size=30)
        title.to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Initial list [1, 2, 3]
        original_list = [1, 2, 3]
        list_mobs = [Integer(num, font_size=36) for num in original_list]
        list_group = VGroup(*list_mobs).arrange(RIGHT, buff=0.5)
        list_group.move_to(DOWN * 0.5)
        self.play(Write(list_group))
        self.wait(0.5)

        # Arrows connecting 1 and 3
        arrow1 = Arrow(list_mobs[0].get_top(), list_mobs[2].get_top(), buff=0.1, stroke_width=3)
        arrow2 = Arrow(list_mobs[2].get_top(), list_mobs[0].get_top(), buff=0.1, stroke_width=3)
        arrow1.shift(0.0 * RIGHT + 0.28 * UP)  # layout: separation vector
        arrow2.shift(0.0 * RIGHT + 0.28 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait(0.5)

        # Sum 1 + 3 = 4
        sum_text = MathTex("1 + 3 = 4", font_size=36)
        sum_text.next_to(list_group, UP, buff=0.5)
        self.play(Write(sum_text))
        self.wait(0.5)

        # Middle element '2' slides to the right
        middle_mob = list_mobs[1]
        result_list = [4, 2]
        result_mobs = [Integer(num, font_size=36) for num in result_list]
        result_group = VGroup(*result_mobs).arrange(RIGHT, buff=0.5)
        result_group.move_to(DOWN * 0.5)

        self.play(
            middle_mob.animate.shift(RIGHT * 2),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(sum_text)
        )
        self.wait(0.5)

        # Show final list [4, 2]
        self.play(Transform(list_group, result_group))
        self.wait(0.5)

        # Label "Middle stays"
        label = Text("Middle stays", font_size=28)
        label.next_to(result_group, UP, buff=0.5)
        self.play(Write(label))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(list_group),
            FadeOut(label)
        )
        self.wait(0.5)
