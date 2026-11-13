from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Backpropagation Calculus: A Visual Journey", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Forward Pass Graph
        x = MathTex("x").shift(LEFT * 4 + UP * 1.5)
        w = MathTex("w").shift(LEFT * 2 + UP * 1.5)
        a = MathTex("a").shift(RIGHT * 0 + UP * 1.5)
        y_hat = MathTex(r"\hat{y}").shift(RIGHT * 2 + UP * 1.5)
        y = MathTex("y").shift(RIGHT * 2 + DOWN * 1.5)

        self.play(Write(x), run_time=0.5)
        self.wait(0.3)
        self.play(Write(w), run_time=0.5)
        self.wait(0.3)
        self.play(Write(a), run_time=0.5)
        self.wait(0.3)
        self.play(Write(y_hat), run_time=0.5)
        self.wait(0.3)
        self.play(Write(y), run_time=0.5)

        # Arrows
        arrow1 = Arrow(x.get_right(), w.get_left(), buff=0.1)
        arrow2 = Arrow(w.get_right(), a.get_left(), buff=0.1)
        arrow3 = Arrow(a.get_right(), y_hat.get_left(), buff=0.1)
        self.play(Create(arrow1), Create(arrow2), Create(arrow3))

        # Loss bracket
        bracket = MathTex(r"\text{Loss } L = (\hat{y} - y)^2").scale(0.7).shift(RIGHT * 2 + UP * 0.5)
        self.play(Write(bracket))
        self.wait(0.5)

        # Domino effect metaphor
        domino_text = Text("Relay Race", font_size=24).to_edge(DOWN)
        self.play(Write(domino_text))
        self.wait(1)

        # Backward pass arrow
        backward_arrow = Arrow(y_hat.get_left(), a.get_right(), buff=0.1, color=RED)
        self.play(Create(backward_arrow), run_time=0.5)
        self.wait(0.5)

        # Batons and handoff
        baton = Circle(radius=0.2, color=YELLOW).move_to(y_hat.get_center())
        baton.shift(0.47 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(baton))
        self.wait(0.3)
        self.play(baton.animate.move_to(a.get_center()))
        self.wait(0.3)
        self.play(baton.animate.move_to(w.get_center()))
        self.wait(0.3)

        # Gradient multiplication example
        grad1 = MathTex("2").scale(0.7).next_to(y_hat, UP)
        grad2 = MathTex("0.5").scale(0.7).next_to(a, UP)
        result = MathTex("= 1").scale(0.7).next_to(grad2, RIGHT)
        self.play(Write(grad1), Write(grad2))
        self.wait(0.5)
        self.play(Write(result))
        self.wait(0.5)

        # Sum of gradients
        grad3 = MathTex("0.3").scale(0.7).next_to(w, DOWN)
        grad4 = MathTex("0.7").scale(0.7).next_to(w, DOWN).shift(RIGHT * 0.5)
        sum_result = MathTex("= 1.0").scale(0.7).next_to(grad4, RIGHT)
        self.play(Write(grad3), Write(grad4))
        self.wait(0.5)
        self.play(Write(sum_result))
        self.wait(0.5)

        # Delta symbol
        delta = MathTex(r"\delta").scale(0.8).next_to(a, UP)
        delta.shift(0.0 * RIGHT + 0.39 * UP)  # layout: separation vector
        self.play(Write(delta))
        self.wait(0.5)

        # Derivative of squared error
        loss_deriv = MathTex(r"\frac{dL}{d\hat{y}} = 2(\hat{y} - y)").scale(0.7).shift(DOWN * 1.5)
        self.play(Write(loss_deriv))
        self.wait(0.5)

        # Activation function
        sigma = MathTex(r"\sigma").scale(0.7).next_to(a, UP)
        self.play(Write(sigma))
        self.wait(0.5)

        # Chain rule with activation
        chain_rule = MathTex(r"\frac{dL}{dw} = \frac{dL}{d\hat{y}} \cdot \frac{d\hat{y}}{da} \cdot \frac{da}{dw}")
        self.play(Write(chain_rule))
        self.wait(0.5)

        # Specific derivative
        specific_deriv = MathTex(r"\frac{dL}{d\hat{y}} = -(y - \hat{y})").scale(0.7).shift(DOWN * 2)
        self.play(Write(specific_deriv))
        self.wait(0.5)

        # Linear activation example
        linear_a = MathTex("a = z").scale(0.7).next_to(a, DOWN)
        self.play(Write(linear_a))
        self.wait(0.5)

        # Gradient preservation
        identity_grad = MathTex(r"\frac{da}{dz} = 1").scale(0.7).next_to(linear_a, DOWN)
        self.play(Write(identity_grad))
        self.wait(0.5)

        # Comparison with other multipliers
        mult1 = MathTex("2 \cdot 1 = 2").scale(0.6).shift(DOWN * 3)
        mult2 = MathTex("0.5 \cdot 1 = 0.5").scale(0.6).next_to(mult1, RIGHT)
        self.play(Write(mult1), Write(mult2))
        self.wait(0.5)

        # Local minimum
        local_min = Text("Local Minimum", font_size=24).to_edge(DOWN)
        self.play(Write(local_min))
        self.wait(1)

        # Cleanup
        self.play(FadeOut(title, x, w, a, y_hat, y, arrow1, arrow2, arrow3, bracket, backward_arrow,
                          baton, grad1, grad2, result, grad3, grad4, sum_result, delta, loss_deriv,
                          chain_rule, specific_deriv, linear_a, identity_grad, mult1, mult2, local_min))
        self.wait(0.5)
