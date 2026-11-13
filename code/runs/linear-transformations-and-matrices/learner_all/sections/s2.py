from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Transforming the Basis", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        # Create grid
        grid = always_redraw(lambda: NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-3.9, 3.9, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY}
        ))
        
        # Create basis vectors
        i_hat = always_redraw(lambda: Vector([1,0], color=RED))
        j_hat = always_redraw(lambda: Vector([0,1], color=BLUE))
        
        # Add grid and basis vectors
        self.play(Create(grid), run_time=1)
        self.play(Create(i_hat), Create(j_hat), run_time=1)
        self.wait(1)

        # Show transformation text
        transform_text = Text("A linear transformation reshapes the space itself.", font_size=24)
        transform_text.to_edge(DOWN)
        self.play(Write(transform_text))
        self.wait(2)

        # Rotate basis vectors 90 degrees counter-clockwise
        self.play(
            i_hat.animate.rotate(PI/2, about_point=ORIGIN),
            j_hat.animate.rotate(PI/2, about_point=ORIGIN),
            run_time=2
        )
        self.wait(1)

        # Show where vectors land
        i_land = Vector([0,1], color=RED, stroke_width=8)
        j_land = Vector([-1,0], color=BLUE, stroke_width=8)
        
        self.play(
            Transform(i_hat, i_land),
            Transform(j_hat, j_land),
            run_time=1
        )
        self.wait(1.5)

        # Show final text
        final_text = Text("Notice how the grid moves rigidly:", font_size=24)
        final_text.to_edge(DOWN)
        self.play(ReplacementTransform(transform_text, final_text))
        self.wait(1.5)

        # Show key point
        key_text = Text("if we know where i-hat and j-hat land, we know exactly where every other point goes.", font_size=24)
        key_text.to_edge(DOWN)
        self.play(ReplacementTransform(final_text, key_text))
        self.wait(3)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(key_text),
            FadeOut(grid),
            FadeOut(i_hat),
            FadeOut(j_hat),
            run_time=1
        )
