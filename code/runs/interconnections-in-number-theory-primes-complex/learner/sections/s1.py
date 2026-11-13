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
            y_range=[0, 20, 5],
            axis_config={"include_tip": False},
            tips=False,
        )
        axes.to_edge(DOWN)
        self.play(Create(axes))
        self.wait(0.5)

        # Bar chart setup
        bars = VGroup()
        prime_colors = []
        
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        for i in range(1, 51):
            is_prim = is_prime(i)
            color = RED if is_prim else GREY
            bar = Rectangle(
                width=0.8,
                height=0.1 * i,
                fill_color=color,
                fill_opacity=1,
                stroke_width=0,
            )
            bar.move_to(axes.c2p(i, 0), aligned_edge=DOWN)
            bars.add(bar)
            prime_colors.append(color)

        # Animate bars appearing one by one
        self.play(
            *[
                GrowFromEdge(bar, DOWN)
                for bar in bars[:1]
            ],
            run_time=0.5
        )
        self.wait(0.2)

        for i in range(1, 50):
            self.play(
                GrowFromEdge(bars[i], DOWN),
                run_time=0.1
            )
            self.wait(0.05)

        # Show key words
        chaos_text = Text("Chaotic", font_size=24).to_edge(LEFT).shift(UP * 2)
        chaos_text.shift(0.0 * RIGHT + 0.88 * UP)  # layout: separation vector
        self.play(Write(chaos_text))
        self.wait(1.0)

        self.play(FadeOut(chaos_text))

        structure_text = Text("Structure", font_size=24).to_edge(RIGHT).shift(UP * 2)
        structure_text.shift(0.0 * RIGHT + 0.87 * UP)  # layout: separation vector
        self.play(Write(structure_text))
        self.wait(1.0)

        self.play(FadeOut(structure_text))

        # Show prime counting function vs logarithmic integral
        self.play(FadeOut(bars), FadeOut(axes), FadeOut(title))
        self.wait(0.5)

        # New axes for comparison
        new_axes = Axes(
            x_range=[0, 100, 20],
            y_range=[0, 10, 2],
            axis_config={"include_tip": False},
            tips=False,
        )
        new_axes.to_edge(DOWN)
        self.play(Create(new_axes))
        self.wait(0.5)

        # Prime counting function (step-like)
        prime_count = [0] * 101
        for i in range(1, 101):
            if is_prime(i):
                prime_count[i] = prime_count[i-1] + 1
            else:
                prime_count[i] = prime_count[i-1]

        # Logarithmic integral approximation
        def li(x):
            if x <= 1:
                return 0
            import math
            return math.log(x) - 1.0451637801125 + 0.0000000000000000000000000000000

        # End of scene
        self.wait(1)
