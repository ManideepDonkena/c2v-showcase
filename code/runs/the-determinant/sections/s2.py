from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Orientation and Sign", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial parallelogram
        i_hat = Arrow(ORIGIN, RIGHT * 2, color=RED, stroke_width=8)
        j_hat = Arrow(ORIGIN, UP * 1.5, color=GREEN, stroke_width=8)
        parallelogram = Polygon(ORIGIN, RIGHT * 2, RIGHT * 2 + UP * 1.5, UP * 1.5, color=YELLOW, fill_opacity=0.5)
        
        det_label = MathTex(r"\det = 2", font_size=36).to_corner(UR)
        
        self.play(Create(i_hat), Create(j_hat), Create(parallelogram), Write(det_label))
        self.wait(1)

        # Show reflection transformation
        reflection = always_redraw(lambda: 
            Polygon(ORIGIN, RIGHT * 2, RIGHT * 2 + UP * 1.5, UP * 1.5, color=YELLOW, fill_opacity=0.5).flip(LEFT)
        )
        
        i_hat_reflected = always_redraw(lambda: Arrow(ORIGIN, LEFT * 2, color=RED, stroke_width=8))
        j_hat_reflected = always_redraw(lambda: Arrow(ORIGIN, UP * 1.5, color=GREEN, stroke_width=8))
        
        det_label_neg = MathTex(r"\det = -2", font_size=36).to_corner(UR)
        
        self.play(
            Transform(parallelogram, reflection),
            Transform(i_hat, i_hat_reflected),
            Transform(j_hat, j_hat_reflected),
            Transform(det_label, det_label_neg),
            run_time=2
        )
        self.wait(1.5)

        # Show orientation change with arrows
        arrow_i = always_redraw(lambda: Arrow(ORIGIN, LEFT * 2, color=RED, stroke_width=8))
        arrow_j = always_redraw(lambda: Arrow(ORIGIN, UP * 1.5, color=GREEN, stroke_width=8))
        
        # Show clockwise vs counter-clockwise
        cw_arrow = always_redraw(lambda: ArcBetweenPoints(LEFT * 2, UP * 1.5, angle=-PI/2, color=BLUE, stroke_width=6))
        ccw_arrow = always_redraw(lambda: ArcBetweenPoints(UP * 1.5, LEFT * 2, angle=PI/2, color=BLUE, stroke_width=6))
        
        # Show the reversal
        self.play(
            FadeOut(i_hat),
            FadeOut(j_hat),
            Transform(parallelogram, reflection),
            Create(arrow_i),
            Create(arrow_j),
            run_time=1
        )
        self.wait(0.5)
        
        # Show clockwise rotation before flip
        self.play(Create(cw_arrow), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(cw_arrow))
        
        # Show counter-clockwise after flip
        self.play(Create(ccw_arrow), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(ccw_arrow))
        
        # Final text
        orientation_text = Text("Orientation flipped", font_size=24).to_edge(DOWN)
        sign_text = Text("Determinant is negative", font_size=24).next_to(orientation_text, DOWN)
        
        self.play(Write(orientation_text), run_time=0.5)
        self.wait(0.5)
        sign_text.shift(0.0 * RIGHT + 0.23 * UP)  # layout: separation vector
        self.play(Write(sign_text), run_time=0.5)
        self.wait(1.5)
        
        # Clean up
        self.play(
            FadeOut(title),
            FadeOut(parallelogram),
            FadeOut(arrow_i),
            FadeOut(arrow_j),
            FadeOut(det_label_neg),
            FadeOut(orientation_text),
            FadeOut(sign_text),
            run_time=1
        )
        self.wait(0.5)
