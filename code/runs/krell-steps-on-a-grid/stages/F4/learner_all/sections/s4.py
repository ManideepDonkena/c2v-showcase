from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Double Step Identity", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(x_range=[-7, 7], y_range=[-4, 4], faded_line_ratio=1)
        grid.set_opacity(0.5)
        self.play(Create(grid))
        self.wait(0.5)

        # Point A at (4, 6)
        A = Dot([4, 6, 0], color=BLUE)
        label_A = MathTex("(4, 6)", font_size=24).next_to(A, UR, buff=0.2)
        A.shift(0.0 * RIGHT + -2.23 * UP)  # layout: separation vector
        self.play(FadeIn(A), Write(label_A))
        self.wait(0.5)

        # Step 1: from (4, 6) to (6, 7)
        step1_arrow = Arrow(A.get_center(), [6, 7, 0], buff=0, color=YELLOW)
        step1_label = MathTex("Step\ 1", font_size=24).next_to(step1_arrow, UP, buff=0.2)
        self.play(GrowArrow(step1_arrow), Write(step1_label))
        self.wait(0.5)

        # Intermediate point after Step 1
        B_intermediate = Dot([6, 7, 0], color=GREEN)
        label_B_int = MathTex("(6, 7)", font_size=24).next_to(B_intermediate, UR, buff=0.2)
        self.play(FadeIn(B_intermediate), Write(label_B_int))
        self.wait(0.5)

        # Step 2: from (6, 7) to (7, 8)
        step2_arrow = Arrow(B_intermediate.get_center(), [7, 8, 0], buff=0, color=YELLOW)
        step2_label = MathTex("Step\ 2", font_size=24).next_to(step2_arrow, UP, buff=0.2)
        self.play(GrowArrow(step2_arrow), Write(step2_label))
        self.wait(0.5)

        # Final point B at (7, 8)
        B = Dot([7, 8, 0], color=BLUE)
        label_B = MathTex("(7, 8)", font_size=24).next_to(B, UR, buff=0.2)
        self.play(FadeIn(B), Write(label_B))
        self.wait(0.5)

        # Simultaneous dashed arrow from A to B (net result)
        net_arrow = DashedLine(A.get_center(), B.get_center(), color=RED)
        net_label = MathTex("(x+1, y+1)", font_size=24).next_to(net_arrow, DR, buff=0.2)
        self.play(Create(net_arrow), Write(net_label))
        self.wait(0.5)

        # Narration text
        narration = Text("Two consecutive Krell steps have a powerful simplification.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)

        # Clear narration and show key message
        self.play(FadeOut(narration))

        # Show specific example: (4, 6) -> (6, 7)
        example_text = Text("The first step takes us from (4, 6) to (6, 7)", font_size=24)
        example_text.to_edge(DOWN)
        self.play(Write(example_text))
        self.wait(1.5)

        # Clear example text
        self.play(FadeOut(example_text))

        # Final message
        final_msg = Text("Regardless of starting position, two steps always move to (x + 1, y + 1).", font_size=24)
        final_msg.to_edge(DOWN)
        self.play(Write(final_msg))
        self.wait(2)

        self.play(FadeOut(final_msg), FadeOut(title), FadeOut(grid), FadeOut(A), FadeOut(label_A),
                  FadeOut(step1_arrow), FadeOut(step1_label), FadeOut(B_intermediate), FadeOut(label_B_int),
                  FadeOut(step2_arrow), FadeOut(step2_label), FadeOut(B), FadeOut(label_B), FadeOut(net_arrow),
                  FadeOut(net_label))
