from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Brisk Folds: Halving Lists with Sum Preservation", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial list: [1, 2, 3, 4, 5, 6] (length 6)
        list1 = [1, 2, 3, 4, 5, 6]
        list1_mob = VGroup(*[Integer(x).scale(0.7) for x in list1])
        list1_mob.arrange(RIGHT, buff=0.5)
        list1_mob.to_edge(UP, buff=1.5)

        # Show initial list
        self.play(Write(list1_mob))
        self.wait(0.5)

        # Fold animation: [1,2,3,4,5,6] -> [7,7,7]
        fold_result = [7, 7, 7]
        result_mob = VGroup(*[Integer(x).scale(0.7) for x in fold_result])
        result_mob.arrange(RIGHT, buff=0.5)
        result_mob.to_edge(DOWN, buff=1.5)

        # Arrow from list to result
        arrow = Arrow(list1_mob.get_bottom(), result_mob.get_top(), buff=0.2)
        label = Text("Length / 2", font_size=24).next_to(arrow, UP)

        label.shift(0.0 * RIGHT + 0.34 * UP)  # layout: separation vector
        self.play(
            Transform(list1_mob.copy(), result_mob),
            GrowArrow(arrow),
            Write(label)
        )
        self.wait(1)

        # Show that length is halved
        len1 = Integer(6).scale(0.7)
        len2 = Integer(3).scale(0.7)
        len1.next_to(list1_mob, DOWN, buff=0.5)
        len2.next_to(result_mob, DOWN, buff=0.5)

        self.play(Write(len1))
        self.wait(0.5)
        self.play(Transform(len1, len2))
        self.wait(1)

        # Show odd-length list: [1, 2, 3, 4, 5] -> [6, 6, 2]
        self.play(FadeOut(list1_mob), FadeOut(result_mob), FadeOut(arrow), FadeOut(label), FadeOut(len1))

        list_odd = [1, 2, 3, 4, 5]
        list_odd_mob = VGroup(*[Integer(x).scale(0.7) for x in list_odd])
        list_odd_mob.arrange(RIGHT, buff=0.5)
        list_odd_mob.to_edge(UP, buff=1.5)

        self.play(Write(list_odd_mob))
        self.wait(0.5)

        fold_odd = [6, 6, 2]
        result_odd_mob = VGroup(*[Integer(x).scale(0.7) for x in fold_odd])
        result_odd_mob.arrange(RIGHT, buff=0.5)
        result_odd_mob.to_edge(DOWN, buff=1.5)

        arrow2 = Arrow(list_odd_mob.get_bottom(), result_odd_mob.get_top(), buff=0.2)
        label2 = Text("Length / 2", font_size=24).next_to(arrow2, UP)

        label2.shift(0.32 * RIGHT + 0.0 * UP)  # layout: separation vector
        label2.shift(0.0 * RIGHT + 0.34 * UP)  # layout: separation vector
        self.play(
            Transform(list_odd_mob.copy(), result_odd_mob),
            GrowArrow(arrow2),
            Write(label2)
        )
        self.wait(1)

        # Show lengths
        len_odd1 = Integer(5).scale(0.7)
        len_odd2 = Integer(3).scale(0.7)
        len_odd1.next_to(list_odd_mob, DOWN, buff=0.5)
        len_odd2.next_to(result_odd_mob, DOWN, buff=0.5)

        self.play(Write(len_odd1))
        self.wait(0.5)
        self.play(Transform(len_odd1, len_odd2))
        self.wait(1)

        # Narration text
        narration = Text("Each brisk fold roughly halves the length of the list.", font_size=24)
        narration.to_edge(DOWN, buff=0.5)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        # Final emphasis: "Length / 2" explicitly contradicts doubling
        contradiction = Text("Not doubled!", font_size=24).set_color(RED)
        contradiction.to_edge(DOWN, buff=0.5)
        self.play(Write(contradiction))
        self.wait(1.5)
        self.play(FadeOut(contradiction))

        # End
        self.play(FadeOut(title), FadeOut(list_odd_mob), FadeOut(result_odd_mob), FadeOut(arrow2), FadeOut(len_odd1), FadeOut(len_odd2))
        self.wait(0.5)
