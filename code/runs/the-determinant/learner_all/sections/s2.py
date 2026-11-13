from manim import *

class S2(Scene):
    def construct(self):
        title = Text("Orientation and Sign", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial parallelogram with positive determinant (2)
        matrix_A = [[1, 2], [3, 4]]
        i_hat = Arrow(start=ORIGIN, end=[1, 0, 0], color=RED, stroke_width=6)
        j_hat = Arrow(start=ORIGIN, end=[0, 1, 0], color=GREEN, stroke_width=6)
        parallelogram_A = Polygon(ORIGIN, i_hat.end, i_hat.end + j_hat.end, j_hat.end, color=BLUE, fill_opacity=0.5)

        self.play(Create(i_hat), Create(j_hat), Create(parallelogram_A))
        self.wait(1)

        # Show determinant magnitude equals area
        area_text = MathTex(r"\text{Area} = |ad - bc| = |1 \cdot 4 - 2 \cdot 3| = |-2| = 2", font_size=24)
        area_text.to_edge(DOWN)
        self.play(Write(area_text))
        self.wait(1.5)

        # Apply reflection transformation
        i_hat_reflect = Arrow(start=ORIGIN, end=[-1, 0, 0], color=RED, stroke_width=6)
        j_hat_reflect = Arrow(start=ORIGIN, end=[0, -1, 0], color=GREEN, stroke_width=6)
        parallelogram_reflect = Polygon(ORIGIN, i_hat_reflect.end, i_hat_reflect.end + j_hat_reflect.end, j_hat_reflect.end, color=BLUE, fill_opacity=0.5)

        self.play(Transform(i_hat, i_hat_reflect), Transform(j_hat, j_hat_reflect), Transform(parallelogram_A, parallelogram_reflect))
        self.wait(1)

        # Show negative determinant
        det_text = MathTex(r"\det(A) = ad - bc = 1 \cdot (-4) - 2 \cdot (-3) = -4 + 6 = 2", font_size=24)
        det_text.to_edge(DOWN).shift(UP * 0.5)
        self.play(Transform(area_text, det_text))
        self.wait(1)

        # Show orientation flip
        flip_text = Text("Orientation Flipped!", font_size=24).next_to(det_text, DOWN)
        self.play(Write(flip_text))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(i_hat), FadeOut(j_hat), FadeOut(parallelogram_A), FadeOut(area_text), FadeOut(flip_text), FadeOut(title))
        self.wait(0.5)
