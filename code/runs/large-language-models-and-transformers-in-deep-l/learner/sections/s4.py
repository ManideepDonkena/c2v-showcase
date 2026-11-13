from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Autoregressive Generation", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial sentence
        sentence = MathTex("The", " ", "cat", " ", "is", " ", "sitting", " ", "on", " ", "the", " ", "mat")
        sentence.scale(0.8)
        sentence.next_to(title, DOWN, buff=0.5)
        self.play(Write(sentence))
        self.wait(1)

        # Highlight 'there' as new token
        there = Text("there", font_size=24).set_color(YELLOW)
        there.next_to(sentence[11], RIGHT, buff=0.2)
        self.play(Write(there))
        self.wait(0.5)

        # Slide sequence forward
        self.play(
            sentence.animate.shift(LEFT * 0.8),
            there.animate.shift(LEFT * 0.8)
        )
        self.wait(0.5)

        # New attention lines
        attention_line = Line(start=DOWN, end=UP).set_color(BLUE)
        attention_line.next_to(sentence[1], DOWN, buff=0.2)
        self.play(Write(attention_line))
        self.wait(0.5)

        # Bar chart with probabilities
        bar_chart = VGroup()
        bars = []
        labels = []
        probs = [0.3, 0.25, 0.2, 0.15, 0.1]
        words = ["is", "was", "are", "were", "am"]
        
        for i, (prob, word) in enumerate(zip(probs, words)):
            bar = Rectangle(height=prob*3, width=0.4, color=BLUE, fill_opacity=0.7)
            bar.next_to(LEFT * 2 + DOWN * (i - 1), UP, buff=0.1)
            label = Text(word, font_size=18).next_to(bar, DOWN, buff=0.1)
            bars.append(bar)
            labels.append(label)
            bar_chart.add(bar, label)

        self.play(Write(bar_chart))
        self.wait(0.5)

        # Highlight 'is' as highest probability
        highlight = bars[0].copy().set_color(RED).set_fill(opacity=1)
        self.play(Transform(bars[0], highlight))
        self.wait(1)

        # Repeat process for next token
        next_token = Text("on", font_size=24).set_color(YELLOW)
        next_token.next_to(sentence[12], RIGHT, buff=0.2)
        self.play(Write(next_token))
        self.wait(0.5)

        self.play(
            sentence.animate.shift(LEFT * 0.8),
            there.animate.shift(LEFT * 0.8),
            next_token.animate.shift(LEFT * 0.8)
        )
        self.wait(0.5)

        # Final text
        final_text = Text("Finally, the model generates text autoregressively by feeding its own output back into the input. It predicts one token at a time, constantly updating its context, which allows it to construct coherent and long-form responses.", font_size=20)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)

        # Cleanup
        self.play(
            FadeOut(title),
            FadeOut(sentence),
            FadeOut(there),
            FadeOut(attention_line),
            FadeOut(bar_chart),
            FadeOut(next_token),
            FadeOut(final_text)
        )
