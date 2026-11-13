from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Brisk Folds: Halving Lists with Sum Preservation", font_size=32)
        title.to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Initial list
        initial_list = [1, 2, 3, 4, 5, 6]
        initial_mobs = [Integer(num, font_size=28) for num in initial_list]
        initial_group = VGroup(*initial_mobs).arrange(RIGHT, buff=0.4)
        initial_group.move_to(ORIGIN)

        # Show initial list
        self.play(Write(initial_group))
        self.wait(1)

        # Add brackets around initial list
        initial_brackets = always_redraw(
            lambda: Brace(initial_group, UP, buff=0.1)
        )
        initial_label = Text("Length 6", font_size=24)
        initial_label.next_to(initial_brackets, UP, buff=0.1)

        self.play(Create(initial_brackets), Write(initial_label))
        self.wait(1)

        # Fold animation
        folded_list = [7, 7, 7]
        folded_mobs = [Integer(num, font_size=28) for num in folded_list]
        folded_group = VGroup(*folded_mobs).arrange(RIGHT, buff=0.4)
        folded_group.move_to(ORIGIN)

        # Arrow from initial to folded
        arrow = Arrow(start=initial_group.get_center() + DOWN * 0.8,
                      end=folded_group.get_center() + UP * 0.8,
                      buff=0.2, color=YELLOW)
        length_label = Text("Length / 2", font_size=24, color=YELLOW)
        length_label.next_to(arrow, RIGHT, buff=0.2)
        length_label.shift(0.39 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Transform(initial_group, folded_group),
                  Transform(initial_brackets, Brace(folded_group, UP, buff=0.1)),
                  Write(length_label),
                  GrowArrow(arrow))
        self.wait(1)

        # Final label
        final_label = Text("Each brisk fold roughly halves the length.", font_size=24)
        final_label.to_edge(DOWN, buff=0.3)
        self.play(Write(final_label))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(title, initial_group, initial_brackets, initial_label,
                          arrow, length_label, final_label))
        self.wait(0.5)
