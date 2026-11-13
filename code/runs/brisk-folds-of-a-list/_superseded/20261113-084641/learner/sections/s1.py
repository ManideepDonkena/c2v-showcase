from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Folding Mechanism", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial list [1, 2, 3, 4]
        list1 = [1, 2, 3, 4]
        mobs1 = [Integer(x, font_size=32) for x in list1]
        mobs1_group = VGroup(*mobs1).arrange(RIGHT, buff=0.5)
        mobs1_group.move_to(ORIGIN)
        self.play(Write(mobs1_group))
        self.wait(0.5)

        # Arrows for first pairing (index 0 to 3)
        arrow1 = Arrow(mobs1[0].get_top(), mobs1[3].get_top(), buff=0.1, color=YELLOW)
        arrow1.shift(0.0 * RIGHT + 0.32 * UP)  # layout: separation vector
        self.play(Create(arrow1))
        self.wait(0.5)

        # Arrows for second pairing (index 1 to 2)
        arrow2 = Arrow(mobs1[1].get_top(), mobs1[2].get_top(), buff=0.1, color=YELLOW)
        self.play(Create(arrow2))
        self.wait(0.5)

        # Show sums
        sum1 = MathTex("1 + 4 = 5", font_size=32).next_to(mobs1[0], UP, buff=0.5)
        sum2 = MathTex("2 + 3 = 5", font_size=32).next_to(mobs1[1], UP, buff=0.5)
        self.play(Write(sum1), Write(sum2))
        self.wait(1)

        # Collapse into new list [5, 5]
        result1 = [5, 5]
        mobs_result1 = [Integer(x, font_size=32) for x in result1]
        mobs_result1_group = VGroup(*mobs_result1).arrange(RIGHT, buff=0.5)
        mobs_result1_group.move_to(ORIGIN)
        self.play(FadeOut(mobs1_group), FadeOut(arrow1), FadeOut(arrow2), FadeOut(sum1), FadeOut(sum2))
        self.wait(0.5)
        self.play(Write(mobs_result1_group))
        self.wait(1)

        # Show list [5, 5, 5, 5]
        list2 = [5, 5, 5, 5]
        mobs2 = [Integer(x, font_size=32) for x in list2]
        mobs2_group = VGroup(*mobs2).arrange(RIGHT, buff=0.5)
        mobs2_group.move_to(ORIGIN)
        self.play(FadeOut(mobs_result1_group))
        self.wait(0.5)
        self.play(Write(mobs2_group))
        self.wait(0.5)

        # Arrows for pairing [5, 5, 5, 5]
        arrow3 = Arrow(mobs2[0].get_top(), mobs2[3].get_top(), buff=0.1, color=YELLOW)
        arrow4 = Arrow(mobs2[1].get_top(), mobs2[2].get_top(), buff=0.1, color=YELLOW)
        self.play(Create(arrow3), Create(arrow4))
        self.wait(0.5)

        # Show sums
        sum3 = MathTex("5 + 5 = 10", font_size=32).next_to(mobs2[0], UP, buff=0.5)
        sum4 = MathTex("5 + 5 = 10", font_size=32).next_to(mobs2[1], UP, buff=0.5)
        self.play(Write(sum3), Write(sum4))
        self.wait(1)

        # Collapse into [10, 10]
        result2 = [10, 10]
        mobs_result2 = [Integer(x, font_size=32) for x in result2]
        mobs_result2_group = VGroup(*mobs_result2).arrange(RIGHT, buff=0.5)
        mobs_result2_group.move_to(ORIGIN)
        self.play(FadeOut(mobs2_group), FadeOut(arrow3), FadeOut(arrow4), FadeOut(sum3), FadeOut(sum4))
        self.wait(0.5)
        self.play(Write(mobs_result2_group))
        self.wait(1)

        # Show list [1, 2]
        list3 = [1, 2]
        mobs3 = [Integer(x, font_size=32) for x in list3]
        mobs3_group = VGroup(*mobs3).arrange(RIGHT, buff=0.5)
        mobs3_group.move_to(ORIGIN)
        self.play(FadeOut(mobs_result2_group))
        self.wait(0.5)
        self.play(Write(mobs3_group))
        self.wait(0.5)

        # Arrow from 1 to 2
        arrow5 = Arrow(mobs3[0].get_top(), mobs3[1].get_top(), buff=0.1, color=YELLOW)
        self.play(Create(arrow5))
        self.wait(0.5)

        # Show calculation and result
        calc = MathTex("1 + 2 = 3", font_size=32).next_to(mobs3[0], UP, buff=0.5)
        self.play(Write(calc))
        self.wait(1)

        # Collapse into [3]
        result3 = [3]
        mobs_result3 = [Integer(x, font_size=32) for x in result3]
        mobs_result3_group = VGroup(*mobs_result3).arrange(RIGHT, buff=0.5)
        mobs_result3_group.move_to(ORIGIN)
        self.play(FadeOut(mobs3_group), FadeOut(arrow5), FadeOut(calc))
        self.wait(0.5)
        self.play(Write(mobs_result3_group))
        self.wait(1)

        # Final text
        final_text = Text("A brisk fold pairs first with last, sums each pair.", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)
        self.play(FadeOut(final_text), FadeOut(title))
