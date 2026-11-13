from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Solution: Parity Bits", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Slots
        slots = VGroup(*[Rectangle(width=1, height=1) for _ in range(4)])
        slots.arrange(RIGHT, buff=0.2)
        slots.move_to(DOWN * 0.5)
        
        slot_labels = VGroup(
            Text("P1", font_size=24),
            Text("D1", font_size=24),
            Text("P2", font_size=24),
            Text("D2", font_size=24),
        )
        for i, label in enumerate(slot_labels):
            label.next_to(slots[i], UP)
        
        self.play(Create(slots), Write(slot_labels))
        self.wait(0.5)

        # Data bits
        d1 = Text("1", font_size=32).move_to(slots[1])
        d2 = Text("0", font_size=32).move_to(slots[3])
        self.play(Write(d1), Write(d2))
        self.wait(0.5)

        # Parity calculations
        calc_text = Text("P1 checks positions 1,3,...", font_size=24)
        calc_text.to_edge(DOWN)
        self.play(Write(calc_text))
        self.wait(1)

        self.play(FadeOut(calc_text))

        calc_text2 = Text("P2 checks positions 2,3,...", font_size=24)
        calc_text2.to_edge(DOWN)
        self.play(Write(calc_text2))
        self.wait(1)

        self.play(FadeOut(calc_text2))

        # Fill parity bits
        p1 = Text("0", font_size=32).move_to(slots[0])
        p2 = Text("1", font_size=32).move_to(slots[2])
        
        self.play(Write(p1), Write(p2))
        self.wait(0.5)

        # Codeword
        codeword = Text("Codeword: 0101", font_size=32)
        codeword.to_edge(UP)
        codeword.shift(DOWN * 0.8)
        self.play(Write(codeword))
        self.wait(1)

        # Final explanation
        final_text = Text("Parity bits detect errors", font_size=24)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(final_text), FadeOut(codeword), FadeOut(title))
        self.wait(0.5)
