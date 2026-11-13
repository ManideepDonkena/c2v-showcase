from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Julia Sets for Quadratic Maps", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial black region (filled Julia set)
        filled_julia = Rectangle(width=14, height=7.8, fill_color=BLACK, fill_opacity=1, stroke_width=0)
        filled_julia.center()
        self.play(FadeIn(filled_julia))
        self.wait(1)

        # White background
        background = Rectangle(width=14, height=7.8, fill_color=WHITE, fill_opacity=1, stroke_width=0)
        background.center()
        self.play(FadeIn(background))
        self.wait(0.5)

        # Julia set boundary (approximated with a fractal-like shape)
        julia_boundary = VMobject()
        julia_boundary.set_points_as_corners([
            [7, 3.9, 0], [6, 3.9, 0], [5, 3.5, 0], [4, 3.0, 0], [3, 2.5, 0],
            [2, 2.0, 0], [1, 1.5, 0], [0.5, 1.0, 0], [0.2, 0.5, 0], [0.1, 0.2, 0],
            [-0.1, 0.1, 0], [-0.2, 0.2, 0], [-0.5, 0.5, 0], [-1, 1.0, 0],
            [-1.5, 1.5, 0], [-2, 2.0, 0], [-2.5, 2.5, 0], [-3, 3.0, 0],
            [-4, 3.5, 0], [-5, 3.9, 0], [-6, 3.9, 0], [-7, 3.9, 0],
            [-7, -3.9, 0], [-6, -3.9, 0], [-5, -3.5, 0], [-4, -3.0, 0],
            [-3, -2.5, 0], [-2, -2.0, 0], [-1, -1.5, 0], [-0.5, -1.0, 0],
            [-0.2, -0.5, 0], [-0.1, -0.2, 0], [0.1, -0.1, 0], [0.2, -0.2, 0],
            [0.5, -0.5, 0], [1, -1.0, 0], [1.5, -1.5, 0], [2, -2.0, 0],
            [2.5, -2.5, 0], [3, -3.0, 0], [4, -3.5, 0], [5, -3.9, 0],
            [6, -3.9, 0], [7, -3.9, 0]
        ])
        julia_boundary.set_fill(BLUE, opacity=0.2)
        julia_boundary.set_stroke(BLUE, width=2)
        self.play(Create(julia_boundary), run_time=3)
        self.wait(1)

        # Redraw the boundary with different style
        julia_boundary = VMobject()
        julia_boundary.set_points_as_corners([
            [7, 3.9, 0], [6, 3.9, 0], [5, 3.5, 0], [4, 3.0, 0], [3, 2.5, 0],
            [2, 2.0, 0], [1, 1.5, 0], [0.5, 1.0, 0], [0.2, 0.5, 0], [0.1, 0.2, 0],
            [-0.1, 0.1, 0], [-0.2, 0.2, 0], [-0.5, 0.5, 0], [-1, 1.0, 0],
            [-1.5, 1.5, 0], [-2, 2.0, 0], [-2.5, 2.5, 0], [-3, 3.0, 0],
            [-4, 3.5, 0], [-5, 3.9, 0], [-6, 3.9, 0], [-7, 3.9, 0],
            [-7, -3.9, 0], [-6, -3.9, 0], [-5, -3.5, 0], [-4, -3.0, 0],
            [-3, -2.5, 0], [-2, -2.0, 0], [-1, -1.5, 0], [-0.5, -1.0, 0],
            [-0.2, -0.5, 0], [-0.1, -0.2, 0], [0.1, -0.1, 0], [0.2, -0.2, 0],
            [0.5, -0.5, 0], [1, -1.0, 0], [1.5, -1.5, 0], [2, -2.0, 0],
            [2.5, -2.5, 0], [3, -3.0, 0], [4, -3.5, 0], [5, -3.9, 0],
            [6, -3.9, 0], [7, -3.9, 0]
        ])
        julia_boundary.set_stroke(WHITE, width=1)
        julia_boundary.set_fill(opacity=0)
        self.play(ShowCreation(julia_boundary))
        self.wait(2)

        # Key text elements
        chaotic = Text("Chaotic Sensitivity", font_size=24).to_edge(LEFT).shift(DOWN*2)
        self.play(Write(chaotic))
        self.wait(1.5)

        threshold = Text("Threshold Between Order and Divergence", font_size=24).next_to(chaotic, DOWN)
        self.play(Write(threshold))
        self.wait(2)

        # Fade out
        self.play(FadeOut(chaotic), FadeOut(threshold), FadeOut(julia_boundary), FadeOut(filled_julia), FadeOut(background))
        self.wait(0.5)

        # Final title fade
        self.play(FadeOut(title))
        self.wait(0.5)
