from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Folding Mechanism", font_size=36).to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Initial list
        original_list = [1, 2, 3, 4]
        mobs = [Integer(x, font_size=24) for x in original_list]
        VGroup(*mobs).arrange(RIGHT, buff=0.5).move_to(DOWN * 0.5)
        self.play(Write(VGroup(*mobs)))
        self.wait(0.5)

        # Indices
        indices = [Integer(i, font_size=18) for i in range(len(original_list))]
        for i, ind in enumerate(indices):
            ind.next_to(mobs[i], UP, buff=0.2)
        self.play(Write(VGroup(*indices)))
        self.wait(0.5)

        # Arrows
        arrow1 = Arrow(mobs[0].get_top(), mobs[3].get_top(), buff=0.1, stroke_width=3)
        arrow2 = Arrow(mobs[1].get_top(), mobs[2].get_top(), buff=0.1, stroke_width=3)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait(0.5)

        # Sum labels
        sum1 = MathTex("1 + 4 = 5", font_size=24).next_to(arrow1, UP, buff=0.3)
        sum2 = MathTex("2 + 3 = 5", font_size=24).next_to(arrow2, UP, buff=0.3)
        sum1.shift(0.0 * RIGHT + 0.21 * UP)  # layout: separation vector
        self.play(Write(sum1), Write(sum2))
        self.wait(1)

        # Collapse into new list
        new_mobs = [Integer(5, font_size=24) for _ in range(2)]
        VGroup(*new_mobs).arrange(RIGHT, buff=0.5).move_to(DOWN * 0.5)
        self.play(
            Transform(mobs[0], new_mobs[0]),
            Transform(mobs[1], new_mobs[1]),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(sum1),
            FadeOut(sum2),
            FadeOut(indices[0]),
            FadeOut(indices[1]),
            FadeOut(indices[2]),
            FadeOut(indices[3]),
        )
        self.wait(0.5)

        # Final text
        definition = Text("A brisk fold pairs first with last, second with second-to-last.", font_size=24)
        definition.to_edge(DOWN, buff=0.5)
        self.play(Write(definition))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(VGroup(*new_mobs)),
            FadeOut(definition)
        )
        self.wait(0.5)
