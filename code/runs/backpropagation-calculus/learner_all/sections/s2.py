from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Chain Rule Unveiled", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Graph setup
        loss_node = Circle(radius=0.4, color=RED).move_to(LEFT * 3 + UP * 1.5)
        loss_label = MathTex("L", font_size=24).move_to(loss_node.get_center())
        act_node = Circle(radius=0.4, color=GREEN).move_to(LEFT * 1 + UP * 1.5)
        act_label = MathTex("a", font_size=24).move_to(act_node.get_center())
        weight_node = Circle(radius=0.4, color=BLUE).move_to(RIGHT * 1 + UP * 1.5)
        weight_label = MathTex("w", font_size=24).move_to(weight_node.get_center())

        # Arrows
        arrow1 = Arrow(loss_node.get_right(), act_node.get_left(), buff=0.1, color=RED)
        arrow2 = Arrow(act_node.get_right(), weight_node.get_left(), buff=0.1, color=GREEN)
        arrow3 = Arrow(weight_node.get_left(), act_node.get_right(), buff=0.1, color=BLUE)
        arrow4 = Arrow(act_node.get_left(), loss_node.get_right(), buff=0.1, color=RED)

        # Labels
        dLda = MathTex("\\frac{\\partial L}{\\partial a}", font_size=24, color=GREEN).next_to(arrow1, UP)
        da_dw = MathTex("\\frac{\\partial a}{\\partial w}", font_size=24, color=BLUE).next_to(arrow2, UP)

        # Equation
        eq = MathTex("\\frac{\\partial L}{\\partial w} =", "\\frac{\\partial L}{\\partial a}", "\\cdot", "\\frac{\\partial a}{\\partial w}",
                     font_size=30).move_to(DOWN * 1.5)
        self.play(Create(loss_node), Write(loss_label))
        self.play(Create(act_node), Write(act_label))
        self.play(Create(weight_node), Write(weight_label))
        self.play(Create(arrow1), Create(arrow2))
        self.wait(0.5)

        # Show Chain Rule
        self.play(Write(eq[0]))
        self.play(Write(eq[1]), FadeIn(dLda))
        self.play(Write(eq[2]))
        self.play(Write(eq[3]), FadeIn(da_dw))
        self.wait(1)

        # Domino effect metaphor
        self.play(Write(Text("Domino Effect", font_size=24).to_edge(UP + LEFT)))
        self.wait(0.5)
        self.play(FadeOut(Text("Domino Effect", font_size=24).to_edge(UP + LEFT)))

        # Relay race baton pass
        self.play(Write(Text("Relay Race", font_size=24).to_edge(UP + LEFT)))
        self.wait(0.5)
        self.play(FadeOut(Text("Relay Race", font_size=24).to_edge(UP + LEFT)))

        # Gradient multiplication example
        mult = MathTex("2 \\times 0.5 =", "1", font_size=30).move_to(DOWN * 2)
        self.play(Write(mult))
        self.wait(1)
        self.play(FadeOut(mult))

        # Two incoming arrows
        node = Circle(radius=0.4, color=YELLOW).move_to(LEFT * 2 + DOWN * 1)
        node_label = MathTex("\\delta", font_size=24).move_to(node.get_center())
        arrow5 = Arrow(node.get_right(), loss_node.get_left(), buff=0.1, color=YELLOW)
        arrow6 = Arrow(node.get_top(), act_node.get_bottom(), buff=0.1, color=YELLOW)
        self.play(Create(node), Write(node_label))
        self.play(Create(arrow5), Create(arrow6))
        self.wait(0.5)

        # Delta symbol
        delta_text = Text("δ = local error signal", font_size=24).next_to(node, DOWN)
        self.play(Write(delta_text))
        self.wait(1)
        self.play(FadeOut(delta_text))

        # Derivative of squared error
        loss_func = MathTex("L = \\frac{1}{2}(\\hat{y} - y)^2", font_size=24).move_to(UP * 2)
        dLdy = MathTex("\\frac{\\partial L}{\\partial \\hat{y}} =", "2(\\hat{y} - y)", font_size=24).next_to(loss_func, DOWN)
        self.play(Write(loss_func))
        self.wait(0.5)
        self.play(Write(dLdy))
        self.wait(1)
        self.play(FadeOut(loss_func), FadeOut(dLdy))

        # Activation function
        sigma = MathTex("\\sigma", font_size=24).next_to(act_node, DOWN)
        self.play(Write(sigma))
        self.wait(0.5)

        # Chain rule with activation
        chain3 = MathTex("\\frac{\\partial L}{\\partial w} =", "\\frac{\\partial L}{\\partial a}", "\\cdot", "\\sigma'(z)", "\\cdot", "x",
                         font_size=24).move_to(DOWN * 1.5)
        self.play(Write(chain3))
        self.wait(1)
        self.play(FadeOut(chain3))

        # Specific derivative
        dLdy2 = MathTex("\\frac{\\partial L}{\\partial \\hat{y}} =", "-(y - \\hat{y})", font_size=24).move_to(DOWN * 1.5)
        self.play(Write(dLdy2))
        self.wait(1)
        self.play(FadeOut(dLdy2))

        # Identity activation
        identity = MathTex("a = z", font_size=24).next_to(act_node, DOWN)
        self.play(Write(identity))
        self.wait(0.5)

        # Gradient flow comparison
        self.play(Write(Text("Gradient flows unchanged (multiplier = 1)", font_size=24).to_edge(DOWN)))
        self.wait(1)
        self.play(FadeOut(Text("Gradient flows unchanged (multiplier = 1)", font_size=24)))

        # Local minimum vs global
        local_min = Circle(radius=0.3, color=PURPLE).move_to(RIGHT * 2 + DOWN * 1)
        local_min_label = MathTex("\\text{Local Min}", font_size=20).next_to(local_min, DOWN)
        self.play(Create(local_min), Write(local_min_label))
        self.wait(1)
        self.play(FadeOut(local_min), FadeOut(local_min_label))

        # Final cleanup
        self.play(FadeOut(title), FadeOut(loss_node), FadeOut(act_node), FadeOut(weight_node),
                  FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3), FadeOut(arrow4),
                  FadeOut(loss_label), FadeOut(act_label), FadeOut(weight_label),
                  FadeOut(dLda), FadeOut(da_dw), FadeOut(eq), FadeOut(sigma), FadeOut(identity))
        self.wait(0.5)
