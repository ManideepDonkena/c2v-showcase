from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Julia Sets for Quadratic Maps", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Mandelbrot-like structure
        try:
            mandelbrot = ImageMobject("./mandelbrot.png").scale(1.2).move_to(ORIGIN)
            self.play(FadeIn(mandelbrot))
            self.wait(1)
        except (OSError, FileNotFoundError):
            # Fallback to a simple shape if image is not found
            mandelbrot = Circle(color=BLUE, fill_opacity=0.5).scale(1.2).move_to(ORIGIN)
            self.play(Create(mandelbrot))
            self.wait(1)

        # Julia set explanation text
        text1 = Text("For more complex functions, the boundary becomes fractal.", font_size=24).to_edge(DOWN)
        self.play(Write(text1))
        self.wait(1.5)
        self.play(FadeOut(text1))

        text2 = Text("This intricate curve is the Julia set,", font_size=24).to_edge(DOWN)
        self.play(Write(text2))
        self.wait(1.5)
        self.play(FadeOut(text2))

        text3 = Text("where points exhibit chaotic sensitivity.", font_size=24).to_edge(DOWN)
        self.play(Write(text3))
        self.wait(1.5)
        self.play(FadeOut(text3))

        # Side-by-side comparison
        c0 = ComplexPlane(x_range=[-2, 2], y_range=[-1.5, 1.5]).set_opacity(0.5)
        c0_labels = c0.get_axis_labels("Re", "Im")
        c0_group = VGroup(c0, c0_labels)

        c_neg1 = ComplexPlane(x_range=[-2, 2], y_range=[-1.5, 1.5]).set_opacity(0.5)
        c_neg1_labels = c_neg1.get_axis_labels("Re", "Im")
        c_neg1_group = VGroup(c_neg1, c_neg1_labels)

        # Show connected Julia set (c=0)
        self.play(TransformFromCopy(mandelbrot, c0_group))
        self.wait(1.5)
        self.play(FadeOut(c0_group))

        # Show disconnected Julia set (c=-2)
        self.play(TransformFromCopy(mandelbrot, c_neg1_group))
        self.wait(1.5)
        self.play(FadeOut(c_neg1_group))

        # Critical point animation
        text4 = Text("When the critical point escapes, the boundary loses its connection.", font_size=24).to_edge(DOWN)
        self.play(Write(text4))
        self.wait(2)
        self.play(FadeOut(text4))

        # Zoom into Mandelbrot set boundary
        try:
            zoomed = ImageMobject("mandelbrot_zoom.png").scale(3).move_to(ORIGIN)
            self.play(Transform(mandelbrot, zoomed))
            self.wait(1.5)
        except (OSError, FileNotFoundError):
            # Fallback if zoom image is not found
            self.play(mandelbrot.animate.scale(3).move_to(ORIGIN))
            self.wait(1.5)

        text5 = Text("The boundary is not a simple smooth line;", font_size=24).to_edge(DOWN)
        self.play(Write(text5))
        self.wait(1.5)
        self.play(FadeOut(text5))

        text6 = Text("it is a rough, self-similar fractal structure.", font_size=24).to_edge(DOWN)
        self.play(Write(text6))
        self.wait(1.5)
        self.play(FadeOut(text6))

        # Final fade out
        self.play(FadeOut(mandelbrot), FadeOut(title))
        self.wait(0.5)
