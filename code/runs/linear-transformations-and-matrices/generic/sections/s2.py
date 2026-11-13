from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Transforming the Basis", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial grid and basis vectors
        grid = always_redraw(lambda: NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-3.9, 3.9, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_opacity": 0.2}
        ))
        
        i_hat = Arrow(start=ORIGIN, end=RIGHT, color=RED, stroke_width=8)
        j_hat = Arrow(start=ORIGIN, end=UP, color=BLUE, stroke_width=8)
        
        i_label = MathTex("\\hat{i}", color=RED).next_to(i_hat.get_end(), DOWN, buff=0.1)
        j_label = MathTex("\\hat{j}", color=BLUE).next_to(j_hat.get_end(), RIGHT, buff=0.1)
        
        self.play(Create(grid), run_time=1)
        self.play(Create(i_hat), Create(j_hat), Write(i_label), Write(j_label))
        self.wait(1)

        # Transformation: 90° counter-clockwise rotation
        i_new = Arrow(start=ORIGIN, end=UP, color=RED, stroke_width=8)
        j_new = Arrow(start=ORIGIN, end=LEFT, color=BLUE, stroke_width=8)
        
        i_new_label = MathTex("\\hat{i}'", color=RED).next_to(i_new.get_end(), RIGHT, buff=0.1)
        j_new_label = MathTex("\\hat{j}'", color=BLUE).next_to(j_new.get_end(), UP, buff=0.1)

        # Show transformation
        self.play(
            Transform(i_hat, i_new),
            Transform(j_hat, j_new),
            Transform(i_label, i_new_label),
            Transform(j_label, j_new_label),
            run_time=2
        )
        self.wait(1)

        # Show grid warping
        self.play(
            grid.animate.apply_function(lambda p: np.array([p[0], p[1], 0])),
            run_time=2
        )
        self.wait(1.5)

        # Final text
        final_text = Text("A linear transformation is fully defined by where it moves the basis vectors.", font_size=24)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)

        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(i_hat),
            FadeOut(j_hat),
            FadeOut(i_label),
            FadeOut(j_label),
            FadeOut(final_text)
        )
