from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Calculating Local Gradients", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Activation node: a = w*x
        activation_eq = MathTex("a = w \\cdot x", font_size=40)
        activation_eq.to_edge(UP).shift(DOWN*1.5)
        self.play(Write(activation_eq))
        self.wait(0.5)

        # Highlight da/dw
        da_dw = MathTex("\\frac{\\partial a}{\\partial w} = x", font_size=40)
        da_dw.to_edge(UP).shift(DOWN*2.5)
        highlight = SurroundingRectangle(da_dw, color=YELLOW, buff=0.1)
        
        self.play(Write(da_dw))
        self.play(Create(highlight))
        self.wait(1)

        # Show x = 2
        x_val = MathTex("x = 2", font_size=32)
        x_val.next_to(da_dw, DOWN, buff=0.5)
        self.play(Write(x_val))
        self.wait(0.5)

        # Fade out activation stuff
        self.play(FadeOut(activation_eq), FadeOut(da_dw), FadeOut(highlight), FadeOut(x_val))
        self.wait(0.5)

        # Loss node: L = (y_hat - y)^2
        loss_eq = MathTex("L = (\\hat{y} - y)^2", font_size=40)
        loss_eq.to_edge(UP).shift(DOWN*1.5)
        self.play(Write(loss_eq))
        self.wait(0.5)

        # Highlight dL/da
        dL_da = MathTex("\\frac{\\partial L}{\\partial a} = 2(\\hat{y} - y)", font_size=40)
        dL_da.to_edge(UP).shift(DOWN*2.5)
        highlight2 = SurroundingRectangle(dL_da, color=YELLOW, buff=0.1)
        
        self.play(Write(dL_da))
        self.play(Create(highlight2))
        self.wait(1)

        # Show gradient contribution
        contrib = MathTex("\\text{Gradient contribution} = 2", font_size=32)
        contrib.next_to(dL_da, DOWN, buff=0.5)
        self.play(Write(contrib))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(loss_eq), FadeOut(dL_da), FadeOut(highlight2), FadeOut(contrib), FadeOut(title))
        self.wait(0.5)
