from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Origin and the Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial X
        x_large = Tex(r"$X$", font_size=120).move_to(ORIGIN)
        self.play(FadeIn(x_large))
        self.wait(1)

        # Arrows and rules
        arrow1 = Arrow(start=DOWN, end=UP, color=BLUE).next_to(x_large, DOWN, buff=0.5)
        rule1 = MathTex(r"X \rightarrow XYY", color=BLUE).next_to(arrow1, DOWN)
        arrow2 = Arrow(start=DOWN, end=UP, color=GREEN).next_to(x_large, DOWN, buff=1.5)
        rule2 = MathTex(r"Y \rightarrow YX", color=GREEN).next_to(arrow2, DOWN)

        self.play(GrowArrow(arrow1), Write(rule1))
        self.wait(0.5)
        arrow2.shift(0.0 * RIGHT + 0.9 * UP)  # layout: separation vector
        rule2.shift(0.0 * RIGHT + 0.17 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow2), Write(rule2))
        self.wait(1)

        # Simultaneous Rewrite pulse
        sim_text = Text("Simultaneous Rewrite", font_size=36).move_to(UP * 2)
        self.play(FadeIn(sim_text))
        self.play(sim_text.animate.scale(1.2).set_color(YELLOW))
        self.wait(0.5)
        self.play(FadeOut(sim_text))

        # Expansion comparison: X -> XYY
        x_before = Tex(r"$X$", font_size=40).move_to(LEFT * 3 + UP * 1)
        x_after = Tex(r"$XYY$", font_size=40).move_to(RIGHT * 3 + UP * 1)
        arrow_exp = Arrow(start=x_before.get_right(), end=x_after.get_left(), buff=0.2)
        self.play(Write(x_before), Write(x_after), GrowArrow(arrow_exp))
        self.wait(1)

        # Y -> YX
        y_before = Tex(r"$Y$", font_size=40).move_to(LEFT * 3 + DOWN * 1)
        y_after = Tex(r"$YX$", font_size=40).move_to(RIGHT * 3 + DOWN * 1)
        arrow_exp2 = Arrow(start=y_before.get_right(), end=y_after.get_left(), buff=0.2)
        self.play(Write(y_before), Write(y_after), GrowArrow(arrow_exp2))
        self.wait(1)

        # Cross out Y
        y_crossed = Tex(r"$Y$", font_size=80).move_to(ORIGIN)
        cross = Line(start=y_crossed.get_corner(DL), end=y_crossed.get_corner(UR), color=RED)
        self.play(Write(y_crossed))
        self.wait(0.5)
        self.play(Create(cross))
        self.wait(1)
        self.play(FadeOut(y_crossed), FadeOut(cross))

        # Start from X
        start_text = Text("Start from X", font_size=36).move_to(UP * 2)
        self.play(Write(start_text))
        self.wait(1)
        self.play(FadeOut(start_text))

        # Show that Y is invalid start
        y_invalid = Tex(r"$Y$", font_size=80).move_to(LEFT * 3 + UP * 1)
        cross2 = Line(start=y_invalid.get_corner(DL), end=y_invalid.get_corner(UR), color=RED)
        self.play(Write(y_invalid))
        self.wait(0.5)
        self.play(Create(cross2))
        self.wait(1)
        self.play(FadeOut(y_invalid), FadeOut(cross2))

        # Show first letter unchanged
        xyy = Tex(r"$XYY$", font_size=40).move_to(RIGHT * 3 + UP * 1)
        arrow_first = Arrow(start=x_before.get_right(), end=xyy.get_left(), buff=0.2, color=YELLOW)
        self.play(Write(xyy), GrowArrow(arrow_first))
        self.wait(1)

        # Show transformation of first letter in longer word
        long_word = Tex(r"$XYYYXYX$", font_size=40).move_to(LEFT * 3 + DOWN * 1.5)
        new_word = Tex(r"$XYY$", font_size=40).move_to(RIGHT * 3 + DOWN * 1.5)
        arrow_x_to_xyy = Arrow(start=long_word.get_left(), end=new_word.get_left(), buff=0.2, color=YELLOW)
        self.play(Write(long_word), Write(new_word), GrowArrow(arrow_x_to_xyy))
        self.wait(1)

        # Step 0 vs Step 1
        step0 = Tex(r"$X$", font_size=40).move_to(LEFT * 3 + DOWN * 2)
        step1 = Tex(r"$XYY$", font_size=40).move_to(RIGHT * 3 + DOWN * 2)
        arrow_step = Arrow(start=step0.get_right(), end=step1.get_left(), buff=0.2)
        self.play(Write(step0), Write(step1), GrowArrow(arrow_step))
        self.wait(1)

        # Fade out
        self.play(FadeOut(x_large), FadeOut(arrow1), FadeOut(rule1), FadeOut(arrow2), FadeOut(rule2),
                  FadeOut(x_before), FadeOut(x_after), FadeOut(y_before), FadeOut(y_after),
                  FadeOut(arrow_exp), FadeOut(arrow_exp2), FadeOut(arrow_first), FadeOut(arrow_x_to_xyy),
                  FadeOut(step0), FadeOut(step1), FadeOut(arrow_step), FadeOut(title))
        self.wait(0.5)
