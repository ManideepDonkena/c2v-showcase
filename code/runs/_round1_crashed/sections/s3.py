from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Area Connection", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Squares
        square_a = Square(side_length=3, color=BLUE, fill_opacity=0.5)
        square_b = Square(side_length=4, color=GREEN, fill_opacity=0.5)
        square_c = Square(side_length=5, color=RED, fill_opacity=0.5)

        # Position squares
        square_a.move_to(LEFT * 2 + DOWN * 1)
        square_b.move_to(RIGHT * 2 + DOWN * 1)
        square_c.move_to(DOWN * 1)

        # Labels for sides
        label_a = MathTex("a=3", font_size=24).next_to(square_a, UP)
        label_b = MathTex("b=4", font_size=24).next_to(square_b, UP)
        label_c = MathTex("c=5", font_size=24).next_to(square_c, UP)

        # Area labels
        area_a = MathTex("a^2 = 9", font_size=24).next_to(square_a, DOWN)
        area_b = MathTex("b^2 = 16", font_size=24).next_to(square_b, DOWN)
        area_c = MathTex("c^2 = 25", font_size=24).next_to(square_c, DOWN)

        # Show initial setup
        self.play(Create(square_a), Create(square_b), Create(square_c))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.play(Write(area_a), Write(area_b), Write(area_c))
        self.wait(1)

        # Fade out labels and areas
        self.play(FadeOut(label_a), FadeOut(label_b), FadeOut(label_c))
        self.play(FadeOut(area_a), FadeOut(area_b), FadeOut(area_c))

        # Animation: liquid flow from small squares to large square
        # Create smaller squares with contents that will flow
        square_a_copy = square_a.copy()
        square_b_copy = square_b.copy()

        # Show the flow animation
        self.play(
            square_a_copy.animate.move_to(square_c.get_center()),
            square_b_copy.animate.move_to(square_c.get_center()),
            run_time=2
        )

        # Show final area equation
        equation = MathTex("a^2 + b^2 = c^2", font_size=40)
        equation.to_edge(UP)
        equation.shift(0.0 * RIGHT + -0.53 * UP)  # layout: separation vector
        self.play(Write(equation))
        self.wait(1)

        # Show numbers merging
        text1 = Text("9", font_size=24).move_to(square_a.get_center())
        text2 = Text("16", font_size=24).move_to(square_b.get_center())
        text3 = Text("25", font_size=24).move_to(square_c.get_center())

        self.play(Write(text1), Write(text2))
        self.wait(0.5)
        text3.shift(-0.31 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(ReplacementTransform(text1, text3), ReplacementTransform(text2, text3))
        self.wait(1)

        # Final explanation
        explanation = Text("The sum of the areas equals the area of the largest square", font_size=24)
        explanation.to_edge(DOWN)
        explanation.shift(0.0 * RIGHT + -0.49 * UP)  # layout: separation vector
        self.play(Write(explanation))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(square_a_copy), FadeOut(square_b_copy), FadeOut(equation), FadeOut(explanation), FadeOut(text3))
        self.wait(0.5)
