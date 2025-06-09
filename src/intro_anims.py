from manim import *

class IconAnim(Scene):
    def construct(self):

        creation_time = 1.5
        shift_time = 0.6
        merge_time = 0.5

        font = "Consolas"

        # state 0: left half
        left_hexagon = RegularPolygon(6, radius=2).move_to(LEFT * 3.5)
        left_mask = Rectangle(width=2, height=4).move_to(LEFT * 4.5)
        left_intersect = Intersection(left_hexagon, left_mask, fill_color=LOGO_BLUE, fill_opacity=0.5)
        left_text = Text("Nick", font=font).move_to(left_intersect.get_center())
        left_part = VGroup(left_intersect, left_text)

        # state 0: right half
        right_hexagon = RegularPolygon(6, radius=2).move_to(RIGHT * 3.5)
        right_mask = Rectangle(width=2, height=4).move_to(RIGHT * 4.5)
        right_intersect = Intersection(right_hexagon, right_mask, fill_color=LOGO_GREEN, fill_opacity=0.5)
        right_text = Text("less", font=font).move_to(right_intersect.get_center())
        right_part = VGroup(right_intersect, right_text)

        # state 1: shift together
        shifted_left_part = left_part.copy().shift(RIGHT * 3.5)
        shifted_right_part = right_part.copy().shift(LEFT * 3.5)

        # state 2: merge
        merged_hexagon = RegularPolygon(6, radius=2, stroke_color=WHITE, fill_color=TEAL, fill_opacity=0.85)
        merged_text = Text("Nickless", font=font)
        fancy_tex_up = Tex(r"$\sum\limits_{i=0}^{\infty}$ stupidity").move_to(UP * 0.9).scale(0.6)
        fancy_tex_down = Tex(r"\[ \lim_{x\to\infty} nonsense \]").move_to(DOWN * 0.9).scale(0.6)
        merged_part = VGroup(merged_hexagon, merged_text, fancy_tex_up, fancy_tex_down)

        switched_text = Text("less Nick", font=font)

        self.play(Create(left_intersect,  run_time=creation_time),    Create(left_text,  run_time=creation_time),
                        Create(right_intersect, run_time=creation_time),    Create(right_text, run_time=creation_time))

        self.play(Transform(left_part,  shifted_left_part,  run_time=shift_time, rate_func=rate_functions.ease_in_quint),
                        Transform(right_part, shifted_right_part, run_time=shift_time, rate_func=rate_functions.ease_in_quint))

        self.play(Transform(left_part, merged_part, run_time=merge_time), Transform(right_part, merged_part, run_time=merge_time))
        self.add(merged_part)
        self.remove(left_part, right_part)
        self.wait(0.6)
        self.play(merged_text.animate.flip(axis=Y_AXIS), Transform(merged_text, switched_text))
        self.wait(1)


class QuoteAnim(Scene):
    def construct(self):

        quote_str = f" \"Infinity might be big, very big, unbelievable big. \n But actually, the truth is that <span fgcolor=\"{BLUE}\">size doesn't matter.\" </span> "
        quoted_person_str = "-Nickless"

        quote_text = MarkupText(quote_str, font_size=36).move_to(UP * 2.75)
        quoted_person_text = Text(quoted_person_str, font_size=36, color=YELLOW).move_to(UP * 1.5)

        self.play(FadeIn(quote_text, lag_ratio=0.175, rate_func=linear, run_time=5))
        self.play(Write(quoted_person_text))

class Intro(Scene):
    def construct(self):

        self.add_sound("assets/sounds/grant_opus.mp3")
        self.wait(0.4)

        IconAnim.construct(self)
        self.clear()
        QuoteAnim.construct(self)
        self.wait(3)