from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Resulting Gaussian", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Original Gaussians
        x = np.linspace(-4, 4, 100)
        gauss1 = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 1)**2), 0), t_range=[-4, 4], color=BLUE)
        gauss2 = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 3)**2), 0), t_range=[-4, 4], color=RED)
        # Labels for means
        mu1_label = MathTex(r"\mu_1 = 1", font_size=24).next_to(gauss1, DOWN)
        mu2_label = MathTex(r"\mu_2 = 3", font_size=24).next_to(gauss2, DOWN)

        self.play(Create(gauss1), Create(gauss2), Write(mu1_label), Write(mu2_label))
        self.wait(1)

        # Merge into new Gaussian
        merged_gauss = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 4)**2), 0), t_range=[-4, 4], color=GREEN)
        new_mu_label = MathTex(r"\mu_{\text{new}} = 1 + 3 = 4", font_size=24).next_to(merged_gauss, DOWN)
        new_sigma_label = MathTex(r"\sigma^2_{\text{new}} = 1 + 1 = 2", font_size=24).next_to(new_mu_label, DOWN)

        self.play(Transform(gauss1, merged_gauss), Transform(gauss2, merged_gauss), 
                  Transform(mu1_label, new_mu_label), Transform(mu2_label, new_sigma_label))
        self.wait(1.5)

        # Fade out original curves
        self.play(FadeOut(gauss1), FadeOut(gauss2), FadeOut(mu1_label), FadeOut(mu2_label))
        self.wait(0.5)

        # Variance boxes
        var_x = Rectangle(width=2, height=1).set_fill(BLUE, opacity=0.3).set_stroke(BLUE)
        var_y = Rectangle(width=2, height=1).set_fill(RED, opacity=0.3).set_stroke(RED)
        var_x_label = MathTex(r"\text{Var}(X) = 1", font_size=24).move_to(var_x.get_center())
        var_y_label = MathTex(r"\text{Var}(Y) = 1", font_size=24).move_to(var_y.get_center())

        total_var = Rectangle(width=3, height=1).set_fill(GREEN, opacity=0.3).set_stroke(GREEN)
        total_var_label = MathTex(r"\text{Total Var} = 1 + 1 = 2", font_size=24).move_to(total_var.get_center())

        var_x.next_to(ORIGIN, LEFT)
        var_y.next_to(var_x, RIGHT, buff=0.5)
        arrow = Arrow(var_x.get_right(), total_var.get_left(), buff=0.2)

        self.play(Create(var_x), Create(var_y), Write(var_x_label), Write(var_y_label))
        self.wait(0.5)
        self.play(GrowArrow(arrow), Create(total_var), Write(total_var_label))
        self.wait(1.5)

        # Variance addition example
        self.play(FadeOut(var_x), FadeOut(var_y), FadeOut(var_x_label), FadeOut(var_y_label),
                  FadeOut(arrow), FadeOut(total_var), FadeOut(total_var_label))

        # Two identical blue curves
        gauss_blue1 = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 2)**2), 0), t_range=[-4, 4], color=BLUE)
        gauss_blue2 = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 2)**2), 0), t_range=[-4, 4], color=BLUE)
        gauss_blue1.shift(LEFT * 0.5)
        gauss_blue2.shift(RIGHT * 0.5)

        self.play(Create(gauss_blue1), Create(gauss_blue2))
        self.wait(0.5)

        # Merge into green
        merged_gauss2 = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 2)**2), 0), t_range=[-4, 4], color=GREEN)
        merged_gauss2.scale(1.5, about_point=ORIGIN)

        self.play(Transform(gauss_blue1, merged_gauss2), Transform(gauss_blue2, merged_gauss2))
        self.wait(1)

        # Show equation
        eq = MathTex(r"\mu_{\text{sum}} = \mu_X + \mu_Y", font_size=30).to_edge(UP)
        self.play(Write(eq))
        self.wait(1.5)

        # Example: N(5,1) + N(5,1) = N(10,2)
        gauss_a = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 5)**2), 0), t_range=[-4, 4], color=BLUE)
        gauss_b = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 5)**2), 0), t_range=[-4, 4], color=RED)
        gauss_a.shift(LEFT * 1)
        gauss_b.shift(RIGHT * 1)

        self.play(Create(gauss_a), Create(gauss_b))
        self.wait(0.5)

        final_gauss = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 10)**2), 0), t_range=[-4, 4], color=GREEN)
        final_gauss.scale(1.5, about_point=ORIGIN)

        self.play(Transform(gauss_a, final_gauss), Transform(gauss_b, final_gauss))
        self.wait(1.5)

        # Point multiplication
        self.play(FadeOut(gauss_a), FadeOut(gauss_b), FadeOut(eq))

        mult_gauss = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 2)**2), 0), t_range=[-4, 4], color=YELLOW)
        mult_eq = MathTex(r"\mu_{\text{mult}} = \frac{\sigma_1^2 \mu_2 + \sigma_2^2 \mu_1}{\sigma_1^2 + \sigma_2^2}", font_size=24).to_edge(UP)
        self.play(Create(mult_gauss), Write(mult_eq))
        self.wait(1.5)

        # Correlated vs Independent
        self.play(FadeOut(mult_gauss), FadeOut(mult_eq))

        corr_gauss = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 2)**2), 0), t_range=[-4, 4], color=BLUE)
        corr_gauss.shift(LEFT * 1)
        corr_gauss2 = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 2)**2), 0), t_range=[-4, 4], color=RED)
        corr_gauss2.shift(RIGHT * 1)

        self.play(Create(corr_gauss), Create(corr_gauss2))
        self.wait(0.5)

        # Show that sum is scaled version
        scaled = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 4)**2), 0), t_range=[-4, 4], color=GREEN)
        scaled.scale(1.5, about_point=ORIGIN)

        self.play(Transform(corr_gauss, scaled), Transform(corr_gauss2, scaled))
        self.wait(1.5)

        # Dice example
        self.play(FadeOut(corr_gauss), FadeOut(corr_gauss2))

        dice1 = Rectangle(width=1, height=1).set_fill(BLUE, opacity=0.3).set_stroke(BLUE)
        dice2 = Rectangle(width=1, height=1).set_fill(RED, opacity=0.3).set_stroke(RED)
        dice1.shift(LEFT * 1)
        dice2.shift(RIGHT * 1)

        self.play(Create(dice1), Create(dice2))
        self.wait(0.5)

        total_dice = Rectangle(width=2, height=1).set_fill(GREEN, opacity=0.3).set_stroke(GREEN)
        total_dice_label = MathTex(r"\text{Total Var} = 1 + 4 = 5", font_size=24).move_to(total_dice.get_center())
        self.play(Create(total_dice), Write(total_dice_label))
        self.wait(1.5)

        # Subtracting variables
        self.play(FadeOut(dice1), FadeOut(dice2), FadeOut(total_dice), FadeOut(total_dice_label))

        sub_gauss1 = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 2)**2), 0), t_range=[-4, 4], color=BLUE)
        sub_gauss2 = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 2)**2), 0), t_range=[-4, 4], color=RED)

        self.play(Create(sub_gauss1), Create(sub_gauss2))
        self.wait(0.5)

        sub_result = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 2)**2), 0), t_range=[-4, 4], color=GREEN)
        sub_result.scale(1.7, about_point=ORIGIN)

        self.play(Transform(sub_gauss1, sub_result), Transform(sub_gauss2, sub_result))
        self.wait(1.5)

        # Add constant
        self.play(FadeOut(sub_gauss1), FadeOut(sub_gauss2))

        shift_gauss = ParametricFunction(lambda t: (t, 0.5 * np.exp(-0.5 * (t - 3)**2), 0), t_range=[-4, 4], color=BLUE)
        shift_eq = MathTex(r"\mu_{\text{new}} = \mu + c", font_size=24).to_edge(UP)
        self.play(Create(shift_gauss), Write(shift_eq))
        self.wait(1.5)

        # Final fade
        self.play(FadeOut(shift_gauss), FadeOut(shift_eq), FadeOut(title))
        self.wait(0.5)
