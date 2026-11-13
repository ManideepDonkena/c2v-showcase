from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Orientation and Sign", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial parallelogram with basis vectors
        plane = NumberPlane()
        self.play(Create(plane), run_time=1)
        
        i_hat = Arrow(start=[0,0,0], end=[1,0,0], color=RED, stroke_width=8)
        j_hat = Arrow(start=[0,0,0], end=[0,1,0], color=GREEN, stroke_width=8)
        
        # Create parallelogram
        parallelogram = Polygon([0,0,0], [1,0,0], [1,1,0], [0,1,0], fill_opacity=0.3, color=BLUE)
        
        # Labels for basis vectors
        i_label = MathTex(r"\hat{\imath}", color=RED).next_to(i_hat.get_end(), DOWN, buff=0.1)
        j_label = MathTex(r"\hat{\jmath}", color=GREEN).next_to(j_hat.get_end(), RIGHT, buff=0.1)
        
        self.play(Create(i_hat), Create(j_hat), Write(i_label), Write(j_label))
        self.play(FadeIn(parallelogram))
        self.wait(1)

        # Show determinant value
        det_text = MathTex(r"\det = 1", color=YELLOW).to_corner(UR)
        self.play(Write(det_text))
        self.wait(1.5)

        # Apply reflection transformation (flip across y-axis)
        # Reflect i-hat and j-hat
        i_hat_reflected = Arrow(start=[0,0,0], end=[-1,0,0], color=RED, stroke_width=8)
        j_hat_reflected = Arrow(start=[0,0,0], end=[0,1,0], color=GREEN, stroke_width=8)
        
        # New parallelogram after reflection
        parallelogram_reflected = Polygon([0,0,0], [-1,0,0], [-1,1,0], [0,1,0], fill_opacity=0.3, color=BLUE)
        
        # Update basis vectors and parallelogram
        self.play(
            Transform(i_hat, i_hat_reflected),
            Transform(j_hat, j_hat_reflected),
            Transform(parallelogram, parallelogram_reflected),
            run_time=1.5
        )
        
        # Update determinant label
        det_text_new = MathTex(r"\det = -1", color=YELLOW).to_corner(UR)
        self.play(Transform(det_text, det_text_new))
        self.wait(1.5)

        # Show orientation change with arrows
        arrow_i = always_redraw(lambda: Arrow(start=[0,0,0], end=[-1,0,0], color=RED, stroke_width=8))
        arrow_j = always_redraw(lambda: Arrow(start=[0,0,0], end=[0,1,0], color=GREEN, stroke_width=8))
        
        # Show clockwise vs counter-clockwise order
        self.play(
            Transform(i_hat, arrow_i),
            Transform(j_hat, arrow_j),
            run_time=0.5
        )
        
        # Add text explanation
        explanation = Text("Orientation flipped!", font_size=24).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(1.5)
        
        # Show the key message
        key_message = Text("Negative determinant indicates orientation flip", font_size=24).move_to(explanation.get_center())
        self.play(Transform(explanation, key_message))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(i_hat),
            FadeOut(j_hat),
            FadeOut(parallelogram),
            FadeOut(det_text),
            FadeOut(explanation),
            FadeOut(plane)
        )
        self.wait(0.5)
