from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Visualizing Vectors", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid
        grid = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-3.9, 3.9, 1],
            axis_config={"stroke_color": GREY_A},
            background_line_style={"stroke_color": GREY_D}
        )
        self.play(Create(grid))
        self.wait(0.5)

        # Point P at (3,4)
        p_label = Text("P", font_size=24).next_to([3, 4, 0], UR, buff=0.2)
        p_dot = Dot(point=[3, 4, 0], color=YELLOW)
        p_dot.shift(0.0 * RIGHT + -0.23 * UP)  # layout: separation vector
        p_label.shift(0.0 * RIGHT + -0.59 * UP)  # layout: separation vector
        self.play(FadeIn(p_dot), Write(p_label))
        self.wait(0.5)

        # Vector arrow from origin to P
        vector_arrow = Arrow(start=[0, 0, 0], end=[3, 4, 0], buff=0, color=BLUE)
        vector_arrow.shift(0.0 * RIGHT + -1.15 * UP)  # layout: separation vector
        self.play(GrowArrow(vector_arrow))
        self.wait(0.5)

        # Components text
        components = MathTex("3\\mathbf{i} + 4\\mathbf{j}", font_size=32)
        components.next_to(vector_arrow, UR, buff=0.2)
        self.play(Write(components))
        self.wait(1.5)

        # Narration key words
        kw1 = Text("vector", font_size=24).to_corner(UL)
        self.play(Write(kw1))
        self.wait(1)
        self.play(FadeOut(kw1))

        kw2 = Text("magnitude", font_size=24).to_corner(UL)
        self.play(Write(kw2))
        self.wait(1)
        self.play(FadeOut(kw2))

        kw3 = Text("direction", font_size=24).to_corner(UL)
        self.play(Write(kw3))
        self.wait(1)
        self.play(FadeOut(kw3))

        kw4 = Text("arrow", font_size=24).to_corner(UL)
        self.play(Write(kw4))
        self.wait(1)
        self.play(FadeOut(kw4))

        kw5 = Text("coordinates", font_size=24).to_corner(UL)
        self.play(Write(kw5))
        self.wait(1)
        self.play(FadeOut(kw5))

        # Final wait
        self.wait(1.5)
