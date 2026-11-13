from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Prime Landscape", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Setup axes
        axes = Axes(
            x_range=[0, 52, 1],
            y_range=[0, 1.5, 1],
            axis_config={"stroke_color": WHITE},
            tips=False,
        )
        axes.to_edge(DOWN)
        self.play(Create(axes))
        self.wait(0.5)

        # Labels
        x_labels = [axes.x_axis.n2p(i) for i in range(1, 51, 5)]
        x_label_texts = [Integer(i, font_size=24) for i in range(1, 51, 5)]
        for i, label in enumerate(x_label_texts):
            label.next_to(x_labels[i], DOWN)
        self.play(*[Write(label) for label in x_label_texts])
        self.wait(0.5)

        # Prime checker function
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True

        # Create bars
        bars = VGroup()
        bar_heights = []
        for i in range(1, 51):
            height = 1 if is_prime(i) else 0
            bar_heights.append(height)
            bar = Rectangle(
                width=0.4,
                height=height,
                color=RED if is_prime(i) else GREY,
                fill_opacity=1,
                stroke_width=0,
            )
            bar.move_to(axes.c2p(i, 0), aligned_edge=DOWN)
            bars.add(bar)

        # Animate bars appearing one by one
        self.play(
            *[
                GrowFromEdge(bar, DOWN)
                for bar in bars
            ],
            run_time=4,
        )
        self.wait(1)

        # Add chaos text with offset to avoid overlap
        chaos_text = Text("chaos", font_size=36).move_to(axes.coords_to_point(0, 2.5))
        self.play(Write(chaos_text), run_time=1)
        self.wait(2)

        # Key words
        chaos = Text("chaotic", font_size=24).to_edge(LEFT).shift(UP*2)
        disorder = Text("disorder", font_size=24).next_to(chaos, DOWN)
        structure = Text("structure", font_size=24).to_edge(RIGHT).shift(UP*2)
        analysis = Text("analysis", font_size=24).next_to(structure, DOWN)

        # Adjust positions to avoid overlap with axes
        disorder.shift(0.0 * RIGHT + 1.39 * UP)  # move up to clear axes
        analysis.shift(0.0 * RIGHT + 1.45 * UP)  # move up to clear axes

        self.play(Write(chaos), Write(disorder))
        self.wait(1)
        self.play(Write(structure), Write(analysis))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(bars),
            FadeOut(chaos),
            FadeOut(disorder),
            FadeOut(structure),
            FadeOut(analysis),
        )
        self.wait(0.5)
