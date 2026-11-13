from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Third Derivative: Jerk", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        # Graph setup
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 4, 1],
            axis_config={'include_tip': False},
        ).scale(0.8).to_edge(DOWN)
        self.play(Create(axes))

        # f''(t) green curve (acceleration)
        f2_func = lambda x: 0.5 * x**2 + x
        f2_graph = axes.plot(f2_func, color=GREEN)
        f2_label = MathTex("f''(t)", color=GREEN).next_to(f2_graph, UR)
        f2_graph.shift(0.0 * RIGHT + -0.25 * UP)  # layout: separation vector
        f2_label.shift(0.0 * RIGHT + -1.02 * UP)  # layout: separation vector
        self.play(Create(f2_graph), Write(f2_label))
        self.wait(0.5)

        # f'''(t) red curve (jerk)
        f3_func = lambda x: x + 1
        f3_graph = axes.plot(f3_func, color=RED)
        f3_label = MathTex("f'''(t)", color=RED).next_to(f3_graph, UR)
        jerk_label = Text("Jerk", font_size=24).next_to(f3_label, DOWN)
        self.play(Create(f3_graph), Write(f3_label), Write(jerk_label))
        self.wait(0.5)

        # Notation d^3y/dx^3
        notation = MathTex("\\frac{d^3 y}{dx^3}").scale(1.2).next_to(jerk_label, DOWN)
        self.play(Write(notation))
        self.wait(0.5)

        # Example: f(x) = x^3
        example_text = Text("Example: f(x) = x³", font_size=24).to_corner(UL)
        self.play(Write(example_text))
        self.wait(0.5)

        # Step-by-step differentiation
        step1 = MathTex("f(x) = x^3").scale(0.8).to_edge(LEFT).shift(UP * 1.5)
        step2 = MathTex("f'(x) = 3x^2").scale(0.8).next_to(step1, DOWN)
        step3 = MathTex("f''(x) = 6x").scale(0.8).next_to(step2, DOWN)
        step4 = MathTex("f'''(x) = 6").scale(0.8).next_to(step3, DOWN)

        self.play(Write(step1))
        self.wait(0.5)
        self.play(Write(step2))
        self.wait(0.5)
        self.play(Write(step3))
        self.wait(0.5)
        self.play(Write(step4))
        self.wait(0.5)

        # Sine/Cosine cycle
        sine_cycle = Text("Cycle of sin(x):", font_size=24).to_corner(UR)
        self.play(Write(sine_cycle))
        self.wait(0.5)

        steps = [
            MathTex("\\frac{d}{dx} \\sin(x) = \\cos(x)"),
            MathTex("\\frac{d^2}{dx^2} \\sin(x) = -\\sin(x)"),
            MathTex("\\frac{d^3}{dx^3} \\sin(x) = -\\cos(x)"),
            MathTex("\\frac{d^4}{dx^4} \\sin(x) = \\sin(x)")
        ]

        for i, step in enumerate(steps):
            step.to_edge(LEFT).shift(DOWN * (i + 1))
            self.play(Write(step))
            self.wait(0.5)

        # Mixed partials
        mixed_text = Text("Mixed Partial Derivatives", font_size=24).to_corner(DL)
        self.play(Write(mixed_text))
        self.wait(0.5)

        # Exponential function example
        exp_func = MathTex("f(x) = e^{2x}").scale(0.8).to_edge(RIGHT).shift(UP * 1.5)
        self.play(Write(exp_func))
        self.wait(0.5)

        d1 = MathTex("\\frac{d}{dx} e^{2x} = 2e^{2x}").scale(0.7).next_to(exp_func, DOWN)
        d2 = MathTex("\\frac{d^2}{dx^2} e^{2x} = 4e^{2x}").scale(0.7).next_to(d1, DOWN)

        self.play(Write(d1))
        self.wait(0.5)
        self.play(Write(d2))
        self.wait(0.5)

        # Concavity
        concave_text = Text("Concave Up → Positive Second Derivative", font_size=24).to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(concave_text))
        self.wait(0.5)

        # Chain Rule example
        chain_text = Text("Chain Rule: cos(x²)", font_size=24).to_corner(UR)
        self.play(Write(chain_text))
        self.wait(0.5)

        chain_steps = [
            MathTex("\\frac{d}{dx} \\cos(x^2) = -\\sin(x^2) \\cdot 2x"),
            MathTex("= -2x \\sin(x^2)")
        ]

        for i, step in enumerate(chain_steps):
            step.to_edge(LEFT).shift(DOWN * (i + 1))
            self.play(Write(step))
            self.wait(0.5)

        # Fade out all
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(f2_graph),
            FadeOut(f3_graph),
            FadeOut(f2_label),
            FadeOut(f3_label),
            FadeOut(jerk_label),
            FadeOut(notation),
            FadeOut(example_text),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            FadeOut(step4),
            FadeOut(sine_cycle),
            FadeOut(steps[0]),
            FadeOut(steps[1]),
            FadeOut(steps[2]),
            FadeOut(steps[3]),
            FadeOut(mixed_text),
            FadeOut(exp_func),
            FadeOut(d1),
            FadeOut(d2),
            FadeOut(concave_text),
            FadeOut(chain_text),
            FadeOut(chain_steps[0]),
            FadeOut(chain_steps[1])
        )
