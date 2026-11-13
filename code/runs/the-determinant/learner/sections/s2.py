from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Orientation and Sign", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial parallelogram with positive determinant
        i_hat = Arrow(start=ORIGIN, end=[2, 0, 0], color=BLUE, buff=0)
        j_hat = Arrow(start=ORIGIN, end=[0, 1.5, 0], color=YELLOW, buff=0)
        parallelogram = Polygon(ORIGIN, [2, 0, 0], [2, 1.5, 0], [0, 1.5, 0], color=GREEN, fill_opacity=0.3)
        det_label = MathTex(r"\det = 3", font_size=30).next_to(parallelogram, DOWN)

        self.play(Create(i_hat), Create(j_hat), Create(parallelogram), Write(det_label))
        self.wait(1)

        # Show the effect of swapping basis vectors
        i_hat_swap = Arrow(start=ORIGIN, end=[0, 1.5, 0], color=BLUE, buff=0)
        j_hat_swap = Arrow(start=ORIGIN, end=[2, 0, 0], color=YELLOW, buff=0)
        parallelogram_swap = Polygon(ORIGIN, [0, 1.5, 0], [2, 1.5, 0], [2, 0, 0], color=GREEN, fill_opacity=0.3)
        det_label_swap = MathTex(r"\det = -3", font_size=30).next_to(parallelogram_swap, DOWN)

        self.play(Transform(i_hat, i_hat_swap), Transform(j_hat, j_hat_swap),
                  Transform(parallelogram, parallelogram_swap), Transform(det_label, det_label_swap))
        self.wait(1.5)

        # Show text explanation
        explanation = Text("Swapping rows reverses orientation", font_size=24).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(i_hat), FadeOut(j_hat), FadeOut(parallelogram),
                  FadeOut(det_label), FadeOut(explanation), FadeOut(title))
        self.wait(0.5)
