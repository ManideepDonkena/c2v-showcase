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
        t2 = ValueTracker(-2.5)
        
        p1 = always_redraw(lambda: Dot(line.point_from_proportion((t1.get_value()+3)/6), color=RED, radius=0.1))
        p2 = always_redraw(lambda: Dot(line.point_from_proportion((t2.get_value()+3)/6), color=BLUE, radius=0.1))
        
        self.play(Create(p1), Create(p2))
        self.wait(0.5)

        # Function mapping (simplified)
        def f(t):
            t = (t + 3) / 6
            x = 4 * t
            y = 2 * (1 - t)
            return np.array([x-2, y-1, 0])
        
        path1 = always_redraw(lambda: Dot(f(t1.get_value()), color=RED))
        path2 = always_redraw(lambda: Dot(f(t2.get_value()), color=BLUE))
        
        self.play(Write(path1), Write(path2))
        self.wait(0.5)

        # Animation
        self.play(
            t1.animate.set_value(2.5),
            t2.animate.set_value(2.5),
            run_time=3,
            rate_func=linear
        )
        
        # Labels for non-injectivity
        label1 = MathTex("f(t_1) = f(t_2)", color=YELLOW, font_size=24)
        label1.move_to(np.array([0, 0, 0]))
        self.play(Write(label1))
        self.wait(1)

        # Surjectivity arrow
        arrow = Arrow(start=np.array([-3, -1.5, 0]), end=np.array([3, 1.5, 0]), color=GREEN)
        arrow_label = Text("Every point in square reached", font_size=24, color=GREEN)
        arrow_label.next_to(arrow, DOWN)
        
        arrow_label.shift(0.0 * RIGHT + -0.51 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow), Write(arrow_label))
        self.wait(1.5)

        # Final text
        final_text = Text("Continuous and surjective but not injective", font_size=24)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(square),
            FadeOut(line),
            FadeOut(p1),
            FadeOut(p2),
            FadeOut(path1),
            FadeOut(path2),
            FadeOut(label1),
            FadeOut(arrow),
            FadeOut(arrow_label),
            FadeOut(final_text)
        )
