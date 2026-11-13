from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Attention Mechanism", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Sentence
        sentence = "The cat sat on the mat"
        words = [Text(word, font_size=24) for word in sentence.split()]
        words_group = VGroup(*words).arrange(RIGHT, buff=0.5)
        words_group.move_to(DOWN * 0.5)
        self.play(Write(words_group))
        self.wait(0.5)

        # Highlight 'sat'
        sat_word = words[2]
        sat_word_copy = sat_word.copy()
        sat_word_copy.set_color(YELLOW)
        self.play(sat_word.animate.set_color(YELLOW))

        # Create attention lines
        lines = VGroup()
        for i, word in enumerate(words):
            if i == 2:  # 'sat'
                continue
            line = Line(
                sat_word.get_center(),
                word.get_center(),
                color=WHITE,
                stroke_width=2
            )
            if i in [0, 5]:  # 'cat' and 'mat'
                line.set_color(GREEN)
                line.set_opacity(1.0)
            else:
                line.set_opacity(0.3)
            lines.add(line)

        self.play(Create(lines))
        self.wait(1.0)

        # Fade out words and lines
        self.play(FadeOut(words_group), FadeOut(lines))

        # Weight matrix
        matrix = [[0 for _ in range(6)] for _ in range(6)]
        matrix[2][0] = 0.8  # sat -> cat
        matrix[2][5] = 0.7  # sat -> mat
        matrix[2][1] = 0.2  # sat -> cat (other)
        matrix[2][3] = 0.1  # sat -> on
        matrix[2][4] = 0.1  # sat -> the

        matrix_tex = MathTex(
            "\\begin{bmatrix}",
            "0 & 0 & 0.8 & 0 & 0 & 0 \\\\",
            "0 & 0 & 0.2 & 0 & 0 & 0 \\\\",
            "0.8 & 0.2 & 0 & 0.1 & 0.1 & 0 \\\\",
            "0 & 0 & 0.1 & 0 & 0 & 0 \\\\",
            "0 & 0 & 0.1 & 0 & 0 & 0 \\\\",
            "0 & 0 & 0.7 & 0 & 0 & 0 \\\\",
            "\\end{bmatrix}",
            font_size=24
        )
        matrix_tex.move_to(UP * 0.5)
        self.play(Write(matrix_tex))
        self.wait(1.5)

        # Narration text
        narration = Text("Unlike older models that read sequentially, Transformers process all words simultaneously using self-attention.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.0)

        # Fade out
        self.play(FadeOut(title), FadeOut(narration), FadeOut(matrix_tex))
        self.wait(0.5)
