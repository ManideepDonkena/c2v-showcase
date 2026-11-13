from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Origin and the Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Large bold 'X' in center
        x_large = Tex("X", font_size=120).move_to(ORIGIN)
        self.play(FadeIn(x_large))
        self.wait(0.5)

        # Arrows and labels
        arrow1 = Arrow(start=LEFT * 1.5, end=RIGHT * 1.5, color=BLUE)
        label1 = MathTex("X \\to XYY", color=BLUE).next_to(arrow1, UP)
        arrow2 = Arrow(start=LEFT * 1.5, end=RIGHT * 1.5, color=GREEN).shift(DOWN * 1.5)
        label2 = MathTex("Y \\to YX", color=GREEN).next_to(arrow2, UP)

        arrow1.shift(0.0 * RIGHT + 0.75 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow1), Write(label1))
        self.wait(0.5)
        self.play(GrowArrow(arrow2), Write(label2))
        self.wait(0.5)

        # Simultaneous Rewrite pulse
        simultaneous = Text("Simultaneous Rewrite", font_size=30).move_to(UP * 2)
        self.play(FadeIn(simultaneous))
        self.play(simultaneous.animate.scale(1.2), run_time=0.3)
        self.play(simultaneous.animate.scale(1/1.2), run_time=0.3)
        self.play(FadeOut(simultaneous))
        self.wait(0.5)

        # Expansion comparison: X → XYY
        x_expanded = MathTex("X \\to XYY").move_to(UP * 1.5)
        self.play(Write(x_expanded))
        self.wait(0.5)

        # Show that each letter expands to two letters
        x1 = Tex("X", font_size=40).move_to(LEFT * 2 + UP * 0.5)
        x2 = Tex("X", font_size=40).move_to(LEFT * 1 + UP * 0.5)
        y1 = Tex("Y", font_size=40).move_to(RIGHT * 1 + UP * 0.5)
        y2 = Tex("Y", font_size=40).move_to(RIGHT * 2 + UP * 0.5)
        self.play(FadeIn(x1, x2, y1, y2))
        self.wait(0.5)

        # Y → YX
        y_expanded = MathTex("Y \\to YX").move_to(DOWN * 1.5)
        self.play(Write(y_expanded))
        self.wait(0.5)

        y3 = Tex("Y", font_size=40).move_to(LEFT * 2 + DOWN * 0.5)
        x3 = Tex("X", font_size=40).move_to(RIGHT * 1 + DOWN * 0.5)
        self.play(FadeIn(y3, x3))
        self.wait(0.5)

        # Show that both rules expand one letter to two letters
        self.play(
            FadeOut(x1, x2, y1, y2, y3, x3),
            FadeOut(x_expanded, y_expanded)
        )
        self.wait(0.5)

        # Show red 'X' through 'Y'
        y_large = Tex("Y", font_size=120).move_to(ORIGIN)
        cross = Cross(y_large, color=RED, stroke_width=10)
        self.play(FadeIn(y_large))
        self.wait(0.5)
        self.play(Write(cross))
        self.wait(0.5)

        # Narration: "The process never begins with Y; it always starts with X."
        text = Text("The process never begins with Y; it always starts with X.", font_size=24).move_to(DOWN * 2)
        self.play(Write(text))
        self.wait(1.5)
        self.play(FadeOut(text))

        # Show that starting from Y is invalid
        y_start = Tex("Y", font_size=60).move_to(LEFT * 3 + UP * 1)
        start_text = Text("Start from X", font_size=24).next_to(y_start, DOWN)
        self.play(FadeIn(y_start))
        self.wait(0.5)
        self.play(Write(start_text))
        self.wait(0.5)

        # Cross out Y
        cross_y = Cross(y_start, color=RED, stroke_width=8)
        self.play(Write(cross_y))
        self.wait(1.0)

        # Fade out everything except title and main X
        self.play(
            FadeOut(title, x_large, arrow1, label1, arrow2, label2, cross, cross_y, start_text),
            run_time=1
        )
        self.wait(0.5)
