from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Higher Order Derivatives: From Velocity to Jerk", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Stack of graphs
        f_t = FunctionGraph(lambda x: 0.2 * (x - 2)**3 + 1, color=BLUE, x_range=[-4, 6]).shift(LEFT*8.84 + UP*38.35)
        f_prime_t = FunctionGraph(lambda x: 0.6 * (x - 2)**2, color=GREEN, x_range=[-4, 6]).shift(LEFT*8.84 + UP*38.35)
        f_double_prime_t = FunctionGraph(lambda x: 1.2 * (x - 2), color=RED, x_range=[-4, 6]).shift(LEFT*8.84 + UP*38.35)
        f_triple_prime_t = FunctionGraph(lambda x: 1.2 * np.ones_like(x), color=ORANGE, x_range=[-4, 6]).shift(LEFT*8.84 + UP*38.35)

        # Labels
        label_f = MathTex("f(t)", color=BLUE).next_to(f_t, DOWN, buff=0.2)
        label_f_prime = MathTex("f'(t)", color=GREEN).next_to(f_prime_t, DOWN, buff=0.2)
        label_f_double_prime = MathTex("f''(t)", color=RED).next_to(f_double_prime_t, DOWN, buff=0.2)
        label_f_triple_prime = MathTex("f'''(t)", color=ORANGE).next_to(f_triple_prime_t, DOWN, buff=0.2)

        # Arrows
        arrow1 = Arrow(start=f_t.get_bottom(), end=f_prime_t.get_top(), color=YELLOW)
        arrow2 = Arrow(start=f_prime_t.get_bottom(), end=f_double_prime_t.get_top(), color=YELLOW)
        arrow3 = Arrow(start=f_double_prime_t.get_bottom(), end=f_triple_prime_t.get_top(), color=YELLOW)

        # Show first three graphs
        f_t.shift(9.8 * RIGHT + 0.0 * UP)  # layout: separation vector
        f_t.shift(0.0 * RIGHT + 7.5 * UP)  # layout: separation vector
        self.play(Create(f_t), Write(label_f))
        self.wait(0.5)
        self.play(Create(arrow1), Create(f_prime_t), Write(label_f_prime))
        self.wait(0.5)
        self.play(Create(arrow2), Create(f_double_prime_t), Write(label_f_double_prime))
        self.wait(0.5)
        self.play(Create(arrow3), Create(f_triple_prime_t), Write(label_f_triple_prime))
        self.wait(1)

        # Show dashed fourth derivative
        f_quad_prime = DashedVMobject(FunctionGraph(lambda x: 0.2 * (x - 2)**3 + 1, color=PURPLE, x_range=[-4, 6]))
        label_f_quad_prime = MathTex("f^{(4)}(t)", color=PURPLE).next_to(f_quad_prime, DOWN, buff=0.2)
        self.play(Create(f_quad_prime), Write(label_f_quad_prime))
        self.wait(1)

        # General formula
        general_formula = MathTex(r"\frac{d^n}{dx^n}").scale(1.5).to_edge(UP)
        self.play(Transform(title, general_formula))
        self.wait(0.5)

        # Show jerk notation
        jerk_label = Text("Jerk", font_size=24).next_to(f_triple_prime_t, RIGHT, buff=0.5)
        jerk_notation = MathTex(r"\frac{d^3y}{dx^3}", color=ORANGE).next_to(jerk_label, DOWN, buff=0.2)
        self.play(Write(jerk_label), Write(jerk_notation))
        self.wait(1)

        # Example: x^3
        example = MathTex("f(x) = x^3").to_edge(DOWN)
        self.play(Write(example))
        self.wait(0.5)

        # Step-by-step differentiation of x^3
        step1 = MathTex("f'(x) = 3x^2").next_to(example, UP, buff=0.5)
        step2 = MathTex("f''(x) = 6x").next_to(step1, UP, buff=0.5)
        step3 = MathTex("f'''(x) = 6").next_to(step2, UP, buff=0.5)

        self.play(Write(step1))
        self.wait(0.5)
        self.play(Write(step2))
        self.wait(0.5)
        self.play(Write(step3))
        self.wait(1)

        # Sine/cosine cycle
        self.play(FadeOut(example), FadeOut(step1), FadeOut(step2), FadeOut(step3))

        sine_graph = FunctionGraph(np.sin, color=BLUE, x_range=[-4, 4])
        cos_graph = FunctionGraph(np.cos, color=GREEN, x_range=[-4, 4])
        neg_sin_graph = FunctionGraph(lambda x: -np.sin(x), color=ORANGE, x_range=[-4, 4])
        neg_cos_graph = FunctionGraph(lambda x: -np.cos(x), color=PURPLE, x_range=[-4, 4])

        sine_label = MathTex("\sin(x)").to_edge(UP)
        self.play(Create(sine_graph), Write(sine_label))
        self.wait(0.5)

        cos_label = MathTex("\cos(x)").next_to(sine_graph, DOWN, buff=0.2)
        self.play(Transform(sine_graph, cos_graph), Write(cos_label))
        self.wait(0.5)

        neg_sin_label = MathTex("-\sin(x)").next_to(cos_graph, DOWN, buff=0.2)
        self.play(Transform(cos_graph, neg_sin_graph), Write(neg_sin_label))
        self.wait(0.5)

        neg_cos_label = MathTex("-\cos(x)").next_to(neg_sin_graph, DOWN, buff=0.2)
        self.play(Transform(neg_sin_graph, neg_cos_graph), Write(neg_cos_label))
        self.wait(0.5)

        final_sin_label = MathTex("\sin(x)").next_to(neg_cos_graph, DOWN, buff=0.2)
        self.play(Transform(neg_cos_graph, sine_graph), Write(final_sin_label))
        self.wait(1)

        # Mixed partials
        self.play(FadeOut(sine_label), FadeOut(cos_label), FadeOut(neg_sin_label), FadeOut(neg_cos_label), FadeOut(final_sin_label))

        # Green line for f''(t)
        green_line = Line(start=LEFT * 3, end=RIGHT * 3, color=GREEN)
        green_line.to_edge(DOWN, buff=1.5)
        green_line_label = MathTex("f''(t)", color=GREEN).next_to(green_line, UP, buff=0.2)

        # Blue curve curving up
        blue_curve = FunctionGraph(lambda x: 0.2 * (x - 2)**3 + 1, color=BLUE, x_range=[-4, 6])
        self.play(Create(blue_curve), Create(green_line), Write(green_line_label))
        self.wait(1)

        # Concavity
        concave_up = Text("Concave Up", font_size=24).next_to(green_line, UP, buff=0.5)
        self.play(Write(concave_up))
        self.wait(1)

        # Exponential example
        self.play(FadeOut(blue_curve), FadeOut(green_line), FadeOut(green_line_label), FadeOut(concave_up))

        exp_func = MathTex("f(x) = e^{2x}").to_edge(UP)
        self.play(Write(exp_func))
        self.wait(0.5)

        first_deriv = MathTex("f'(x) = 2e^{2x}").next_to(exp_func, DOWN, buff=0.5)
        second_deriv = MathTex("f''(x) = 4e^{2x}").next_to(first_deriv, DOWN, buff=0.5)

        self.play(Write(first_deriv))
        self.wait(0.5)
        self.play(Write(second_deriv))
        self.wait(1)

        # Chain rule example
        self.play(FadeOut(exp_func), FadeOut(first_deriv), FadeOut(second_deriv))

        chain_example = MathTex("f(x) = \cos(x^2)").to_edge(UP)
        self.play(Write(chain_example))
        self.wait(0.5)

        outer_diff = MathTex(r"\frac{d}{dx} \cos(x^2) = -\sin(x^2)").next_to(chain_example, DOWN, buff=0.5)
        inner_diff = MathTex(r"= -\sin(x^2) \cdot 2x").next_to(outer_diff, DOWN, buff=0.5)

        self.play(Write(outer_diff))
        self.wait(0.5)
        self.play(Write(inner_diff))
        self.wait(1)

        # Final fade
        self.play(FadeOut(chain_example), FadeOut(outer_diff), FadeOut(inner_diff))
        self.wait(0.5)
