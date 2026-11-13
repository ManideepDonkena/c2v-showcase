from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Rule 2: Length Reduction", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial list [1, 2, 3, 4, 5, 6] folding to [7, 7, 7]
        orig_list = [1, 2, 3, 4, 5, 6]
        folded_list = [7, 7, 7]

        orig_mob = VGroup(*[Integer(x).scale(0.8) for x in orig_list]).arrange(RIGHT, buff=0.5)
        folded_mob = VGroup(*[Integer(x).scale(0.8) for x in folded_list]).arrange(RIGHT, buff=0.5)

        orig_mob.to_edge(UP, buff=1)
        folded_mob.next_to(orig_mob, DOWN, buff=1)

        self.play(Write(orig_mob))
        self.wait(0.5)

        # Arrows for pairing
        arrows = VGroup()
        for i in range(3):
            start = orig_mob[i]
            end = orig_mob[5 - i]
            arrow = Arrow(start.get_center(), end.get_center(), buff=0.1)
            label = MathTex(f"{orig_list[i]} + {orig_list[5-i]} = {orig_list[i] + orig_list[5-i]}", font_size=24).next_to(arrow, UP)
            self.play(GrowArrow(arrow), Write(label))
            arrows.add(arrow, label)

        self.wait(0.5)

        # Folded list
        self.play(Transform(orig_mob.copy(), folded_mob))
        self.wait(0.5)

        # Length / 2 arrow
        length_arrow = Arrow(start=orig_mob.get_center(), end=folded_mob.get_center(), buff=0.1)
        length_label = Text("Length / 2", font_size=24).next_to(length_arrow, UP)
        self.play(GrowArrow(length_arrow), Write(length_label))
        self.wait(1)

        # Show [10, 20, 30] folding
        self.play(FadeOut(arrows, length_arrow, length_label))

        list_10_20_30 = VGroup(Integer(10), Integer(20), Integer(30)).arrange(RIGHT, buff=0.5)
        list_10_20_30.to_edge(UP, buff=1)

        self.play(Write(list_10_20_30))
        self.wait(0.5)

        arrow_10_30 = Arrow(list_10_20_30[0].get_center(), list_10_20_30[2].get_center(), buff=0.1)
        label_sum = MathTex("10 + 30 = 40", font_size=24).next_to(arrow_10_30, UP)
        self.play(GrowArrow(arrow_10_30), Write(label_sum))
        self.wait(0.5)

        # Slide 20 to the right
        slide_arrow = Arrow(list_10_20_30[1].get_center(), list_10_20_30[1].get_center() + RIGHT * 2, buff=0.1)
        self.play(GrowArrow(slide_arrow))
        self.wait(0.5)

        # Final result
        final_mob = VGroup(
            Rectangle().scale(0.4).set_fill(BLUE, opacity=0.5),
            Text("40", font_size=24).move_to(Rectangle().scale(0.4).get_center()),
            Rectangle().scale(0.4).set_fill(GREEN, opacity=0.5),
            Text("20", font_size=24).move_to(Rectangle().scale(0.4).get_center())
        ).arrange(RIGHT, buff=0.5)
        final_mob.next_to(list_10_20_30, DOWN, buff=1)

        self.play(TransformMatchingShapes(VGroup(list_10_20_30[0], list_10_20_30[2]), final_mob[0]))
        self.play(Write(final_mob[1]))
        self.play(TransformMatchingShapes(list_10_20_30[1], final_mob[2]))
        self.play(Write(final_mob[3]))

        self.wait(1)

        # Show [1, 2, 3] folding
        self.play(FadeOut(list_10_20_30, arrow_10_30, label_sum, slide_arrow, final_mob))

        list_123 = VGroup(Integer(1), Integer(2), Integer(3)).arrange(RIGHT, buff=0.5)
        list_123.to_edge(UP, buff=1)

        self.play(Write(list_123))
        self.wait(0.5)

        arrow_13 = Arrow(list_123[0].get_center(), list_123[2].get_center(), buff=0.1)
        label_13 = MathTex("1 + 3 = 4", font_size=24).next_to(arrow_13, UP)
        self.play(GrowArrow(arrow_13), Write(label_13))
        self.wait(0.5)

        # Highlight middle element
        middle = list_123[1].copy().set_color(YELLOW)
        self.play(Write(middle))
        self.wait(0.5)

        # Result [4, 2]
        result_123 = VGroup(
            Rectangle().scale(0.4).set_fill(BLUE, opacity=0.5),
            Text("4", font_size=24).move_to(Rectangle().scale(0.4).get_center()),
            Rectangle().scale(0.4).set_fill(GREEN, opacity=0.5),
            Text("2", font_size=24).move_to(Rectangle().scale(0.4).get_center())
        ).arrange(RIGHT, buff=0.5)
        result_123.next_to(list_123, DOWN, buff=1)

        self.play(TransformMatchingShapes(VGroup(list_123[0], list_123[2]), result_123[0]))
        self.play(Write(result_123[1]))
        self.play(TransformMatchingShapes(list_123[1], result_123[2]))
        self.play(Write(result_123[3]))

        self.wait(1)

        # Show [1, 2, 3, 4, 5] folding
        self.play(FadeOut(list_123, arrow_13, label_13, result_123))

        list_12345 = VGroup(Integer(1), Integer(2), Integer(3), Integer(4), Integer(5)).arrange(RIGHT, buff=0.5)
        list_12345.to_edge(UP, buff=1)

        self.play(Write(list_12345))
        self.wait(0.5)

        arrow_15 = Arrow(list_12345[0].get_center(), list_12345[4].get_center(), buff=0.1)
        label_15 = MathTex("1 + 5 = 6", font_size=24).next_to(arrow_15, UP)
        self.play(GrowArrow(arrow_15), Write(label_15))
        self.wait(0.5)

        arrow_24 = Arrow(list_12345[1].get_center(), list_12345[3].get_center(), buff=0.1)
        label_24 = MathTex("2 + 4 = 6", font_size=24).next_to(arrow_24, UP)
        self.play(GrowArrow(arrow_24), Write(label_24))
        self.wait(0.5)

        # Middle element
        middle_3 = list_12345[2].copy().set_color(YELLOW)
        self.play(Write(middle_3))
        self.wait(0.5)

        # Result [6, 6, 3]
        result_12345 = VGroup(
            Rectangle().scale(0.4).set_fill(BLUE, opacity=0.5),
            Text("6", font_size=24).move_to(Rectangle().scale(0.4).get_center()),
            Rectangle().scale(0.4).set_fill(BLUE, opacity=0.5),
            Text("6", font_size=24).move_to(Rectangle().scale(0.4).get_center()),
            Rectangle().scale(0.4).set_fill(GREEN, opacity=0.5),
            Text("3", font_size=24).move_to(Rectangle().scale(0.4).get_center())
        ).arrange(RIGHT, buff=0.5)
        result_12345.next_to(list_12345, DOWN, buff=1)

        self.play(TransformMatchingShapes(VGroup(list_12345[0], list_12345[4]), result_12345[0]))
        self.play(Write(result_12345[1]))
        self.play(TransformMatchingShapes(VGroup(list_12345[1], list_12345[3]), result_12345[2]))
        self.play(Write(result_12345[3]))
        self.play(TransformMatchingShapes(list_12345[2], result_12345[4]))
        self.play(Write(result_12345[5]))

        self.wait(1)

        # Show [0, 0, 0]
        self.play(FadeOut(list_12345, arrow_15, label_15, arrow_24, label_24, middle_3, result_12345))

        list_000 = VGroup(Integer(0), Integer(0), Integer(0)).arrange(RIGHT, buff=0.5)
        list_000.to_edge(UP, buff=1)

        self.play(Write(list_000))
        self.wait(0.5)

        arrow_00 = Arrow(list_000[0].get_center(), list_000[2].get_center(), buff=0.1)
        label_00 = MathTex("0 + 0 = 0", font_size=24).next_to(arrow_00, UP)
        self.play(GrowArrow(arrow_00), Write(label_00))
        self.wait(0.5)

        # Middle element
        middle_0 = list_000[1].copy().set_color(YELLOW)
        self.play(Write(middle_0))
        self.wait(0.5)

        # Result [0, 0]
        result_000 = VGroup(
            Rectangle().scale(0.4).set_fill(BLUE, opacity=0.5),
            Text("0", font_size=24).move_to(Rectangle().scale(0.4).get_center()),
            Rectangle().scale(0.4).set_fill(GREEN, opacity=0.5),
            Text("0", font_size=24).move_to(Rectangle().scale(0.4).get_center())
        ).arrange(RIGHT, buff=0.5)
        result_000.next_to(list_000, DOWN, buff=1)

        self.play(TransformMatchingShapes(VGroup(list_000[0], list_000[2]), result_000[0]))
        self.play(Write(result_000[1]))
        self.play(TransformMatchingShapes(list_000[1], result_000[2]))
        self.play(Write(result_000[3]))

        self.wait(1)

        # Show odd length list folding to (n/2)+1
        self.play(FadeOut(list_000, arrow_00, label_00, middle_0, result_000))

        list_odd = VGroup(Integer(1), Integer(2), Integer(3), Integer(4), Integer(5)).arrange(RIGHT, buff=0.5)
        list_odd.to_edge(UP, buff=1)

        self.play(Write(list_odd))
        self.wait(0.5)

        # Show length shrinking
        length_arrow = Arrow(start=list_odd.get_center(), end=list_odd.get_center() + DOWN * 2, buff=0.1)
        length_label = Text("Length / 2", font_size=24).next_to(length_arrow, LEFT)
        self.play(GrowArrow(length_arrow), Write(length_label))
        self.wait(0.5)

        # Show result
        result_odd = VGroup(
            Rectangle().scale(0.4).set_fill(BLUE, opacity=0.5),
            Text("6", font_size=24).move_to(Rectangle().scale(0.4).get_center()),
            Rectangle().scale(0.4).set_fill(BLUE, opacity=0.5),
            Text("6", font_size=24).move_to(Rectangle().scale(0.4).get_center()),
            Rectangle().scale(0.4).set_fill(GREEN, opacity=0.5),
            Text("3", font_size=24).move_to(Rectangle().scale(0.4).get_center())
        ).arrange(RIGHT, buff=0.5)
        result_odd.next_to(list_odd, DOWN, buff=1)

        self.play(TransformMatchingShapes(VGroup(list_odd[0], list_odd[4]), result_odd[0]))
        self.play(Write(result_odd[1]))
        self.play(TransformMatchingShapes(VGroup(list_odd[1], list_odd[3]), result_odd[2]))
        self.play(Write(result_odd[3]))
        self.play(TransformMatchingShapes(list_odd[2], result_odd[4]))
        self.play(Write(result_odd[5]))

        self.wait(1)

        # Show sum preservation
        self.play(FadeOut(list_odd, length_arrow, length_label, result_odd))

        orig_sum = MathTex("1 + 2 + 3 + 4 + 5 = 15", font_size=24).to_edge(UP)
        folded_sum = MathTex("6 + 6 + 3 = 15", font_size=24).next_to(orig_sum, DOWN)

        self.play(Write(orig_sum))
        self.wait(0.5)

        self.play(Write(folded_sum))
        self.wait(1)

        # Show [5, 5, 5, 5] folding
        self.play(FadeOut(orig_sum, folded_sum))

        list_5555 = VGroup(Integer(5), Integer(5), Integer(5), Integer(5)).arrange(RIGHT, buff=0.5)
        list_5555.to_edge(UP, buff=1)

        self.play(Write(list_5555))
        self.wait(0.5)

        arrow_55 = Arrow(list_5555[0].get_center(), list_5555[3].get_center(), buff=0.1)
        label_55 = MathTex("5 + 5 = 10", font_size=24).next_to(arrow_55, UP)
        self.play(GrowArrow(arrow_55), Write(label_55))
        self.wait(0.5)

        arrow_55_2 = Arrow(list_5555[1].get_center(), list_5555[2].get_center(), buff=0.1)
        label_55_2 = MathTex("5 + 5 = 10", font_size=24).next_to(arrow_55_2, UP)
        self.play(GrowArrow(arrow_55_2), Write(label_55_2))
        self.wait(0.5)

        # Result [10, 10]
        result_5555 = VGroup(
            Rectangle().scale(0.4).set_fill(BLUE, opacity=0.5),
            Text("10", font_size=24).move_to(Rectangle().scale(0.4).get_center()),
            Rectangle().scale(0.4).set_fill(BLUE, opacity=0.5),
            Text("10", font_size=24).move_to(Rectangle().scale(0.4).get_center())
        ).arrange(RIGHT, buff=0.5)
        result_5555.next_to(list_5555, DOWN, buff=1)

        self.play(TransformMatchingShapes(VGroup(list_5555[0], list_5555[3]), result_5555[0]))
        self.play(Write(result_5555[1]))
        self.play(TransformMatchingShapes(VGroup(list_5555[1], list_5555[2]), result_5555[2]))
        self.play(Write(result_5555[3]))

        self.wait(1)

        # Show [1, 2] folding
        self.play(FadeOut(list_5555, arrow_55, label_55, arrow_55_2, label_55_2, result_5555))

        list_12 = VGroup(Integer(1), Integer(2)).arrange(RIGHT, buff=0.5)
        list_12.to_edge(UP, buff=1)

        self.play(Write(list_12))
        self.wait(0.5)

        arrow_12 = Arrow(list_12[0].get_center(), list_12[1].get_center(), buff=0.1)
        label_12 = MathTex("1 + 2 = 3", font_size=24).next_to(arrow_12, UP)
        self.play(GrowArrow(arrow_12), Write(label_12))
        self.wait(0.5)

        # Result [3]
        result_12 = VGroup(
            Rectangle().scale(0.4).set_fill(BLUE, opacity=0.5),
            Text("3", font_size=24).move_to(Rectangle().scale(0.4).get_center())
        ).arrange(RIGHT, buff=0.5)
        result_12.next_to(list_12, DOWN, buff=1)

        self.play(TransformMatchingShapes(VGroup(list_12[0], list_12[1]), result_12[0]))
        self.play(Write(result_12[1]))

        self.wait(1)

        # Final summary
        self.play(FadeOut(title, list_12, arrow_12, label_12, result_12))
        final_text = Text("Each brisk fold roughly halves the length of the list.", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1)

        self.play(FadeOut(final_text))
