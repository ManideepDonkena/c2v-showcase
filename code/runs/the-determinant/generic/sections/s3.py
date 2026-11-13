from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Singularity and Collapse", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial basis vectors and parallelogram
        basis_i = Arrow(start=ORIGIN, end=[1, 0, 0], color=BLUE, stroke_width=8)
        basis_j = Arrow(start=ORIGIN, end=[0, 1, 0], color=YELLOW, stroke_width=8)
        
        par = Polygon(ORIGIN, [1, 0, 0], [1, 1, 0], [0, 1, 0], color=RED, fill_opacity=0.5)
        
        self.play(Create(basis_i), Create(basis_j), FadeIn(par))
        self.wait(1)

        # Labels for basis vectors
        i_label = MathTex("\\vec{\\imath}", font_size=24).next_to(basis_i.get_end(), DOWN)
        j_label = MathTex("\\vec{\\jmath}", font_size=24).next_to(basis_j.get_end(), RIGHT)
        self.play(Write(i_label), Write(j_label))
        self.wait(0.5)

        # Transform to collapse
        target_i = Arrow(start=ORIGIN, end=[1, 0, 0], color=BLUE, stroke_width=8)
        target_j = Arrow(start=ORIGIN, end=[1, 0, 0], color=YELLOW, stroke_width=8)  # Collinear
        
        self.play(
            Transform(basis_i, target_i),
            Transform(basis_j, target_j),
            run_time=2
        )
        
        # Update parallelogram to line
        new_par = Line(start=ORIGIN, end=[1, 0, 0], color=RED, stroke_width=8)
        self.play(Transform(par, new_par), run_time=1.5)
        
        # Fade out labels and shape
        self.play(FadeOut(i_label), FadeOut(j_label), FadeOut(par))
        self.wait(0.5)

        # Show determinant = 0
        det_text = MathTex("\\det(A) = 0", font_size=40).to_edge(UP)
        self.play(ReplacementTransform(title, det_text))
        self.wait(1.5)

        # Explanation text
        collapse_text = Text("The shape collapses completely", font_size=24)
        collapse_text.to_edge(DOWN)
        self.play(Write(collapse_text))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(collapse_text), FadeOut(det_text))
        self.wait(0.5)
