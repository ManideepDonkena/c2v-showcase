from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining Mirth", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Triangle
        a, b, c = 4, 5, 6
        # Scale for display
        scale = 1.2
        A = np.array([-3, -1, 0])
        B = np.array([3, -1, 0])
        C = np.array([0, 2.5, 0])
        triangle = Polygon(A, B, C, color=WHITE)
        
        # Side labels
        label_a = MathTex("a", font_size=24).next_to((A+B)/2, DOWN)
        label_b = MathTex("b", font_size=24).next_to((B+C)/2, RIGHT)
        label_c = MathTex("c", font_size=24).next_to((A+C)/2, LEFT)

        # Assign a, b, c to sides
        self.play(Create(triangle), Write(label_a), Write(label_b), Write(label_c))
        self.wait(0.5)

        # Inequality setup
        two_c = MathTex("2 \\times c", font_size=32).to_edge(LEFT)
        less_equal = MathTex("\\leq", font_size=32).next_to(two_c, RIGHT)
        three_a = MathTex("3 \\times a", font_size=32).next_to(less_equal, RIGHT)

        self.play(Write(two_c), Write(less_equal), Write(three_a))
        self.wait(1)

        # Show calculation
        calc_text = Text("2 × 6 = 12", font_size=24).to_edge(DOWN).shift(UP)
        calc_text2 = Text("3 × 4 = 12", font_size=24).next_to(calc_text, RIGHT)
        self.play(Write(calc_text), Write(calc_text2))
        self.wait(1.5)

        # Check condition
        is_mirthful = Text("Mirthful!", font_size=28, color=GREEN)
        is_mirthful.next_to(VGroup(two_c, less_equal, three_a), DOWN, buff=0.4)
        self.play(Write(is_mirthful))
        triangle.set_color(GREEN)
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(triangle), FadeOut(label_a), FadeOut(label_b), FadeOut(label_c),
                  FadeOut(two_c), FadeOut(less_equal), FadeOut(three_a),
                  FadeOut(calc_text), FadeOut(calc_text2), FadeOut(is_mirthful))
        self.wait(0.5)

        # Narration text
        narration = Text("A triangle is mirthful if twice its longest side is at most three times its shortest side.", font_size=24)
        if narration.width > config.frame_width - 1:
            narration.scale_to_fit_width(config.frame_width - 1)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)

        self.play(FadeOut(narration))
        self.wait(0.5)

        # Rules
        rule1 = Text("1. Every equilateral triangle is mirthful.", font_size=24)
        rule2 = Text("2. Scaling does not change mirthfulness.", font_size=24).next_to(rule1, DOWN, aligned_edge=LEFT)
        rule3 = Text("3. The middle side does not matter.", font_size=24).next_to(rule2, DOWN, aligned_edge=LEFT)
        VGroup(rule1, rule2, rule3).move_to(ORIGIN)

        self.play(Write(rule1))
        self.wait(1.5)
        self.play(Write(rule2))
        self.wait(1.5)
        self.play(Write(rule3))
        self.wait(2)

        self.play(FadeOut(rule1), FadeOut(rule2), FadeOut(rule3))
        self.wait(0.5)

        # Worked example
        example = Text("Example: sides 4, 5, 6", font_size=24).to_edge(DOWN)
        self.play(Write(example))
        self.wait(1.5)

        # Show that it's mirthful
        calc1 = MathTex("2 \\times 6 = 12", font_size=24).to_edge(LEFT).shift(UP)
        calc2 = MathTex("3 \\times 4 = 12", font_size=24).next_to(calc1, RIGHT)
        self.play(Write(calc1), Write(calc2))
        self.wait(1.5)

        # Not mirthful example
        not_mirthful = Text("Example: sides 3, 4, 5", font_size=24).to_edge(DOWN).shift(2*UP)
        self.play(Write(not_mirthful))
        self.wait(1.5)

        calc3 = MathTex("2 \\times 5 = 10", font_size=24).next_to(calc1, DOWN, aligned_edge=LEFT, buff=0.4)
        calc4 = MathTex("3 \\times 3 = 9", font_size=24).next_to(calc3, RIGHT)
        self.play(Write(calc3), Write(calc4))
        self.wait(1.5)

        # Final fade
        self.play(FadeOut(example), FadeOut(not_mirthful),
                  FadeOut(calc1), FadeOut(calc2), FadeOut(calc3), FadeOut(calc4))
        self.wait(0.5)
