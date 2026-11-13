from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Singularity and Collapse", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial basis vectors
        i_hat = Arrow(ORIGIN, RIGHT, color=BLUE, stroke_width=8)
        j_hat = Arrow(ORIGIN, UP, color=YELLOW, stroke_width=8)
        
        # Labels for basis vectors
        i_label = MathTex(r"\vec{i}", color=BLUE).next_to(i_hat.get_end(), DOWN)
        j_label = MathTex(r"\vec{j}", color=YELLOW).next_to(j_hat.get_end(), RIGHT)
        
        # Parallelogram
        parallelogram = Polygon(ORIGIN, RIGHT, RIGHT+UP, UP, color=RED, fill_opacity=0.5)
        
        # Initial text
        initial_text = Text("Determinant ≠ 0", font_size=24).to_corner(UL)
        parallelogram.shift(0.67 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(
            Create(i_hat), 
            Create(j_hat),
            Write(i_label),
            Write(j_label),
            FadeIn(parallelogram),
            Write(initial_text)
        )
        self.wait(1)

        # Transformation to collapse
        target_i = Arrow(ORIGIN, RIGHT, color=BLUE, stroke_width=8)
        target_j = Arrow(ORIGIN, RIGHT, color=YELLOW, stroke_width=8)  # Collinear
        
        # Animation of collapse
        self.play(
            Transform(j_hat, target_j),
            Transform(i_hat, target_i),
            parallelogram.animate.scale(0.5, about_edge=DOWN),
            run_time=2
        )
        
        # Update labels
        self.play(
            i_label.animate.next_to(target_i.get_end(), DOWN),
            j_label.animate.next_to(target_j.get_end(), DOWN)
        )
        
        # Final text
        collapse_text = Text("Shape collapses to line", font_size=24).to_corner(UL)
        self.play(ReplacementTransform(initial_text, collapse_text))
        self.wait(1)

        # Final transformation to point
        final_i = Arrow(ORIGIN, RIGHT, color=BLUE, stroke_width=8)
        final_j = Arrow(ORIGIN, RIGHT*0.01, color=YELLOW, stroke_width=8)  # Nearly zero
        
        self.play(
            Transform(j_hat, final_j),
            Transform(i_hat, final_i),
            parallelogram.animate.scale(0.1, about_edge=DOWN),
            run_time=2
        )
        
        # Update labels
        self.play(
            i_label.animate.next_to(final_i.get_end(), DOWN),
            j_label.animate.next_to(final_j.get_end(), DOWN)
        )
        
        # Final text
        final_text = Text("Shape collapses to point", font_size=24).to_corner(UL)
        self.play(ReplacementTransform(collapse_text, final_text))
        self.wait(1)

        # Zero determinant label
        zero_label = MathTex(r"\det(A) = 0", color=RED, font_size=40).to_edge(DOWN)
        self.play(Write(zero_label))
        self.wait(1)

        # Explanation text
        explanation = Text("Transformation is singular", font_size=24).next_to(zero_label, UP)
        self.play(Write(explanation))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(i_hat),
            FadeOut(j_hat),
            FadeOut(i_label),
            FadeOut(j_label),
            FadeOut(parallelogram),
            FadeOut(zero_label),
            FadeOut(explanation),
            FadeOut(title)
        )
        self.wait(0.5)
