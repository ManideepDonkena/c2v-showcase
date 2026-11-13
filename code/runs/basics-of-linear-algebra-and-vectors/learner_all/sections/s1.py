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
            y_range=[-4, 4, 1],
            axis_config={"stroke_color": GREY_A},
            background_line_style={"stroke_color": GREY_D}
        )
        grid.scale(0.8)
        self.play(Create(grid))
        self.wait(0.5)

        # Point P at (3,4)
        point_P = Dot(color=YELLOW)
        point_P.move_to([3, 4, 0])
        label_P = Tex("P", font_size=24).next_to(point_P, UR, buff=0.1)
        point_P.shift(0.0 * RIGHT + -0.23 * UP)  # layout: separation vector
        label_P.shift(0.0 * RIGHT + -0.5 * UP)  # layout: separation vector
        self.play(FadeIn(point_P), Write(label_P))
        self.wait(0.5)

        # Vector arrow from origin to P
        vector_arrow = Arrow(
            start=[0, 0, 0],
            end=[3, 4, 0],
            buff=0,
            color=BLUE
        )
        vector_arrow.shift(0.0 * RIGHT + -1.15 * UP)  # layout: separation vector
        self.play(Create(vector_arrow))
        self.wait(0.5)

        # Components text
        components = MathTex("3\\mathbf{i} + 4\\mathbf{j}", font_size=32)
        components.next_to(vector_arrow, UR, buff=0.2)
        self.play(Write(components))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(point_P),
            FadeOut(label_P),
            FadeOut(vector_arrow),
            FadeOut(components)
        )
        self.wait(0.5)
