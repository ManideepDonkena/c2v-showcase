from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Second Bell", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First Gaussian: N(0, 1)
        x = np.linspace(-4, 4, 100)
        y1 = np.exp(-0.5 * (x)**2) / np.sqrt(2*np.pi)
        curve1 = VMobject()
        curve1.set_points_as_corners([*[[x[i], y1[i], 0] for i in range(len(x))]])
        curve1.set_color(BLUE)
        curve1.shift(LEFT * 2)

        # Second Gaussian: N(2, 4) - red, wider
        y2 = np.exp(-0.5 * (x - 2)**2 / 4) / np.sqrt(4*2*np.pi)
        curve2 = VMobject()
        curve2.set_points_as_corners([*[[x[i], y2[i], 0] for i in range(len(x))]])
        curve2.set_color(RED)
        curve2.shift(LEFT * 2)

        # Show first bell
        self.play(Create(curve1))
        self.wait(0.5)

        # Slide in second bell from right
        self.play(curve2.animate.shift(RIGHT * 4), run_time=2)
        self.wait(1)

        # Labels for X and Y
        label_x = Text("Variance of X", font_size=24).shift(UP * 2 + LEFT * 3)
        label_y = Text("Variance of Y", font_size=24).shift(UP * 2 + RIGHT * 3)
        self.play(Write(label_x), Write(label_y))
        self.wait(0.5)

        # Arrow to total variance
        arrow = Arrow(start=LEFT * 1.5, end=RIGHT * 1.5, buff=0.2)
        label_total = Text("Total Variance", font_size=24).next_to(arrow, DOWN)
        self.play(GrowArrow(arrow), Write(label_total))
        self.wait(0.5)

        # Show addition of variances
        self.play(FadeOut(label_x), FadeOut(label_y), FadeOut(arrow), FadeOut(label_total))

        # Two identical blue curves side-by-side
        curve3 = VMobject().set_points_as_corners([*[[x[i], y1[i], 0] for i in range(len(x))]])
        curve3.set_color(BLUE)
        curve4 = VMobject().set_points_as_corners([*[[x[i], y1[i], 0] for i in range(len(x))]])
        curve4.set_color(BLUE)
        curve3.shift(LEFT * 2)
        curve4.shift(RIGHT * 2)

        self.play(Create(curve3), Create(curve4))
        self.wait(0.5)

        # Merge into green curve
        y_sum = np.exp(-0.5 * (x)**2) / np.sqrt(2*np.pi) + np.exp(-0.5 * (x)**2) / np.sqrt(2*np.pi)
        y_sum = y_sum / 2
        curve_sum = VMobject()
        curve_sum.set_points_as_corners([*[[x[i], y_sum[i], 0] for i in range(len(x))]])
        curve_sum.set_color(GREEN)
        self.play(Transform(curve3, curve_sum), Transform(curve4, curve_sum))
        self.wait(1)

        # Show formula
        formula = MathTex(r"\mu_{\text{sum}} = \mu_X + \mu_Y", font_size=30).to_edge(UP)
        formula.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        self.play(Write(formula))
        self.wait(1)

        # Example: N(5, 1) + N(5, 1) = N(10, 2)
        x5 = np.linspace(-7, 13, 100)
        y5 = np.exp(-0.5 * (x5 - 10)**2 / 2) / np.sqrt(2*2*np.pi)
        curve5 = VMobject()
        curve5.set_points_as_corners([*[[x5[i], y5[i], 0] for i in range(len(x5))]])
        curve5.set_color(GREEN)
        self.play(Transform(curve_sum, curve5))
        self.wait(1)

        # Show specific values
        formula2 = MathTex(r"\mu_{\text{sum}} = 5 + 5 = 10", font_size=30).to_edge(DOWN)
        self.play(Write(formula2))
        self.wait(1)

        # Multiply two Gaussians (pointwise)
        y_mult = np.exp(-0.5 * (x)**2) / np.sqrt(2*np.pi) * np.exp(-0.5 * (x)**2) / np.sqrt(2*np.pi)
        y_mult = y_mult / (np.sqrt(2*np.pi)**2)
        curve_mult = VMobject()
        curve_mult.set_points_as_corners([*[[x[i], y_mult[i], 0] for i in range(len(x))]])
        curve_mult.set_color(GREEN)
        self.play(Transform(curve_sum, curve_mult))
        self.wait(1)

        # Show that multiplication results in narrower Gaussian
        formula3 = MathTex(r"\text{Multiplication: } \mathcal{N}(0,1) \times \mathcal{N}(0,1) = \mathcal{N}(0, 0.5)", font_size=24).to_edge(DOWN)
        formula3.shift(0.0 * RIGHT + -0.4 * UP)  # layout: separation vector
        self.play(Write(formula3))
        self.wait(1)

        # Show perfect correlation case
        curve6 = VMobject()
        curve6.set_points_as_corners([*[[x[i], y1[i], 0] for i in range(len(x))]])
        curve6.set_color(BLUE)
        curve7 = VMobject()
        curve7.set_points_as_corners([*[[x[i], y1[i], 0] for i in range(len(x))]])
        curve7.set_color(RED)
        curve6.shift(LEFT * 2)
        curve7.shift(LEFT * 2)
        self.play(Create(curve6), Create(curve7))
        self.wait(0.5)

        # Sum of correlated variables (scaled version)
        y_corr = np.exp(-0.5 * (x)**2) / np.sqrt(2*np.pi) * 2
        curve_corr = VMobject()
        curve_corr.set_points_as_corners([*[[x[i], y_corr[i], 0] for i in range(len(x))]])
        curve_corr.set_color(GREEN)
        self.play(Transform(curve6, curve_corr), Transform(curve7, curve_corr))
        self.wait(1)

        # Contrast with independent case
        formula4 = MathTex(r"\text{Independent: } \sigma^2_X + \sigma^2_Y", font_size=24).to_edge(DOWN)
        formula2.shift(0.0 * RIGHT + -0.42 * UP)  # layout: separation vector
        self.play(Transform(formula3, formula4))
        self.wait(1)

        # Dice example
        dice1 = Square(side_length=1, color=BLUE).shift(LEFT * 2)
        dice2 = Square(side_length=1, color=RED).shift(RIGHT * 2)
        self.play(Create(dice1), Create(dice2))
        self.wait(0.5)

        # Add variances
        var_text = Text("Variance: 1 + 4 = 5", font_size=24).next_to(dice1, DOWN)
        self.play(Write(var_text))
        self.wait(1)

        # Subtract case
        curve8 = VMobject()
        curve8.set_points_as_corners([*[[x[i], y1[i], 0] for i in range(len(x))]])
        curve8.set_color(BLUE)
        curve9 = VMobject()
        curve9.set_points_as_corners([*[[x[i], -y1[i], 0] for i in range(len(x))]])
        curve9.set_color(BLUE)
        curve8.shift(LEFT * 2)
        curve9.shift(RIGHT * 2)
        self.play(Create(curve8), Create(curve9))
        self.wait(0.5)

        # Resulting wider curve
        y_sub = np.exp(-0.5 * (x)**2) / np.sqrt(2*np.pi) + np.exp(-0.5 * (x)**2) / np.sqrt(2*np.pi)
        y_sub = y_sub / 2
        curve_sub = VMobject()
        curve_sub.set_points_as_corners([*[[x[i], y_sub[i], 0] for i in range(len(x))]])
        curve_sub.set_color(GREEN)
        self.play(Transform(curve8, curve_sub), Transform(curve9, curve_sub))
        self.wait(1)

        # Show variance addition
        formula5 = MathTex(r"\text{Var}(X - Y) = \sigma^2 + \sigma^2 = 2\sigma^2", font_size=24).to_edge(DOWN)
        self.play(Transform(formula3, formula5))
        self.wait(1)

        # Shift curve by constant
        curve_shifted = VMobject()
        curve_shifted.set_points_as_corners([*[[x[i], y1[i], 0] for i in range(len(x))]])
        curve_shifted.set_color(BLUE)
        curve_shifted.shift(LEFT * 2 + UP * 1)
        self.play(Create(curve_shifted))
        self.wait(0.5)

        # Show constant shift doesn't change variance
        formula6 = MathTex(r"\text{Adding } c \text{ shifts center, not spread}", font_size=24).to_edge(DOWN)
        self.play(Transform(formula3, formula6))
        self.wait(1)

        # Final fade out
        self.play(FadeOut(title), FadeOut(curve1), FadeOut(curve2), FadeOut(curve_sum), FadeOut(curve_shifted),
                  FadeOut(formula), FadeOut(formula2), FadeOut(formula3), FadeOut(formula4), FadeOut(formula5), FadeOut(formula6),
                  FadeOut(dice1), FadeOut(dice2), FadeOut(var_text))
        self.wait(0.5)
