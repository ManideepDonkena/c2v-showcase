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
            y_range=[0, 60, 10],
            axis_config={"include_tip": False},
            tips=False,
        )
        axes.to_edge(DOWN)
        self.play(Create(axes))
        self.wait(0.5)

        # Labels
        x_labels = [axes.x_axis.n2p(i) for i in range(1, 51, 5)]
        x_text = [Text(str(i), font_size=24) for i in range(1, 51, 5)]
        for i, t in enumerate(x_text):
            t.next_to(x_labels[i], DOWN)
        self.play(*[Write(t) for t in x_text])
        self.wait(0.5)

        # Prime detection function
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True

        # Create bars
        bars = VGroup()
        bar_colors = []
        for i in range(1, 51):
            height = i
            bar = Rectangle(
                width=0.4,
                height=height,
                color=RED if is_prime(i) else GRAY,
                fill_opacity=1,
                stroke_width=0,
            )
            bar.move_to(axes.c2p(i, 0), aligned_edge=DOWN)
            bars.add(bar)
            bar_colors.append(RED if is_prime(i) else GRAY)

        # Animate bars appearing one by one
        for i in range(50):
            self.play(
                bars[i].animate.scale_to_fit_height(i+1),
                run_time=0.1,
                rate_func=linear
            )
            self.wait(0.02)

        # Key words
        chaos = Text("chaotic", font_size=24, color=RED).to_edge(LEFT).shift(UP*2)
        chaos.shift(0.0 * RIGHT + 0.88 * UP)  # layout: separation vector
        self.play(Write(chaos))
        self.wait(1)

        self.play(FadeOut(chaos))

        structure = Text("structure", font_size=24, color=BLUE).to_edge(RIGHT).shift(UP*2)
        structure.shift(0.0 * RIGHT + 0.86 * UP)  # layout: separation vector
        self.play(Write(structure))
        self.wait(1)

        self.play(FadeOut(structure))

        # Fade out everything except title
        self.play(
            FadeOut(bars),
            FadeOut(axes),
            FadeOut(title),
        )
