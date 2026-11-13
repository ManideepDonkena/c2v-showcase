from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Linear Combinations", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": WHITE},
            tips=False
        )
        axes.to_edge(DOWN)
        self.play(Create(axes))
        self.wait(0.5)

        # Basis vectors i and j
        i_vec = Arrow(axes.coords_to_point(0,0), axes.coords_to_point(1,0), color=RED, buff=0)
        j_vec = Arrow(axes.coords_to_point(0,0), axes.coords_to_point(0,1), color=BLUE, buff=0)
        
        i_label = MathTex("\\mathbf{i}", color=RED).next_to(i_vec.get_end(), DOWN, buff=0.1)
        j_label = MathTex("\\mathbf{j}", color=BLUE).next_to(j_vec.get_end(), LEFT, buff=0.1)
        
        i_vec.shift(-0.21 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(i_vec), Write(i_label))
        self.play(Create(j_vec), Write(j_label))
        self.wait(1)

        # Vector v
        v_vec = Arrow(axes.coords_to_point(0,0), axes.coords_to_point(2,3), color=GREEN, buff=0)
        v_label = MathTex("\\mathbf{v}", color=GREEN).next_to(v_vec.get_end(), UR, buff=0.1)
        
        self.play(Create(v_vec), Write(v_label))
        self.wait(1.5)

        # Decomposition components
        v_i_proj = Arrow(axes.coords_to_point(0,0), axes.coords_to_point(2,0), color=YELLOW, buff=0)
        v_j_proj = Arrow(axes.coords_to_point(2,0), axes.coords_to_point(2,3), color=YELLOW, buff=0)
        
        v_i_label = MathTex("2\\mathbf{i}", color=YELLOW).next_to(v_i_proj.get_end(), DOWN, buff=0.1)
        v_j_label = MathTex("3\\mathbf{j}", color=YELLOW).next_to(v_j_proj.get_end(), RIGHT, buff=0.1)
        
        v_i_proj.shift(0.0 * RIGHT + 0.23 * UP)  # layout: separation vector
        self.play(Create(v_i_proj), Write(v_i_label))
        v_j_label.shift(0.0 * RIGHT + 0.37 * UP)  # layout: separation vector
        self.play(Create(v_j_proj), Write(v_j_label))
        self.wait(2)

        # Formula
        formula = MathTex("\\mathbf{v} = 2\\mathbf{i} + 3\\mathbf{j}")
        formula.to_edge(UP)
        self.play(ReplacementTransform(title, formula))
        self.wait(2.5)

        # Clear and end
        self.play(
            FadeOut(i_vec), FadeOut(j_vec), 
            FadeOut(v_vec), FadeOut(v_i_proj), FadeOut(v_j_proj),
            FadeOut(i_label), FadeOut(j_label), FadeOut(v_label),
            FadeOut(v_i_label), FadeOut(v_j_label),
            FadeOut(axes), FadeOut(formula)
        )
        self.wait(0.5)
