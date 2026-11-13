from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Multiple of Ten Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Number line with multiples of 10
        numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        number_mobs = []
        for num in numbers:
            mob = Integer(num, font_size=32)
            number_mobs.append(mob)

        # Animate each number sliding in and turning green
        for i, mob in enumerate(number_mobs):
            mob.move_to([i * 1.2 - 4, 0, 0])
            self.play(
                mob.animate.shift(UP * 0.5),
                run_time=0.3
            )
            self.play(
                mob.animate.set_color(GREEN),
                run_time=0.2
            )
            label = Text("Dapple", font_size=24).next_to(mob, DOWN)
            self.play(Write(label), run_time=0.2)
            self.wait(0.1)

        # Show 0 separately with red X and label
        zero_mob = Integer(0, font_size=32).move_to([0, -1, 0])
        self.play(Write(zero_mob))
        self.wait(0.5)
        cross = Cross(zero_mob, stroke_color=RED, stroke_width=8)
        self.play(Create(cross))
        label_zero = Text("Not Dapple (No Tens Digit)", font_size=24).next_to(zero_mob, DOWN)
        self.play(Write(label_zero))
        self.wait(1)

        # Show 77
        self.play(FadeOut(title), FadeOut(label_zero), FadeOut(cross))
        num_77 = Integer(77, font_size=32)
        tens_77 = Integer(7, font_size=32).set_color(YELLOW).move_to([-1.5, 0, 0])
        units_77 = Integer(7, font_size=32).set_color(BLUE).move_to([1.5, 0, 0])
        eq_77 = MathTex("=", font_size=40).move_to([0, 0, 0])
        self.play(Write(num_77))
        self.wait(0.5)
        self.play(
            ReplacementTransform(num_77.copy(), tens_77),
            ReplacementTransform(num_77.copy(), units_77),
            Write(eq_77)
        )
        self.wait(0.5)
        self.play(
            num_77.animate.set_color(RED),
            run_time=0.3
        )
        label_77 = Text("Not Dapple (Tens = Units)", font_size=24).next_to(num_77, DOWN)
        self.play(Write(label_77))
        self.wait(1)

        # Show 44
        self.play(FadeOut(num_77), FadeOut(tens_77), FadeOut(units_77), FadeOut(eq_77), FadeOut(label_77))
        num_44 = Integer(44, font_size=32)
        tens_44 = Integer(4, font_size=32).set_color(YELLOW).move_to([-1.5, 0, 0])
        units_44 = Integer(4, font_size=32).set_color(BLUE).move_to([1.5, 0, 0])
        eq_44 = MathTex("=", font_size=40).move_to([0, 0, 0])
        self.play(Write(num_44))
        self.wait(0.5)
        self.play(
            ReplacementTransform(num_44.copy(), tens_44),
            ReplacementTransform(num_44.copy(), units_44),
            Write(eq_44)
        )
        self.wait(0.5)
        self.play(
            num_44.animate.set_color(RED),
            run_time=0.3
        )
        label_44 = Text("Not Dapple (Tens = Units)", font_size=24).next_to(num_44, DOWN)
        self.play(Write(label_44))
        self.wait(1)

        # Show 44 and 10 comparison
        self.play(FadeOut(num_44), FadeOut(tens_44), FadeOut(units_44), FadeOut(eq_44), FadeOut(label_44))
        num_44_comp = Integer(44, font_size=32)
        tens_44_c = Integer(4, font_size=32).set_color(YELLOW).move_to([-1.5, 0, 0])
        units_44_c = Integer(4, font_size=32).set_color(BLUE).move_to([1.5, 0, 0])
        eq_44_c = MathTex("=", font_size=40).move_to([0, 0, 0])
        num_10_comp = Integer(10, font_size=32)
        tens_10_c = Integer(1, font_size=32).set_color(YELLOW).move_to([-1.5, -1, 0])
        units_10_c = Integer(0, font_size=32).set_color(BLUE).move_to([1.5, -1, 0])
        lt_10 = MathTex("<", font_size=40).move_to([0, -1, 0])
        self.play(Write(num_44_comp))
        self.wait(0.5)
        self.play(
            ReplacementTransform(num_44_comp.copy(), tens_44_c),
            ReplacementTransform(num_44_comp.copy(), units_44_c),
            Write(eq_44_c)
        )
        self.wait(0.5)
        self.play(
            num_44_comp.animate.set_color(RED),
            run_time=0.3
        )
        label_44_not = Text("Not Dapple", font_size=24).next_to(num_44_comp, DOWN)
        self.play(Write(label_44_not))
        self.wait(1)

        self.play(FadeOut(num_44_comp), FadeOut(tens_44_c), FadeOut(units_44_c), FadeOut(eq_44_c), FadeOut(label_44_not))

        self.play(Write(num_10_comp))
        self.wait(0.5)
        self.play(
            ReplacementTransform(num_10_comp.copy(), tens_10_c),
            ReplacementTransform(num_10_comp.copy(), units_10_c),
            Write(lt_10)
        )
        self.wait(0.5)
        self.play(
            num_10_comp.animate.set_color(RED),
            run_time=0.3
        )
        label_10_not = Text("Not Dapple", font_size=24).next_to(num_10_comp, DOWN)
        self.play(Write(label_10_not))
        self.wait(1)

        # Show 10 is dapple
        self.play(FadeOut(num_10_comp), FadeOut(tens_10_c), FadeOut(units_10_c), FadeOut(lt_10), FadeOut(label_10_not))
        num_10_d = Integer(10, font_size=32)
        tens_10 = Integer(1, font_size=32).set_color(YELLOW).move_to([-1.5, 0, 0])
        units_10 = Integer(0, font_size=32).set_color(BLUE).move_to([1.5, 0, 0])
        gt_10 = MathTex(">", font_size=40).move_to([0, 0, 0])
        self.play(Write(num_10_d))
        self.wait(0.5)
        self.play(
            ReplacementTransform(num_10_d.copy(), tens_10),
            ReplacementTransform(num_10_d.copy(), units_10),
            Write(gt_10)
        )
        self.wait(0.5)
        self.play(
            num_10_d.animate.set_color(GREEN),
            run_time=0.3
        )
        label_10 = Text("Dapple", font_size=24).next_to(num_10_d, DOWN)
        self.play(Write(label_10))
        self.wait(1)

        # Show 11 is not dapple
        self.play(FadeOut(num_10_d), FadeOut(tens_10), FadeOut(units_10), FadeOut(gt_10), FadeOut(label_10))
        num_11 = Integer(11, font_size=32)
        tens_11 = Integer(1, font_size=32).set_color(YELLOW).move_to([-1.5, 0, 0])
        units_11 = Integer(1, font_size=32).set_color(BLUE).move_to([1.5, 0, 0])
        eq_11 = MathTex("=", font_size=40).move_to([0, 0, 0])
        self.play(Write(num_11))
        self.wait(0.5)
        self.play(
            ReplacementTransform(num_11.copy(), tens_11),
            ReplacementTransform(num_11.copy(), units_11),
            Write(eq_11)
        )
        self.wait(0.5)
        self.play(
            num_11.animate.set_color(RED),
            run_time=0.3
        )
        label_11 = Text("Not Dapple (Tens = Units)", font_size=24).next_to(num_11, DOWN)
        self.play(Write(label_11))
        self.wait(1)

        # Show 7 as one-digit number
        self.play(FadeOut(num_11), FadeOut(tens_11), FadeOut(units_11), FadeOut(eq_11), FadeOut(label_11))
        num_7 = Integer(7, font_size=32)
        tens_7 = Integer(0, font_size=32).set_color(YELLOW).move_to([-1.5, 0, 0])
        units_7 = Integer(7, font_size=32).set_color(BLUE).move_to([1.5, 0, 0])
        gt_7 = MathTex(">", font_size=40).move_to([0, 0, 0])
        comp_7 = MathTex("0 > 7", font_size=32)
        self.play(Write(num_7))
        self.wait(0.5)
        self.play(
            ReplacementTransform(num_7.copy(), tens_7),
            ReplacementTransform(num_7.copy(), units_7),
            Write(gt_7)
        )
        self.wait(0.5)
        comp_7.next_to(num_7, DOWN)
        self.play(Write(comp_7))
        self.wait(0.5)
        self.play(
            num_7.animate.set_color(RED),
            run_time=0.3
        )
        label_7 = Text("Not Dapple (0 > 7 is false)", font_size=24).next_to(num_7, DOWN)
        self.play(Write(label_7))
        self.wait(1)

        # Show 98 is dapple
        self.play(FadeOut(num_7), FadeOut(tens_7), FadeOut(units_7), FadeOut(gt_7), FadeOut(comp_7), FadeOut(label_7))
        num_98 = Integer(98, font_size=32)
        tens_98 = Integer(9, font_size=32).set_color(YELLOW).move_to([-1.5, 0, 0])
        units_98 = Integer(8, font_size=32).set_color(BLUE).move_to([1.5, 0, 0])
        gt_98 = MathTex(">", font_size=40).move_to([0, 0, 0])
        self.play(Write(num_98))
        self.wait(0.5)
        self.play(
            ReplacementTransform(num_98.copy(), tens_98),
            ReplacementTransform(num_98.copy(), units_98),
            Write(gt_98)
        )
        self.wait(0.5)
        self.play(
            num_98.animate.set_color(GREEN),
            run_time=0.3
        )
        label_98 = Text("Tens > Units", font_size=24).next_to(num_98, DOWN)
        self.play(Write(label_98))
        self.wait(1)

        # Show 0 alone
        self.play(FadeOut(num_98), FadeOut(tens_98), FadeOut(units_98), FadeOut(gt_98), FadeOut(label_98))
        zero_alone = Integer(0, font_size=32)
        self.play(Write(zero_alone))
        self.wait(0.5)
        label_zero_final = Text("Not Dapple (No tens digit)", font_size=24).next_to(zero_alone, DOWN)
        self.play(Write(label_zero_final))
        self.wait(1)

        # End
        self.play(FadeOut(zero_alone), FadeOut(label_zero_final))
