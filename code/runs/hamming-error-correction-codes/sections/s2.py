from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Solution: Parity Bits", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Slots
        slots = VGroup()
        for i in range(4):
            slot = Rectangle(width=1, height=1, color=WHITE)
            slot.shift((i-1.5)*RIGHT)
            slots.add(slot)
        
        slot_labels = VGroup()
        for i, label in enumerate(["P1", "D1", "P2", "D2"]):
            text = Text(label, font_size=24)
            text.next_to(slots[i], DOWN)
            slot_labels.add(text)
            
        self.play(Create(slots), Write(slot_labels))
        self.wait(1)

        # Data bits
        d1 = Text("1", font_size=24).move_to(slots[1])
        d2 = Text("0", font_size=24).move_to(slots[3])
        self.play(Write(d1), Write(d2))
        self.wait(1)

        # Parity calculations
        calc_text = Text("P1 checks positions 1,3...", font_size=24)
        calc_text.to_edge(DOWN)
        self.play(Write(calc_text))
        self.wait(1.5)

        p1 = Text("0", font_size=24).move_to(slots[0])
        p2 = Text("1", font_size=24).move_to(slots[2])
        self.play(Write(p1), Write(p2))
        self.wait(1.5)

        # Final codeword
        self.play(FadeOut(calc_text))
        codeword = Text("Codeword: 0101", font_size=30)
        codeword.to_edge(DOWN)
        self.play(Write(codeword))
        self.wait(2)

        self.play(FadeOut(title, slots, slot_labels, d1, d2, p1, p2, codeword))
