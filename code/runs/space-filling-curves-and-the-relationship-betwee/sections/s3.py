from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Surjectivity vs. Injectivity", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Square and line segment
        square = Square(side_length=4, color=WHITE, fill_opacity=0.1)
        square.move_to(ORIGIN)
        
        line = Line(start=LEFT*3, end=RIGHT*3, color=WHITE)
        line.move_to(DOWN*2)
        
        self.play(Create(square), Create(line))
        self.wait(0.5)

        # Points on line
        t1 = ValueTracker(-2.5)
        t2 = ValueTracker(2.5)
        
        p1 = always_redraw(lambda: Dot(line.point_from_proportion(t1.get_value()/6 + 0.5), color=RED, radius=0.1))
        p2 = always_redraw(lambda: Dot(line.point_from_proportion(t2.get_value()/6 + 0.5), color=BLUE, radius=0.1))
        
        self.play(Create(p1), Create(p2))
        self.wait(0.5)

        # Function mapping
        def f(t):
            t = (t + 3) / 6  # normalize to [0,1]
            x = 4 * t
            y = 4 * (1 - t)
            return np.array([x-2, y-2, 0])
        
        # Traces
        trace1 = VMobject(color=RED, stroke_width=3)
        trace2 = VMobject(color=BLUE, stroke_width=3)
        
        trace1.set_points_as_corners([f(t1.get_value())])
        trace2.set_points_as_corners([f(t2.get_value())])
        
        trace1_copy = trace1.copy()
        trace2_copy = trace2.copy()
        self.play(
            Create(trace1),
            Create(trace2),
            run_time=1
        )
        self.wait(0.5)

        # Animate points moving
        self.play(
            t1.animate.set_value(2.5),
            t2.animate.set_value(-2.5),
            rate_func=linear,
            run_time=3
        )
        
        # Show overlap
        overlap = Dot(color=YELLOW, radius=0.1)
        overlap.move_to(f(0))
        self.play(FadeIn(overlap))
        
        # Label
        label = MathTex("f(t_1) = f(t_2)", font_size=30)
        label.next_to(overlap, DOWN)
        self.play(Write(label))
        self.wait(1)

        # Surjectivity arrow
        arrow = Arrow(start=UP*2, end=DOWN*2, color=GREEN)
        arrow_label = Text("Surjective", font_size=24).next_to(arrow, RIGHT)
        
        self.play(GrowArrow(arrow), Write(arrow_label))
        self.wait(1)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(square),
            FadeOut(line),
            FadeOut(p1),
            FadeOut(p2),
            FadeOut(trace1),
            FadeOut(trace2),
            FadeOut(overlap),
            FadeOut(label),
            FadeOut(arrow),
            FadeOut(arrow_label)
        )
        self.wait(0.5)
