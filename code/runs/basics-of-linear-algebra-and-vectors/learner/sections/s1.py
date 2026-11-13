from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Visualizing Vectors", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Coordinate grid
        grid = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-3.9, 3.9, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY}
        )
        self.play(Create(grid))
        self.wait(0.5)

        # Point P at (3,4)
        point_P = Dot(point=RIGHT*3 + UP*4, color=YELLOW)
        label_P = Tex("P", font_size=24).next_to(point_P, UR, buff=0.1)
        point_P.shift(0.0 * RIGHT + -0.23 * UP)  # layout: separation vector
        label_P.shift(0.0 * RIGHT + -0.5 * UP)  # layout: separation vector
        self.play(FadeIn(point_P), Write(label_P))
        self.wait(0.5)

        # Vector from origin to P
        vector_OP = Arrow(start=ORIGIN, end=RIGHT*3 + UP*4, color=BLUE, buff=0)
        vector_OP.shift(0.0 * RIGHT + -1.15 * UP)  # layout: separation vector
        self.play(GrowArrow(vector_OP))
        self.wait(0.5)

        # Components text
        components = MathTex("3\\mathbf{i} + 4\\mathbf{j}", font_size=30)
        components.next_to(vector_OP, UR, buff=0.2)
        self.play(Write(components))
        self.wait(1)

        # Right triangle
        triangle = Polygon(ORIGIN, RIGHT*3, RIGHT*3 + UP*4, color=RED, fill_opacity=0.3)
        self.play(Create(triangle))
        self.wait(0.5)

        # Show Pythagorean theorem
        theorem_text = Text("The length is found using the Pythagorean theorem:", font_size=24)
        theorem_text.to_edge(DOWN)
        self.play(Write(theorem_text))
        self.wait(1)

        # Formula
        formula = MathTex("3^2 + 4^2 = 9 + 16 = 25", font_size=30)
        formula.next_to(theorem_text, DOWN, buff=0.2)
        self.play(Write(formula))
        self.wait(1)

        # Final square root
        final = MathTex(" \\Rightarrow \\sqrt{25} = 5", font_size=30)
        final.next_to(formula, RIGHT, buff=0.2)
        self.play(Write(final))
        self.wait(1.5)

        # Clean up
        self.play(
            FadeOut(triangle),
            FadeOut(theorem_text),
            FadeOut(formula),
            FadeOut(final),
            FadeOut(title),
            FadeOut(grid),
            FadeOut(point_P),
            FadeOut(label_P),
            FadeOut(vector_OP),
            FadeOut(components)
        )
        self.wait(0.5)
