from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Concept of Invariance", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Axes
        axes = Axes(x_range=[-4, 4], y_range=[-2, 2], axis_config={"include_tip": True})
        axes.to_edge(DOWN)
        self.play(Create(axes))
        self.wait(0.5)

        # Original vector v
        v = Vector([1, 1], color=YELLOW)
        v_label = MathTex("v", font_size=24).next_to(v.get_end(), UR, buff=0.1)
        self.play(GrowArrow(v), Write(v_label))
        self.wait(0.5)
        
        # Matrix M
        M = Matrix([['a', 'b'], ['c', 'd']])
        M.to_edge(UP).shift(DOWN)
        M.shift(-0.19 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(M))
        self.wait(0.5)

        # Transformation
        Av = Vector([2, 2], color=GREEN)
        Av_label = MathTex("Av", font_size=24).next_to(Av.get_end(), UR, buff=0.1)
        self.play(Transform(v.copy(), Av), Write(Av_label))
        self.wait(0.5)

        # Highlight invariance
        line = DashedLine(LEFT * 5, RIGHT * 5, color=BLUE)
        line.shift(DOWN * 0.5)  # Adjust to match vector direction
        self.play(Create(line))
        self.wait(0.5)

        # Text explanation
        text = Text("Direction unchanged", font_size=24).to_edge(LEFT).shift(UP*2)
        text.shift(0.0 * RIGHT + 0.82 * UP)  # layout: separation vector
        self.play(Write(text))
        self.wait(1)

        # Clear screen
        self.play(FadeOut(VGroup(title, axes, v, v_label, M, Av, Av_label, line, text)))
        self.wait(0.5)

        # New title for section
        title2 = Text("Eigenvectors", font_size=36)
        title2.to_edge(UP)
        title2.shift(0.0 * RIGHT + -0.65 * UP)  # layout: separation vector
        self.play(Write(title2))
        self.wait(0.5)

        # Final vector and explanation
        v_final = Vector([1, 1], color=YELLOW)
        Av_final = Vector([1, 1], color=GREEN)
        Av_final.shift(v_final.get_start() - Av_final.get_start())
        
        self.play(GrowArrow(v_final))
        self.wait(0.5)
        self.play(Transform(v_final.copy(), Av_final))
        self.wait(0.5)

        # Final text
        final_text = Text("Eigenvectors reveal fundamental axes", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(VGroup(title2, v_final, Av_final, final_text)))
