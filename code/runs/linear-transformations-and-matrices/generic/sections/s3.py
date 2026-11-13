from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("From Vectors to Columns", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Original basis vectors
        i_hat = Arrow(ORIGIN, RIGHT, color=RED, stroke_width=8)
        j_hat = Arrow(ORIGIN, UP, color=GREEN, stroke_width=8)
        i_label = MathTex("\\hat{i}", font_size=24).next_to(i_hat.get_end(), DOWN)
        j_label = MathTex("\\hat{j}", font_size=24).next_to(j_hat.get_end(), LEFT)

        # Transformed basis vectors
        i_hat_transformed = Arrow(ORIGIN, UP, color=RED, stroke_width=8)
        j_hat_transformed = Arrow(ORIGIN, LEFT, color=GREEN, stroke_width=8)
        i_label_t = MathTex("\\hat{i}'", font_size=24).next_to(i_hat_transformed.get_end(), DOWN)
        j_label_t = MathTex("\\hat{j}'", font_size=24).next_to(j_hat_transformed.get_end(), LEFT)

        # Setup scene
        self.play(Create(i_hat), Create(j_hat), Write(i_label), Write(j_label))
        self.wait(1)

        # Transform vectors
        self.play(
            Transform(i_hat, i_hat_transformed),
            Transform(j_hat, j_hat_transformed),
            Transform(i_label, i_label_t),
            Transform(j_label, j_label_t),
            run_time=1.5
        )
        self.wait(1)

        # Highlight transformed vectors
        i_highlight = always_redraw(lambda: SurroundingRectangle(i_hat_transformed, color=RED, buff=0.1))
        j_highlight = always_redraw(lambda: SurroundingRectangle(j_hat_transformed, color=GREEN, buff=0.1))
        self.play(Create(i_highlight), Create(j_highlight))
        self.wait(0.5)

        # Matrix brackets
        matrix_brackets = always_redraw(lambda: VGroup(
            MathTex("[", font_size=40),
            MathTex("]", font_size=40)
        ).arrange(DOWN, buff=0.1).scale(1.2).next_to(i_hat_transformed.get_end(), LEFT, buff=0.3))
        
        # Matrix entries
        matrix_entries = always_redraw(lambda: VGroup(
            MathTex("0", font_size=30).move_to(matrix_brackets[0].get_center() + UP*0.2),
            MathTex("-1", font_size=30).move_to(matrix_brackets[0].get_center() + DOWN*0.2),
            MathTex("1", font_size=30).move_to(matrix_brackets[1].get_center() + UP*0.2),
            MathTex("0", font_size=30).move_to(matrix_brackets[1].get_center() + DOWN*0.2)
        ))

        self.play(Write(matrix_brackets), Write(matrix_entries))
        self.wait(1)

        # Pulse animation
        self.play(
            LaggedStart(
                matrix_entries[0].animate.scale(1.3),
                matrix_entries[1].animate.scale(1.3),
                matrix_entries[2].animate.scale(1.3),
                matrix_entries[3].animate.scale(1.3),
                lag_ratio=0.2,
                run_time=1
            ),
            LaggedStart(
                matrix_entries[0].animate.scale(1/1.3),
                matrix_entries[1].animate.scale(1/1.3),
                matrix_entries[2].animate.scale(1/1.3),
                matrix_entries[3].animate.scale(1/1.3),
                lag_ratio=0.2,
                run_time=1
            )
        )

        # Narration text
        narration = Text("The destination of i-hat becomes the first column", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        narration2 = Text("The destination of j-hat becomes the second column", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1.5)
        self.play(FadeOut(narration2))

        # Final matrix
        final_matrix = MathTex("\\begin{bmatrix} 0 & -1 \\\\ 1 & 0 \\end{bmatrix}", font_size=36)
        final_matrix.to_edge(DOWN)
        self.play(Write(final_matrix))
        self.wait(1.5)

        self.play(FadeOut(title, i_hat, j_hat, i_label, j_label, i_highlight, j_highlight, matrix_brackets, matrix_entries, final_matrix))
