from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Scaling Invariance", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial mirthful triangle: sides 4, 5, 6
        a, b, c = 4, 5, 6
        triangle = Polygon(
            LEFT * c/2, RIGHT * c/2, UP * (np.sqrt(3) * c / 2),
            color=GREEN, fill_opacity=0.5
        ).shift(UP * 1)
        side_a = Line(triangle.get_vertices()[0], triangle.get_vertices()[1]).add_tip()
        side_b = Line(triangle.get_vertices()[1], triangle.get_vertices()[2]).add_tip()
        side_c = Line(triangle.get_vertices()[2], triangle.get_vertices()[0]).add_tip()

        label_a = MathTex("4", font_size=24).next_to(side_a, DOWN)
        label_b = MathTex("5", font_size=24).next_to(side_b, RIGHT)
        label_c = MathTex("6", font_size=24).next_to(side_c, UP)

        side_b.shift(0.0 * RIGHT + -3.35 * UP)  # layout: separation vector
        side_c.shift(0.0 * RIGHT + -3.35 * UP)  # layout: separation vector
        triangle.shift(0.0 * RIGHT + -2.35 * UP)  # layout: separation vector
        self.play(Create(triangle), Create(side_a), Create(side_b), Create(side_c))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(1)

        # Scaling up to 8, 10, 12
        self.play(
            triangle.animate.scale(2),
            side_a.animate.scale(2),
            side_b.animate.scale(2),
            side_c.animate.scale(2),
            label_a.animate.become(MathTex("8", font_size=24)).next_to(side_a, DOWN),
            label_b.animate.become(MathTex("10", font_size=24)).next_to(side_b, RIGHT),
            label_c.animate.become(MathTex("12", font_size=24)).next_to(side_c, UP),
        )
        self.wait(1)

        # Text: Scaling preserves mirth
        text = Text("Scaling preserves mirth", font_size=24).to_edge(DOWN)
        self.play(Write(text))
        self.wait(1.5)

        # Scaling down to 2, 2.5, 3
        self.play(
            triangle.animate.scale(0.5),
            side_a.animate.scale(0.5),
            side_b.animate.scale(0.5),
            side_c.animate.scale(0.5),
            label_a.animate.become(MathTex("2", font_size=24)).next_to(side_a, DOWN),
            label_b.animate.become(MathTex("2.5", font_size=24)).next_to(side_b, RIGHT),
            label_c.animate.become(MathTex("3", font_size=24)).next_to(side_c, UP),
        )
        self.wait(1)
        # Fade out previous text
        self.play(FadeOut(text))

        # New check: sides 2, 3, 4
        triangle2 = Polygon(
            LEFT * 4/2, RIGHT * 4/2, UP * (np.sqrt(3) * 4 / 2),
            color=GREEN, fill_opacity=0.5
        ).shift(DOWN * 1)
        side_a2 = Line(triangle2.get_vertices()[0], triangle2.get_vertices()[1]).add_tip()
        side_b2 = Line(triangle2.get_vertices()[1], triangle2.get_vertices()[2]).add_tip()
        side_c2 = Line(triangle2.get_vertices()[2], triangle2.get_vertices()[0]).add_tip()
        label_a2 = MathTex("2", font_size=24).next_to(side_a2, DOWN)
        label_b2 = MathTex("3", font_size=24).next_to(side_b2, RIGHT)
        label_c2 = MathTex("4", font_size=24).next_to(side_c2, UP)

        self.play(Create(triangle2), Create(side_a2), Create(side_b2), Create(side_c2))
        self.play(Write(label_a2), Write(label_b2), Write(label_c2))
        self.wait(1)

        # Ask: Is twice the longest side at most three times the shortest?
        question = Text("Is twice the longest side at most three times the shortest?", font_size=24).to_edge(DOWN)
        self.play(Write(question))
        self.wait(1.5)

        # Show calculation
        calc = MathTex("2 \\times 4 \\leq 3 \\times 2", font_size=30).move_to(UP * 1.5)
        self.play(Write(calc))
        self.wait(1)

        # Resolve to 8 <= 6
        result = MathTex("8 \\leq 6", font_size=30).move_to(UP * 1.5)
        self.play(ReplacementTransform(calc, result))
        self.wait(1.5)

        # Red X or pulse red to indicate failure
        cross = Cross(result, color=RED, stroke_width=10)
        self.play(Create(cross))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(triangle), FadeOut(side_a), FadeOut(side_b), FadeOut(side_c),
            FadeOut(label_a), FadeOut(label_b), FadeOut(label_c),
            FadeOut(triangle2), FadeOut(side_a2), FadeOut(side_b2), FadeOut(side_c2),
            FadeOut(label_a2), FadeOut(label_b2), FadeOut(label_c2),
            FadeOut(calc), FadeOut(result), FadeOut(cross),
            FadeOut(question),
            FadeOut(title)
        )
