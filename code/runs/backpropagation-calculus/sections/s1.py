from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Forward Pass & The Loss", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Input node
        x = Circle(radius=0.4, color=BLUE).shift(LEFT * 3 + UP * 0.5)
        x_label = MathTex("x", font_size=24).move_to(x.get_center())
        self.play(Create(x), Write(x_label))
        self.wait(0.5)

        # Weight node
        w = Circle(radius=0.4, color=GREEN).shift(RIGHT * 1 + UP * 0.5)
        w_label = MathTex("w", font_size=24).move_to(w.get_center())
        self.play(Create(w), Write(w_label))
        self.wait(0.5)

        # Activation node
        a = Circle(radius=0.4, color=YELLOW).shift(RIGHT * 5 + UP * 0.5)
        a_label = MathTex("a", font_size=24).move_to(a.get_center())
        self.play(Create(a), Write(a_label))
        self.wait(0.5)

        # Prediction node
        y_hat = Circle(radius=0.4, color=ORANGE).shift(RIGHT * 5 + DOWN * 1)
        y_hat_label = MathTex("\\hat{y}", font_size=24).move_to(y_hat.get_center())
        self.play(Create(y_hat), Write(y_hat_label))
        self.wait(0.5)

        # Target node
        y = Circle(radius=0.4, color=RED).shift(RIGHT * 5 + DOWN * 2.5)
        y_label = MathTex("y", font_size=24).move_to(y.get_center())
        self.play(Create(y), Write(y_label))
        self.wait(0.5)

        # Forward pass arrows
        arrow1 = Arrow(LEFT * 3 + UP * 0.5, RIGHT * 1 + UP * 0.5, buff=0.2)
        arrow2 = Arrow(RIGHT * 1 + UP * 0.5, RIGHT * 5 + UP * 0.5, buff=0.2)
        arrow3 = Arrow(RIGHT * 5 + UP * 0.5, RIGHT * 5 + DOWN * 1, buff=0.2)
        self.play(Write(arrow1), Write(arrow2), Write(arrow3))
        self.wait(0.5)

        # Loss bracket
        bracket = always_redraw(
            lambda: BraceBetweenPoints(
                y_hat.get_bottom(),
                y.get_top(),
                direction=RIGHT,
                buff=0.1
            )
        )
        loss_label = MathTex("L = (\\hat{y} - y)^2", font_size=24)
        loss_label.next_to(bracket, RIGHT, buff=0.1)

        self.play(Create(bracket), Write(loss_label))
        self.wait(1)
        # Show loss growing
        self.play(
            y.animate.shift(DOWN * 0.5),
            run_time=1
        )
        self.wait(0.5)

        # Narration text
        narration = Text("We begin with the forward pass...", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(x), FadeOut(w), FadeOut(a), FadeOut(y_hat), FadeOut(y),
            FadeOut(x_label), FadeOut(w_label), FadeOut(a_label), FadeOut(y_hat_label), FadeOut(y_label),
            FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3),
            FadeOut(bracket), FadeOut(loss_label),
            FadeOut(narration)
        )
        self.wait(0.5)
