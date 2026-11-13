from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Area Connection", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Squares
        a = 3
        b = 4
        c = 5

        # Blue square (side a)
        blue_square = Square(side_length=a, color=BLUE, fill_opacity=0.5)
        blue_square.shift(LEFT * 2 + DOWN * 1)
        blue_label = MathTex("a", font_size=24).next_to(blue_square, DOWN)
        
        # Green square (side b)
        green_square = Square(side_length=b, color=GREEN, fill_opacity=0.5)
        green_square.shift(RIGHT * 2 + DOWN * 1)
        green_label = MathTex("b", font_size=24).next_to(green_square, DOWN)

        # Red square (side c)
        red_square = Square(side_length=c, color=RED, fill_opacity=0.5)
        red_square.shift(DOWN * 1)
        red_label = MathTex("c", font_size=24).next_to(red_square, DOWN)

        # Area labels
        blue_area = MathTex(f"a^2 = {a}^2 = {a**2}", font_size=24)
        blue_area.next_to(blue_square, UP)
        
        green_area = MathTex(f"b^2 = {b}^2 = {b**2}", font_size=24)
        green_area.next_to(green_square, UP)

        red_area = MathTex(f"c^2 = {c}^2 = {c**2}", font_size=24)
        red_area.next_to(red_square, UP)

        # Show initial setup
        self.play(Create(blue_square), Create(green_square), Create(red_square))
        self.play(Write(blue_label), Write(green_label), Write(red_label))
        self.wait(1)

        blue_area.shift(0.0 * RIGHT + 0.9 * UP)  # layout: separation vector
        green_area.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        self.play(Write(blue_area), Write(green_area), Write(red_area))
        self.wait(1.5)

        # Animation: liquid flow
        # Fade out labels and areas
        self.play(FadeOut(blue_label, green_label, red_label, blue_area, green_area, red_area))

        # Create the "liquid" effect using smaller squares that move into red square
        # Blue area pieces
        blue_pieces = VGroup()
        for i in range(a):
            for j in range(a):
                piece = Square(side_length=1, color=BLUE, fill_opacity=0.5)
                piece.move_to(blue_square.get_center() + LEFT * (a/2 - 0.5) + RIGHT * (i - a/2 + 0.5) + UP * (a/2 - 0.5) + DOWN * (j - a/2 + 0.5))
                blue_pieces.add(piece)

        # Green area pieces
        green_pieces = VGroup()
        for i in range(b):
            for j in range(b):
                piece = Square(side_length=1, color=GREEN, fill_opacity=0.5)
                piece.move_to(green_square.get_center() + LEFT * (b/2 - 0.5) + RIGHT * (i - b/2 + 0.5) + UP * (b/2 - 0.5) + DOWN * (j - b/2 + 0.5))
                green_pieces.add(piece)

        # Move blue pieces to red square
        self.play(AnimationGroup(*[Transform(piece, Square(side_length=1, color=BLUE, fill_opacity=0.5).move_to(red_square.get_center() + LEFT * (c/2 - 0.5) + RIGHT * (i - c/2 + 0.5) + UP * (c/2 - 0.5) + DOWN * (j - c/2 + 0.5))) for i in range(c) for j in range(c) if i < a and j < a], run_time=1.5, rate_func=linear))

        # Move green pieces to red square
        self.play(AnimationGroup(*[Transform(piece, Square(side_length=1, color=GREEN, fill_opacity=0.5).move_to(red_square.get_center() + LEFT * (c/2 - 0.5) + RIGHT * (i - c/2 + 0.5) + UP * (c/2 - 0.5) + DOWN * (j - c/2 + 0.5))) for i in range(c) for j in range(c) if i >= a or j >= b], run_time=1.5, rate_func=linear))

        # Show the final area relationship
        self.wait(0.5)
        
        final_text = Text("Magic!", font_size=36).to_edge(UP)
        self.play(Transform(title, final_text))
        self.wait(0.5)

        # Show equation
        equation = MathTex("a^2 + b^2 = c^2", font_size=40)
        equation.to_edge(DOWN)
        self.play(Write(equation))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(blue_square, green_square, red_square, equation, title))
        self.wait(0.5)
