from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Rule 1: Total Preservation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Example 1: [1,2,3,4] -> [5,5]
        orig_list = [1, 2, 3, 4]
        folded_list = [5, 5]
        orig_mob = VGroup(*[Integer(x).scale(0.8) for x in orig_list]).arrange(RIGHT, buff=0.5)
        fold_mob = VGroup(*[Integer(x).scale(0.8) for x in folded_list]).arrange(RIGHT, buff=0.5)
        orig_mob.to_edge(LEFT).shift(DOWN * 0.5)
        fold_mob.to_edge(RIGHT).shift(DOWN * 0.5)

        # Arrows
        arrow1 = Arrow(orig_mob[0].get_top(), fold_mob[0].get_bottom(), buff=0.2)
        arrow2 = Arrow(orig_mob[3].get_top(), fold_mob[0].get_bottom(), buff=0.2)
        arrow3 = Arrow(orig_mob[1].get_top(), fold_mob[1].get_bottom(), buff=0.2)
        arrow4 = Arrow(orig_mob[2].get_top(), fold_mob[1].get_bottom(), buff=0.2)

        # Sum labels
        sum1 = MathTex("1 + 4 = 5").next_to(arrow1, UP)
        sum2 = MathTex("2 + 3 = 5").next_to(arrow3, UP)

        self.play(Write(orig_mob), run_time=0.5)
        self.wait(0.5)
        arrow1.shift(0.0 * RIGHT + -0.42 * UP)  # layout: separation vector
        self.play(Create(arrow1), Create(arrow2), Write(sum1))
        self.wait(0.5)
        arrow3.shift(0.0 * RIGHT + -0.42 * UP)  # layout: separation vector
        self.play(Create(arrow3), Create(arrow4), Write(sum2))
        self.wait(0.5)

        # Folded result
        self.play(Transform(orig_mob, fold_mob), run_time=0.5)
        self.wait(0.5)

        # Sum counters
        orig_sum = Integer(10).scale(0.8)
        fold_sum = Integer(10).scale(0.8)
        orig_sum.next_to(orig_mob, DOWN)
        fold_sum.next_to(fold_mob, DOWN)
        self.play(Write(orig_sum), Write(fold_sum))
        self.wait(0.5)

        # Checkmark
        check = Tex(r"$\checkmark$").scale(1.2).next_to(fold_sum, RIGHT)
        self.play(Write(check))
        self.wait(1)

        # Example 2: [10, 20, 30]
        self.play(FadeOut(orig_mob, fold_mob, arrow1, arrow2, arrow3, arrow4, sum1, sum2, orig_sum, fold_sum, check))
        list2 = [10, 20, 30]
        mob2 = VGroup(*[Integer(x).scale(0.8) for x in list2]).arrange(RIGHT, buff=0.5)
        mob2.to_edge(LEFT).shift(DOWN * 0.5)
        self.play(Write(mob2))
        self.wait(0.5)

        arrow_10_30 = Arrow(mob2[0].get_top(), mob2[2].get_bottom(), buff=0.2)
        sum_label = MathTex("10 + 30 = 40").next_to(arrow_10_30, UP)
        self.play(Create(arrow_10_30), Write(sum_label))
        self.wait(0.5)

        # Slide middle element
        slide_arrow = Arrow(mob2[1].get_right(), mob2[1].get_right() + RIGHT * 2, buff=0.2)
        self.play(Create(slide_arrow))
        self.wait(0.5)

        # Final result blocks
        block40 = Rectangle(width=1, height=0.6).set_fill(BLUE, opacity=0.5).scale(0.8)
        block20 = Rectangle(width=1, height=0.6).set_fill(GREEN, opacity=0.5).scale(0.8)
        result_mob = VGroup(block40, block20).arrange(RIGHT, buff=0.5).to_edge(RIGHT).shift(DOWN * 0.5)
        self.play(Transform(mob2[0], block40), Transform(mob2[1], block20), Transform(mob2[2], block20))
        self.wait(0.5)

        # Example 3: [1,2,3] (odd length)
        self.play(FadeOut(mob2, arrow_10_30, sum_label, slide_arrow))
        list3 = [1, 2, 3]
        mob3 = VGroup(*[Integer(x).scale(0.8) for x in list3]).arrange(RIGHT, buff=0.5)
        mob3.to_edge(LEFT).shift(DOWN * 0.5)
        self.play(Write(mob3))
        self.wait(0.5)

        arrow_1_3 = Arrow(mob3[0].get_top(), mob3[2].get_bottom(), buff=0.2)
        sum_label3 = MathTex("1 + 3 = 4").next_to(arrow_1_3, UP)
        self.play(Create(arrow_1_3), Write(sum_label3))
        self.wait(0.5)

        # Middle stays
        middle = mob3[1].copy()
        self.play(middle.animate.shift(RIGHT * 2))
        self.wait(0.5)

        # Final result
        block4 = Rectangle(width=1, height=0.6).set_fill(BLUE, opacity=0.5).scale(0.8)
        block2 = Rectangle(width=1, height=0.6).set_fill(GREEN, opacity=0.5).scale(0.8)
        result3 = VGroup(block4, block2).arrange(RIGHT, buff=0.5).to_edge(RIGHT).shift(DOWN * 0.5)
        self.play(Transform(mob3[0], block4), Transform(mob3[1], block2), Transform(mob3[2], block2))
        self.wait(0.5)

        # Example 4: [1,2,3,4,5]
        self.play(FadeOut(mob3, arrow_1_3, sum_label3))
        list4 = [1, 2, 3, 4, 5]
        mob4 = VGroup(*[Integer(x).scale(0.8) for x in list4]).arrange(RIGHT, buff=0.5)
        mob4.to_edge(LEFT).shift(DOWN * 0.5)
        self.play(Write(mob4))
        self.wait(0.5)

        arrow_1_5 = Arrow(mob4[0].get_top(), mob4[4].get_bottom(), buff=0.2)
        sum_label4a = MathTex("1 + 5 = 6").next_to(arrow_1_5, UP)
        self.play(Create(arrow_1_5), Write(sum_label4a))
        self.wait(0.5)

        arrow_2_4 = Arrow(mob4[1].get_top(), mob4[3].get_bottom(), buff=0.2)
        sum_label4b = MathTex("2 + 4 = 6").next_to(arrow_2_4, UP)
        self.play(Create(arrow_2_4), Write(sum_label4b))
        self.wait(0.5)

        # Middle stays
        middle4 = mob4[2].copy()
        self.play(middle4.animate.shift(RIGHT * 2))
        self.wait(0.5)

        # Final result
        block6a = Rectangle(width=1, height=0.6).set_fill(BLUE, opacity=0.5).scale(0.8)
        block6b = Rectangle(width=1, height=0.6).set_fill(BLUE, opacity=0.5).scale(0.8)
        block3 = Rectangle(width=1, height=0.6).set_fill(GREEN, opacity=0.5).scale(0.8)
        result4 = VGroup(block6a, block6b, block3).arrange(RIGHT, buff=0.5).to_edge(RIGHT).shift(DOWN * 0.5)
        self.play(Transform(mob4[0], block6a), Transform(mob4[1], block6b), Transform(mob4[2], block3), Transform(mob4[3], block6b), Transform(mob4[4], block6a))
        self.wait(0.5)

        # Example 5: [0,0,0]
        self.play(FadeOut(mob4, arrow_1_5, sum_label4a, arrow_2_4, sum_label4b))
        list5 = [0, 0, 0]
        mob5 = VGroup(*[Integer(x).scale(0.8) for x in list5]).arrange(RIGHT, buff=0.5)
        mob5.to_edge(LEFT).shift(DOWN * 0.5)
        self.play(Write(mob5))
        self.wait(0.5)

        arrow_0_0 = Arrow(mob5[0].get_top(), mob5[2].get_bottom(), buff=0.2)
        sum_label5 = MathTex("0 + 0 = 0").next_to(arrow_0_0, UP)
        self.play(Create(arrow_0_0), Write(sum_label5))
        self.wait(0.5)

        # Middle stays
        middle5 = mob5[1].copy()
        self.play(middle5.animate.shift(RIGHT * 2))
        self.wait(0.5)

        # Final result
        block0a = Rectangle(width=1, height=0.6).set_fill(BLUE, opacity=0.5).scale(0.8)
        block0b = Rectangle(width=1, height=0.6).set_fill(GREEN, opacity=0.5).scale(0.8)
        result5 = VGroup(block0a, block0b).arrange(RIGHT, buff=0.5).to_edge(RIGHT).shift(DOWN * 0.5)
        self.play(Transform(mob5[0], block0a), Transform(mob5[1], block0b), Transform(mob5[2], block0b))
        self.wait(0.5)

        # Example 6: Length shrinking
        self.play(FadeOut(mob5, arrow_0_0, sum_label5, middle5))
        list6 = [1, 2, 3, 4, 5, 6]
        mob6 = VGroup(*[Integer(x).scale(0.8) for x in list6]).arrange(RIGHT, buff=0.5)
        mob6.to_edge(LEFT).shift(DOWN * 0.5)
        self.play(Write(mob6))
        self.wait(0.5)

        # Folded result
        folded6 = [7, 7, 7]
        fold_mob6 = VGroup(*[Integer(x).scale(0.8) for x in folded6]).arrange(RIGHT, buff=0.5)
        fold_mob6.to_edge(RIGHT).shift(DOWN * 0.5)
        self.play(Transform(mob6, fold_mob6))
        self.wait(0.5)

        # Length label
        length_label = MathTex(r"\text{Length } \rightarrow \frac{n}{2}").next_to(fold_mob6, DOWN)
        self.play(Write(length_label))
        self.wait(1)

        # Example 7: Sum preservation
        self.play(FadeOut(mob6, fold_mob6, length_label))
        list7 = [1, 2, 3, 4]
        mob7 = VGroup(*[Integer(x).scale(0.8) for x in list7]).arrange(RIGHT, buff=0.5)
        mob7.to_edge(LEFT).shift(DOWN * 0.5)
        self.play(Write(mob7))
        self.wait(0.5)

        # Folded
        folded7 = [5, 5]
        fold_mob7 = VGroup(*[Integer(x).scale(0.8) for x in folded7]).arrange(RIGHT, buff=0.5)
        fold_mob7.to_edge(RIGHT).shift(DOWN * 0.5)
        self.play(Transform(mob7, fold_mob7))
        self.wait(0.5)

        # Sum labels
        sum_orig = MathTex("1 + 2 + 3 + 4 = 10").next_to(mob7[0], DOWN)
        sum_fold = MathTex("5 + 5 = 10").next_to(mob7[1], DOWN)
        self.play(Write(sum_orig), Write(sum_fold))
        self.wait(1)

        # Example 8: [5,5,5,5]
        self.play(FadeOut(mob7, sum_orig, sum_fold))
        list8 = [5, 5, 5, 5]
        mob8 = VGroup(*[Integer(x).scale(0.8) for x in list8]).arrange(RIGHT, buff=0.5)
        mob8.to_edge(LEFT).shift(DOWN * 0.5)
        self.play(Write(mob8))
        self.wait(0.5)

        arrow_5_5 = Arrow(mob8[0].get_top(), mob8[3].get_bottom(), buff=0.2)
        sum_label8a = MathTex("5 + 5 = 10").next_to(arrow_5_5, UP)
        self.play(Create(arrow_5_5), Write(sum_label8a))
        self.wait(0.5)

        arrow_5_5b = Arrow(mob8[1].get_top(), mob8[2].get_bottom(), buff=0.2)
        sum_label8b = MathTex("5 + 5 = 10").next_to(arrow_5_5b, UP)
        self.play(Create(arrow_5_5b), Write(sum_label8b))
        self.wait(0.5)

        # Final result
        block10a = Rectangle(width=1, height=0.6).set_fill(BLUE, opacity=0.5).scale(0.8)
        block10b = Rectangle(width=1, height=0.6).set_fill(BLUE, opacity=0.5).scale(0.8)
        result8 = VGroup(block10a, block10b).arrange(RIGHT, buff=0.5).to_edge(RIGHT).shift(DOWN * 0.5)
        self.play(Transform(mob8[0], block10a), Transform(mob8[1], block10b), Transform(mob8[2], block10b), Transform(mob8[3], block10a))
        self.wait(0.5)

        # Example 9: [1,2] -> [3]
        self.play(FadeOut(mob8, arrow_5_5, sum_label8a, arrow_5_5b, sum_label8b))
        list9 = [1, 2]
        mob9 = VGroup(*[Integer(x).scale(0.8) for x in list9]).arrange(RIGHT, buff=0.5)
        mob9.to_edge(LEFT).shift(DOWN * 0.5)
        self.play(Write(mob9))
        self.wait(0.5)

        arrow_1_2 = Arrow(mob9[0].get_top(), mob9[1].get_bottom(), buff=0.2)
        sum_label9 = MathTex("1 + 2 = 3").next_to(arrow_1_2, UP)
        self.play(Create(arrow_1_2), Write(sum_label9))
        self.wait(0.5)

        # Final result
        block3 = Rectangle(width=1, height=0.6).set_fill(BLUE, opacity=0.5).scale(0.8)
        result9 = VGroup(block3).to_edge(RIGHT).shift(DOWN * 0.5)
        self.play(Transform(mob9[0], block3), Transform(mob9[1], block3))
        self.wait(0.5)

        # Final summary
        self.play(FadeOut(mob9, arrow_1_2, sum_label9, result9))
        self.wait(0.5)
        self.play(FadeOut(title))
