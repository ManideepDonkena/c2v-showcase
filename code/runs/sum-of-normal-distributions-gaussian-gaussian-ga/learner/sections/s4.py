from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Resulting Gaussian", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Original Gaussians
        x = np.linspace(-4, 6, 100)
        y1 = np.exp(-0.5 * (x - 1)**2) / np.sqrt(2*np.pi)
        y2 = np.exp(-0.5 * (x - 2)**2) / np.sqrt(2*np.pi)

        blue_curve = VMobject(color=BLUE).set_points_as_corners([*zip(x, y1, [0]*len(x))])
        red_curve = VMobject(color=RED).set_points_as_corners([*zip(x, y2, [0]*len(x))])
        self.play(Create(blue_curve), Create(red_curve))
        self.wait(1)

        # Fade out original curves
        self.play(FadeOut(blue_curve), FadeOut(red_curve))
        self.wait(0.5)

        # New green curve (result)
        y3 = np.exp(-0.5 * (x - 3)**2 / 2) / np.sqrt(2*np.pi * 2)
        green_curve = VMobject(color=GREEN).set_points_as_corners([*zip(x, y3, np.zeros_like(x))])
        self.play(Create(green_curve))
        self.wait(1)

        # Labels
        mu_label = MathTex(r"\mu_{\text{new}} = 1 + 2 = 3", font_size=24).to_edge(DOWN)
        sigma_label = MathTex(r"\sigma^2_{\text{new}} = 1 + 1 = 2", font_size=24).next_to(mu_label, DOWN)
        sigma_label.shift(0.0 * RIGHT + 0.18 * UP)  # layout: separation vector
        self.play(Write(mu_label), Write(sigma_label))
        self.wait(1.5)

        # Variance boxes
        var_x = Rectangle(width=2, height=1, color=BLUE).set_fill(BLUE, opacity=0.3)
        var_y = Rectangle(width=2, height=1, color=RED).set_fill(RED, opacity=0.3)
        var_x_label = Text("Variance of X", font_size=20).move_to(var_x.get_center())
        var_y_label = Text("Variance of Y", font_size=20).move_to(var_y.get_center())

        total_var = Rectangle(width=2, height=1, color=GREEN).set_fill(GREEN, opacity=0.3)
        total_var_label = Text("Total Variance", font_size=20).move_to(total_var.get_center())
        arrow = Arrow(start=var_x.get_right(), end=total_var.get_left(), buff=0.2)

        var_y_label.shift(0.0 * RIGHT + 0.37 * UP)  # layout: separation vector
        self.play(
            FadeIn(var_x), FadeIn(var_y),
            Write(var_x_label), Write(var_y_label)
        )
        self.wait(1)
        arrow.shift(0.0 * RIGHT + 0.43 * UP)  # layout: separation vector
        self.play(Create(arrow), FadeIn(total_var), Write(total_var_label))
        self.wait(1.5)
        self.play(FadeOut(var_x), FadeOut(var_y), FadeOut(var_x_label), FadeOut(var_y_label),
                  FadeOut(arrow), FadeOut(total_var), FadeOut(total_var_label))

        # Merging two identical curves
        x = np.linspace(-3, 3, 100)
        y1 = np.exp(-0.5 * (x - 0)**2) / np.sqrt(2*np.pi)
        y2 = np.exp(-0.5 * (x - 0)**2) / np.sqrt(2*np.pi)
        curve1 = VMobject(color=BLUE).set_points_as_corners([*zip(x, y1, [0]*len(x))])
        curve2 = VMobject(color=BLUE).set_points_as_corners([*zip(x, y2, [0]*len(x))])

        self.play(Create(curve1), Create(curve2))
        self.wait(1)

        # Merge into one wider green curve
        y3 = np.exp(-0.5 * (x - 0)**2 / 2) / np.sqrt(2*np.pi * 2)
        merged_curve = VMobject(color=GREEN).set_points_as_corners([*zip(x, y3, [0]*len(x))])
        self.play(Transform(curve1, merged_curve), Transform(curve2, merged_curve))
        self.wait(1.5)

        # Equation for mean
        mean_eq = MathTex(r"\mu_{\text{sum}} = \mu_X + \mu_Y", font_size=30).to_edge(UP)
        self.play(Write(mean_eq))
        self.wait(1.5)

        # Example with N(5,1) + N(5,1)
        x = np.linspace(-2, 12, 100)
        y1 = np.exp(-0.5 * (x - 5)**2) / np.sqrt(2*np.pi)
        y2 = np.exp(-0.5 * (x - 5)**2) / np.sqrt(2*np.pi)
        curve1 = VMobject(color=BLUE).set_points_as_corners([*zip(x, y1, [0]*len(x))])
        curve2 = VMobject(color=RED).set_points_as_corners([*zip(x, y2, [0]*len(x))])

        self.play(Create(curve1), Create(curve2))
        self.wait(1)

        # Resulting curve
        y3 = np.exp(-0.5 * (x - 10)**2 / 2) / np.sqrt(2*np.pi * 2)
        result_curve = VMobject(color=GREEN).set_points_as_corners([*zip(x, y3, [0]*len(x))])
        self.play(Transform(curve1, result_curve), Transform(curve2, result_curve))
        self.wait(1.5)

        # Final equation with values
        final_eq = MathTex(r"\mu_{\text{sum}} = 5 + 5 = 10", font_size=30).to_edge(UP)
        self.play(Transform(mean_eq, final_eq))
        self.wait(1.5)

        # Multiply Gaussians (point-wise)
        x = np.linspace(-4, 6, 100)
        y1 = np.exp(-0.5 * (x - 1)**2) / np.sqrt(2*np.pi)
        y2 = np.exp(-0.5 * (x - 2)**2) / np.sqrt(2*np.pi)
        curve1 = VMobject(color=BLUE).set_points_as_corners([*zip(x, y1, [0]*len(x))])
        curve2 = VMobject(color=RED).set_points_as_corners([*zip(x, y2, [0]*len(x))])

        self.play(Create(curve1), Create(curve2))
        self.wait(1)

        # Multiply point-wise
        y3 = np.exp(-0.5 * (x - 1.5)**2 / 0.5) / np.sqrt(2*np.pi * 0.5)
        mult_curve = VMobject(color=YELLOW).set_points_as_corners([*zip(x, y3, [0]*len(x))])
        self.play(Transform(curve1, mult_curve), Transform(curve2, mult_curve))
        self.wait(1.5)

        # Final text
        final_text = Text("Adding Gaussians preserves Gaussian shape", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(mean_eq), FadeOut(final_text), FadeOut(green_curve), FadeOut(mult_curve))
