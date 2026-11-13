from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Autoregressive Generation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial sentence and tokenization
        sentence = "The cat sat there"
        tokens = sentence.split()
        token_mobs = [Text(t, font_size=24) for t in tokens]
        token_group = VGroup(*token_mobs).arrange(RIGHT, buff=0.5)
        token_group.to_edge(DOWN)
        self.play(Write(token_group))
        self.wait(1)

        # Add new token 'is'
        new_token = Text("is", font_size=24)
        new_token.next_to(token_group[-1], RIGHT, buff=0.5)
        self.play(Write(new_token))
        self.wait(0.5)

        # Slide tokens forward
        self.play(
            token_group.animate.shift(LEFT * 0.5),
            new_token.animate.shift(LEFT * 0.5)
        )
        self.wait(0.5)

        # Attention lines
        attention_lines = []
        for i in range(len(tokens)):
            line = Line(token_mobs[i].get_top(), token_mobs[i].get_bottom())
            line.set_color(BLUE)
            line.set_opacity(0.5)
            attention_lines.append(line)
        self.play(Create(VGroup(*attention_lines)))
        self.wait(0.5)

        # Bar chart for probabilities
        bar_chart = VGroup()
        bars = []
        labels = ["the", "cat", "sat", "there", "is"]
        probs = [0.1, 0.2, 0.3, 0.25, 0.15]
        max_prob = max(probs)
        for i, (label, prob) in enumerate(zip(labels, probs)):
            bar = Rectangle(height=prob/max_prob * 2, width=0.4)
            bar.to_edge(DOWN).shift(RIGHT*(i-2)*0.6)
            label_mob = Text(label, font_size=16).next_to(bar, DOWN, buff=0.1)
            bar_chart.add(bar)
            bars.append(bar)
        bar_chart.shift(0.0 * RIGHT + 0.39 * UP)  # layout: separation vector
        self.play(Create(bar_chart))
        self.wait(0.5)

        # Highlight 'is'
        self.play(bars[4].animate.set_fill(YELLOW, opacity=0.8))
        self.wait(1)

        # Loop animation
        for _ in range(3):
            self.play(
                token_group.animate.shift(LEFT * 0.5),
                new_token.animate.shift(LEFT * 0.5)
            )
            self.wait(0.2)
            self.play(bars[4].animate.set_fill(YELLOW, opacity=0.8))
            self.wait(0.2)

        # RNN vs Transformer comparison
        rnn_text = Text("RNN", font_size=24).to_edge(LEFT, buff=1)
        trans_text = Text("Transformer", font_size=24).to_edge(RIGHT, buff=1)
        self.play(Write(rnn_text), Write(trans_text))
        self.wait(0.5)

        rnn_chain = VGroup(
            Rectangle(width=0.8, height=0.6).set_fill(BLUE, opacity=0.5),
            Rectangle(width=0.8, height=0.6).set_fill(BLUE, opacity=0.5),
            Rectangle(width=0.8, height=0.6).set_fill(BLUE, opacity=0.5)
        ).arrange(RIGHT, buff=0.1)
        rnn_chain.next_to(rnn_text, DOWN, buff=0.5)

        trans_attention = VGroup(
            Circle(radius=0.3).set_fill(GREEN, opacity=0.5),
            Circle(radius=0.3).set_fill(GREEN, opacity=0.5),
            Circle(radius=0.3).set_fill(GREEN, opacity=0.5)
        ).arrange(RIGHT, buff=0.5)
        trans_attention.next_to(trans_text, DOWN, buff=0.5)

        self.play(Create(rnn_chain), Create(trans_attention))
        self.wait(1)

        # Attention weights for swapped sentences
        sent1 = "Cat sat"
        sent2 = "Sat cat"
        t1 = Text(sent1, font_size=24).to_edge(LEFT, buff=1)
        t2 = Text(sent2, font_size=24).to_edge(RIGHT, buff=1)
        t1.shift(0.0 * RIGHT + 0.39 * UP)  # layout: separation vector
        t2.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        self.play(Write(t1), Write(t2))
        self.wait(0.5)

        # Wave pattern overlay
        wave1 = always_redraw(lambda: 
            VGroup(
                Line(start=[-3, 0, 0], end=[-3, 0.5, 0], color=RED),
                Line(start=[-2.5, 0, 0], end=[-2.5, 0.5, 0], color=BLUE),
                Line(start=[-2, 0, 0], end=[-2, 0.5, 0], color=GREEN)
            ).arrange(RIGHT, buff=0.1).next_to(t1, DOWN, buff=0.5)
        )
        wave2 = always_redraw(lambda: 
            VGroup(
                Line(start=[3, 0, 0], end=[3, 0.5, 0], color=RED),
                Line(start=[2.5, 0, 0], end=[2.5, 0.5, 0], color=BLUE),
                Line(start=[2, 0, 0], end=[2, 0.5, 0], color=GREEN)
            ).arrange(RIGHT, buff=0.1).next_to(t2, DOWN, buff=0.5)
        )
        self.play(Create(wave1), Create(wave2))
        self.wait(1)

        # Dot product visualization
        q = Vector([1, 1], color=YELLOW)
        k = Vector([1, -1], color=BLUE)
        q.next_to([0, 0, 0], LEFT, buff=1)
        k.next_to([0, 0, 0], RIGHT, buff=1)
        self.play(Create(q), Create(k))
        self.wait(0.5)

        dot_result = MathTex("1 \\cdot 1 + 1 \\cdot (-1) = 0", font_size=24).next_to([0, 0, 0], DOWN, buff=1)
        self.play(Write(dot_result))
        self.wait(1)

        # Transformer block
        block = Rectangle(width=3, height=2, color=ORANGE, fill_opacity=0.5)
        block_label = Text("Transformer Block", font_size=24).next_to(block, UP)
        self.play(Create(block), Write(block_label))
        self.wait(0.5)

        # Multi-head attention
        mha = Rectangle(width=1.5, height=1, color=PURPLE, fill_opacity=0.5)
        mha.next_to(block, LEFT, buff=0.5)
        mha_label = Text("Multi-Head\nAttention", font_size=16).next_to(mha, DOWN)
        self.play(Create(mha), Write(mha_label))
        self.wait(0.5)

        # Feed-forward network
        ff = Rectangle(width=1.5, height=1, color=GREEN, fill_opacity=0.5)
        ff.next_to(block, RIGHT, buff=0.5)
        ff_label = Text("Feed-Forward\nNetwork", font_size=16).next_to(ff, DOWN)
        self.play(Create(ff), Write(ff_label))
        self.wait(0.5)

        # Decoder-only vs Encoder-Decoder
        dec_only = Rectangle(width=3, height=2, color=RED, fill_opacity=0.5)
        enc_dec = Rectangle(width=3, height=2, color=BLUE, fill_opacity=0.5)
        dec_label = Text("Decoder-only", font_size=24).next_to(dec_only, UP)
        enc_label = Text("Encoder-Decoder", font_size=24).next_to(enc_dec, UP)
        self.play(Create(dec_only), Write(dec_label))
        self.play(Create(enc_dec), Write(enc_label))
        self.wait(1)

        # Cross attention
        cross_attn = Line(start=[0, 0, 0], end=[0.5, 0, 0], color=WHITE)
        cross_attn.next_to(enc_dec, DOWN, buff=0.5)
        self.play(Create(cross_attn))
        self.wait(1)

        # Triangular mask
        matrix = VGroup(*[VGroup(*[Square(side_length=0.3) for _ in range(4)]) for _ in range(4)])
        matrix.arrange_in_grid(rows=4, cols=4, buff=0.1)
        matrix.to_edge(DOWN, buff=1)
        self.play(Create(matrix))
        self.wait(0.5)

        # Masking animation
        mask = Rectangle(width=0.3*4, height=0.3*2, color=RED, fill_opacity=0.5)
        mask.next_to(matrix[0], UP, buff=0.1)
        self.play(Create(mask))
        self.wait(1)

        # Normalization comparison
        norm_text = Text("With Layer Norm", font_size=24).to_edge(LEFT, buff=1)
        no_norm_text = Text("Without Layer Norm", font_size=24).to_edge(RIGHT, buff=1)
        self.play(Write(norm_text), Write(no_norm_text))
        self.wait(0.5)

        # Fade out all
        self.play(
            FadeOut(title),
            FadeOut(token_group),
            FadeOut(new_token),
            FadeOut(VGroup(*attention_lines)),
            FadeOut(bar_chart),
            FadeOut(rnn_text),
            FadeOut(trans_text),
            FadeOut(rnn_chain),
            FadeOut(trans_attention),
            FadeOut(t1),
            FadeOut(t2),
            FadeOut(wave1),
            FadeOut(wave2),
            FadeOut(q),
            FadeOut(k),
            FadeOut(dot_result),
            FadeOut(block),
            FadeOut(block_label),
            FadeOut(mha),
            FadeOut(mha_label),
            FadeOut(ff),
            FadeOut(ff_label),
            FadeOut(dec_only),
            FadeOut(enc_dec),
            FadeOut(dec_label),
            FadeOut(enc_label),
            FadeOut(cross_attn),
            FadeOut(matrix),
            FadeOut(mask),
            FadeOut(norm_text),
            FadeOut(no_norm_text)
        )
        self.wait(0.5)
