from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Brisk Folds: Halving Lists with Sum Preservation", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Section 1: [1, 2, 3, 4]
        list1 = [1, 2, 3, 4]
        mob_list1 = [Integer(x, font_size=28) for x in list1]
        mob_list1 = VGroup(*mob_list1).arrange(RIGHT, buff=0.5)
        mob_list1.move_to(ORIGIN)
        self.play(Write(mob_list1))
        self.wait(0.5)

        # Arrows
        arrow1 = Arrow(mob_list1[0].get_left(), mob_list1[3].get_right(), buff=0.1, color=YELLOW)
        arrow2 = Arrow(mob_list1[1].get_left(), mob_list1[2].get_right(), buff=0.1, color=YELLOW)
        self.play(Create(arrow1), Create(arrow2))
        self.wait(0.5)

        # Labels
        label1 = MathTex("1 + 4 = 5", font_size=28).next_to(arrow1, UP)
        label1.shift([-0.17, 0.0, 0])
        label2 = MathTex("2 + 3 = 5", font_size=28).next_to(arrow2, UP)
        self.play(Write(label1), Write(label2))
        self.wait(0.5)

        # Collapse
        result1 = [5, 5]
        mob_result1 = [Integer(x, font_size=28) for x in result1]
        mob_result1 = VGroup(*mob_result1).arrange(RIGHT, buff=0.5)
        mob_result1.move_to(ORIGIN)
        self.play(Transform(mob_list1, mob_result1))
        self.wait(1)

        # Section 2: [10, 20, 30]
        self.play(FadeOut(arrow1), FadeOut(arrow2), FadeOut(label1), FadeOut(label2))
        list2 = [10, 20, 30]
        mob_list2 = [Integer(x, font_size=28) for x in list2]
        mob_list2 = VGroup(*mob_list2).arrange(RIGHT, buff=0.5)
        mob_list2.move_to(ORIGIN)
        self.play(Transform(mob_result1, mob_list2))
        self.wait(0.5)

        arrow3 = Arrow(mob_list2[0].get_left(), mob_list2[2].get_right(), buff=0.1, color=YELLOW)
        label3 = MathTex("10 + 30 = 40", font_size=28).next_to(arrow3, UP)
        self.play(Create(arrow3), Write(label3))
        self.wait(0.5)

        # Slide middle element
        middle = mob_list2[1].copy()
        self.play(middle.animate.shift(RIGHT * 2))
        self.wait(0.5)

        # Final result
        result2 = [40, 20]
        mob_result2 = [Integer(x, font_size=28) for x in result2]
        mob_result2 = VGroup(*mob_result2).arrange(RIGHT, buff=0.5)
        mob_result2.move_to(ORIGIN)
        self.play(Transform(mob_list2, mob_result2))
        self.wait(1)

        # Section 3: [1, 2, 3]
        self.play(FadeOut(arrow3), FadeOut(label3), FadeOut(middle))
        list3 = [1, 2, 3]
        mob_list3 = [Integer(x, font_size=28) for x in list3]
        mob_list3 = VGroup(*mob_list3).arrange(RIGHT, buff=0.5)
        mob_list3.move_to(ORIGIN)
        self.play(Transform(mob_result2, mob_list3))
        self.wait(0.5)

        arrow4 = Arrow(mob_list3[0].get_left(), mob_list3[2].get_right(), buff=0.1, color=YELLOW)
        label4 = MathTex("1 + 3 = 4", font_size=28).next_to(arrow4, UP)
        self.play(Create(arrow4), Write(label4))
        self.wait(0.5)

        # Middle element stays alone
        middle3 = mob_list3[1].copy()
        self.play(middle3.animate.shift(RIGHT * 2))
        self.wait(0.5)

        result3 = [4, 2]
        mob_result3 = [Integer(x, font_size=28) for x in result3]
        mob_result3 = VGroup(*mob_result3).arrange(RIGHT, buff=0.5)
        mob_result3.move_to(ORIGIN)
        self.play(Transform(mob_list3, mob_result3))
        self.wait(1)

        # Section 4: [1, 2, 3, 4, 5]
        self.play(FadeOut(arrow4), FadeOut(label4), FadeOut(middle3))
        list4 = [1, 2, 3, 4, 5]
        mob_list4 = [Integer(x, font_size=28) for x in list4]
        mob_list4 = VGroup(*mob_list4).arrange(RIGHT, buff=0.5)
        mob_list4.move_to(ORIGIN)
        self.play(Transform(mob_result3, mob_list4))
        self.wait(0.5)

        arrow5 = Arrow(mob_list4[0].get_left(), mob_list4[4].get_right(), buff=0.1, color=YELLOW)
        label5 = MathTex("1 + 5 = 6", font_size=28).next_to(arrow5, UP)
        arrow6 = Arrow(mob_list4[1].get_left(), mob_list4[3].get_right(), buff=0.1, color=YELLOW)
        label6 = MathTex("2 + 4 = 6", font_size=28).next_to(arrow6, UP)
        self.play(Create(arrow5), Write(label5), Create(arrow6), Write(label6))
        self.wait(0.5)

        # Middle element
        middle4 = mob_list4[2].copy()
        self.play(middle4.animate.shift(RIGHT * 2))
        self.wait(0.5)

        result4 = [6, 6, 3]
        mob_result4 = [Integer(x, font_size=28) for x in result4]
        mob_result4 = VGroup(*mob_result4).arrange(RIGHT, buff=0.5)
        mob_result4.move_to(ORIGIN)
        self.play(Transform(mob_list4, mob_result4))
        self.wait(1)

        # Section 5: [0, 0, 0]
        self.play(FadeOut(arrow5), FadeOut(label5), FadeOut(arrow6), FadeOut(label6), FadeOut(middle4))
        list5 = [0, 0, 0]
        mob_list5 = [Integer(x, font_size=28) for x in list5]
        mob_list5 = VGroup(*mob_list5).arrange(RIGHT, buff=0.5)
        mob_list5.move_to(ORIGIN)
        self.play(Transform(mob_result4, mob_list5))
        self.wait(0.5)

        arrow7 = Arrow(mob_list5[0].get_left(), mob_list5[2].get_right(), buff=0.1, color=YELLOW)
        label7 = MathTex("0 + 0 = 0", font_size=28).next_to(arrow7, UP)
        self.play(Create(arrow7), Write(label7))
        self.wait(0.5)

        # Middle element
        middle5 = mob_list5[1].copy()
        self.play(middle5.animate.shift(RIGHT * 2))
        self.wait(0.5)

        result5 = [0, 0]
        mob_result5 = [Integer(x, font_size=28) for x in result5]
        mob_result5 = VGroup(*mob_result5).arrange(RIGHT, buff=0.5)
        mob_result5.move_to(ORIGIN)
        self.play(Transform(mob_list5, mob_result5))
        self.wait(1)

        # Section 6: Length comparison
        self.play(FadeOut(arrow7), FadeOut(label7), FadeOut(middle5))
        list6 = [1, 2, 3, 4, 5, 6]
        mob_list6 = [Integer(x, font_size=28) for x in list6]
        mob_list6 = VGroup(*mob_list6).arrange(RIGHT, buff=0.5)
        mob_list6.move_to(ORIGIN)
        self.play(Transform(mob_result5, mob_list6))
        self.wait(0.5)

        # Show length / 2
        label_length = MathTex("6 \\rightarrow 3", font_size=28).next_to(mob_list6, DOWN)
        self.play(Write(label_length))
        self.wait(1)

        # Section 7: Sum preservation
        self.play(FadeOut(label_length))
        sum_original = MathTex("1 + 2 + 3 + 4 = 10", font_size=28).to_edge(UP)
        sum_folded = MathTex("5 + 5 = 10", font_size=28).to_edge(DOWN)
        self.play(Write(sum_original), Write(sum_folded))
        self.wait(1)

        # Section 8: [5, 5, 5, 5]
        self.play(FadeOut(sum_original), FadeOut(sum_folded))
        list7 = [5, 5, 5, 5]
        mob_list7 = [Integer(x, font_size=28) for x in list7]
        mob_list7 = VGroup(*mob_list7).arrange(RIGHT, buff=0.5)
        mob_list7.move_to(ORIGIN)
        self.play(Transform(mob_result5, mob_list7))
        self.wait(0.5)

        arrow8 = Arrow(mob_list7[0].get_left(), mob_list7[3].get_right(), buff=0.1, color=YELLOW)
        label8 = MathTex("5 + 5 = 10", font_size=28).next_to(arrow8, UP)
        arrow9 = Arrow(mob_list7[1].get_left(), mob_list7[2].get_right(), buff=0.1, color=YELLOW)
        label9 = MathTex("5 + 5 = 10", font_size=28).next_to(arrow9, UP)
        self.play(Create(arrow8), Write(label8), Create(arrow9), Write(label9))
        self.wait(0.5)

        result7 = [10, 10]
        mob_result7 = [Integer(x, font_size=28) for x in result7]
        mob_result7 = VGroup(*mob_result7).arrange(RIGHT, buff=0.5)
        mob_result7.move_to(ORIGIN)
        self.play(Transform(mob_list7, mob_result7))
        self.wait(1)

        # Section 9: [1, 2]
        self.play(FadeOut(arrow8), FadeOut(label8), FadeOut(arrow9), FadeOut(label9))
        list8 = [1, 2]
        mob_list8 = [Integer(x, font_size=28) for x in list8]
        mob_list8 = VGroup(*mob_list8).arrange(RIGHT, buff=0.5)
        mob_list8.move_to(ORIGIN)
        self.play(Transform(mob_result7, mob_list8))
        self.wait(0.5)

        arrow10 = Arrow(mob_list8[0].get_left(), mob_list8[1].get_right(), buff=0.1, color=YELLOW)
        label10 = MathTex("1 + 2 = 3", font_size=28).next_to(arrow10, UP)
        self.play(Create(arrow10), Write(label10))
        self.wait(0.5)

        result8 = [3]
        mob_result8 = [Integer(x, font_size=28) for x in result8]
        mob_result8 = VGroup(*mob_result8).arrange(RIGHT, buff=0.5)
        mob_result8.move_to(ORIGIN)
        self.play(Transform(mob_list8, mob_result8))
        self.wait(1)

        # Final cleanup
        self.play(FadeOut(title), FadeOut(mob_result8))
        self.wait(0.5)
