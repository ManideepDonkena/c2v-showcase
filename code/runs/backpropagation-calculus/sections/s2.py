from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Chain Rule Unveiled", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Graph setup
        axes = Axes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1], 
            axis_config={"color": WHITE},
            tips=False
        )
        axes.to_edge(DOWN)
        
        # Function paths
        a_func = axes.plot(lambda x: x**2, color=YELLOW)
        l_func = axes.plot(lambda x: x**2, color=RED)
        
        # Labels
        a_label = Text("a = w²", font_size=24).next_to(a_func, UP)
        l_label = Text("L = a²", font_size=24).next_to(l_func, UP)
        
        # Weight and loss points
        w_point = axes.coords_to_point(1, 1)
        a_point = axes.coords_to_point(1, 1)
        l_point = axes.coords_to_point(1, 1)
        
        # Weight point
        w_dot = Dot(w_point, color=BLUE)
        w_text = Text("w", font_size=24).next_to(w_dot, DOWN)
        
        # Intermediate point
        a_dot = Dot(a_point, color=YELLOW)
        a_text = Text("a", font_size=24).next_to(a_dot, UP)
        
        # Loss point
        l_dot = Dot(l_point, color=RED)
        l_text = Text("L", font_size=24).next_to(l_dot, UP)
        
        # Arrows along path
        arrow1 = Arrow(w_point, a_point, color=YELLOW)
        arrow2 = Arrow(a_point, l_point, color=RED)
        
        # Show setup
        self.play(Create(axes), run_time=0.5)
        a_func.shift(0.0 * RIGHT + -1.65 * UP)  # layout: separation vector
        l_func.shift(0.0 * RIGHT + -1.65 * UP)  # layout: separation vector
        self.play(Create(a_func), Create(l_func), run_time=0.5)
        l_label.shift(0.0 * RIGHT + 0.43 * UP)  # layout: separation vector
        self.play(Write(a_label), Write(l_label), run_time=0.5)
        self.play(FadeIn(w_dot, a_dot, l_dot), run_time=0.5)
        self.play(Write(w_text), Write(a_text), Write(l_text), run_time=0.5)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2), run_time=0.5)
        
        # Equation
        eq = MathTex(r"\frac{dL}{dw} = \frac{dL}{da} \cdot \frac{da}{dw}", font_size=40)
        eq.to_edge(UP)
        self.play(Transform(title, eq), run_time=0.5)
        
        # Highlight parts
        dL_da = MathTex(r"\frac{dL}{da}", font_size=32).set_color(RED)
        da_dw = MathTex(r"\frac{da}{dw}", font_size=32).set_color(YELLOW)
        
        dL_da.next_to(arrow2, UP)
        da_dw.next_to(arrow1, DOWN)
        
        self.play(Write(dL_da), Write(da_dw), run_time=0.5)
        self.wait(1)
        
        # Fade out
        self.play(FadeOut(title, axes, a_func, l_func, w_dot, a_dot, l_dot, 
                          w_text, a_text, l_text, arrow1, arrow2, dL_da, da_dw), run_time=0.5)
