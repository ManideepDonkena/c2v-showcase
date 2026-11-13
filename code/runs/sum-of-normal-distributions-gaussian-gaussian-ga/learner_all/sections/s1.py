from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The First Bell", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={"color": WHITE},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        axes_labels.shift(0.0 * RIGHT + -0.58 * UP)  # layout: separation vector
        self.play(Create(axes), Create(axes_labels))
        self.wait(0.5)

        # Standard Normal Curve
        normal_curve = axes.plot(lambda x: 1 / np.sqrt(2 * PI) * np.exp(-0.5 * x**2), color=BLUE)
        self.play(Create(normal_curve))
        self.wait(0.5)

        # Labels
        mu_label = MathTex(r"\mu = 0", font_size=24).next_to(normal_curve.get_top(), UP, buff=0.2)
        sigma2_label = MathTex(r"\sigma^2 = 1", font_size=24).next_to(normal_curve.point_from_proportion(0.5), RIGHT, buff=0.2)
        sigma2_label.shift(0.0 * RIGHT + 0.26 * UP)  # layout: separation vector
        sigma2_label.shift(0.24 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(FadeIn(mu_label), FadeIn(sigma2_label))
        self.wait(0.5)

        # Pulse effect
        self.play(
            normal_curve.animate.scale(1.03),
            run_time=0.5,
            rate_func=there_and_back
        )
        self.wait(0.5)

        # Variance boxes and arrow
        var_x = Rectangle(width=2, height=1).set_fill(BLUE, opacity=0.5).set_stroke(WHITE)
        var_y = Rectangle(width=2, height=1).set_fill(BLUE, opacity=0.5).set_stroke(WHITE)
        var_x_label = Text("Variance of X", font_size=20).move_to(var_x.get_center())
        var_y_label = Text("Variance of Y", font_size=20).move_to(var_y.get_center())

        total_var = Rectangle(width=2, height=1).set_fill(GREEN, opacity=0.5).set_stroke(WHITE)
        total_var_label = Text("Total Variance", font_size=20).move_to(total_var.get_center())
        arrow = Arrow(start=var_x.get_right(), end=total_var.get_left(), buff=0.1)

        var_x.next_to(axes, DOWN, buff=0.5).shift(LEFT)
        var_y.next_to(var_x, RIGHT, buff=0.2)
        total_var.next_to(var_y, RIGHT, buff=0.2)
        arrow.next_to(var_y, RIGHT, buff=0.1)

        self.play(
            Create(var_x),
            Write(var_x_label),
            Create(var_y),
            Write(var_y_label),
            run_time=0.5
        )
        self.wait(0.5)

        self.play(
            Create(arrow),
            Create(total_var),
            Write(total_var_label),
            run_time=0.5
        )
        self.wait(0.5)

        # Narration text
        narration = Text("When independent variables add up, their uncertainties (variances) also add up directly.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        # Two identical curves merging
        curve1 = axes.plot(lambda x: 1 / np.sqrt(2 * PI) * np.exp(-0.5 * x**2), color=BLUE)
        curve2 = axes.plot(lambda x: 1 / np.sqrt(2 * PI) * np.exp(-0.5 * (x - 2)**2), color=BLUE)
        self.play(Create(curve1), Create(curve2))
        self.wait(0.5)

        # Merge into green curve
        merged_curve = axes.plot(lambda x: 1 / np.sqrt(2 * PI * 2) * np.exp(-0.5 * (x - 1)**2), color=GREEN)
        self.play(Transform(curve1, merged_curve), Transform(curve2, merged_curve))
        self.wait(0.5)

        # Variance arithmetic
        variance_eq = MathTex(r"1 + 1 = 2", font_size=30).to_edge(UP).shift(DOWN)
        self.play(Write(variance_eq))
        self.wait(1.0)
        self.play(FadeOut(variance_eq))

        # Mean sum equation
        mean_sum_eq = MathTex(r"\mu_{\text{sum}} = \mu_X + \mu_Y", font_size=30).to_edge(UP).shift(DOWN)
        self.play(Write(mean_sum_eq))
        self.wait(1.5)
        self.play(FadeOut(mean_sum_eq))

        # Example: N(5, 1) + N(5, 1)
        curve_a = axes.plot(lambda x: 1 / np.sqrt(2 * PI) * np.exp(-0.5 * (x - 5)**2), color=BLUE)
        curve_b = axes.plot(lambda x: 1 / np.sqrt(2 * PI) * np.exp(-0.5 * (x - 5)**2), color=BLUE)
        self.play(Create(curve_a), Create(curve_b))
        self.wait(0.5)

        result_curve = axes.plot(lambda x: 1 / np.sqrt(2 * PI * 2) * np.exp(-0.5 * (x - 10)**2), color=GREEN)
        self.play(Transform(curve_a, result_curve), Transform(curve_b, result_curve))
        self.wait(0.5)

        # Specific mean equation
        specific_mean = MathTex(r"\mu_{\text{sum}} = 5 + 5 = 10", font_size=30).to_edge(UP).shift(DOWN)
        self.play(Write(specific_mean))
        self.wait(1.5)
        self.play(FadeOut(specific_mean))

        # Multiplication of curves
        red_curve = axes.plot(lambda x: 1 / np.sqrt(2 * PI) * np.exp(-0.5 * (x - 1)**2), color=RED)
        self.play(Create(red_curve))
        self.wait(0.5)

        # Multiply point-wise (simplified visual)
        product_curve = axes.plot(lambda x: 1 / np.sqrt(2 * PI * 0.5) * np.exp(-0.5 * (x - 1)**2), color=YELLOW)
        self.play(Transform(red_curve, product_curve))
        self.wait(0.5)

        # Narration
        narration2 = Text("Multiplying Gaussians also yields a Gaussian.", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1.5)
        self.play(FadeOut(narration2))

        # Correlated vs Independent
        corr_curve = axes.plot(lambda x: 1 / np.sqrt(2 * PI) * np.exp(-0.5 * (x - 1)**2), color=BLUE)
        self.play(Create(corr_curve))
        self.wait(0.5)

        # Show sum is scaled version of one
        scaled_curve = axes.plot(lambda x: 1 / np.sqrt(2 * PI) * np.exp(-0.5 * (x - 1)**2), color=GREEN)
        self.play(Transform(corr_curve, scaled_curve))
        self.wait(0.5)

        # Narration
        narration3 = Text("Only independent variables add variances.", font_size=24)
        narration3.to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(1.5)
        self.play(FadeOut(narration3))

        # Dice example
        dice1 = Rectangle(width=1, height=1).set_fill(BLUE, opacity=0.5).set_stroke(WHITE)
        dice2 = Rectangle(width=1, height=1).set_fill(BLUE, opacity=0.5).set_stroke(WHITE)
        dice1.shift(LEFT * 2)
        dice2.shift(RIGHT * 2)

        self.play(Create(dice1), Create(dice2))
        self.wait(0.5)

        # Show variance addition
        total_dice = Rectangle(width=2, height=1).set_fill(GREEN, opacity=0.5).set_stroke(WHITE)
        total_dice.next_to(dice2, RIGHT, buff=0.2)
        arrow2 = Arrow(start=dice1.get_right(), end=total_dice.get_left(), buff=0.1)

        self.play(
            Create(arrow2),
            Create(total_dice),
            run_time=0.5
        )
        self.wait(0.5)

        # Narration
        narration4 = Text("Independent events add variances.", font_size=24)
        narration4.to_edge(DOWN)
        self.play(Write(narration4))
        self.wait(1.5)
        self.play(FadeOut(narration4))

        # Subtracting variables
        sub_curve1 = axes.plot(lambda x: 1 / np.sqrt(2 * PI) * np.exp(-0.5 * x**2), color=BLUE)
        sub_curve2 = axes.plot(lambda x: 1 / np.sqrt(2 * PI) * np.exp(-0.5 * (x - 2)**2), color=BLUE)
        self.play(Create(sub_curve1), Create(sub_curve2))
        self.wait(0.5)

        diff_curve = axes.plot(lambda x: 1 / np.sqrt(2 * PI * 2) * np.exp(-0.5 * (x - 1)**2), color=GREEN)
        self.play(Transform(sub_curve1, diff_curve), Transform(sub_curve2, diff_curve))
        self.wait(0.5)

        # Narration
        narration5 = Text("When we subtract independent variables, their variances ADD.", font_size=24)
        narration5.to_edge(DOWN)
        self.play(Write(narration5))
        self.wait(1.5)
        self.play(FadeOut(narration5))

        # Shift curve
        shifted_curve = axes.plot(lambda x: 1 / np.sqrt(2 * PI) * np.exp(-0.5 * (x - 3)**2), color=BLUE)
        self.play(Create(shifted_curve))
        self.wait(0.5)

        # Narration
        narration6 = Text("Adding a constant shifts the center, not the spread.", font_size=24)
        narration6.to_edge(DOWN)
        self.play(Write(narration6))
        self.wait(1.5)
        self.play(FadeOut(narration6))

        # Final fade
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(mu_label),
            FadeOut(sigma2_label),
            FadeOut(var_x),
            FadeOut(var_y),
            FadeOut(total_var),
            FadeOut(arrow),
            FadeOut(var_x_label),
            FadeOut(var_y_label),
            FadeOut(total_var_label),
            FadeOut(curve1),
            FadeOut(curve2),
            FadeOut(red_curve),
            FadeOut(corr_curve),
            FadeOut(dice1),
            FadeOut(dice2),
            FadeOut(total_dice),
            FadeOut(arrow2),
            FadeOut(shifted_curve),
            FadeOut(normal_curve),
            FadeOut(merged_curve),
            FadeOut(product_curve),
            FadeOut(scaled_curve),
            FadeOut(diff_curve)
        )
        self.wait(0.5)
