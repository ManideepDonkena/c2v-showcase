from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Equilateral Case", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Draw equilateral triangle with side length 5
        triangle = Triangle().scale(1.5).move_to(ORIGIN)
        triangle.set_stroke(width=8)
        side_labels = VGroup()
        for i in range(3):
            label = MathTex("5").next_to(triangle.get_vertices()[i] + triangle.get_vertices()[(i+1)%3], 
                                        direction=UR if i == 0 else UL if i == 1 else DR, buff=0.2)
            side_labels.add(label)
            side_labels.add(label)
        self.play(Create(triangle), Write(side_labels))

        # Show inequality for sides = 5
        inequality = MathTex("2 \\times 5 \\leq 3 \\times 5").move_to(DOWN * 1.5)
        self.play(Write(inequality))
        self.wait(0.5)

        # Simplify to 10 <= 15 and show green bounce
        result = MathTex("10 \\leq 15").next_to(inequality, DOWN)
        result.shift(0.0 * RIGHT + -0.25 * UP)  # layout: separation vector
        self.play(Write(result))
        self.wait(0.5)

        # Make triangle green and bounce
        self.play(triangle.animate.set_fill(GREEN, opacity=0.8), 
                  triangle.animate.scale(1.05),
                  run_time=0.3)
        self.play(triangle.animate.scale(0.95),
                  run_time=0.3)
        self.wait(0.5)

        # Fade out first triangle and inequality
        self.play(FadeOut(triangle), FadeOut(side_labels), FadeOut(inequality), FadeOut(result))

        # Show general case with side x
        general_triangle = Triangle().scale(1.5).move_to(ORIGIN)
        general_triangle.set_stroke(width=8)
        x_label = MathTex("x").next_to(general_triangle.get_vertices()[0] + general_triangle.get_vertices()[1], 
                                       direction=UR, buff=0.2)
        self.play(Create(general_triangle), Write(x_label))
        self.wait(0.5)

        # Show inequality with x
        general_inequality = MathTex("2 \\times x \\leq 3 \\times x").move_to(DOWN * 1.5)
        self.play(Write(general_inequality))
        self.wait(0.5)

        # Simplify to 2 <= 3
        simplified = MathTex("2 \\leq 3").next_to(general_inequality, DOWN)
        self.play(Write(simplified))
        self.wait(1)

        # Fade out everything
        self.play(FadeOut(general_triangle), FadeOut(x_label), FadeOut(general_inequality), FadeOut(simplified))
        self.wait(0.5)

        # Narration text at bottom
        narration = Text("Every equilateral triangle is mirthful because its longest and shortest sides are equal.", 
                         font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        # Final narration
        final_narration = Text("Since twice any side is always less than three times that same side, the condition is satisfied.", 
                               font_size=24).to_edge(DOWN)
        self.play(Write(final_narration))
        self.wait(2)
        self.play(FadeOut(final_narration), FadeOut(title))
