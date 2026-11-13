from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Brisk Folds: Halving Lists with Sum Preservation", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Initial list [1, 2, 3]
        original_list = [1, 2, 3]
        mobs = [Integer(x, font_size=36) for x in original_list]
        mobs_group = Group(*mobs).arrange(RIGHT, buff=0.5)
        mobs_group.move_to(ORIGIN)
        self.play(Write(mobs_group))
        self.wait(1)

        # Arrows from 1 and 3
        arrow1 = Arrow(start=mobs[0].get_left(), end=mobs[2].get_right(), buff=0.1, color=YELLOW)
        arrow2 = Arrow(start=mobs[2].get_right(), end=mobs[0].get_left(), buff=0.1, color=YELLOW)
        self.play(Create(arrow1), Create(arrow2))
        self.wait(1)

        # Sum 1 + 3 = 4
        sum_text = MathTex("1 + 3 =", "4", font_size=36)
        sum_text.next_to(mobs_group, DOWN, buff=0.5)
        self.play(Write(sum_text))
        self.wait(1)

        # Middle element '2' slides to the right
        middle_mob = mobs[1]
        final_list = [4, 2]
        result_mobs = [Integer(x, font_size=36) for x in final_list]
        result_group = Group(*result_mobs).arrange(RIGHT, buff=0.5)
        result_group.move_to(ORIGIN)

        self.play(
            middle_mob.animate.move_to(result_mobs[1].get_center()),
            FadeOut(arrow1),
            FadeOut(arrow2),
            Transform(sum_text, MathTex("4", ",", "2", font_size=36).next_to(mobs_group, DOWN, buff=0.5)),
        )
        self.wait(1)

        # Show result list
        self.play(Transform(mobs_group, result_group))
        self.wait(1)

        # Label 'Middle stays'
        label = Text("Middle stays", font_size=24).next_to(result_group, DOWN, buff=0.5)
        self.play(Write(label))
        self.wait(2)

        # Clean up
        self.play(
            FadeOut(title),
            FadeOut(mobs_group),
            FadeOut(sum_text),
            FadeOut(label)
        )
        self.wait(0.5)
