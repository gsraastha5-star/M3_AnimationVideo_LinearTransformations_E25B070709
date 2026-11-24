"""
Scene 3: Visual Intuition (1:20 - 2:20)
Clean visual hierarchy, properly scaled basis vectors, labels and callouts.
"""

from manim import *
import numpy as np
from src.config import (
    COLOR_BG, COLOR_E1, COLOR_E2,
    COLOR_TEXT_PRIMARY, COLOR_TEXT_SECONDARY, COLOR_TEXT_HIGHLIGHT,
    get_styled_plane
)
from src.typst_math import typst_math


class Scene3VisualIntuition(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # Scene Header Banner
        header = Text(
            "VISUAL INTUITION: BASIS VECTORS IN ACTION",
            font="Helvetica",
            font_size=22,
            color=COLOR_TEXT_PRIMARY,
            weight=BOLD
        ).to_edge(UP, buff=0.3)
        header_bg = BackgroundRectangle(header, fill_color="#0B0F19", fill_opacity=0.92, buff=0.1)
        header_grp = VGroup(header_bg, header)
        self.add(header_grp)

        # 1. Coordinate Grid Setup
        orig_plane = get_styled_plane(x_range=(-6, 6, 1), y_range=(-3.5, 3.5, 1))
        orig_plane.set_opacity(0.25)

        grid = get_styled_plane(x_range=(-6, 6, 1), y_range=(-3.5, 3.5, 1))
        
        self.play(Create(orig_plane, run_time=1.8), Create(grid, run_time=1.8), lag_ratio=0.05)
        self.wait(1.0)

        # 2. Standard Basis Vectors e1 and e2
        origin = grid.c2p(0, 0)
        
        # e1: (1, 0) in green
        e1_arrow = Arrow(
            start=origin,
            end=grid.c2p(1, 0),
            color=COLOR_E1,
            buff=0,
            stroke_width=4.5,
            max_tip_length_to_length_ratio=0.22
        )
        e1_label = typst_math('e_1 = vec(1, 0)', color="#2ECC71", height=0.35).next_to(grid.c2p(1, 0), DOWN, buff=0.15)

        # e2: (0, 1) in red
        e2_arrow = Arrow(
            start=origin,
            end=grid.c2p(0, 1),
            color=COLOR_E2,
            buff=0,
            stroke_width=4.5,
            max_tip_length_to_length_ratio=0.22
        )
        e2_label = typst_math('e_2 = vec(0, 1)', color="#E74C3C", height=0.35).next_to(grid.c2p(0, 1), LEFT, buff=0.15)

        # Unit Square (area = 1)
        unit_square = Polygon(
            grid.c2p(0, 0),
            grid.c2p(1, 0),
            grid.c2p(1, 1),
            grid.c2p(0, 1),
            fill_color="#38BDF8",
            fill_opacity=0.22,
            stroke_color="#38BDF8",
            stroke_width=1.8
        )
        unit_square_label = Text("Unit Square\nArea = 1", font="Helvetica", font_size=11, color="#38BDF8").move_to(grid.c2p(0.5, 0.5))

        self.play(
            GrowArrow(e1_arrow),
            FadeIn(e1_label),
            run_time=1.5
        )
        self.wait(1.0)
        
        self.play(
            GrowArrow(e2_arrow),
            FadeIn(e2_label),
            FadeIn(unit_square),
            FadeIn(unit_square_label),
            run_time=1.8
        )
        self.wait(2.5)

        # 3. Introduce Matrix A with Color-Coded Columns
        matrix_card = RoundedRectangle(
            corner_radius=0.12,
            width=5.0,
            height=2.3,
            fill_color="#0F172A",
            fill_opacity=0.96,
            stroke_color="#64748B",
            stroke_width=1.2
        ).to_corner(UL, buff=0.55)

        matrix_title = Text("Transformation Matrix A", font="Helvetica", font_size=13, color=COLOR_TEXT_PRIMARY, weight=BOLD).move_to(matrix_card.get_top() + DOWN * 0.25)
        
        matrix_eq = typst_math(
            'A = mat(#text(fill: rgb("#2ECC71"))[2], #text(fill: rgb("#E74C3C"))[1]; #text(fill: rgb("#2ECC71"))[0], #text(fill: rgb("#E74C3C"))[1])',
            color="#FFFFFF",
            height=0.52
        ).next_to(matrix_title, DOWN, buff=0.15)

        col_expl = typst_math(
            'mat(#text(fill: rgb("#2ECC71"))[T(e_1)], #text(fill: rgb("#E74C3C"))[T(e_2)]) = mat(#text(fill: rgb("#2ECC71"))[vec(2, 0)], #text(fill: rgb("#E74C3C"))[vec(1, 1)])',
            color="#FFFFFF",
            height=0.45
        ).next_to(matrix_eq, DOWN, buff=0.15)

        matrix_group = VGroup(matrix_card, matrix_title, matrix_eq, col_expl)
        self.play(FadeIn(matrix_group, shift=RIGHT * 0.3), run_time=1.5)
        self.wait(3.5)

        # 4. Highlight Columns
        e1_focus = SurroundingRectangle(e1_arrow, color=COLOR_E1, buff=0.12)
        self.play(Create(e1_focus), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(e1_focus), run_time=0.8)

        e2_focus = SurroundingRectangle(e2_arrow, color=COLOR_E2, buff=0.12)
        self.play(Create(e2_focus), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(e2_focus), run_time=0.8)

        # 5. Synchronized Grid & Basis Vector Transformation
        te1_arrow = Arrow(
            start=origin,
            end=grid.c2p(2, 0),
            color=COLOR_E1,
            buff=0,
            stroke_width=4.5,
            max_tip_length_to_length_ratio=0.22
        )
        te1_label = typst_math('T(e_1) = vec(2, 0)', color="#2ECC71", height=0.35).next_to(grid.c2p(2, 0), DOWN, buff=0.15)

        te2_arrow = Arrow(
            start=origin,
            end=grid.c2p(1, 1),
            color=COLOR_E2,
            buff=0,
            stroke_width=4.5,
            max_tip_length_to_length_ratio=0.22
        )
        te2_label = typst_math('T(e_2) = vec(1, 1)', color="#E74C3C", height=0.35).next_to(grid.c2p(1, 1), UP, buff=0.15)

        # Transformed Parallelogram
        trans_parallelogram = Polygon(
            grid.c2p(0, 0),
            grid.c2p(2, 0),
            grid.c2p(3, 1),
            grid.c2p(1, 1),
            fill_color="#BB86FC",
            fill_opacity=0.28,
            stroke_color="#BB86FC",
            stroke_width=2.0
        )
        trans_area_label = Text("Parallelogram\nArea = 2", font="Helvetica", font_size=11, color="#BB86FC").move_to(grid.c2p(1.5, 0.5))

        transform_matrix = np.array([[2.0, 1.0, 0.0],
                                     [0.0, 1.0, 0.0],
                                     [0.0, 0.0, 1.0]])

        # The transformation animation
        self.play(
            grid.animate.apply_matrix(transform_matrix),
            Transform(e1_arrow, te1_arrow),
            Transform(e1_label, te1_label),
            Transform(e2_arrow, te2_arrow),
            Transform(e2_label, te2_label),
            Transform(unit_square, trans_parallelogram),
            Transform(unit_square_label, trans_area_label),
            run_time=5.0,
            rate_func=smooth
        )
        self.wait(4.0)

        # 6. Explanatory Callout Banner
        callout_box = RoundedRectangle(
            corner_radius=0.12,
            width=11.2,
            height=1.1,
            fill_color="#0F172A",
            fill_opacity=0.96,
            stroke_color=COLOR_TEXT_HIGHLIGHT,
            stroke_width=1.2
        ).to_edge(DOWN, buff=0.25)

        callout_line1 = Text(
            "THE FOUNDATIONAL PRINCIPLE OF LINEAR ALGEBRA",
            font="Helvetica",
            font_size=14,
            color=COLOR_TEXT_HIGHLIGHT,
            weight=BOLD
        ).move_to(callout_box.get_top() + DOWN * 0.25)

        callout_line2 = Text(
            "The columns of matrix A describe exactly where basis vectors e₁ and e₂ move.\nTheir destination completely determines how all other vectors in the plane transform!",
            font="Helvetica",
            font_size=13,
            color=COLOR_TEXT_PRIMARY,
            line_spacing=1.15
        ).next_to(callout_line1, DOWN, buff=0.1)

        callout_group = VGroup(callout_box, callout_line1, callout_line2)
        self.play(FadeIn(callout_group, shift=UP * 0.2), run_time=1.5)
        self.wait(5.0)

        # Transition out
        self.play(
            FadeOut(header_grp),
            FadeOut(orig_plane),
            FadeOut(grid),
            FadeOut(e1_arrow),
            FadeOut(e1_label),
            FadeOut(e2_arrow),
            FadeOut(e2_label),
            FadeOut(unit_square),
            FadeOut(unit_square_label),
            FadeOut(matrix_group),
            FadeOut(callout_group),
            run_time=1.5
        )
        self.wait(0.5)
