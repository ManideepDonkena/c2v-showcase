from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Linear Combinations", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        # Axes
        axes = Axes(x_range=[-4, 4, 1], y_range=[-3, 3, 1], 
                    axis_config={"stroke_color": WHITE}, 
                    tips=False)
        axes.to_edge(DOWN)
        self.play(Create(axes))
        self.wait(0.5)

        # Basis vectors i and j
        i_vec = Arrow(axes.coords_to_point(0,0), axes.coords_to_point(1,0), 
                      color=RED, buff=0)
        j_vec = Arrow(axes.coords_to_point(0,0), axes.coords_to_point(0,1), 
                      color=BLUE, buff=0)
        
        i_label = MathTex("\\mathbf{i}", font_size=24).next_to(i_vec.get_end(), DOWN)
        j_label = MathTex("\\mathbf{j}", font_size=24).next_to(j_vec.get_end(), LEFT)

        self.play(Create(i_vec), Write(i_label))
        self.play(Create(j_vec), Write(j_label))
        self.wait(1)

        # Vector v
        v_vec = Arrow(axes.coords_to_point(0,0), axes.coords_to_point(2,3), 
                      color=GREEN, buff=0)
        v_label = MathTex("\\mathbf{v}", font_size=24).next_to(v_vec.get_end(), UR)

        self.play(Create(v_vec), Write(v_label))
        self.wait(1.5)

        # Decomposition components
        v_comp_i = Arrow(axes.coords_to_point(0,0), axes.coords_to_point(2,0), 
                         color=GREEN, buff=0, stroke_width=3)
        v_comp_j = Arrow(axes.coords_to_point(2,0), axes.coords_to_point(2,3), 
                         color=GREEN, buff=0, stroke_width=3)

        self.play(Create(v_comp_i))
        self.wait(0.5)
        self.play(Create(v_comp_j))
        self.wait(1.5)

        # Show linear combination formula
        formula = MathTex("\\mathbf{v} = 2\\mathbf{i} + 3\\mathbf{j}", font_size=40)
        formula.to_edge(UP)
        self.play(Transform(title, formula))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(i_vec), FadeOut(j_vec), FadeOut(v_vec),
                  FadeOut(v_comp_i), FadeOut(v_comp_j),
                  FadeOut(i_label), FadeOut(j_label), FadeOut(v_label),
                  FadeOut(title))
        self.wait(0.5)
