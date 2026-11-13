from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Orbit of a Point", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Complex plane
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            axis_config={"stroke_color": GREY_A},
            background_line_style={"stroke_color": GREY_D}
        )
        plane.scale(1.5)
        self.play(Create(plane))
        self.wait(0.5)

        # Fixed point z = 0
        origin = Dot(plane.coords_to_point(0, 0), color=WHITE)
        origin_label = MathTex("0", font_size=24).next_to(origin, DOWN, buff=0.1)
        self.play(FadeIn(origin), Write(origin_label))
        self.wait(0.5)

        # Initial point z_0
        z0 = Dot(plane.coords_to_point(1, 0), color=RED)
        z0_label = MathTex("z_0", font_size=24).next_to(z0, UR, buff=0.1)
        self.play(FadeIn(z0), Write(z0_label))
        self.wait(0.5)

        # Function f(z) = z^2
        func_text = MathTex("f(z) = z^2", font_size=30).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(func_text))
        self.wait(0.5)

        # First iteration: z_1 = f(z_0)
        z1 = Dot(plane.coords_to_point(-1, 0), color=RED)
        z1_label = MathTex("z_1", font_size=24).next_to(z1, DL, buff=0.1)
        self.play(Transform(z0, z1), Transform(z0_label, z1_label))
        self.wait(0.5)

        # Second iteration: z_2 = f(z_1)
        z2 = Dot(plane.coords_to_point(-1, 0), color=RED)
        z2_label = MathTex("z_2", font_size=24).next_to(z2, DR, buff=0.1)
        self.play(Transform(z1, z2), Transform(z1_label, z2_label))
        self.wait(0.5)

        # Show orbit path
        orbit_path = VMobject(color=YELLOW, stroke_width=3)
        orbit_path.set_points_as_corners([
            plane.coords_to_point(1, 0),
            plane.coords_to_point(-1, 0),
            plane.coords_to_point(1, 0)
        ])
        self.play(Create(orbit_path))
        self.wait(1)

        # Fade out
        self.play(
            FadeOut(z0), FadeOut(z0_label),
            FadeOut(z1), FadeOut(z1_label),
            FadeOut(z2), FadeOut(z2_label),
            FadeOut(orbit_path),
            FadeOut(func_text),
            FadeOut(origin), FadeOut(origin_label),
            FadeOut(title)
        )
        self.wait(0.5)
