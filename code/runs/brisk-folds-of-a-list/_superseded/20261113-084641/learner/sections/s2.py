from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Brisk Folds: Halving Lists with Sum Preservation", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Example 1: [1, 2, 3]
        list1 = [1, 2, 3]
        mobs1 = [Integer(x, font_size=36) for x in list1]
        mobs1 = VGroup(*mobs1).arrange(RIGHT, buff=0.5)
        mobs1.move_to(ORIGIN)
        self.play(Write(mobs1))
        self.wait(0.5)

        # Arrows from 1 to 3
        arrow1 = Arrow(mobs1[0].get_right(), mobs1[2].get_left(), buff=0.1, color=YELLOW)
        sum_label1 = MathTex("1 + 3 = 4", font_size=30).next_to(arrow1, UP)
        self.play(Create(arrow1), Write(sum_label1))
        self.wait(0.5)

        # Middle element slides to the right
        middle_mob = mobs1[1].copy()
        self.play(middle_mob.animate.move_to(mobs1.get_right() + RIGHT * 1.5))
        self.wait(0.5)

        # Result: [4, 2]
        result1 = VGroup(
            Integer(4, font_size=36),
            Integer(2, font_size=36)
        ).arrange(RIGHT, buff=0.5).move_to(ORIGIN + DOWN * 1.5)
        self.play(FadeOut(mobs1), FadeOut(arrow1), FadeOut(sum_label1))
        self.play(Write(result1))
        self.wait(0.5)

        # Label: Middle stays
        label = Text("Middle stays", font_size=24).next_to(result1, UP)
        self.play(Write(label))
        self.wait(1)

        # Fade out
        self.play(FadeOut(title), FadeOut(result1), FadeOut(label))

        # Example 2: [10, 20, 30]
        list2 = [10, 20, 30]
        mobs2 = [Integer(x, font_size=36) for x in list2]
        mobs2 = VGroup(*mobs2).arrange(RIGHT, buff=0.5)
        mobs2.move_to(ORIGIN)
        self.play(Write(mobs2))
        self.wait(0.5)

        arrow2 = Arrow(mobs2[0].get_right(), mobs2[2].get_left(), buff=0.1, color=YELLOW)
        sum_label2 = MathTex("10 + 30 = 40", font_size=30).next_to(arrow2, UP)
        self.play(Create(arrow2), Write(sum_label2))
        self.wait(0.5)

        # Middle slides alone
        middle_mob2 = mobs2[1].copy()
        self.play(middle_mob2.animate.move_to(mobs2.get_right() + RIGHT * 1.5))
        self.wait(0.5)

        # Final result as two blocks: [40] and [20]
        block1 = Rectangle(width=1, height=1).set_fill(BLUE, opacity=0.5).move_to(LEFT)
        block2 = Rectangle(width=1, height=1).set_fill(GREEN, opacity=0.5).move_to(RIGHT)
        text1 = MathTex("40", font_size=30).move_to(block1.get_center())
        text2 = MathTex("20", font_size=30).move_to(block2.get_center())
        self.play(FadeOut(mobs2), FadeOut(arrow2), FadeOut(sum_label2))
        self.play(Create(block1), Create(block2), Write(text1), Write(text2))
        self.wait(1)

        # Fade out
        self.play(FadeOut(block1), FadeOut(block2), FadeOut(text1), FadeOut(text2))

        # Example 3: [1, 2, 3, 4, 5]
        list3 = [1, 2, 3, 4, 5]
        mobs3 = [Integer(x, font_size=36) for x in list3]
        mobs3 = VGroup(*mobs3).arrange(RIGHT, buff=0.5)
        mobs3.move_to(ORIGIN)
        self.play(Write(mobs3))
        self.wait(0.5)

        # Arrows: 1+5 and 2+4
        arrow3a = Arrow(mobs3[0].get_right(), mobs3[4].get_left(), buff=0.1, color=YELLOW)
        sum_label3a = MathTex("1 + 5 = 6", font_size=30).next_to(arrow3a, UP)
        arrow3b = Arrow(mobs3[1].get_right(), mobs3[3].get_left(), buff=0.1, color=YELLOW)
        sum_label3b = MathTex("2 + 4 = 6", font_size=30).next_to(arrow3b, UP)

        self.play(Create(arrow3a), Write(sum_label3a))
        self.wait(0.5)
        self.play(Create(arrow3b), Write(sum_label3b))
        self.wait(0.5)

        # Middle stays alone
        middle_mob3 = mobs3[2].copy()
        self.play(middle_mob3.animate.move_to(mobs3.get_right() + RIGHT * 1.5))
        self.wait(0.5)

        # Final result: [6, 6, 3]
        result3 = VGroup(
            Integer(6, font_size=36),
            Integer(6, font_size=36),
            Integer(3, font_size=36)
        ).arrange(RIGHT, buff=0.5).move_to(ORIGIN + DOWN * 1.5)
        self.play(FadeOut(mobs3), FadeOut(arrow3a), FadeOut(sum_label3a), FadeOut(arrow3b), FadeOut(sum_label3b))
        self.play(Write(result3))
        self.wait(1)

        # Fade out
        self.play(FadeOut(result3))

        # Example 4: [0, 0, 0]
        list4 = [0, 0, 0]
        mobs4 = [Integer(x, font_size=36) for x in list4]
        mobs4 = VGroup(*mobs4).arrange(RIGHT, buff=0.5)
        mobs4.move_to(ORIGIN)
        self.play(Write(mobs4))
        self.wait(0.5)

        arrow4 = Arrow(mobs4[0].get_right(), mobs4[2].get_left(), buff=0.1, color=YELLOW)
        sum_label4 = MathTex("0 + 0 = 0", font_size=30).next_to(arrow4, UP)
        self.play(Create(arrow4), Write(sum_label4))
        self.wait(0.5)

        # Middle stays alone
        middle_mob4 = mobs4[1].copy()
        self.play(middle_mob4.animate.move_to(mobs4.get_right() + RIGHT * 1.5))
        self.wait(0.5)

        # Final result: [0, 0]
        result4 = VGroup(
            Integer(0, font_size=36),
            Integer(0, font_size=36)
        ).arrange(RIGHT, buff=0.5).move_to(ORIGIN + DOWN * 1.5)
        self.play(FadeOut(mobs4), FadeOut(arrow4), FadeOut(sum_label4))
        self.play(Write(result4))
        self.wait(1)

        # Final text
        final_text = Text("The sum of the paired ends is 0 + 0 = 0. The middle element remains 0. The result is [0, 0].", font_size=24)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1)

        # Fade out
        self.play(FadeOut(result4), FadeOut(final_text))
