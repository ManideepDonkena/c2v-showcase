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
            grid.add(Line(start=LEFT*3 + UP*i, end=RIGHT*3 + UP*i, color=BLUE, stroke_width=1))
            grid.add(Line(start=LEFT*i + DOWN*3, end=LEFT*i + UP*3, color=BLUE, stroke_width=1))
        
        # Label
        label = Text("Angle Preserved", font_size=24)
        label.to_edge(DOWN)
        self.play(Create(grid), Write(label))
        self.wait(1)

        # Transform grid under f(z) = z^2 (c=0 for simplicity)
        new_grid = VGroup()
        for i in range(-3, 4):
            # Horizontal lines
            new_line_h = VMobject()
            points_h = [complex(x, i) for x in np.linspace(-3, 3, 100)]
            transformed_points_h = [z**2 for z in points_h]
            new_line_h.set_points_as_corners([np.array([z.real, z.imag, 0]) for z in transformed_points_h])
            new_line_h.set_color(RED)
            new_line_h.stroke_width = 1
            new_grid.add(new_line_h)
            
            # Vertical lines
            new_line_v = VMobject()
            points_v = [complex(i, y) for y in np.linspace(-3, 3, 100)]
            transformed_points_v = [z**2 for z in points_v]
            new_line_v.set_points_as_corners([np.array([z.real, z.imag, 0]) for z in transformed_points_v])
            new_line_v.set_color(RED)
            new_line_v.stroke_width = 1
            new_grid.add(new_line_v)

        # Show transformation
        self.play(Transform(grid, new_grid), run_time=2)
        self.wait(1.5)

        # Add more labels at different points
        label1 = Text("Angle Preserved", font_size=24).move_to(UP*1.5 + RIGHT*2)
        label2 = Text("Angle Preserved", font_size=24).move_to(DOWN*1.5 + LEFT*2)
        
        self.play(FadeIn(label1), FadeIn(label2))
        self.wait(1)

        # Clear labels
        self.play(FadeOut(label1), FadeOut(label2))

        # Final explanation text
        explanation = Text("Holomorphic functions are conformal", font_size=24)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(1.5)

        # Clear everything
        self.play(FadeOut(grid), FadeOut(explanation), FadeOut(title))
        self.wait(0.5)
