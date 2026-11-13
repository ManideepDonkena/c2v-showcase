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
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": WHITE},
            tips=False,
        )
        axes.to_edge(DOWN)
        self.play(Create(axes))
        
        # Function paths
        a_func = axes.plot(lambda x: x**2, color=YELLOW)
        l_func = axes.plot(lambda x: (x - 1)**2, color=RED)
        
        # Labels for functions
        a_label = MathTex("a = w^2", color=YELLOW).next_to(a_func, UR)
        l_label = MathTex("L = (a-1)^2", color=RED).next_to(l_func, UR)
        
        a_func.shift(0.0 * RIGHT + -1.65 * UP)  # layout: separation vector
        self.play(Create(a_func), Write(a_label))
        self.play(Create(l_func), Write(l_label))
        self.wait(0.5)

        # Weight and activation points
        w_point = axes.coords_to_point(-1, 1)
        a_point = axes.coords_to_point(1, 1)
        l_point = axes.coords_to_point(0, 0)

        w_dot = Dot(w_point, color=BLUE)
        a_dot = Dot(a_point, color=YELLOW)
        l_dot = Dot(l_point, color=RED)

        self.play(FadeIn(w_dot), FadeIn(a_dot), FadeIn(l_dot))
        
        # Connecting lines
        w_a_line = Line(w_point, a_point, color=YELLOW)
        a_l_line = Line(a_point, l_point, color=RED)
        
        self.play(Create(w_a_line), Create(a_l_line))
        self.wait(0.5)

        # Chain rule equation
        eq = MathTex("\\frac{dL}{dw} =", "\\frac{dL}{da}", "\\cdot", "\\frac{da}{dw}")
        eq.scale(1.2)
        eq.to_edge(UP)
        eq.shift(DOWN * 0.5)
        
        self.play(Write(eq))
        self.wait(0.5)

        # Highlighting parts of equation with graph
        dL_da = eq[1]
        da_dw = eq[3]

        self.play(
            dL_da.animate.set_color(RED),
            a_l_line.animate.set_color(RED),
            run_time=0.5
        )
        self.wait(0.5)

        self.play(
            da_dw.animate.set_color(YELLOW),
            w_a_line.animate.set_color(YELLOW),
            run_time=0.5
        )
        self.wait(1)

        # Final explanation text
        explanation = Text("To update the weight, we must apply the Chain Rule", font_size=24)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)

        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(a_func),
            FadeOut(l_func),
            FadeOut(w_dot),
            FadeOut(a_dot),
            FadeOut(l_dot),
            FadeOut(w_a_line),
            FadeOut(a_l_line),
            FadeOut(eq),
            FadeOut(explanation)
        )
