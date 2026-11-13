from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Geometric Interpretation", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Unit square
        square = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        square.move_to(ORIGIN)
        
        # Basis vectors
        i_hat = Arrow(ORIGIN, RIGHT, color=YELLOW)
        j_hat = Arrow(ORIGIN, UP, color=YELLOW)
        
        # Labels for basis vectors
        i_label = MathTex(r"\hat{i}", font_size=24).next_to(i_hat.get_end(), DOWN)
        j_label = MathTex(r"\hat{j}", font_size=24).next_to(j_hat.get_end(), LEFT)
        
        # Initial setup
        self.play(Create(square), run_time=1)
        self.play(Create(i_hat), Create(j_hat), Write(i_label), Write(j_label))
        self.wait(1)

        # Transformation matrix
        matrix = Matrix([[2, 1], [1, 2]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        matrix.to_corner(UL)
        matrix_label = Text("Transformation Matrix", font_size=24).next_to(matrix, DOWN)
        matrix_label.shift(0.4 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(matrix), Write(matrix_label))
        self.wait(1)

        # Apply transformation
        # New vectors after transformation
        new_i = Vector([2, 1], color=RED)
        new_j = Vector([1, 2], color=RED)
        
        # Parallelogram
        parallelogram = Polygon(ORIGIN, new_i.get_end(), new_i.get_end() + new_j.get_end(), new_j.get_end(), 
                               color=GREEN, fill_opacity=0.5)
        
        # Area label
        area_label = MathTex(r"\text{Area} = 3", font_size=24).next_to(parallelogram, DOWN)
        
        # Transform square to parallelogram
        self.play(
            ReplacementTransform(i_hat, new_i),
            ReplacementTransform(j_hat, new_j),
            FadeOut(square),
            FadeOut(i_label),
            FadeOut(j_label),
            run_time=2
        )
        self.wait(0.5)
        
        # Show parallelogram
        self.play(Create(parallelogram), Write(area_label))
        self.wait(1.5)

        # Narration text
        narration1 = Text("Imagine the determinant as a measure", font_size=24)
        narration1.to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(1)
        
        self.play(FadeOut(narration1))
        self.wait(0.5)
        
        narration2 = Text("of how much space stretches or shrinks", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1)
        
        self.play(FadeOut(narration2))
        self.wait(0.5)
        
        narration3 = Text("We start with a simple unit square", font_size=24)
        narration3.to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(1)
        
        self.play(FadeOut(narration3))
        self.wait(0.5)
        
        narration4 = Text("When we apply a linear transformation", font_size=24)
        narration4.to_edge(DOWN)
        self.play(Write(narration4))
        self.wait(1)
        
        self.play(FadeOut(narration4))
        self.wait(0.5)
        
        narration5 = Text("this shape morphs into a parallelogram", font_size=24)
        narration5.to_edge(DOWN)
        self.play(Write(narration5))
        self.wait(1)
        
        self.play(FadeOut(narration5))
        self.wait(0.5)
        
        narration6 = Text("and the determinant tells us exactly", font_size=24)
        narration6.to_edge(DOWN)
        self.play(Write(narration6))
        self.wait(1)
        
        self.play(FadeOut(narration6))
        self.wait(0.5)
        
        narration7 = Text("how its area has changed.", font_size=24)
        narration7.to_edge(DOWN)
        self.play(Write(narration7))
        self.wait(1.5)
        
        self.play(FadeOut(narration7), FadeOut(matrix), FadeOut(matrix_label), FadeOut(parallelogram), FadeOut(area_label))
        self.wait(0.5)
        
        self.play(FadeOut(title))
        self.wait(0.5)
