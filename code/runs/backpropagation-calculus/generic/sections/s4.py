from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Gradient Assembly & Update", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Local gradients
        grad1 = MathTex(r"\frac{\partial L}{\partial y} = 2(y - t)", font_size=30)
        grad2 = MathTex(r"\frac{\partial y}{\partial w} = x", font_size=30)
        grad1.next_to(title, DOWN, buff=0.5)
        grad2.next_to(grad1, DOWN, buff=0.5)
        self.play(Write(grad1), Write(grad2))
        self.wait(1)

        # Multiplication
        multiply = MathTex(r"\times", font_size=30)
        multiply.next_to(grad1, RIGHT, buff=0.5)
        self.play(Write(multiply))

        # Result gradient
        grad_result = MathTex(r"\frac{\partial L}{\partial w} = 2(y - t) \cdot x", font_size=30)
        grad_result.next_to(multiply, RIGHT, buff=0.5)
        self.play(Write(grad_result))
        self.wait(1.5)

        # Arrow to weight node
        arrow = Arrow(start=grad_result.get_bottom(), end=DOWN*1.5, buff=0.2, color=YELLOW)
        arrow.shift(0.53 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow))

        # Weight node
        w_node = MathTex(r"w", font_size=30)
        w_node.next_to(arrow, DOWN, buff=0.3)
        self.play(Write(w_node))
        self.wait(0.5)

        # Minus sign
        minus = Text("-", font_size=30)
        minus.next_to(w_node, LEFT, buff=0.3)
        self.play(Write(minus))
        self.wait(0.5)

        # Learning rate
        lr = MathTex(r"\alpha", font_size=24)
        lr.next_to(minus, LEFT, buff=0.3)
        self.play(Write(lr))
        self.wait(0.5)

        # Weight update
        w_new = MathTex(r"w_{new} = w - \alpha \cdot \frac{\partial L}{\partial w}", font_size=24)
        w_new.next_to(w_node, DOWN, buff=0.5)
        self.play(Write(w_new))
        self.wait(1.5)

        # Weight decrease animation
        old_w = ValueTracker(3.0)
        new_w = always_redraw(lambda: MathTex(f"{old_w.get_value():.2f}", font_size=30))
        new_w.next_to(w_node, DOWN, buff=0.3)
        self.play(Write(new_w))
        self.wait(0.5)

        # Simulate weight decrease
        self.play(old_w.animate.set_value(2.7), run_time=1.5)
        self.wait(0.5)

        # Loss bracket shrinking
        loss_bracket = always_redraw(lambda: Rectangle(
            width=3, height=1.5,
            color=RED, fill_opacity=0.3
        ).move_to(DOWN*1.5))
        self.play(Create(loss_bracket))
        self.wait(0.5)

        # Fade out
        self.play(FadeOut(VGroup(title, grad1, grad2, multiply, grad_result, arrow, w_node, minus, lr, w_new, new_w, loss_bracket)))
        self.wait(0.5)
