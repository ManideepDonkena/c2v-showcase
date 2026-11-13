from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Folding Mechanism", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial list
        original_list = [1, 2, 3, 4]
        mobs = [Integer(x, font_size=32) for x in original_list]
        VGroup(*mobs).arrange(RIGHT, buff=0.5).move_to(ORIGIN)
        self.play(Write(VGroup(*mobs)))
        self.wait(0.5)

        # Indices
        indices = [Integer(i, font_size=24) for i in range(len(original_list))]
        for i, ind in enumerate(indices):
            ind.next_to(mobs[i], DOWN)
        self.play(Write(VGroup(*indices)))
        self.wait(0.5)

        # Arrows and sums
        arrow1 = Arrow(mobs[0].get_top(), mobs[3].get_top(), buff=0.1, stroke_width=3)
        arrow2 = Arrow(mobs[1].get_top(), mobs[2].get_top(), buff=0.1, stroke_width=3)

        sum1 = MathTex("1 + 4 = 5", font_size=32).next_to(arrow1, UP)
        sum2 = MathTex("2 + 3 = 5", font_size=32).next_to(arrow2, UP)

        self.play(GrowArrow(arrow1), Write(sum1))
        self.wait(0.5)
        self.play(GrowArrow(arrow2), Write(sum2))
        self.wait(1)

        # Collapse into new list
        new_mobs = [Integer(5, font_size=32) for _ in range(2)]
        VGroup(*new_mobs).arrange(RIGHT, buff=0.5).move_to(ORIGIN)
        self.play(
            Transform(mobs[0], new_mobs[0]),
            Transform(mobs[1], new_mobs[1]),
            FadeOut(mobs[2]),
            FadeOut(mobs[3]),
            FadeOut(indices),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(sum1),
            FadeOut(sum2)
        )
        self.wait(0.5)

        # Show result
        result_text = Text("Result: [5, 5]", font_size=32).move_to(ORIGIN)
        self.play(Write(result_text))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(title), FadeOut(result_text))
        self.wait(0.5)
