from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Autoregressive Generation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial sentence
        sentence = MathTex("The", " ", "cat", " ", "is", " ", "there", font_size=32)
        sentence.to_edge(UP, buff=1.5)
        self.play(Write(sentence))
        self.wait(0.5)

        # Highlight 'there' and show it being appended
        there = sentence[6]
        there_copy = there.copy()
        self.play(there_copy.animate.move_to(ORIGIN).scale(1.5), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(there_copy))

        # Slide sequence forward
        new_sentence = MathTex("The", " ", "cat", " ", "is", " ", "there", " ", "and", font_size=32)
        new_sentence.to_edge(UP, buff=1.5)
        self.play(Transform(sentence, new_sentence))
        self.wait(0.5)

        # Show attention lines
        attention_line = Line(
            start=sentence[4].get_center() + UP * 0.2,
            end=sentence[6].get_center() + DOWN * 0.2,
            color=YELLOW,
        )
        attention_line.shift(0.0 * RIGHT + 0.47 * UP)  # layout: separation vector
        self.play(Create(attention_line))
        self.wait(0.5)
        self.play(FadeOut(attention_line))
        self.play(Create(attention_line))
        self.wait(0.5)
        self.play(FadeOut(attention_line))

        # Bar chart for probabilities
        bars = VGroup()
        probs = [0.1, 0.25, 0.3, 0.2, 0.15]
        max_prob = max(probs)
        bar_height = 2
        for i, p in enumerate(probs):
            bar = Rectangle(
                width=0.4,
                height=p / max_prob * bar_height,
                color=BLUE,
                fill_opacity=0.7
            )
            bar.move_to(LEFT * (2 - i * 0.6) + DOWN * 1)
            label = Text(["is", "and", "the", "cat", "there"][i], font_size=18).next_to(bar, DOWN, buff=0.1)
            bars.add(VGroup(bar, label))
        self.play(Write(bars))
        self.wait(0.5)

        # Highlight 'is' as highest
        is_bar = bars[1][0]
        is_label = bars[1][1]
        self.play(
            is_bar.animate.set_fill(RED),
            is_label.animate.set_color(RED)
        )
        self.wait(1)

        # Simulate loop with new token
        tokens = ["is", "there", "and", "the", "cat"]
        for i, token in enumerate(tokens[1:], 1):
            # Update sentence
            old_sentence = sentence.copy()
            new_sentence = MathTex("The", " ", "cat", " ", "is", " ", "there", " ", "and", " ", "the", " ", "cat", font_size=32)
            new_sentence.to_edge(UP, buff=1.5)
            self.play(Transform(sentence, new_sentence))
            self.wait(0.3)

            # Update attention
            attention_line = Line(
                start=sentence[4].get_center() + UP * 0.2,
                end=sentence[i+2].get_center() + DOWN * 0.2,
                color=YELLOW,
                stroke_width=3
            )
            self.play(Create(attention_line))
            self.wait(0.3)
            self.play(FadeOut(attention_line))

        # Final text
        final_text = Text("Autoregressive Generation", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(sentence),
            FadeOut(bars),
            FadeOut(final_text)
        )
        self.wait(0.5)
