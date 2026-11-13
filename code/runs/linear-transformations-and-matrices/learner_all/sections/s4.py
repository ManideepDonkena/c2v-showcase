from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Matrix-Vector Multiplication", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Setup coordinate system
        axes = Axes(x_range=[-4, 4], y_range=[-4, 4], axis_config={"include_tip": True})
        axes.to_edge(DOWN)
        self.play(Create(axes))
        self.wait(0.5)

        # Original point
        point = Dot([2, 1, 0], color=GREEN)
        label = Tex("$(2,1)$", font_size=24).next_to(point, UR)
        self.play(FadeIn(point), Write(label))
        self.wait(0.5)

        # Transformation matrix
        matrix = Matrix([[0, -1], [1, 0]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        matrix.to_edge(LEFT).shift(UP*1.5)
        self.play(Write(matrix))
        self.wait(0.5)
        
        # Vector
        vector = Matrix([2, 1], bracket_h_buff=0.2, bracket_v_buff=0.2)
        vector.next_to(matrix, RIGHT)
        self.play(Write(vector))
        self.wait(0.5)

        # Equals sign
        equals = Tex("=", font_size=36).next_to(vector, RIGHT)
        self.play(Write(equals))
        self.wait(0.5)

        # Result vector
        result = Matrix([-1, 2], bracket_h_buff=0.2, bracket_v_buff=0.2)
        result.next_to(equals, RIGHT)
        self.play(Write(result))
        self.wait(0.5)

        # Show linear combination breakdown
        # First column of matrix
        col1 = Vector([0, 1], color=YELLOW)
        col1_label = Tex("$\\vec{v_1}$", font_size=24).next_to(col1.get_end(), UR)
        self.play(ShowCreation(col1), Write(col1_label))
        self.wait(0.5)

        # Second column of matrix
        col2 = Vector([-1, 0], color=RED)
        col2_label = Tex("$\\vec{v_2}$", font_size=24).next_to(col2.get_end(), UL)
        self.play(ShowCreation(col2), Write(col2_label))
        self.wait(0.5)

        # Scale first column by 2
        scaled_col1 = Vector([0, 2], color=YELLOW)
        scaled_col1_label = Tex("$2\\vec{v_1}$", font_size=24).next_to(scaled_col1.get_end(), UR)
        self.play(Transform(col1, scaled_col1), Write(scaled_col1_label))
        self.wait(0.5)

        # Scale second column by 1
        scaled_col2 = Vector([-1, 0], color=RED)
        scaled_col2_label = Tex("$1\\vec{v_2}$", font_size=24).next_to(scaled_col2.get_end(), UL)
        self.play(Transform(col2, scaled_col2), Write(scaled_col2_label))
        self.wait(0.5)

        # Add scaled vectors
        sum_vector = Vector([-1, 2], color=PURPLE)
        sum_vector_label = Tex("$2\\vec{v_1} + 1\\vec{v_2}$", font_size=24).next_to(sum_vector.get_end(), DL)
        self.play(ShowCreation(sum_vector), Write(sum_vector_label))
        self.wait(0.5)

        # Show final destination
        final_point = Dot([-1, 2, 0], color=GREEN)
        final_label = Tex("$(-1,2)$", font_size=24).next_to(final_point, DL)
        self.play(FadeIn(final_point), Write(final_label))
        self.wait(0.5)

        # Narration text
        narration1 = Text("To find where any point goes", font_size=24)
        narration1.to_edge(BOTTOM).shift(UP*0.5)
        self.play(Write(narration1))
        self.wait(1.0)
        self.play(FadeOut(narration1))

        narration2 = Text("we multiply the matrix by its coordinates", font_size=24)
        narration2.to_edge(BOTTOM).shift(UP*0.5)
        self.play(Write(narration2))
        self.wait(1.0)
        self.play(FadeOut(narration2))

        narration3 = Text("This operation is a linear combination", font_size=24)
        narration3.to_edge(BOTTOM).shift(UP*0.5)
        self.play(Write(narration3))
        self.wait(1.0)
        self.play(FadeOut(narration3))

        # Cleanup
        self.play(
            FadeOut(matrix),
            FadeOut(vector),
            FadeOut(equals),
            FadeOut(result),
            FadeOut(col1),
            FadeOut(col2),
            FadeOut(scaled_col1_label),
            FadeOut(scaled_col2_label),
            FadeOut(sum_vector_label),
            FadeOut(col1_label),
            FadeOut(col2_label),
            FadeOut(label),
            FadeOut(final_label),
            FadeOut(axes),
            FadeOut(title)
        )
        self.wait(0.5)
