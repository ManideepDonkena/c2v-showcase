from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Shape of Distance 2", font_size=36).to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Grid and center point
        grid = NumberPlane(x_range=[-6.5, 6.5], y_range=[-3.6, 3.6], 
                           axis_config={"stroke_color": GREY_A}, 
                           background_line_style={"stroke_color": GREY_D})
        self.play(Create(grid))
        self.wait(0.5)

        # Center point C
        C = Dot(color=WHITE).move_to(ORIGIN)
        c_label = Tex("C").next_to(C, DOWN, buff=0.1)
        self.play(FadeIn(C), Write(c_label))
        self.wait(0.5)
        
        # Point (2, 0)
        p1 = Dot(color=YELLOW).move_to([2, 0, 0])
        p1_label = Tex("(2, 0)").next_to(p1, DOWN, buff=0.1)
        calc1 = MathTex("2 + 0 = 2").next_to(p1, UP, buff=0.3)
        self.play(FadeIn(p1), Write(p1_label), Write(calc1))
        self.wait(1)

        # Point (-2, 0)
        p2 = Dot(color=YELLOW).move_to([-2, 0, 0])
        p2_label = Tex("(-2, 0)").next_to(p2, DOWN, buff=0.1)
        calc2 = MathTex("2 + 0 = 2").next_to(p2, UP, buff=0.3)
        self.play(FadeIn(p2), Write(p2_label), Write(calc2))
        self.wait(1)

        # Point (0, 1)
        p3 = Dot(color=YELLOW).move_to([0, 1, 0])
        p3_label = Tex("(0, 1)").next_to(p3, UP, buff=0.1)
        calc3 = MathTex("0 + 2 = 2").next_to(p3, DOWN, buff=0.3)
        self.play(FadeIn(p3), Write(p3_label), Write(calc3))
        self.wait(1)

        # Point (0, -1)
        p4 = Dot(color=YELLOW).move_to([0, -1, 0])
        p4_label = Tex("(0, -1)").next_to(p4, DOWN, buff=0.1)
        calc4 = MathTex("0 + 2 = 2").next_to(p4, UP, buff=0.3)
        calc4.shift(0.0 * RIGHT + -0.3 * UP)  # layout: separation vector
        self.play(FadeIn(p4), Write(p4_label), Write(calc4))
        self.wait(1)

        # Dim point (1, 1) with cost 3
        p5 = Dot(color=GREY).move_to([1, 1, 0])
        p5_label = Tex("(1, 1)").next_to(p5, UP, buff=0.1)
        cost_label = Tex("Cost: 3").next_to(p5, DOWN, buff=0.3)
        cost_label.shift(0.0 * RIGHT + -0.39 * UP)  # layout: separation vector
        self.play(FadeIn(p5), Write(p5_label), Write(cost_label))
        self.wait(1.5)

        # Narration text
        narration = Text("Consider all points exactly at quill distance 2 from the center.", font_size=24).to_edge(DOWN, buff=0.3)
        self.play(Write(narration))
        self.wait(1.5)

        self.play(FadeOut(narration))

        narration2 = Text("These include two steps sideways, or just one step up or down.", font_size=24).to_edge(DOWN, buff=0.3)
        self.play(Write(narration2))
        self.wait(1.5)

        self.play(FadeOut(narration2))

        narration3 = Text("Points like (1,1) are further away because their cost is 3.", font_size=24).to_edge(DOWN, buff=0.3)
        self.play(Write(narration3))
        self.wait(1.5)

        self.play(FadeOut(narration3))

        # New: Show central point and four specific points lighting up in sequence
        # Point at (6, 0) - cost 6
        p6 = Dot(color=GREEN).move_to([6, 0, 0])
        self.play(FadeIn(p6))
        self.wait(0.5)

        # Point at (-6, 0) - cost 6
        p7 = Dot(color=GREEN).move_to([-6, 0, 0])
        self.play(FadeIn(p7))
        self.wait(0.5)

        # Point at (0, 3) - cost 6
        p8 = Dot(color=GREEN).move_to([0, 3, 0])
        self.play(FadeIn(p8))
        self.wait(0.5)

        # Point at (0, -3) - cost 6
        p9 = Dot(color=GREEN).move_to([0, -3, 0])
        self.play(FadeIn(p9))
        self.wait(0.5)

        # Narration for distance 6
        narration4 = Text("Distance 6 requires 6 sideways steps or 3 vertical steps.", font_size=24).to_edge(DOWN, buff=0.3)
        self.play(Write(narration4))
        self.wait(1.5)

        self.play(FadeOut(narration4))

        # Clean up
        self.play(FadeOut(title, C, c_label, p1, p1_label, calc1, p2, p2_label, calc2,
                          p3, p3_label, calc3, p4, p4_label, calc4, p5, p5_label, cost_label,
                          p6, p7, p8, p9))
        self.wait(0.5)
