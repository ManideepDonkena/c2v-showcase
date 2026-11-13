from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Backpropagation Calculus: A Visual Journey", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Forward pass nodes
        x = MathTex("x", font_size=36).to_corner(UL)
        w = MathTex("w", font_size=36).next_to(x, RIGHT, buff=1)
        a = MathTex("a", font_size=36).next_to(w, RIGHT, buff=1)
        y_hat = MathTex("\\hat{y}", font_size=36).next_to(a, RIGHT, buff=1)
        y = MathTex("y", font_size=36).next_to(y_hat, DOWN, buff=1.5)

        # Arrows
        arrow1 = Arrow(x.get_right(), w.get_left(), buff=0.1)
        arrow2 = Arrow(w.get_right(), a.get_left(), buff=0.1)
        arrow3 = Arrow(a.get_right(), y_hat.get_left(), buff=0.1)

        # Show nodes one by one
        self.play(Write(x), run_time=0.5)
        self.wait(0.5)
        w.shift(-0.19 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(w), run_time=0.5)
        self.wait(0.5)
        a.shift(0.0 * RIGHT + 0.32 * UP)  # layout: separation vector
        self.play(Write(a), run_time=0.5)
        self.wait(0.5)
        y_hat.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        self.play(Write(y_hat), run_time=0.5)
        self.wait(0.5)
        # Arrows
        self.play(Create(arrow1), run_time=0.5)
        self.wait(0.5)
        self.play(Create(arrow2), run_time=0.5)
        self.wait(0.5)
        self.play(Create(arrow3), run_time=0.5)
        self.wait(0.5)

        # Show y
        self.play(Write(y), run_time=0.5)
        self.wait(0.5)
        # Loss bracket and label
        bracket = always_redraw(
            lambda: BraceBetweenPoints(
                y_hat.get_bottom(),
                y.get_top(),
                direction=RIGHT,
                buff=0.1
            )
        )
        loss_label = MathTex("L = (\\hat{y} - y)^2", font_size=36)
        loss_label.next_to(bracket, RIGHT, buff=0.2)

        self.play(Create(bracket), run_time=0.5)
        self.wait(0.5)
        self.play(Write(loss_label), run_time=0.5)
        self.wait(0.5)

        # Show loss grows with gap
        self.play(
            y_hat.animate.shift(UP * 1),
            run_time=1
        )
        self.wait(1)

        # Narration text
        forward_text = Text("Forward Pass", font_size=24).to_edge(DOWN).shift(UP*0.5)
        self.play(Write(forward_text), run_time=0.5)
        self.wait(1)

        loss_text = Text("Loss Function", font_size=24).next_to(forward_text, UP, buff=0.3)
        self.play(Write(loss_text), run_time=0.5)
        self.wait(1)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(x), FadeOut(w), FadeOut(a), FadeOut(y_hat), FadeOut(y),
            FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3),
            FadeOut(bracket), FadeOut(loss_label),
            FadeOut(forward_text), FadeOut(loss_text),
            run_time=0.5
        )
        self.wait(0.5)
