"""
Scene 4: Step-by-Step Worked Example (2:20 - 3:45)
Detailed algebraic computation and geometric movement for vector v = [1, 1].
Formulas and text are properly sized, aligned, and beautifully formatted.
"""

from manim import *
import numpy as np
from src.config import (
    COLOR_BG, COLOR_E1, COLOR_E2, COLOR_V, COLOR_AV,
    COLOR_TEXT_PRIMARY, COLOR_TEXT_SECONDARY, COLOR_TEXT_HIGHLIGHT,
    get_styled_plane
)
from src.typst_math import typst_math


class Scene4WorkedExample(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # Scene Header
        header = Text(
            "WORKED EXAMPLE: TRANSFORMING VECTOR v = [1, 1]ᵀ",
            font="Helvetica",
            font_size=22,
            color=COLOR_TEXT_PRIMARY,
            weight=BOLD
        ).to_edge(UP, buff=0.3)
        header_bg = BackgroundRectangle(header, fill_color="#0B0F19", fill_opacity=0.92, buff=0.1)
        header_grp = VGroup(header_bg, header)
        self.add(header_grp)

        # Coordinate plane on the right half, algebra on the left half
        plane = get_styled_plane(x_range=(-1, 5, 1), y_range=(-1, 3.5, 1), x_length=6.0, y_length=4.4)
        plane.to_edge(RIGHT, buff=0.6).shift(DOWN * 0.15)
        origin = plane.c2p(0, 0)

        self.play(Create(plane, run_time=1.8))
        self.wait(1.0)

        # 1. Vector v = [1, 1] on plane
        v_arrow = Arrow(
            start=origin,
            end=plane.c2p(1, 1),
            color=COLOR_V,
            buff=0,
            stroke_width=4.5,
            max_tip_length_to_length_ratio=0.22
        )
        v_label = typst_math('v = vec(1, 1)', color="#F1C40F", height=0.32).next_to(plane.c2p(1, 1), UR, buff=0.12)

        # Basis components e1 and e2 making up v
        comp_e1 = Arrow(start=origin, end=plane.c2p(1, 0), color=COLOR_E1, buff=0, stroke_width=3.5, max_tip_length_to_length_ratio=0.22)
        comp_e2 = Arrow(start=plane.c2p(1, 0), end=plane.c2p(1, 1), color=COLOR_E2, buff=0, stroke_width=3.5, max_tip_length_to_length_ratio=0.22)
        decomp_txt = typst_math('v = 1 dot e_1 + 1 dot e_2', color="#FFFFFF", height=0.32).next_to(plane.c2p(1, 0), DOWN, buff=0.25)

        self.play(
            GrowArrow(comp_e1),
            GrowArrow(comp_e2),
            FadeIn(decomp_txt),
            run_time=2.0
        )
        self.wait(1.5)

        self.play(
            GrowArrow(v_arrow),
            FadeIn(v_label),
            FadeOut(comp_e1),
            FadeOut(comp_e2),
            FadeOut(decomp_txt),
            run_time=1.8
        )
        self.wait(2.0)

        # Projection lines showing (1, 1) coordinates
        proj_x = DashedLine(plane.c2p(1, 0), plane.c2p(1, 1), color="#64748B", stroke_width=1.5)
        proj_y = DashedLine(plane.c2p(0, 1), plane.c2p(1, 1), color="#64748B", stroke_width=1.5)
        self.play(Create(proj_x), Create(proj_y), run_time=1.2)
        self.wait(1.5)

        # 2. Algebraic Calculation Board on Left (properly proportioned)
        calc_box = RoundedRectangle(
            corner_radius=0.15,
            width=5.6,
            height=5.2,
            fill_color="#0F172A",
            fill_opacity=0.96,
            stroke_color="#334155",
            stroke_width=1.5
        ).to_edge(LEFT, buff=0.5).shift(DOWN * 0.15)

        calc_title = Text("Algebraic Matrix Multiplication", font="Helvetica", font_size=15, color=COLOR_TEXT_HIGHLIGHT, weight=BOLD).move_to(calc_box.get_top() + DOWN * 0.32)
        calc_div = Line(calc_box.get_left() + RIGHT * 0.3, calc_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(calc_title, DOWN, buff=0.12)

        self.play(FadeIn(calc_box), FadeIn(calc_title), Create(calc_div), run_time=1.2)
        self.wait(1.0)

        # Step 1: Definition of Product
        step1 = typst_math(
            'A v = mat(2, 1; 0, 1) vec(1, 1)',
            color="#FFFFFF",
            height=0.48
        ).next_to(calc_div, DOWN, buff=0.22)
        
        self.play(FadeIn(step1, shift=DOWN * 0.15), run_time=1.2)
        self.wait(3.5)

        # Step 2: Dot Products Expanded (Explicit multiplication)
        step2 = typst_math(
            '= vec(2(1) + 1(1), 0(1) + 1(1))',
            color="#38BDF8",
            height=0.48
        ).next_to(step1, DOWN, buff=0.22)

        step2_annot = Text("Row × Column Dot Products", font="Helvetica", font_size=11, color=COLOR_TEXT_SECONDARY).next_to(step2, DOWN, buff=0.08)

        self.play(FadeIn(step2, shift=DOWN * 0.15), FadeIn(step2_annot), run_time=1.5)
        self.wait(4.5)

        # Step 3: Arithmetic addition
        step3 = typst_math(
            '= vec(2 + 1, 0 + 1)',
            color="#FFFFFF",
            height=0.45
        ).next_to(step2_annot, DOWN, buff=0.22)

        self.play(FadeIn(step3, shift=DOWN * 0.15), run_time=1.2)
        self.wait(3.5)

        # Step 4: Final Vector Result
        step4 = typst_math(
            '= vec(3, 1)',
            color="#00E5FF",
            height=0.52
        ).next_to(step3, DOWN, buff=0.22)
        res_box = SurroundingRectangle(step4, color=COLOR_AV, buff=0.1, stroke_width=1.8)

        self.play(FadeIn(step4, shift=DOWN * 0.15), Create(res_box), run_time=1.5)
        self.wait(4.0)

        # 3. Geometric Transformation of the Vector
        trans_v_arrow = Arrow(
            start=origin,
            end=plane.c2p(3, 1),
            color=COLOR_AV,
            buff=0,
            stroke_width=4.5,
            max_tip_length_to_length_ratio=0.22
        )
        trans_v_label = typst_math('A v = vec(3, 1)', color="#00E5FF", height=0.32).next_to(plane.c2p(3, 1), UR, buff=0.12)

        trans_proj_x = DashedLine(plane.c2p(3, 0), plane.c2p(3, 1), color=COLOR_AV, stroke_width=1.5)
        trans_proj_y = DashedLine(plane.c2p(0, 1), plane.c2p(3, 1), color=COLOR_AV, stroke_width=1.5)

        self.play(
            FadeOut(proj_x),
            FadeOut(proj_y),
            Transform(v_arrow, trans_v_arrow),
            Transform(v_label, trans_v_label),
            Create(trans_proj_x),
            Create(trans_proj_y),
            run_time=4.0,
            rate_func=smooth
        )
        self.wait(3.5)

        # 4. Geometric Basis Vector Addition Breakdown
        te1_arrow = Arrow(
            start=origin,
            end=plane.c2p(2, 0),
            color=COLOR_E1,
            buff=0,
            stroke_width=3.8,
            max_tip_length_to_length_ratio=0.22
        )
        te1_txt = typst_math('1 dot T(e_1) = vec(2, 0)', color="#2ECC71", height=0.28).next_to(plane.c2p(2, 0), DOWN, buff=0.12)

        te2_tip_to_tail = Arrow(
            start=plane.c2p(2, 0),
            end=plane.c2p(3, 1),
            color=COLOR_E2,
            buff=0,
            stroke_width=3.8,
            max_tip_length_to_length_ratio=0.22
        )
        te2_txt = typst_math('1 dot T(e_2) = vec(1, 1)', color="#E74C3C", height=0.28).next_to(plane.c2p(2.5, 0.5), DR, buff=0.12)

        self.play(
            GrowArrow(te1_arrow),
            FadeIn(te1_txt),
            run_time=1.8
        )
        self.wait(2.0)

        self.play(
            GrowArrow(te2_tip_to_tail),
            FadeIn(te2_txt),
            run_time=1.8
        )
        self.wait(3.5)

        # Bottom synthesis banner
        syn_banner = Rectangle(width=11.5, height=0.65, fill_color="#0F172A", fill_opacity=0.96, stroke_color=COLOR_TEXT_HIGHLIGHT, stroke_width=1.2).to_edge(DOWN, buff=0.2)
        syn_text = Text(
            "Algebra meets Geometry:  T(v) = 1 · T(e₁) + 1 · T(e₂) = [2, 0]ᵀ + [1, 1]ᵀ = [3, 1]ᵀ",
            font="Helvetica",
            font_size=13,
            color=COLOR_TEXT_HIGHLIGHT,
            weight=BOLD
        ).move_to(syn_banner.get_center())
        syn_grp = VGroup(syn_banner, syn_text)

        self.play(FadeIn(syn_grp, shift=UP * 0.2), run_time=1.2)
        self.wait(5.0)

        # Transition out
        self.play(
            FadeOut(header_grp),
            FadeOut(plane),
            FadeOut(v_arrow),
            FadeOut(v_label),
            FadeOut(trans_proj_x),
            FadeOut(trans_proj_y),
            FadeOut(calc_box),
            FadeOut(calc_title),
            FadeOut(calc_div),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step2_annot),
            FadeOut(step3),
            FadeOut(step4),
            FadeOut(res_box),
            FadeOut(te1_arrow),
            FadeOut(te1_txt),
            FadeOut(te2_tip_to_tail),
            FadeOut(te2_txt),
            FadeOut(syn_grp),
            run_time=1.5
        )
        self.wait(0.5)
