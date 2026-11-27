"""
Scene 5: Geometric Interpretation (3:45 - 4:35)
Clear, well-proportioned typography, neat analytical boxes, and precise shear visualization.
"""

from manim import *
import numpy as np
from src.config import (
    COLOR_BG,
    COLOR_TEXT_PRIMARY, COLOR_TEXT_SECONDARY, COLOR_TEXT_HIGHLIGHT,
    get_styled_plane
)
from src.typst_math import typst_math


class Scene5GeometricInterpretation(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # Scene Header
        header = Text(
            "GEOMETRIC INTERPRETATION: THE SHEAR EFFECT",
            font="Helvetica",
            font_size=22,
            color=COLOR_TEXT_PRIMARY,
            weight=BOLD
        ).to_edge(UP, buff=0.3)
        header_bg = BackgroundRectangle(header, fill_color="#0B0F19", fill_opacity=0.92, buff=0.1)
        header_grp = VGroup(header_bg, header)
        self.add(header_grp)

        # Coordinate plane on the left, geometric analysis on the right
        plane = get_styled_plane(x_range=(-1, 6, 1), y_range=(-1, 3.5, 1), x_length=5.8, y_length=4.4)
        plane.to_edge(LEFT, buff=0.6).shift(DOWN * 0.15)
        origin = plane.c2p(0, 0)

        self.play(Create(plane, run_time=1.8))
        self.wait(1.0)

        # 1. Three reference points at different heights to demonstrate shear:
        p0 = Dot(plane.c2p(1, 0), color="#38BDF8", radius=0.08)
        p1 = Dot(plane.c2p(1, 1), color="#F1C40F", radius=0.08)
        p2 = Dot(plane.c2p(1, 2), color="#BB86FC", radius=0.08)

        l0 = typst_math("(1, 0)", color="#38BDF8", height=0.24).next_to(p0, DOWN, buff=0.1)
        l1 = typst_math("(1, 1)", color="#F1C40F", height=0.24).next_to(p1, UR, buff=0.1)
        l2 = typst_math("(1, 2)", color="#BB86FC", height=0.24).next_to(p2, UR, buff=0.1)

        # Vertical line connecting them (x = 1)
        vert_line = Line(plane.c2p(1, 0), plane.c2p(1, 2), color="#94A3B8", stroke_width=2.2)

        self.play(
            Create(vert_line),
            FadeIn(p0), FadeIn(l0),
            FadeIn(p1), FadeIn(l1),
            FadeIn(p2), FadeIn(l2),
            run_time=2.0
        )
        self.wait(1.2)

        # 2. Right Side: Analytical Panels
        info_box = RoundedRectangle(
            corner_radius=0.15,
            width=5.6,
            height=5.2,
            fill_color="#0F172A",
            fill_opacity=0.96,
            stroke_color="#334155",
            stroke_width=1.5
        ).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.15)

        info_title = Text("Coordinate Equations", font="Helvetica", font_size=15, color=COLOR_TEXT_HIGHLIGHT, weight=BOLD).move_to(info_box.get_top() + DOWN * 0.32)
        info_div = Line(info_box.get_left() + RIGHT * 0.3, info_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(info_title, DOWN, buff=0.12)

        self.play(FadeIn(info_box), FadeIn(info_title), Create(info_div), run_time=1.2)
        self.wait(0.8)

        # Equations:
        # x' = 2x + y
        # y' = y
        eq_sys = typst_math(
            'cases(x\' = 2x + 1y, y\' = 0x + 1y = y)',
            color="#FFFFFF",
            height=0.55
        ).next_to(info_div, DOWN, buff=0.2)
        
        self.play(FadeIn(eq_sys, shift=DOWN * 0.15), run_time=1.5)
        self.wait(2.5)

        # Observation 1: Vertical invariance
        obs1_box = RoundedRectangle(corner_radius=0.1, width=5.0, height=0.95, fill_color="#1E293B", fill_opacity=0.9, stroke_color="#2ECC71", stroke_width=1.2).next_to(eq_sys, DOWN, buff=0.2)
        obs1_t1 = Text("1. Vertical Invariance (y' = y)", font="Helvetica", font_size=12, color="#2ECC71", weight=BOLD).move_to(obs1_box.get_top() + DOWN * 0.22)
        obs1_t2 = Text("Horizontal lines stay at the exact same height.", font="Helvetica", font_size=11, color=COLOR_TEXT_SECONDARY).next_to(obs1_t1, DOWN, buff=0.08)
        obs1_grp = VGroup(obs1_box, obs1_t1, obs1_t2)

        self.play(FadeIn(obs1_grp, shift=RIGHT * 0.2), run_time=1.2)
        self.wait(2.0)

        # Observation 2: Horizontal Shear
        obs2_box = RoundedRectangle(corner_radius=0.1, width=5.0, height=1.05, fill_color="#1E293B", fill_opacity=0.9, stroke_color="#F1C40F", stroke_width=1.2).next_to(obs1_box, DOWN, buff=0.16)
        obs2_t1 = Text("2. Horizontal Shear & Stretch", font="Helvetica", font_size=12, color="#F1C40F", weight=BOLD).move_to(obs2_box.get_top() + DOWN * 0.22)
        obs2_t2 = Text("x is scaled by 2, and sheared right by y.\nHigher points shift further to the right!", font="Helvetica", font_size=10.5, color=COLOR_TEXT_SECONDARY, line_spacing=1.1).next_to(obs2_t1, DOWN, buff=0.06)
        obs2_grp = VGroup(obs2_box, obs2_t1, obs2_t2)

        self.play(FadeIn(obs2_grp, shift=RIGHT * 0.2), run_time=1.2)
        self.wait(2.3)

        # 3. Animate the shear on the plane:
        tp0 = Dot(plane.c2p(2, 0), color="#38BDF8", radius=0.08)
        tp1 = Dot(plane.c2p(3, 1), color="#F1C40F", radius=0.08)
        tp2 = Dot(plane.c2p(4, 2), color="#BB86FC", radius=0.08)

        tl0 = typst_math("(2, 0)", color="#38BDF8", height=0.24).next_to(tp0, DOWN, buff=0.1)
        tl1 = typst_math("(3, 1)", color="#F1C40F", height=0.24).next_to(tp1, UR, buff=0.1)
        tl2 = typst_math("(4, 2)", color="#BB86FC", height=0.24).next_to(tp2, UR, buff=0.1)

        # Transformed slanted line
        trans_line = Line(plane.c2p(2, 0), plane.c2p(4, 2), color="#E2E8F0", stroke_width=2.2)

        transform_matrix = np.array([[2.0, 1.0, 0.0],
                                     [0.0, 1.0, 0.0],
                                     [0.0, 0.0, 1.0]])

        self.play(
            plane.animate.apply_matrix(transform_matrix),
            Transform(vert_line, trans_line),
            Transform(p0, tp0), Transform(l0, tl0),
            Transform(p1, tp1), Transform(l1, tl1),
            Transform(p2, tp2), Transform(l2, tl2),
            run_time=4.5,
            rate_func=smooth
        )
        self.wait(3.0)

        # 4. Summary Invariant Callout
        inv_banner = Rectangle(width=11.5, height=0.65, fill_color="#0F172A", fill_opacity=0.96, stroke_color=COLOR_TEXT_HIGHLIGHT, stroke_width=1.2).to_edge(DOWN, buff=0.2)
        inv_text = Text(
            "Linearity Invariants:  Origin stays at (0,0)  •  Straight lines stay straight  •  Areas double: det(A) = 2",
            font="Helvetica",
            font_size=12.5,
            color=COLOR_TEXT_HIGHLIGHT,
            weight=BOLD
        ).move_to(inv_banner.get_center())
        inv_grp = VGroup(inv_banner, inv_text)

        self.play(FadeIn(inv_grp, shift=UP * 0.2), run_time=1.2)
        self.wait(3.6)

        # Transition out
        self.play(
            FadeOut(header_grp),
            FadeOut(plane),
            FadeOut(vert_line),
            FadeOut(p0), FadeOut(l0),
            FadeOut(p1), FadeOut(l1),
            FadeOut(p2), FadeOut(l2),
            FadeOut(info_box),
            FadeOut(info_title),
            FadeOut(info_div),
            FadeOut(eq_sys),
            FadeOut(obs1_grp),
            FadeOut(obs2_grp),
            FadeOut(inv_grp),
            run_time=1.5
        )
        self.wait(0.5)
