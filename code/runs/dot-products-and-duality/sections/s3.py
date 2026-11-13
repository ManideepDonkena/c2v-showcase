from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Duality via Linear Functionals", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Vector A
        A = Vector([3, 2], color=YELLOW)
        A_label = MathTex("\\vec{A}", font_size=24).next_to(A.get_end(), UR, buff=0.1)
        
        # Grid of points
        grid = VGroup()
        for i in range(-6, 7):
            for j in range(-4, 5):
                dot = Dot([i, j, 0], color=WHITE, radius=0.03)
                grid.add(dot)
        # Show A and grid
        self.play(Create(A), Write(A_label))
        grid.shift(0.0 * RIGHT + -0.18 * UP)  # layout: separation vector
        self.play(FadeIn(grid))
        self.wait(1)

        # Show a few test vectors B
        B1 = Vector([1, 2], color=GREEN)
        B1_label = MathTex("\\vec{B}_1", font_size=24).next_to(B1.get_end(), UR, buff=0.1)
        
        B2 = Vector([3, 0], color=GREEN)
        B2_label = MathTex("\\vec{B}_2", font_size=24).next_to(B2.get_end(), UR, buff=0.1)
        
        # Show first B
        self.play(Create(B1), Write(B1_label))
        self.wait(1)
        
        # Show second B
        self.play(Create(B2), Write(B2_label))
        self.wait(1)

        # Fade out B vectors and labels
        self.play(FadeOut(B1), FadeOut(B1_label), FadeOut(B2), FadeOut(B2_label))
        
        # Show level sets (contours)
        contour1 = DashedLine([-7, 2, 0], [7, 2, 0], color=BLUE, stroke_width=2)
        contour2 = DashedLine([-7, 1, 0], [7, 1, 0], color=BLUE, stroke_width=2)
        contour3 = DashedLine([-7, 0, 0], [7, 0, 0], color=BLUE, stroke_width=2)
        
        # Show contours
        self.play(Create(contour1), Create(contour2), Create(contour3))
        self.wait(1)

        # Show dot product values
        dot_val1 = MathTex("\\vec{A} \\cdot \\vec{B}_1 = 7", font_size=24).to_corner(UL)
        dot_val2 = MathTex("\\vec{A} \\cdot \\vec{B}_2 = 3", font_size=24).to_corner(UL)
        
        self.play(Write(dot_val1))
        self.wait(1)
        self.play(Transform(dot_val1, dot_val2))
        self.wait(1)
        self.play(FadeOut(dot_val1))

        # Show final narration text
        narration = Text("All vectors ending on the line perpendicular to A", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        
        self.play(FadeOut(narration), FadeOut(title), FadeOut(A), FadeOut(A_label), 
                  FadeOut(grid), FadeOut(contour1), FadeOut(contour2), FadeOut(contour3))
        self.wait(0.5)
