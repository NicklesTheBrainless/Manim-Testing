from manim import *

class Consts:
    time_per_char = 0.04

    say_font = "Consolas"
    say_size = 26
    say_pos = UP * 2
    say_default = Text("", font=say_font, font_size=say_size).move_to(say_pos)

    simple_harmonic_series = r"1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \dots"
    fancy_harmonic_series  = r"\sum_{n=1}^{\infty} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \dots"

class QuestionAnim(Scene):

    say_text = None
    math_tex = None

    def construct(self):

        # state 0: saying hello
        self.say_text = Text("Hello everyone, I have an interesting math problem for you all",
                             font=Consts.say_font, font_size=Consts.say_size).move_to(Consts.say_pos)
        self.play(FadeIn(self.say_text, lag_ratio=0.2, rate_func=linear, run_time=2))
        self.wait(1)

        # state 1: showing the harmonic series
        self.math_tex = MathTex(Consts.simple_harmonic_series)
        self.play(Write(self.math_tex))
        self.wait(0.5)

        # state 2: explaining the sequence/series
        self.change_say_text("That is a infinite sequence of numbers, that all get added together")
        self.wait(2)

        # state 3: teasing a definition
        self.change_say_text("There is actually a word for that")
        self.wait(0.5)

        # state 4: defining the word "series"
        self.change_say_text(" an \"infinite series\" is the mathematical term for an \n"
                             "infinite sequence of number that get all added together")
        self.wait(2.5)

        # state 5: asking the question
        self.change_say_text("So now to the question, does the sum of \n"
                             " this infinite series reach Infinity?")
        self.wait(3)

        # state 6:
        self.change_say_text("As we already know, not every sum of \n"
                             "  infinite numbers equals Infinity")
        self.change_math_tex("")
        self.wait(1)

        # state 7:
        self.change_say_text("Look at this for example")
        self.change_math_tex(r"0.\overline{3} = 0.3 + 0.03 + 0.003 + 0.0003 + \dots")
        self.wait(2)

        # state 8:
        self.change_say_text("That is also a sum of an infinite series, but it doesn't \n"
                             "  reach Infinity. It doesn't even get bigger than 3.4")
        self.wait(2)

        # state 9:
        self.change_math_tex("")
        self.change_say_text(" So now that we know that there are infinite series that \n"
                             "  don't add up to Infinity we can answer if this series, \n"
                             "that is called harmonic series by the way, reaches Infinity")
        self.change_math_tex(Consts.fancy_harmonic_series)
        self.wait(3)

    def change_say_text(self, new: str):
        self.remove(self.say_text)
        new_text = Text(new, font=Consts.say_font, font_size=Consts.say_size).move_to(Consts.say_pos)
        self.play(FadeIn(new_text, lag_ratio=0.2, rate_func=linear, run_time=len(new)*Consts.time_per_char))
        self.say_text = new_text

    def change_math_tex(self, new: str):
        if self.math_tex is not None:
            self.remove(self.math_tex)
        new_tex = MathTex(new) if new else VGroup()
        self.play(ReplacementTransform(self.math_tex, new_tex))
        self.math_tex = new_tex