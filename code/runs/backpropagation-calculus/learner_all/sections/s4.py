from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Gradient Assembly & Update", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Step 1: Gradient multiplication
        grad1 = MathTex("2").scale(1.5).to_corner(UL)
        grad2 = MathTex("0.5").scale(1.5).next_to(grad1, RIGHT, buff=0.5)
        mult_arrow = Arrow(grad1.get_right(), grad2.get_left(), buff=0.1)
        equals = MathTex("=").scale(1.5).next_to(grad2, RIGHT, buff=0.5)
        result = MathTex("1").scale(1.5).next_to(equals, RIGHT, buff=0.5)

        self.play(Write(grad1), Write(grad2), Create(mult_arrow))
        self.wait(0.5)
        result.shift(-0.36 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(equals), Write(result))
        self.wait(1)

        # Step 2: Weight update visualization
        w_node = Circle(radius=0.4, color=BLUE).move_to(DOWN * 1.5)
        w_label = MathTex("w").move_to(w_node.get_center())
        w_value = MathTex("3.0").next_to(w_node, DOWN, buff=0.2)

        self.play(Write(w_node), Write(w_label), Write(w_value))
        self.wait(0.5)
        # Arrow from result to weight
        arrow = Arrow(result.get_bottom(), w_node.get_top(), color=YELLOW)
        minus_sign = MathTex("-").scale(1.2).next_to(arrow, RIGHT, buff=0.3)
        lr = MathTex("lr").scale(1.2).next_to(minus_sign, RIGHT, buff=0.2)

        self.play(Create(arrow), Write(minus_sign), Write(lr))
        self.wait(0.5)

        # Weight decreases
        new_w_value = MathTex("2.0").move_to(w_value)
        self.play(Transform(w_value, new_w_value))
        self.wait(1)

        # Loss bracket shrinks
        loss_bracket = always_redraw(lambda: Arc(start_angle=PI/2, angle=PI, radius=1.5, color=RED).move_to(DOWN * 1.5))
        self.play(Create(loss_bracket))
        self.wait(0.5)

        # Step 3: Chain Rule Metaphor - Relay Race
        self.play(FadeOut(title), FadeOut(grad1), FadeOut(grad2), FadeOut(mult_arrow), FadeOut(equals), FadeOut(result),
                  FadeOut(w_node), FadeOut(w_label), FadeOut(w_value), FadeOut(arrow), FadeOut(minus_sign), FadeOut(lr),
                  FadeOut(loss_bracket))

        relay_title = Text("Chain Rule: Relay Race", font_size=30).to_edge(UP)
        self.play(Write(relay_title))
        self.wait(0.5)

        # Nodes
        loss_node = Circle(radius=0.4, color=RED).move_to(LEFT * 3 + UP)
        loss_label = MathTex("L").move_to(loss_node.get_center())
        act_node = Circle(radius=0.4, color=YELLOW).move_to(LEFT * 1 + UP)
        act_label = MathTex("a").move_to(act_node.get_center())
        w_node = Circle(radius=0.4, color=BLUE).move_to(RIGHT * 1 + UP)
        w_label = MathTex("w").move_to(w_node.get_center())

        self.play(Write(loss_node), Write(loss_label))
        self.wait(0.3)
        self.play(Write(act_node), Write(act_label))
        self.wait(0.3)
        self.play(Write(w_node), Write(w_label))
        self.wait(0.5)

        # Arrows
        arrow1 = Arrow(loss_node.get_right(), act_node.get_left(), color=GREEN)
        arrow2 = Arrow(act_node.get_right(), w_node.get_left(), color=GREEN)
        baton = always_redraw(lambda: Dot(color=ORANGE).move_to(arrow1.get_end()))
        self.play(Create(arrow1), Create(arrow2))
        self.play(Write(baton))
        self.wait(0.5)

        # Move baton
        self.play(MoveAlongPath(baton, arrow1), run_time=1)
        self.wait(0.3)
        self.play(MoveAlongPath(baton, arrow2), run_time=1)
        self.wait(0.5)

        # Step 4: δ symbol and error signal
        self.play(FadeOut(relay_title), FadeOut(arrow1), FadeOut(arrow2), FadeOut(baton))
        delta = MathTex(r"\delta").scale(1.5).next_to(act_node, UP)
        self.play(Write(delta))
        self.wait(0.5)

        # Step 5: Derivative of squared error
        loss_func = MathTex("L = \\frac{1}{2}(\\hat{y} - y)^2").to_corner(UL)
        dLdy = MathTex("\\frac{dL}{d\\hat{y}} = \\hat{y} - y").next_to(loss_func, DOWN)
        self.play(Write(loss_func))
        self.wait(0.5)
        self.play(Write(dLdy))
        self.wait(1)

        # Step 6: Chain rule with activation
        self.play(FadeOut(loss_func), FadeOut(dLdy))

        z_node = Circle(radius=0.4, color=PURPLE).move_to(LEFT * 2 + DOWN)
        z_label = MathTex("z").move_to(z_node.get_center())
        act_node2 = Circle(radius=0.4, color=YELLOW).move_to(RIGHT * 0 + DOWN)
        act_label2 = MathTex("\\sigma(z)").move_to(act_node2.get_center())
        self.play(Write(z_node), Write(z_label))
        self.wait(0.3)
        act_label2.shift(0.0 * RIGHT + -0.8 * UP)  # layout: separation vector
        self.play(Write(act_node2), Write(act_label2))
        self.wait(0.5)

        arrow_z_act = Arrow(z_node.get_right(), act_node2.get_left(), color=GREEN)
        self.play(Create(arrow_z_act))
        self.wait(0.5)

        # Chain rule formula
        chain_rule = MathTex("\\frac{dL}{dw} = \\frac{dL}{da} \\cdot \\frac{da}{dz} \\cdot \\frac{dz}{dw}")
        chain_rule.to_corner(DR)
        self.play(Write(chain_rule))
        self.wait(1)

        # Step 7: Linear activation example
        self.play(FadeOut(chain_rule), FadeOut(z_node), FadeOut(z_label), FadeOut(act_node2), FadeOut(act_label2),
                  FadeOut(arrow_z_act))

        linear_act = Circle(radius=0.4, color=YELLOW).move_to(RIGHT * 1 + DOWN)
        linear_label = MathTex("a = z").move_to(linear_act.get_center())
        linear_label.shift(0.0 * RIGHT + -0.66 * UP)  # layout: separation vector
        self.play(Write(linear_act), Write(linear_label))
        self.wait(0.5)

        # Gradient passes through unchanged
        arrow_pass = Arrow(linear_act.get_left(), linear_act.get_right(), color=GREEN)
        self.play(Create(arrow_pass))
        self.wait(0.5)

        # Step 8: Local vs Global Minimum
        self.play(FadeOut(linear_act), FadeOut(linear_label), FadeOut(arrow_pass))

        # Simulate loss landscape
        graph = ParametricFunction(lambda t: [t, 0.2 * (t - 1)**2 + 0.5, 0], t_range=[-3, 3], color=BLUE)
        self.play(Create(graph))
        self.wait(0.5)

        # Weight at local minimum
        weight_point = Dot(color=RED).move_to([1, 0.5, 0])
        self.play(Write(weight_point))
        self.wait(1)

        self.play(FadeOut(title), FadeOut(delta), FadeOut(graph), FadeOut(weight_point))
