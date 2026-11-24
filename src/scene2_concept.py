"""
Scene 2: Understanding the Concept (0:35 - 1:20)
Clean, well-spaced cards and properly sized equations.
"""

from manim import *
from src.config import (
    COLOR_BG, COLOR_E1, COLOR_V, COLOR_TEXT_PRIMARY,
    COLOR_TEXT_SECONDARY, COLOR_TEXT_HIGHLIGHT
)
from src.typst_math import typst_math


class Scene2Concept(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # Scene Header
        header = Text(
            "THE CORE CONCEPTS",
            font="Helvetica",
            font_size=28,
            color=COLOR_TEXT_PRIMARY,
            weight=BOLD
        ).to_edge(UP, buff=0.4)

        sub_header = Text(
            "What is a vector, a matrix, and a linear transformation?",
            font="Helvetica",
            font_size=16,
            color=COLOR_TEXT_SECONDARY
        ).next_to(header, DOWN, buff=0.12)

        self.play(FadeIn(header, shift=DOWN * 0.2), FadeIn(sub_header, shift=DOWN * 0.15), run_time=1.2)
        self.wait(1.0)

        # -------------------------------------------------------------
        # Part 1: Three Concept Cards
        # -------------------------------------------------------------
        card_w, card_h = 3.6, 2.3
        y_pos = 0.65

        # Card 1: Vector
        c1_box = RoundedRectangle(corner_radius=0.15, width=card_w, height=card_h, fill_color="#1E293B", fill_opacity=0.9, stroke_color="#334155", stroke_width=1.5).move_to(LEFT * 4.0 + UP * y_pos)
        c1_title = Text("1. Vector", font="Helvetica", font_size=17, color=COLOR_V, weight=BOLD).move_to(c1_box.get_top() + DOWN * 0.3)
        c1_math = typst_math("v = vec(x, y)", color="#F1C40F", height=0.45).next_to(c1_title, DOWN, buff=0.2)
        c1_desc = Text("Magnitude & direction\nA point in 2D space", font="Helvetica", font_size=12, color=COLOR_TEXT_SECONDARY, line_spacing=1.2).next_to(c1_math, DOWN, buff=0.2)
        card1 = VGroup(c1_box, c1_title, c1_math, c1_desc)

        # Card 2: Matrix
        c2_box = RoundedRectangle(corner_radius=0.15, width=card_w, height=card_h, fill_color="#1E293B", fill_opacity=0.9, stroke_color="#334155", stroke_width=1.5).move_to(UP * y_pos)
        c2_title = Text("2. Matrix", font="Helvetica", font_size=17, color=COLOR_TEXT_HIGHLIGHT, weight=BOLD).move_to(c2_box.get_top() + DOWN * 0.3)
        c2_math = typst_math("A = mat(a, b; c, d)", color="#38BDF8", height=0.5).next_to(c2_title, DOWN, buff=0.2)
        c2_desc = Text("A geometric machine\nTransforms entire space", font="Helvetica", font_size=12, color=COLOR_TEXT_SECONDARY, line_spacing=1.2).next_to(c2_math, DOWN, buff=0.2)
        card2 = VGroup(c2_box, c2_title, c2_math, c2_desc)

        # Card 3: Transformation
        c3_box = RoundedRectangle(corner_radius=0.15, width=card_w, height=card_h, fill_color="#1E293B", fill_opacity=0.9, stroke_color="#334155", stroke_width=1.5).move_to(RIGHT * 4.0 + UP * y_pos)
        c3_title = Text("3. Linear Map", font="Helvetica", font_size=17, color=COLOR_E1, weight=BOLD).move_to(c3_box.get_top() + DOWN * 0.3)
        c3_math = typst_math("T: RR^2 -> RR^2", color="#2ECC71", height=0.45).next_to(c3_title, DOWN, buff=0.2)
        c3_desc = Text("Origin stays fixed\nLines remain straight", font="Helvetica", font_size=12, color=COLOR_TEXT_SECONDARY, line_spacing=1.2).next_to(c3_math, DOWN, buff=0.2)
        card3 = VGroup(c3_box, c3_title, c3_math, c3_desc)

        self.play(
            FadeIn(card1, shift=UP * 0.25),
            FadeIn(card2, shift=UP * 0.25),
            FadeIn(card3, shift=UP * 0.25),
            run_time=1.8,
            lag_ratio=0.25
        )
        self.wait(4.0)

        # -------------------------------------------------------------
        # Part 2: Two Linearity Properties
        # -------------------------------------------------------------
        self.play(
            FadeOut(card1, shift=UP * 0.15),
            FadeOut(card2, shift=UP * 0.15),
            FadeOut(card3, shift=UP * 0.15),
            FadeOut(sub_header),
            run_time=1.0
        )

        prop_header = Text(
            "THE TWO DEFINING PROPERTIES OF LINEARITY",
            font="Helvetica",
            font_size=18,
            color=COLOR_TEXT_HIGHLIGHT,
            weight=BOLD
        ).next_to(header, DOWN, buff=0.18)
        self.play(FadeIn(prop_header), run_time=0.8)
        self.wait(1.0)

        # Property 1 Container (Additivity)
        p1_box = RoundedRectangle(corner_radius=0.12, width=10.5, height=1.65, fill_color="#1E293B", fill_opacity=0.92, stroke_color="#2ECC71", stroke_width=1.5).move_to(UP * 0.8)
        p1_label = Text("Property 1: Additivity (Superposition)", font="Helvetica", font_size=15, color="#2ECC71", weight=BOLD).move_to(p1_box.get_top() + DOWN * 0.28)
        p1_eq = typst_math("T(u + v) = T(u) + T(v)", color="#FFFFFF", height=0.55).next_to(p1_label, DOWN, buff=0.14)
        p1_note = Text("Transforming a vector sum equals the sum of each transformed vector.", font="Helvetica", font_size=12, color=COLOR_TEXT_SECONDARY).next_to(p1_eq, DOWN, buff=0.1)
        p1_group = VGroup(p1_box, p1_label, p1_eq, p1_note)

        # Property 2 Container (Homogeneity)
        p2_box = RoundedRectangle(corner_radius=0.12, width=10.5, height=1.65, fill_color="#1E293B", fill_opacity=0.92, stroke_color="#F1C40F", stroke_width=1.5).move_to(DOWN * 1.15)
        p2_label = Text("Property 2: Homogeneity (Scalar Scaling)", font="Helvetica", font_size=15, color="#F1C40F", weight=BOLD).move_to(p2_box.get_top() + DOWN * 0.28)
        p2_eq = typst_math("T(c v) = c T(v)", color="#FFFFFF", height=0.55).next_to(p2_label, DOWN, buff=0.14)
        p2_note = Text("Scaling a vector before or after the transformation gives the identical result.", font="Helvetica", font_size=12, color=COLOR_TEXT_SECONDARY).next_to(p2_eq, DOWN, buff=0.1)
        p2_group = VGroup(p2_box, p2_label, p2_eq, p2_note)

        self.play(FadeIn(p1_group, shift=RIGHT * 0.3), run_time=1.4)
        self.wait(4.5)

        self.play(FadeIn(p2_group, shift=RIGHT * 0.3), run_time=1.4)
        self.wait(4.5)

        # Bottom punchline banner
        takeaway_bg = Rectangle(width=11.2, height=0.65, fill_color="#0F172A", fill_opacity=0.95, stroke_color="#64748B", stroke_width=1).to_edge(DOWN, buff=0.25)
        takeaway_txt = Text(
            "Consequence: If we track where standard basis vectors go, we know where EVERY vector goes!",
            font="Helvetica",
            font_size=14,
            color="#38BDF8",
            weight=BOLD
        ).move_to(takeaway_bg.get_center())
        takeaway_group = VGroup(takeaway_bg, takeaway_txt)

        self.play(FadeIn(takeaway_group, shift=UP * 0.25), run_time=1.2)
        self.wait(5.0)

        # Transition out
        self.play(
            FadeOut(header),
            FadeOut(prop_header),
            FadeOut(p1_group),
            FadeOut(p2_group),
            FadeOut(takeaway_group),
            run_time=1.5
        )
        self.wait(0.5)
