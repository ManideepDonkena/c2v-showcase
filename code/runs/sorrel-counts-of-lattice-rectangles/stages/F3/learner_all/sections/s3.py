from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Symmetry Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial 4x2 rectangle
        w, h = 4, 2
        rect = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        interior_points = (w - 1) * (h - 1)
        edge_points = 2 * (w + h)
        sorrel_count = interior_points - edge_points

        # Show initial rectangle
        self.play(Create(rect))
        self.wait(0.5)

        # Label interior points
        interior_label = MathTex(f"({w}-1)\\times({h}-1) = {interior_points}", font_size=24).next_to(rect, DOWN)
        self.play(Write(interior_label))
        self.wait(0.5)

        # Label edge points
        edge_label = MathTex(f"2\\times({w}+{h}) = {edge_points}", font_size=24).next_to(interior_label, DOWN)
        self.play(Write(edge_label))
        self.wait(0.5)

        # Show sorrel count formula and value
        formula = MathTex(
            "\\text{Sorrel Count} = (w-1)(h-1) - 2(w+h)",
            font_size=24
        ).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(formula))
        self.wait(0.5)

        count_label = MathTex(f"= {interior_points} - {edge_points} = {sorrel_count}", font_size=24).next_to(formula, DOWN)
        self.play(Write(count_label))
        self.wait(1)

        # Rotate rectangle to 2x4
        interior_label.shift(0.0 * RIGHT + -0.9 * UP)  # layout: separation vector
        self.play(Rotate(rect, 90 * DEGREES, about_point=ORIGIN), run_time=1.5)
        self.wait(0.5)

        # Update labels after rotation
        w, h = 2, 4
        new_interior = (w - 1) * (h - 1)
        new_edge = 2 * (w + h)
        new_sorrel = new_interior - new_edge

        new_interior_label = MathTex(f"({w}-1)\\times({h}-1) = {new_interior}", font_size=24).next_to(rect, DOWN)
        new_edge_label = MathTex(f"2\\times({w}+{h}) = {new_edge}", font_size=24).next_to(new_interior_label, DOWN)
        new_count_label = MathTex(f"= {new_interior} - {new_edge} = {new_sorrel}", font_size=24).next_to(formula, DOWN)

        self.play(
            Transform(interior_label, new_interior_label),
            Transform(edge_label, new_edge_label),
            Transform(count_label, new_count_label),
            run_time=0.5
        )
        self.wait(1)

        # Show that sorrel counts are equal
        equal_text = Text("Sorrel count unchanged!", font_size=24).set_color(GREEN).to_edge(DOWN)
        self.play(Write(equal_text))
        self.wait(1.5)

        # Show generic formula and example with w=2, h=3
        self.play(FadeOut(equal_text, count_label, edge_label, interior_label, formula))

        generic = MathTex(
            "\\text{Sorrel Count} = (w-1)(h-1) - 2(w+h)",
            font_size=30
        ).to_edge(UP)
        generic.shift(0.0 * RIGHT + 0.46 * UP)  # layout: separation vector
        self.play(Write(generic))
        self.wait(0.5)

        # Example with w=2, h=3
        example_w, example_h = 2, 3
        interior_ex = (example_w - 1) * (example_h - 1)
        edge_ex = 2 * (example_w + example_h)
        sorrel_ex = interior_ex - edge_ex
        ex_label = Text("Example: w=2, h=3", font_size=24).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(ex_label))
        self.wait(0.5)

        ex_interior = MathTex(f"Interior = ({example_w}-1)\times({example_h}-1) = {interior_ex}", font_size=24).next_to(generic, DOWN).shift(DOWN * 0.5)
        self.play(Write(ex_interior))
        self.wait(0.5)

        ex_edge = MathTex(f"Edge = 2\times({example_w}+{example_h}) = {edge_ex}", font_size=24).next_to(ex_interior, DOWN)
        self.play(Write(ex_edge))
        self.wait(0.5)

        ex_final = MathTex(f"Count = {interior_ex} - {edge_ex} = {sorrel_ex}", font_size=24).next_to(ex_edge, DOWN)
        self.play(Write(ex_final))
        self.wait(1.5)

        # Final note
        final_note = Text("Small rectangles have negative sorrel counts.", font_size=24).to_edge(DOWN)
        self.play(Write(final_note))
        self.wait(1.5)

        self.play(FadeOut(title, generic, ex_label, ex_interior, ex_edge, ex_final, final_note))
