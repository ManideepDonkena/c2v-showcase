from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Rule 2: Length Reduction", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial list
        initial_list = [1, 2, 3, 4, 5, 6]
        initial_mobs = [Integer(x, font_size=24) for x in initial_list]
        initial_group = VGroup(*initial_mobs).arrange(RIGHT, buff=0.5)
        initial_group.to_edge(UP, buff=1.5)

        # Show initial list
        self.play(Create(initial_group))
        self.wait(1)

        # Fold animation
        folded_list = [7, 7, 7]
        folded_mobs = [Integer(x, font_size=24) for x in folded_list]
        folded_group = VGroup(*folded_mobs).arrange(RIGHT, buff=0.5)
        folded_group.to_edge(DOWN, buff=1.5)

        # Arrows and label
        arrow = Arrow(start=initial_group.get_center() + UP * 0.5,
                      end=folded_group.get_center() + DOWN * 0.5,
                      color=YELLOW, buff=0.2)
        label = Text("Length / 2", font_size=24).next_to(arrow, RIGHT)

        self.play(GrowArrow(arrow), Write(label))
        self.wait(1)

        # Show folded list
        self.play(Transform(initial_group, folded_group))
        self.wait(1.5)

        # Emphasize halving
        highlight_initial = initial_group[0].copy().set_color(RED)
        highlight_folded = initial_group[0].copy().set_color(GREEN)
        self.play(
            FadeOut(label),
            FadeOut(arrow),
            Transform(initial_group[0], highlight_initial),
            Transform(initial_group[1], highlight_folded),
            Transform(initial_group[2], highlight_folded),
            Transform(initial_group[3], highlight_folded),
            Transform(initial_group[4], highlight_folded),
            Transform(initial_group[5], highlight_folded)
        )
        self.wait(1)

        # Narration text
        narration = Text("Each brisk fold roughly halves the length of the list.", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        self.play(FadeOut(narration), FadeOut(title), FadeOut(initial_group))
        self.wait(0.5)
