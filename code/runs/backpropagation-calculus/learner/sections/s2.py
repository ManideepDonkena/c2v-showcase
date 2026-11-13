from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Chain Rule Unveiled", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Graph nodes
        loss_node = Circle(radius=0.5, color=RED).move_to(LEFT * 3 + UP * 1)
        loss_text = MathTex("L", color=RED).move_to(loss_node.get_center())
        act_node = Circle(radius=0.5, color=GREEN).move_to(LEFT * 1 + UP * 1)
        act_text = MathTex("a", color=GREEN).move_to(act_node.get_center())
        weight_node = Circle(radius=0.5, color=BLUE).move_to(RIGHT * 1 + UP * 1)
        weight_text = MathTex("w", color=BLUE).move_to(weight_node.get_center())

        # Arrows
        arrow_la = Arrow(loss_node.get_right(), act_node.get_left(), buff=0.1)
        arrow_aw = Arrow(act_node.get_right(), weight_node.get_left(), buff=0.1)

        # Labels for gradients
        dLda = MathTex("\\frac{\\partial L}{\\partial a} = 2", color=GREEN).next_to(act_node, DOWN)
        daW = MathTex("\\frac{\\partial a}{\\partial w} = 0.5", color=BLUE).next_to(weight_node, DOWN)

        # Equation
        equation = MathTex("\\frac{\\partial L}{\\partial w} =", "\\frac{\\partial L}{\\partial a}", "\\cdot", "\\frac{\\partial a}{\\partial w}", "=", "1")
        equation.scale(0.8).to_edge(DOWN)
        equation[0].set_color(WHITE)
        equation[1].set_color(GREEN)
        equation[3].set_color(BLUE)
        equation[5].set_color(YELLOW)

        # Show nodes and arrows
        self.play(
            Create(loss_node), Write(loss_text),
            Create(act_node), Write(act_text),
            Create(weight_node), Write(weight_text),
            Create(arrow_la),
            Create(arrow_aw),
            run_time=1
        )
        self.wait(0.5)

        # Show gradient labels
        self.play(Write(dLda))
        self.wait(0.5)
        self.play(Write(daW))
        self.wait(0.5)

        # Show equation
        self.play(Write(equation[0]))
        self.wait(0.3)
        self.play(Write(equation[1]))
        self.wait(0.3)
        self.play(Write(equation[2]))
        self.wait(0.3)
        self.play(Write(equation[3]))
        self.wait(0.3)
        self.play(Write(equation[4]))
        self.wait(0.3)
        self.play(Write(equation[5]))
        self.wait(1)

        # Domino effect / relay race metaphor
        self.play(FadeOut(dLda), FadeOut(daW))
        self.play(Write(Text("Relay Race", font_size=24).next_to(loss_node, DOWN)))
        self.wait(0.5)
        self.play(FadeOut(Text("Relay Race", font_size=24).next_to(loss_node, DOWN)))

        # Animated arrow tracing backward
        arrow_trace = always_redraw(lambda: Arrow(
            loss_node.get_left(), act_node.get_right(),
            color=YELLOW, buff=0.1, stroke_width=8
        ))
        self.play(Create(arrow_trace))
        self.wait(0.5)
        self.play(arrow_trace.animate.become(Arrow(
            act_node.get_left(), weight_node.get_right(),
            color=YELLOW, buff=0.1, stroke_width=8
        )))
        self.wait(0.5)
        self.play(FadeOut(arrow_trace))

        # Baton pass analogy
        baton = Circle(radius=0.2, color=YELLOW).move_to(loss_node.get_center())
        self.play(Create(baton))
        self.wait(0.3)
        self.play(baton.animate.move_to(act_node.get_center()))
        self.wait(0.3)
        self.play(baton.animate.move_to(weight_node.get_center()))
        self.wait(0.5)
        self.play(FadeOut(baton))

        # Multiplication of gradients
        mult_text = MathTex("2 \\times 0.5 = 1", font_size=30).to_edge(DOWN)
        mult_text.shift(0.0 * RIGHT + -0.36 * UP)  # layout: separation vector
        self.play(Write(mult_text))
        self.wait(1)
        self.play(FadeOut(mult_text))

        # Parallel paths (summing gradients)
        node_a = Circle(radius=0.4, color=GREEN).move_to(LEFT * 2 + DOWN * 1)
        node_b = Circle(radius=0.4, color=GREEN).move_to(RIGHT * 2 + DOWN * 1)
        node_c = Circle(radius=0.4, color=BLUE).move_to(DOWN * 1)
        arrow_a = Arrow(loss_node.get_bottom(), node_a.get_top(), buff=0.1)
        arrow_b = Arrow(loss_node.get_bottom(), node_b.get_top(), buff=0.1)
        arrow_c1 = Arrow(node_a.get_bottom(), node_c.get_top(), buff=0.1)
        arrow_c2 = Arrow(node_b.get_bottom(), node_c.get_top(), buff=0.1)

        arrow_a.shift(0.0 * RIGHT + -0.66 * UP)  # layout: separation vector
        arrow_b.shift(0.0 * RIGHT + -0.71 * UP)  # layout: separation vector
        self.play(
            Create(node_a), Create(node_b), Create(node_c),
            Create(arrow_a), Create(arrow_b), Create(arrow_c1), Create(arrow_c2),
            run_time=1
        )
        self.wait(0.5)
        self.play(Write(Text("Sum of paths", font_size=24).next_to(node_c, DOWN)))
        self.wait(1)
        self.play(FadeOut(node_a), FadeOut(node_b), FadeOut(node_c),
                  FadeOut(arrow_a), FadeOut(arrow_b), FadeOut(arrow_c1), FadeOut(arrow_c2),
                  FadeOut(Text("Sum of paths", font_size=24).next_to(node_c, DOWN)))

        # Delta symbol
        delta_node = Circle(radius=0.5, color=PURPLE).move_to(RIGHT * 3 + UP * 1)
        delta_text = MathTex("\\delta", color=PURPLE).move_to(delta_node.get_center())
        self.play(Create(delta_node), Write(delta_text))
        self.wait(0.5)
        self.play(Write(Text("Local error signal", font_size=24).next_to(delta_node, DOWN)))
        self.wait(1)
        self.play(FadeOut(delta_node), FadeOut(delta_text), FadeOut(Text("Local error signal", font_size=24).next_to(delta_node, DOWN)))

        # Final fade
        self.play(
            FadeOut(title),
            FadeOut(loss_node), FadeOut(act_node), FadeOut(weight_node),
            FadeOut(loss_text), FadeOut(act_text), FadeOut(weight_text),
            FadeOut(arrow_la), FadeOut(arrow_aw),
            FadeOut(equation)
        )
        self.wait(0.5)
