from manim import *

class QuoteAnim(Scene):
    def construct(self):

        quote_str = " \"Infinity might be big, very big, unbelievable big. \n But actually, the truth is that size doesn't matter.\" "
        quoted_person_str = "-Nickles"

        quote_text = Text(quote_str, font_size=36).move_to(UP * 2)
        quoted_person_text = Text(quoted_person_str, font_size=36, color=YELLOW)

        self.play(Write(quote_text))
        self.play(Write(quoted_person_text))