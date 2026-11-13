from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Rule 2: Length Reduction", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial list
        list1 = [1, 2, 3, 4, 5, 6]
        list1_mob = VGroup(*[Integer(x, font_size=24) for x in list1]).arrange(RIGHT, buff=0.5)
        list1_mob.to_edge(LEFT).shift(UP * 0.5)

        # Final list
        list2 = [7, 7, 7]
        list2_mob = VGroup(*[Integer(x, font_size=24) for x in list2]).arrange(RIGHT, buff=0.5)
        list2_mob.to_edge(RIGHT).shift(UP * 0.5)

        # Arrows and label
        arrow = Arrow(list1_mob.get_center() + RIGHT * 2, list2_mob.get_center() + LEFT * 2, color=YELLOW)
        length_label = Text("Length / 2", font_size=24).next_to(arrow, UP)

        # Show initial list
        self.play(Write(list1_mob))
        self.wait(0.5)

        # Show folding process (conceptual)
        self.play(Write(arrow), Write(length_label))
        self.wait(0.5)

        # Show final list
        self.play(Write(list2_mob))
        self.wait(0.5)

        # Key words on screen
        key1 = Text("halves", font_size=24).to_edge(DOWN).shift(LEFT * 2)
        key2 = Text("compression", font_size=24).to_edge(DOWN).shift(RIGHT * 2)
        self.play(Write(key1), Write(key2))
        self.wait(1.0)

        # Fade out
        self.play(FadeOut(title), FadeOut(list1_mob), FadeOut(list2_mob),
                  FadeOut(arrow), FadeOut(length_label), FadeOut(key1), FadeOut(key2))
        self.wait(0.5)
