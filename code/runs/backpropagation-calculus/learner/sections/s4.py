from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Gradient Assembly & Update", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Local gradients
        grad1 = MathTex("\\frac{\\partial L}{\\partial z} = 2", font_size=30).to_corner(UL)
        grad2 = MathTex("\\frac{\\partial z}{\\partial w} = 3", font_size=30).next_to(grad1, DOWN)
        self.play(Write(grad1), Write(grad2))
        self.wait(1)

        # Multiply gradients
        mult_arrow = Arrow(grad1.get_bottom(), grad2.get_top(), buff=0.1, color=YELLOW)
        result = MathTex("\\frac{\\partial L}{\\partial w} = 6", font_size=30).next_to(mult_arrow, DOWN)
        self.play(GrowArrow(mult_arrow))
        self.wait(0.5)
        result.shift(0.0 * RIGHT + -0.65 * UP)  # layout: separation vector
        self.play(Write(result))
        self.wait(1)

        # Weight node
        weight_node = Circle(radius=0.4, color=BLUE).move_to(DOWN * 1.5)
        weight_label = MathTex("w", font_size=24).move_to(weight_node.get_center())
        self.play(Create(weight_node), Write(weight_label))
        self.wait(0.5)

        # Arrow from gradient to weight
        arrow = Arrow(result.get_bottom(), weight_node.get_top(), buff=0.1, color=RED)
        minus_sign = Tex("-", font_size=24).next_to(arrow, RIGHT)
        self.play(GrowArrow(arrow))
        self.wait(0.5)
        self.play(Write(minus_sign))
        self.wait(1)

        # Weight decreases
        new_weight = Circle(radius=0.4, color=BLUE).move_to(DOWN * 1.5 + LEFT * 0.3)
        new_label = MathTex("w'", font_size=24).move_to(new_weight.get_center())
        self.play(Transform(weight_node, new_weight), Transform(weight_label, new_label))
        self.wait(1)

        # Loss bracket shrinks
        loss_bracket = always_redraw(
            lambda: ArcBetweenPoints(
                LEFT * 0.5 + UP * 0.5,
                LEFT * 0.5 + DOWN * 0.5,
                angle=PI/2,
                color=GREEN
            ).move_to(LEFT * 0.5)
        )
        self.play(Create(loss_bracket))
        self.wait(1)

        # Show local valley vs global minimum
        valley = MathTex("\\text{Local Valley}", font_size=24).next_to(weight_node, DOWN)
        self.play(Write(valley))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(grad1),
            FadeOut(grad2),
            FadeOut(mult_arrow),
            FadeOut(result),
            FadeOut(arrow),
            FadeOut(minus_sign),
            FadeOut(weight_node),
            FadeOut(weight_label),
            FadeOut(loss_bracket),
            FadeOut(valley)
        )
        self.wait(0.5)
