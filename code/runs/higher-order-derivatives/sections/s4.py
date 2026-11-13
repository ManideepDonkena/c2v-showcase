from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Higher Order Derivatives: From Velocity to Jerk", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial function f(t)
        f_t = FunctionGraph(lambda x: 0.5 * x**3 - x**2 - 3*x + 2, color=BLUE, x_range=[-4, 4])
        f_label = MathTex("f(t)", color=BLUE).next_to(f_t, DOWN, buff=0.2)
        
        # First derivative f'(t)
        df_t = FunctionGraph(lambda x: 1.5 * x**2 - 2*x - 3, color=GREEN, x_range=[-4, 4])
        df_label = MathTex("f'(t)", color=GREEN).next_to(df_t, DOWN, buff=0.2)
        
        # Second derivative f''(t)
        d2f_t = FunctionGraph(lambda x: 3*x - 2, color=ORANGE, x_range=[-4, 4])
        d2f_label = MathTex("f''(t)", color=ORANGE).next_to(d2f_t, DOWN, buff=0.2)
        
        # Third derivative f'''(t)
        d3f_t = FunctionGraph(lambda x: 3, color=RED, x_range=[-4, 4])
        d3f_label = MathTex("f'''(t)", color=RED).next_to(d3f_t, DOWN, buff=0.2)
        
        # Fourth derivative f^(4)(t) - dashed
        d4f_t = FunctionGraph(lambda x: 0, color=PURPLE, x_range=[-4, 4])
        d4f_t.set_stroke(width=2)
        d4f_t.set_dashed(True)
        d4f_label = MathTex("f^{(4)}(t)", color=PURPLE).next_to(d4f_t, DOWN, buff=0.2)
        
        # Stack graphs
        f_t.shift(0.0 * RIGHT + -3.15 * UP)  # layout: separation vector
        self.play(Create(f_t), Write(f_label))
        self.wait(1)
        
        arrow1 = Arrow(start=f_t.get_top(), end=df_t.get_bottom(), buff=0.1)
        arrow1_label = MathTex("\\frac{d}{dt}", font_size=24).next_to(arrow1, RIGHT)
        self.play(GrowArrow(arrow1), Write(arrow1_label))
        self.wait(0.5)
        self.play(Create(df_t), Write(df_label))
        self.wait(1)

        arrow2 = Arrow(start=df_t.get_top(), end=d2f_t.get_bottom(), buff=0.1)
        arrow2_label = MathTex("\\frac{d}{dt}", font_size=24).next_to(arrow2, RIGHT)
        self.play(GrowArrow(arrow2), Write(arrow2_label))
        self.wait(0.5)
        self.play(Create(d2f_t), Write(d2f_label))
        self.wait(1)

        arrow3 = Arrow(start=d2f_t.get_top(), end=d3f_t.get_bottom(), buff=0.1)
        arrow3_label = MathTex("\\frac{d}{dt}", font_size=24).next_to(arrow3, RIGHT)
        self.play(GrowArrow(arrow3), Write(arrow3_label))
        self.wait(0.5)
        self.play(Create(d3f_t), Write(d3f_label))
        self.wait(1)

        arrow4 = Arrow(start=d3f_t.get_top(), end=d4f_t.get_bottom(), buff=0.1)
        arrow4_label = MathTex("\\frac{d}{dt}", font_size=24).next_to(arrow4, RIGHT)
        self.play(GrowArrow(arrow4), Write(arrow4_label))
        self.wait(0.5)
        self.play(Create(d4f_t), Write(d4f_label))
        self.wait(1)

        # Fade out arrows and labels
        self.play(FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3), FadeOut(arrow4),
                  FadeOut(arrow1_label), FadeOut(arrow2_label), FadeOut(arrow3_label), FadeOut(arrow4_label))

        # Show general formula
        general = MathTex("\\frac{d^n}{dx^n}", font_size=40).move_to(ORIGIN)
        self.play(Transform(d4f_t, general))
        self.wait(1)

        # Text: Mathematical Abstraction
        abstraction_text = Text("Mathematical Abstraction", font_size=30).to_edge(DOWN)
        self.play(Write(abstraction_text))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(f_t), FadeOut(df_t), FadeOut(d2f_t), FadeOut(d3f_t),
                  FadeOut(d4f_t), FadeOut(f_label), FadeOut(df_label), FadeOut(d2f_label),
                  FadeOut(d3f_label), FadeOut(d4f_label), FadeOut(abstraction_text))
