from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("From Vectors to Columns", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Axes
        axes = Axes(x_range=[-2, 2], y_range=[-2, 2], axis_config={"include_tip": True})
        axes.to_edge(DOWN)
        self.play(Create(axes))
        self.wait(0.5)

        # Original basis vectors
        i_hat = Arrow(axes.coords_to_point(0,0), axes.coords_to_point(1,0), color=RED, tip_length=0.2)
        j_hat = Arrow(axes.coords_to_point(0,0), axes.coords_to_point(0,1), color=GREEN, tip_length=0.2)
        i_label = MathTex("\\hat{i}", font_size=24).next_to(i_hat.get_end(), DOWN)
        j_label = MathTex("\\hat{j}", font_size=24).next_to(j_hat.get_end(), LEFT)

        self.play(Create(i_hat), Create(j_hat), Write(i_label), Write(j_label))
        self.wait(1)

        # Transform: i-hat goes to (0,1), j-hat goes to (-1,0)
        i_transformed = Arrow(axes.coords_to_point(0,0), axes.coords_to_point(0,1), color=RED, tip_length=0.2)
        j_transformed = Arrow(axes.coords_to_point(0,0), axes.coords_to_point(-1,0), color=GREEN, tip_length=0.2)
        i_label_t = MathTex("\\hat{i}'", font_size=24).next_to(i_transformed.get_end(), DOWN)
        j_label_t = MathTex("\\hat{j}'", font_size=24).next_to(j_transformed.get_end(), LEFT)

        self.play(Transform(i_hat, i_transformed), Transform(i_label, i_label_t))
        self.wait(0.5)
        self.play(Transform(j_hat, j_transformed), Transform(j_label, j_label_t))
        self.wait(1)

        # Highlight transformed vectors
        i_transformed_copy = i_transformed.copy().set_color(YELLOW)
        j_transformed_copy = j_transformed.copy().set_color(YELLOW)
        self.play(ShowPassingFlash(i_transformed_copy), ShowPassingFlash(j_transformed_copy))
        self.wait(0.5)

        # Matrix formation
        matrix_brackets = MathTex("\\begin{bmatrix} 0 & -1 \\\\ 1 & 0 \\end{bmatrix}", font_size=40)
        matrix_brackets.next_to(axes, UP, buff=1)
        
        self.play(Write(matrix_brackets))
        self.wait(1)

        # Pulse effect on matrix entries
        # Accessing matrix elements safely by ensuring they exist
        matrix_elements = matrix_brackets[0]  # Get the first row
        if len(matrix_elements) >= 2:
            entry_11 = matrix_elements[0]
            entry_12 = matrix_elements[1]
        else:
            entry_11 = entry_12 = None
            
        matrix_elements2 = matrix_brackets[1]  # Get the second row
        if len(matrix_elements2) >= 2:
            entry_21 = matrix_elements2[0]
            entry_22 = matrix_elements2[1]
        else:
            entry_21 = entry_22 = None

        if entry_11 and entry_12 and entry_21 and entry_22:
            self.play(
                entry_11.animate.scale(1.2).set_color(YELLOW),
                entry_12.animate.scale(1.2).set_color(YELLOW),
                entry_21.animate.scale(1.2).set_color(YELLOW),
                entry_22.animate.scale(1.2).set_color(YELLOW),
                rate_func=there_and_back,
                run_time=2
            )
        self.wait(0.5)

        # Key text explanation
        explanation = Text("The destination of i-hat becomes the first column", font_size=24)
        explanation.to_edge(UP)
        self.play(Write(explanation))
        self.wait(1)
        
        self.play(FadeOut(explanation))
        
        explanation2 = Text("The destination of j-hat becomes the second column", font_size=24)
        explanation2.to_edge(UP)
        self.play(Write(explanation2))
        self.wait(1.5)
        
        self.play(FadeOut(explanation2))

        # Final wait
        self.wait(1)
