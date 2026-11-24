"""
Scene 6: Summary and Credits (4:35 - 5:10)
Clean typography, well-margined summary cards, and legible credits.
"""

from manim import *
from src.config import (
    COLOR_BG, COLOR_E1, COLOR_V, COLOR_TEXT_PRIMARY,
    COLOR_TEXT_SECONDARY, COLOR_TEXT_HIGHLIGHT
)


class Scene6Summary(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # Scene Header
        header = Text(
            "KEY TAKEAWAYS",
            font="Helvetica",
            font_size=28,
            color=COLOR_TEXT_PRIMARY,
            weight=BOLD
        ).to_edge(UP, buff=0.45)

        sub_header = Text(
            "What we have learned about linear transformations",
            font="Helvetica",
            font_size=15,
            color=COLOR_TEXT_SECONDARY
        ).next_to(header, DOWN, buff=0.12)

        self.play(FadeIn(header, shift=DOWN * 0.2), FadeIn(sub_header, shift=DOWN * 0.15), run_time=1.2)
        self.wait(1.0)

        # -------------------------------------------------------------
        # 1. Three Main Takeaways (Cards)
        # -------------------------------------------------------------
        card_w, card_h = 11.0, 1.2

        # Takeaway 1
        t1_box = RoundedRectangle(corner_radius=0.12, width=card_w, height=card_h, fill_color="#1E293B", fill_opacity=0.92, stroke_color="#38BDF8", stroke_width=1.2).move_to(UP * 1.1)
        t1_title = Text("1. A Matrix Defines How Vectors Transform Space", font="Helvetica", font_size=15, color="#38BDF8", weight=BOLD).move_to(t1_box.get_top() + DOWN * 0.26)
        t1_desc = Text("It is not just a static table of numbers; it is a dynamic geometric map transforming ℝ² to ℝ².", font="Helvetica", font_size=12, color=COLOR_TEXT_SECONDARY).next_to(t1_title, DOWN, buff=0.1)
        card1 = VGroup(t1_box, t1_title, t1_desc)

        # Takeaway 2
        t2_box = RoundedRectangle(corner_radius=0.12, width=card_w, height=card_h, fill_color="#1E293B", fill_opacity=0.92, stroke_color="#2ECC71", stroke_width=1.2).move_to(DOWN * 0.3)
        t2_title = Text("2. The Columns Describe Transformed Basis Vectors", font="Helvetica", font_size=15, color="#2ECC71", weight=BOLD).move_to(t2_box.get_top() + DOWN * 0.26)
        t2_desc = Text("Column 1 is where e₁ lands ([2, 0]ᵀ); Column 2 is where e₂ lands ([1, 1]ᵀ). This determines ALL vectors!", font="Helvetica", font_size=12, color=COLOR_TEXT_SECONDARY).next_to(t2_title, DOWN, buff=0.1)
        card2 = VGroup(t2_box, t2_title, t2_desc)

        # Takeaway 3
        t3_box = RoundedRectangle(corner_radius=0.12, width=card_w, height=card_h, fill_color="#1E293B", fill_opacity=0.92, stroke_color="#F1C40F", stroke_width=1.2).move_to(DOWN * 1.7)
        t3_title = Text("3. Linearity Preserves Parallelism and Origin", font="Helvetica", font_size=15, color="#F1C40F", weight=BOLD).move_to(t3_box.get_top() + DOWN * 0.26)
        t3_desc = Text("Straight lines remain straight, grid lines remain evenly spaced, and the origin (0, 0) never moves.", font="Helvetica", font_size=12, color=COLOR_TEXT_SECONDARY).next_to(t3_title, DOWN, buff=0.1)
        card3 = VGroup(t3_box, t3_title, t3_desc)

        self.play(FadeIn(card1, shift=UP * 0.25), run_time=1.2)
        self.wait(2.5)
        self.play(FadeIn(card2, shift=UP * 0.25), run_time=1.2)
        self.wait(2.5)
        self.play(FadeIn(card3, shift=UP * 0.25), run_time=1.2)
        self.wait(4.0)

        # -------------------------------------------------------------
        # 2. Iconic Punchline Card
        # -------------------------------------------------------------
        self.play(
            FadeOut(card1, shift=UP * 0.15),
            FadeOut(card2, shift=UP * 0.15),
            FadeOut(card3, shift=UP * 0.15),
            FadeOut(sub_header),
            run_time=1.2
        )

        quote_box = RoundedRectangle(
            corner_radius=0.15,
            width=11.0,
            height=2.0,
            fill_color="#0F172A",
            fill_opacity=0.95,
            stroke_color="#38BDF8",
            stroke_width=2.0
        ).move_to(UP * 0.35)

        quote_text1 = Text(
            "\"One matrix. Two basis vectors.",
            font="Helvetica",
            font_size=24,
            color=COLOR_TEXT_PRIMARY,
            weight=BOLD
        ).move_to(quote_box.get_center() + UP * 0.3)

        quote_text2 = Text(
            "An entire transformed plane.\"",
            font="Helvetica",
            font_size=28,
            color="#38BDF8",
            weight=BOLD
        ).next_to(quote_text1, DOWN, buff=0.18)

        quote_grp = VGroup(quote_box, quote_text1, quote_text2)
        self.play(FadeIn(quote_grp, scale=0.92), run_time=1.8)
        self.wait(5.0)

        # -------------------------------------------------------------
        # 3. Credits & AI Disclosure
        # -------------------------------------------------------------
        self.play(FadeOut(quote_grp), FadeOut(header), run_time=1.2)

        credits_title = Text("PROJECT CREDITS & DISCLOSURE", font="Helvetica", font_size=20, color=COLOR_TEXT_HIGHLIGHT, weight=BOLD).to_edge(UP, buff=0.7)

        cred_box = RoundedRectangle(
            corner_radius=0.15,
            width=11.0,
            height=4.4,
            fill_color="#1E293B",
            fill_opacity=0.9,
            stroke_color="#334155",
            stroke_width=1.2
        ).next_to(credits_title, DOWN, buff=0.2)

        c_line1 = Text("Course: B.Tech Linear Algebra and Calculus (M3) — Internal Assessment", font="Helvetica", font_size=14, color=COLOR_TEXT_PRIMARY).move_to(cred_box.get_top() + DOWN * 0.4)
        c_line2 = Text("Topic: Geometric & Algebraic Foundations of Linear Transformations", font="Helvetica", font_size=13, color=COLOR_TEXT_SECONDARY).next_to(c_line1, DOWN, buff=0.18)
        c_line3 = Text("Animation Engine: Manim Community Edition (Python)  •  Typesetting: Typst", font="Helvetica", font_size=13, color=COLOR_TEXT_SECONDARY).next_to(c_line2, DOWN, buff=0.18)
        c_line4 = Text("Visual & Pedagogical Style: Inspired by 3Blue1Brown (Grant Sanderson)", font="Helvetica", font_size=13, color=COLOR_TEXT_SECONDARY).next_to(c_line3, DOWN, buff=0.18)
        c_div = Line(cred_box.get_left() + RIGHT * 0.5, cred_box.get_right() + LEFT * 0.5, color="#475569", stroke_width=1).next_to(c_line4, DOWN, buff=0.22)
        c_line5 = Text("AI Assistance Disclosure: Developed with the assistance of Google Antigravity / Gemini AI", font="Helvetica", font_size=12, color="#94A3B8").next_to(c_div, DOWN, buff=0.22)
        c_line6 = Text("for visual architecture and code generation. All mathematical proofs and calculations verified independently.", font="Helvetica", font_size=11, color="#64748B").next_to(c_line5, DOWN, buff=0.1)

        cred_grp = VGroup(credits_title, cred_box, c_line1, c_line2, c_line3, c_line4, c_div, c_line5, c_line6)

        self.play(FadeIn(cred_grp, shift=UP * 0.25), run_time=1.8)
        self.wait(6.0)

        self.play(FadeOut(cred_grp), run_time=1.5)
        self.wait(0.5)
