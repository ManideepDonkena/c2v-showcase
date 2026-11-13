from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Absorbing Element (-1)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First animation: -1 absorbs b
        minus_one = Circle(radius=1, color=DARK_BLUE, fill_color=DARK_BLUE, fill_opacity=1)
        minus_one_label = MathTex("-1", font_size=36).move_to(minus_one.get_center())
        b_circle = Circle(radius=1, color=GREEN, fill_color=GREEN, fill_opacity=1)
        b_label = MathTex("b", font_size=36).move_to(b_circle.get_center())

        self.play(Create(minus_one), Write(minus_one_label))
        b_label.shift(0.0 * RIGHT + 0.41 * UP)  # layout: separation vector
        self.play(Create(b_circle), Write(b_label))
        self.wait(0.5)

        self.play(minus_one.animate.shift(RIGHT * 2), b_circle.animate.shift(LEFT * 2))
        self.wait(0.5)

        # Collision and absorption
        self.play(FadeOut(b_circle), FadeOut(b_label))
        result = MathTex("-1", font_size=36).move_to(minus_one.get_center())
        self.play(Write(result))
        self.wait(1)

        # Chain example: 4 ⊕ (-1) ⊕ 2
        self.play(FadeOut(minus_one), FadeOut(result))

        chain_labels = [MathTex("4", font_size=24), MathTex("-1", font_size=24), MathTex("2", font_size=24)]
        chain_circles = [
            Circle(radius=0.5, color=BLUE, fill_color=BLUE, fill_opacity=1).move_to(LEFT * 2),
            Circle(radius=0.5, color=DARK_BLUE, fill_color=DARK_BLUE, fill_opacity=1).move_to(ORIGIN),
            Circle(radius=0.5, color=GREEN, fill_color=GREEN, fill_opacity=1).move_to(RIGHT * 2)
        ]

        for i in range(3):
            self.play(Create(chain_circles[i]), Write(chain_labels[i]))
            self.wait(0.3)

        # Label "When chaining, we go left to right"
        direction_text = Text("When chaining, we go left to right.", font_size=24).to_edge(DOWN)
        self.play(Write(direction_text))
        self.wait(1)

        # First merge: 4 ⊕ (-1) = -1
        self.play(FadeOut(direction_text))

        first_merge_circle = Circle(radius=0.5, color=DARK_BLUE, fill_color=DARK_BLUE, fill_opacity=1).move_to(LEFT * 2)
        first_merge_label = MathTex("-1", font_size=24).move_to(first_merge_circle.get_center())
        self.play(Transform(chain_circles[0], first_merge_circle), Transform(chain_labels[0], first_merge_label))
        self.wait(0.5)

        # Second merge: (-1) ⊕ 2 = -1
        second_merge_circle = Circle(radius=0.5, color=DARK_BLUE, fill_color=DARK_BLUE, fill_opacity=1).move_to(RIGHT * 2)
        second_merge_label = MathTex("-1", font_size=24).move_to(second_merge_circle.get_center())
        self.play(Transform(chain_circles[1], second_merge_circle), Transform(chain_labels[1], second_merge_label))
        self.wait(0.5)

        # Final result
        final_result = MathTex("-1", font_size=36).move_to(RIGHT * 2)
        self.play(Write(final_result))
        self.wait(1.5)

        # Formula expansion: (-1) + 5 + ((-1) × 5)
        self.play(FadeOut(chain_circles[0]), FadeOut(chain_circles[1]), FadeOut(chain_labels[0]), FadeOut(chain_labels[1]), FadeOut(final_result))

        formula = MathTex("(-1) + 5 + ((-1) \\times 5)", font_size=36)
        self.play(Write(formula))
        self.wait(1)

        # Step-by-step simplification
        step1 = MathTex("-1 + 5 - 5", font_size=36).move_to(formula.get_center())
        self.play(Transform(formula, step1))
        self.wait(1)

        step2 = MathTex("= -1", font_size=36).next_to(step1, RIGHT)
        self.play(Write(step2))
        self.wait(1.5)

        # Final statement
        final_text = Text("Even though 5 is added, the multiplication term (-1 × 5) cancels it out completely, leaving only the absorbing element.", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)

        self.play(FadeOut(formula), FadeOut(step2), FadeOut(final_text))
        self.wait(0.5)

        # End
        self.play(FadeOut(title))
        self.wait(0.5)
