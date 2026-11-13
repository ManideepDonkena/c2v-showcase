from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Rectangle Case", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Circle and inscribed square
        circle = Circle(radius=2, color=WHITE)
        square = Square(side_length=2*np.sqrt(2), color=RED)
        square.move_to(circle.get_center())
        
        # Show circle and square
        self.play(Create(circle))
        self.play(Create(square))
        self.wait(1)

        # Label diagonal and radius
        diag = Line(circle.get_left(), circle.get_right(), color=YELLOW)
        diag_label = MathTex("d = 2", font_size=24).next_to(diag, DOWN)
        radius = Line(circle.get_center(), circle.get_top(), color=BLUE)
        radius_label = MathTex("r = 1", font_size=24).next_to(radius, LEFT)
        
        self.play(Create(diag), Write(diag_label))
        self.play(Create(radius), Write(radius_label))
        self.wait(1)

        # Pythagorean theorem explanation
        triangle = Triangle().scale(0.5).move_to(square.get_center())
        triangle.shift(DOWN * 0.5)
        side_a = Line(triangle.get_vertices()[0], triangle.get_vertices()[1])
        side_b = Line(triangle.get_vertices()[1], triangle.get_vertices()[2])
        hypotenuse = Line(triangle.get_vertices()[2], triangle.get_vertices()[0])
        
        a_label = MathTex("a", font_size=24).next_to(side_a, DOWN)
        b_label = MathTex("a", font_size=24).next_to(side_b, RIGHT)
        c_label = MathTex("2", font_size=24).next_to(hypotenuse, UP)
        
        self.play(Create(triangle), Write(a_label), Write(b_label), Write(c_label))
        self.wait(1)

        # Formula for side length
        formula = MathTex("a^2 + a^2 = 2^2 \\Rightarrow a = \\sqrt{2}", font_size=30)
        formula.to_edge(DOWN)
        self.play(Write(formula))
        self.wait(1.5)

        # Morph square into rectangle
        rect = Rectangle(width=2*np.sqrt(2), height=1.2, color=RED)
        rect.move_to(square.get_center())
        
        morph = Transform(square, rect)
        self.play(morph)
        self.wait(1)

        # Labels for rectangle
        points_label = Text("4 Points", font_size=24).next_to(rect.get_vertices()[0], UL)
        angles_label = Text("Right Angles", font_size=24).next_to(rect.get_vertices()[0], UR)
        
        angles_label.shift(0.49 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(points_label), Write(angles_label))
        self.wait(1.5)

        # Comparison: rectangle vs square
        rect_comp = Rectangle(width=3, height=1.5, color=BLUE, fill_opacity=0.3).to_edge(DOWN)
        square_comp = Square(side_length=1.5, color=GREEN, fill_opacity=0.3).next_to(rect_comp, RIGHT)
        
        self.play(FadeOut(points_label), FadeOut(angles_label))
        rect_comp.shift(0.0 * RIGHT + 0.46 * UP)  # layout: separation vector
        self.play(Create(rect_comp), Create(square_comp))
        self.wait(1)

        # Text explanation
        text = Text("Rectangle: 2 degrees of freedom", font_size=24).next_to(rect_comp, UP)
        text2 = Text("Square: 1 degree of freedom", font_size=24).next_to(square_comp, UP)
        
        text.shift(0.0 * RIGHT + -1.2 * UP)  # layout: separation vector
        self.play(Write(text), Write(text2))
        self.wait(2)

        # Final theorem statement
        theorem = Text("Every simple closed curve contains an inscribed rectangle.", font_size=28)
        theorem.to_edge(DOWN)
        self.play(Write(theorem))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(circle), FadeOut(square), FadeOut(rect), 
                  FadeOut(diag), FadeOut(diag_label), FadeOut(radius), FadeOut(radius_label),
                  FadeOut(triangle), FadeOut(a_label), FadeOut(b_label), FadeOut(c_label),
                  FadeOut(formula), FadeOut(rect_comp), FadeOut(square_comp),
                  FadeOut(text), FadeOut(text2), FadeOut(theorem))
