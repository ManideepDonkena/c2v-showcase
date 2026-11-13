from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Calculating Local Gradients", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Activation node: a = w*x
        a_node = MathTex("a = w \\cdot x", font_size=32).shift(UP * 1.5)
        da_dw = MathTex("\\frac{\\partial a}{\\partial w} = x", font_size=32).shift(DOWN * 1.5)
        self.play(Write(a_node))
        self.wait(0.5)
        self.play(Write(da_dw))
        self.wait(1)

        # Highlight da/dw and show x = 2
        highlight = SurroundingRectangle(da_dw, color=YELLOW, buff=0.1)
        self.play(Create(highlight))
        self.wait(0.5)
        x_val = MathTex("x = 2 \\Rightarrow \\text{ gradient contribution} = 2", font_size=24).shift(DOWN * 2.5)
        self.play(Write(x_val))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(highlight), FadeOut(da_dw), FadeOut(a_node), FadeOut(x_val))

        # Loss node: L = (ŷ - y)^2
        loss_node = MathTex("L = (\\hat{y} - y)^2", font_size=32).shift(UP * 1.5)
        dL_da = MathTex("\\frac{\\partial L}{\\partial \\hat{y}} = 2(\\hat{y} - y)", font_size=32).shift(DOWN * 1.5)
        self.play(Write(loss_node))
        self.wait(0.5)
        self.play(Write(dL_da))
        self.wait(1)

        # Show derivation step
        deriv_step = MathTex("\\frac{d}{d\\hat{y}} (\\hat{y} - y)^2 = 2(\\hat{y} - y)", font_size=24).shift(DOWN * 2.5)
        self.play(Write(deriv_step))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(loss_node), FadeOut(dL_da), FadeOut(deriv_step))

        # Add activation function: a = σ(z)
        act_node = MathTex("a = \\sigma(z)", font_size=32).shift(UP * 1.5)
        sigma_prime = MathTex("\\sigma'(z)", font_size=32).shift(DOWN * 1.5)
        self.play(Write(act_node))
        self.wait(0.5)
        self.play(Write(sigma_prime))
        self.wait(1)

        # Chain rule: dL/da * σ'(z) * x
        chain_rule = MathTex("\\frac{\\partial L}{\\partial w} = \\frac{\\partial L}{\\partial a} \\cdot \\sigma'(z) \\cdot x", font_size=24).shift(DOWN * 2.5)
        self.play(Write(chain_rule))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(act_node), FadeOut(sigma_prime), FadeOut(chain_rule))

        # Show derivative of squared error with respect to ŷ, simplified
        dL_da_simplified = MathTex("\\frac{\\partial L}{\\partial \\hat{y}} = -(y - \\hat{y})", font_size=32).shift(UP * 1.5)
        self.play(Write(dL_da_simplified))
        self.wait(1)

        # Explain factor of 1/2 cancels exponent
        explanation = MathTex("\\text{Factor } \\frac{1}{2} \\text{ cancels the } 2 \\text{ from exponent}", font_size=24).shift(DOWN * 2.5)
        self.play(Write(explanation))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(dL_da_simplified), FadeOut(explanation))

        # Identity activation: a = z, so derivative is 1
        identity_act = MathTex("a = z \\Rightarrow \\frac{\\partial z}{\\partial z} = 1", font_size=32).shift(UP * 1.5)
        self.play(Write(identity_act))
        self.wait(1)

        # Compare with other slopes
        compare = MathTex("\\text{Slope } 0.5 \\Rightarrow \\text{ halved signal}", font_size=24).next_to(identity_act, DOWN, buff=0.5)
        compare2 = MathTex("\\text{Slope } 2 \\Rightarrow \\text{ doubled signal}", font_size=24).next_to(compare, DOWN, buff=0.5)
        self.play(Write(compare))
        self.wait(0.5)
        self.play(Write(compare2))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(identity_act), FadeOut(compare), FadeOut(compare2))

        # Final fade
        self.play(FadeOut(title))
        self.wait(0.5)
