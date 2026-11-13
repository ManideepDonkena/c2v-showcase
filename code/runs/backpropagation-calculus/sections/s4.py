from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Gradient Assembly & Update", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Local gradients
        grad1 = MathTex("\\frac{\\partial L}{\\partial z} = 2", font_size=32)
        grad2 = MathTex("\\frac{\\partial z}{\\partial w} = 3", font_size=32)
        
        grad1.next_to(title, DOWN, buff=0.5)
        grad2.next_to(grad1, DOWN, buff=0.5)
        
        self.play(Write(grad1))
        self.wait(0.5)
        self.play(Write(grad2))
        self.wait(0.5)

        # Multiplication
        multiply = MathTex("\\times", font_size=32)
        multiply.next_to(grad2, RIGHT, buff=0.5)
        
        result = MathTex("\\frac{\\partial L}{\\partial w} = 6", font_size=32)
        result.next_to(multiply, RIGHT, buff=0.5)
        
        self.play(Write(multiply))
        self.wait(0.5)
        self.play(Write(result))
        self.wait(1)

        # Weight node
        weight_node = Circle(radius=0.4, color=BLUE)
        weight_node.move_to(DOWN * 1.5)
        w_label = MathTex("w", font_size=24)
        w_label.move_to(weight_node.get_center())
        
        self.play(FadeOut(grad1), FadeOut(grad2), FadeOut(multiply))
        self.play(Create(weight_node), Write(w_label))
        self.wait(0.5)

        # Arrow from result to weight
        arrow = Arrow(result.get_right(), weight_node.get_left(), 
                     buff=0.1, color=YELLOW)
        minus = MathTex("-", font_size=32)
        minus.next_to(arrow, UP, buff=0.1)
        
        arrow.shift(0.0 * RIGHT + -0.44 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow))
        self.play(Write(minus))
        self.wait(0.5)

        # Weight update
        old_w = 5.0
        new_w = old_w - 0.01 * 6  # learning rate = 0.01
        
        old_w_text = MathTex(f"w = {old_w}", font_size=24)
        old_w_text.next_to(weight_node, DOWN, buff=0.5)
        
        new_w_text = MathTex(f"w = {new_w:.2f}", font_size=24)
        new_w_text.next_to(weight_node, DOWN, buff=0.5)
        
        self.play(Write(old_w_text))
        self.wait(0.5)
        self.play(Transform(old_w_text, new_w_text))
        self.wait(1)

        # Loss bracket
        loss_bracket = always_redraw(
            lambda: Polygon(
                [-2, 1.5, 0], [-2, -1.5, 0], [2, -1.5, 0], [2, 1.5, 0],
                color=RED, fill_opacity=0.2
            )
        )
        
        self.play(FadeOut(old_w_text), FadeOut(minus))
        self.play(Create(loss_bracket))
        self.wait(0.5)
        
        # Shrink bracket to show improvement
        self.play(
            loss_bracket.animate.scale(0.8),
            run_time=1
        )
        self.wait(1)

        self.play(FadeOut(title), FadeOut(result), FadeOut(weight_node), 
                 FadeOut(w_label), FadeOut(arrow), FadeOut(loss_bracket))
        self.wait(0.5)
