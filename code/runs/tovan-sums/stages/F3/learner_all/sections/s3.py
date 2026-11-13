from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Absorbing Element (-1)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Part 1: -1 absorbs any number
        neg_one_circle = Circle(radius=1, color=BLUE, fill_color=BLUE, fill_opacity=1).move_to(LEFT * 3)
        b_circle = Circle(radius=1, color=GREEN, fill_color=GREEN, fill_opacity=1).move_to(RIGHT * 3)
        neg_one_label = MathTex("-1", font_size=36).move_to(neg_one_circle.get_center())
        b_label = MathTex("b", font_size=36).move_to(b_circle.get_center())

        self.play(Create(neg_one_circle), Create(b_circle), Write(neg_one_label), Write(b_label))
        self.wait(0.5)

        # Move -1 towards b
        self.play(neg_one_circle.animate.move_to((neg_one_circle.get_center() + b_circle.get_center()) / 2),
                  b_circle.animate.move_to((neg_one_circle.get_center() + b_circle.get_center()) / 2))
        self.wait(0.5)

        # Consume b
        self.play(FadeOut(b_circle), FadeOut(b_label))
        self.wait(0.5)

        result_label = MathTex("-1", font_size=36).move_to(neg_one_circle.get_center())
        self.play(Write(result_label))
        self.wait(1)

        # Part 2: Chain of three circles
        self.play(FadeOut(title), FadeOut(neg_one_circle), FadeOut(result_label))

        chain_labels = [MathTex("4", font_size=24), MathTex("-1", font_size=24), MathTex("2", font_size=24)]
        chain_circles = [Circle(radius=0.5, color=BLUE, fill_color=BLUE, fill_opacity=1),
                         Circle(radius=0.5, color=RED, fill_color=RED, fill_opacity=1),
                         Circle(radius=0.5, color=GREEN, fill_color=GREEN, fill_opacity=1)]

        for i in range(3):
            chain_labels[i].move_to(chain_circles[i].get_center())
            self.play(FadeIn(chain_circles[i]), FadeIn(chain_labels[i]))
            chain_labels[i].move_to(chain_circles[i].get_center())
            self.play(FadeIn(chain_circles[i]), FadeIn(chain_labels[i]))
            chain_circles[i].move_to(LEFT * 2 + RIGHT * i)
            chain_labels[i].move_to(chain_circles[i].get_center())

        self.play(Create(chain_circles[0]), Create(chain_circles[1]), Create(chain_circles[2]),
                  Write(chain_labels[0]), Write(chain_labels[1]), Write(chain_labels[2]))
        self.wait(0.5)

        # First merge: 4 ⊕ (-1) = -1
        first_merge_circle = Circle(radius=0.5, color=RED, fill_color=RED, fill_opacity=1).move_to(LEFT)
        first_merge_label = MathTex("-1", font_size=24).move_to(first_merge_circle.get_center())
        self.play(Transform(chain_circles[0], first_merge_circle),
                  Transform(chain_labels[0], first_merge_label))
        self.wait(0.5)

        # Second merge: (-1) ⊕ 2 = -1
        second_merge_circle = Circle(radius=0.5, color=RED, fill_color=RED, fill_opacity=1).move_to(RIGHT)
        second_merge_label = MathTex("-1", font_size=24).move_to(second_merge_circle.get_center())
        self.play(Transform(chain_circles[2], second_merge_circle),
                  Transform(chain_labels[2], second_merge_label))
        self.wait(0.5)

        # Final result
        final_result = MathTex("-1", font_size=36).move_to(ORIGIN)
        self.play(Write(final_result))
        self.wait(1.5)

        # Part 3: Formula expansion
        self.play(FadeOut(chain_circles[0]), FadeOut(chain_circles[2]), FadeOut(chain_labels[0]),
                  FadeOut(chain_labels[2]), FadeOut(final_result))

        formula = MathTex("(-1) + 5 + ((-1) \\times 5)", font_size=36)
        self.play(Write(formula))
        self.wait(0.5)

        step1 = MathTex("-1 + 5 - 5", font_size=36).move_to(DOWN * 1.5)
        self.play(Write(step1))
        self.wait(0.5)

        step2 = MathTex("= -1", font_size=36).move_to(DOWN * 2.5)
        self.play(Write(step2))
        self.wait(1.5)

        # Part 4: Parentheses
        self.play(FadeOut(formula), FadeOut(step1), FadeOut(step2))

        nested = MathTex("a \\oplus (b \\oplus c)", font_size=36)
        self.play(Write(nested))
        self.wait(0.5)

        # Highlight inner parentheses
        inner_group = SurroundingRectangle(MathTex("b \\oplus c", font_size=36), color=YELLOW, buff=0.1)
        self.play(Create(inner_group))
        self.wait(0.5)

        self.play(FadeOut(nested), FadeOut(inner_group))
        self.wait(0.5)

        # Final message
        final_msg = Text("Because -1 swallows everything it touches, the entire chain collapses to -1.", font_size=24)
        self.play(Write(final_msg))
        self.wait(1.5)

        self.play(FadeOut(final_msg))
        self.wait(0.5)
