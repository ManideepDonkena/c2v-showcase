from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Calculating Local Gradients", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Activation node a = w*x
        a_node = MathTex("a = w \\cdot x").scale(1.2).to_corner(UL)
        self.play(Write(a_node))
        self.wait(0.5)

        da_dw = MathTex("\\frac{\\partial a}{\\partial w} = x").scale(1.2).next_to(a_node, DOWN)
        self.play(Write(da_dw))
        self.wait(0.5)

        # Highlight x
        x_val = Integer(2).scale(1.2).next_to(da_dw, RIGHT)
        self.play(Write(x_val))
        self.wait(0.5)

        # Loss node
        loss_node = MathTex("L = (\\hat{y} - y)^2").scale(1.2).to_corner(UR)
        self.play(Write(loss_node))
        self.wait(0.5)

        dL_da = MathTex("\\frac{\\partial L}{\\partial a} = 2(\\hat{y} - y)").scale(1.2).next_to(loss_node, DOWN)
        self.play(Write(dL_da))
        self.wait(0.5)

        # Domino effect / Relay race
        arrow = Arrow(LEFT, RIGHT, buff=0.2).scale(0.8).to_edge(DOWN)
        self.play(Write(arrow))
        self.wait(0.5)

        self.play(arrow.animate.shift(RIGHT * 2), run_time=1)
        self.wait(0.5)

        # Batons
        baton = Square(side_length=0.4, color=YELLOW).move_to(arrow.get_start())
        self.play(Write(baton))
        self.wait(0.5)

        self.play(baton.animate.shift(RIGHT * 2), run_time=1)
        self.wait(0.5)

        # Multiplication
        mult = MathTex("2 \\times 0.5 = 1").scale(1.2).to_edge(DOWN)
        self.play(Write(mult))
        self.wait(0.5)

        # Sum of gradients
        sum_node = Circle().scale(0.4).move_to(LEFT * 2 + DOWN * 1.5)
        arrow1 = Arrow(sum_node.get_right(), sum_node.get_left(), buff=0.1)
        arrow2 = Arrow(sum_node.get_top(), sum_node.get_bottom(), buff=0.1)
        self.play(Create(sum_node), Create(arrow1), Create(arrow2))
        self.wait(0.5)

        # Delta symbol
        delta = MathTex("\\delta").scale(1.2).next_to(sum_node, DOWN)
        self.play(Write(delta))
        self.wait(0.5)

        # Derivative of squared error
        dL_dy = MathTex("\\frac{\\partial L}{\\partial \\hat{y}} = 2(\\hat{y} - y)").scale(1.2).to_edge(UP)
        dL_dy.shift(0.0 * RIGHT + -0.65 * UP)  # layout: separation vector
        self.play(Write(dL_dy))
        self.wait(0.5)

        # Activation function
        act_node = MathTex("\\sigma(z)").scale(1.2).next_to(a_node, DOWN)
        act_node.shift(0.0 * RIGHT + 0.75 * UP)  # layout: separation vector
        self.play(Write(act_node))
        self.wait(0.5)

        sigma_prime = MathTex("\\sigma'(z)").scale(1.2).next_to(act_node, RIGHT)
        self.play(Write(sigma_prime))
        self.wait(0.5)

        # Chain rule
        chain_rule = MathTex("\\frac{\\partial L}{\\partial w} = \\frac{\\partial L}{\\partial a} \\cdot \\frac{\\partial a}{\\partial z} \\cdot \\frac{\\partial z}{\\partial w}")
        self.play(Write(chain_rule))
        self.wait(0.5)

        # Identity activation
        identity = MathTex("a = z").scale(1.2).to_edge(DOWN)
        self.play(Write(identity))
        self.wait(0.5)

        # Gradient preservation
        one_mult = MathTex("\\times 1").scale(1.2).next_to(identity, RIGHT)
        self.play(Write(one_mult))
        self.wait(0.5)

        # Local minima
        local_min = Circle(radius=0.3, color=RED).move_to(RIGHT * 2 + UP * 1)
        self.play(Create(local_min))
        self.wait(0.5)

        self.play(FadeOut(title), FadeOut(a_node), FadeOut(da_dw), FadeOut(x_val),
                  FadeOut(loss_node), FadeOut(dL_da), FadeOut(arrow), FadeOut(baton),
                  FadeOut(mult), FadeOut(sum_node), FadeOut(arrow1), FadeOut(arrow2),
                  FadeOut(delta), FadeOut(dL_dy), FadeOut(act_node), FadeOut(sigma_prime),
                  FadeOut(chain_rule), FadeOut(identity), FadeOut(one_mult), FadeOut(local_min))
