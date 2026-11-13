from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Holomorphicity and Conformality", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial grid
        grid = VGroup()
        for i in range(-3, 4):
            grid.add(Line(start=LEFT*3 + UP*i, end=RIGHT*3 + UP*i, color=BLUE, stroke_width=2))
            grid.add(Line(start=LEFT*i + DOWN*3, end=LEFT*i + UP*3, color=BLUE, stroke_width=2))
        
        # Add initial grid
        self.play(Create(grid), run_time=1)
        self.wait(0.5)

        # Function label
        func_label = MathTex("f(z) = z^2 + c", font_size=30)
        func_label.to_corner(UR)
        self.play(Write(func_label))
        self.wait(0.5)

        # Animation of grid transformation
        transformed_grid = VGroup()
        for line in grid:
            new_line = line.copy()
            # Simple transformation to show conformality
            new_line.points = [point + UP*0.1*abs(point[0]) for point in line.points]
        self.play(Transform(grid, transformed_grid), run_time=2)
        self.wait(1)
        # Angle preserved labels
        label1 = Text("Angle Preserved", font_size=24, color=YELLOW)
        label1.move_to(UP*1.5 + LEFT*2)
        self.play(FadeIn(label1))
        self.wait(0.5)

        label2 = Text("Angle Preserved", font_size=24, color=YELLOW)
        label2.move_to(DOWN*1 + RIGHT*2)
        self.play(FadeIn(label2))
        self.wait(0.5)

        # Explanation text
        explanation = Text("Holomorphic functions are conformal", font_size=24)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(title), FadeOut(grid), FadeOut(func_label), 
                  FadeOut(label1), FadeOut(label2), FadeOut(explanation))
        self.wait(0.5)
