"""
Scene 1: Hook and Introduction (0:00 - 0:35)
Clean, well-proportioned typography and vector movement.
"""

from manim import *
import numpy as np
from src.config import (
    COLOR_BG, COLOR_V, COLOR_TEXT_PRIMARY,
    COLOR_TEXT_SECONDARY, COLOR_TEXT_HIGHLIGHT, get_styled_plane
)
from src.typst_math import typst_math


class Scene1Hook(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # 1. Coordinate plane
        plane = get_styled_plane(x_range=(-7, 7, 1), y_range=(-4, 4, 1))
        self.play(Create(plane, run_time=2.0, lag_ratio=0.1))
        self.wait(0.5)

        # 2. Moving Vector on the plane
        origin_pt = plane.c2p(0, 0)
        vx = ValueTracker(1.0)
        vy = ValueTracker(1.0)

        arrow = always_redraw(
            lambda: Arrow(
                start=origin_pt,
                end=plane.c2p(vx.get_value(), vy.get_value()),
                color=COLOR_V,
                buff=0,
                stroke_width=4.5,
                max_tip_length_to_length_ratio=0.22
            )
        )
        
        # Coordinate label tracking vector tip with clean small font
        coord_label = always_redraw(
            lambda: Text(
                f"v = [{vx.get_value():.1f}, {vy.get_value():.1f}]ᵀ",
                font="Helvetica",
                font_size=15,
                color=COLOR_V,
                weight=BOLD
            ).next_to(plane.c2p(vx.get_value(), vy.get_value()), UR, buff=0.12)
        )

        self.play(GrowArrow(arrow), FadeIn(coord_label), run_time=1.5)
        self.wait(1.0)

        # Vector moving across the plane to demonstrate coordinates
        self.play(
            vx.animate.set_value(2.5),
            vy.animate.set_value(1.5),
            run_time=2.0,
            rate_func=smooth
        )
        self.wait(0.5)
        self.play(
            vx.animate.set_value(-1.5),
            vy.animate.set_value(2.0),
            run_time=2.0,
            rate_func=smooth
        )
        self.wait(0.5)
        self.play(
            vx.animate.set_value(1.0),
            vy.animate.set_value(1.0),
            run_time=1.5,
            rate_func=smooth
        )
        self.wait(1.0)

        # 3. Provocative Question Banner (properly sized and formatted)
        q_banner = Rectangle(
            width=11.2,
            height=1.2,
            fill_color="#0F172A",
            fill_opacity=0.94,
            stroke_color=COLOR_TEXT_HIGHLIGHT,
            stroke_width=1.5
        ).to_edge(UP, buff=0.35)

        q_text1 = Text(
            "What happens to vectors and coordinate grids",
            font="Helvetica",
            font_size=20,
            color=COLOR_TEXT_PRIMARY,
            weight=BOLD
        ).move_to(q_banner.get_center() + UP * 0.18)

        q_text2 = Text(
            "when we multiply them by a simple 2 × 2 matrix?",
            font="Helvetica",
            font_size=17,
            color=COLOR_TEXT_HIGHLIGHT
        ).move_to(q_banner.get_center() + DOWN * 0.18)

        q_group = VGroup(q_banner, q_text1, q_text2)
        self.play(FadeIn(q_group, shift=DOWN * 0.3), run_time=1.2)
        self.wait(2.5)

        # 4. Teaser: Matrix preview & subtle grid flex
        matrix_teaser = typst_math(
            'A = mat(2, 1; 0, 1)',
            color="#38BDF8",
            size="22pt",
            height=0.55
        ).next_to(q_banner, DOWN, buff=0.25)
        matrix_bg = BackgroundRectangle(matrix_teaser, fill_color="#0B0F19", fill_opacity=0.9, buff=0.15)
        m_group = VGroup(matrix_bg, matrix_teaser)

        self.play(FadeIn(m_group, shift=UP * 0.2), run_time=1.0)
        self.wait(1.5)

        # Subtle shear pulse teaser
        shear_matrix = np.array([[1.4, 0.4, 0.0],
                                 [0.0, 1.0, 0.0],
                                 [0.0, 0.0, 1.0]])
        self.play(
            plane.animate.apply_matrix(shear_matrix),
            vx.animate.set_value(1.8),
            vy.animate.set_value(1.0),
            run_time=2.0,
            rate_func=there_and_back
        )
        self.wait(1.0)

        # 5. Clear teaser and display Main Title Card
        self.play(
            FadeOut(q_group),
            FadeOut(m_group),
            FadeOut(arrow),
            FadeOut(coord_label),
            plane.animate.set_opacity(0.12),
            run_time=1.5
        )

        title = Text(
            "LINEAR TRANSFORMATIONS",
            font="Helvetica",
            font_size=38,
            color=COLOR_TEXT_PRIMARY,
            weight=BOLD
        ).shift(UP * 0.7)

        underline = Line(
            start=title.get_left() + DOWN * 0.08,
            end=title.get_right() + DOWN * 0.08,
            color=COLOR_TEXT_HIGHLIGHT,
            stroke_width=3.0
        )

        subtitle = Text(
            "Understanding how matrices reshape space",
            font="Helvetica",
            font_size=20,
            color=COLOR_TEXT_SECONDARY
        ).next_to(underline, DOWN, buff=0.3)

        badge_box = RoundedRectangle(corner_radius=0.15, width=4.6, height=0.5, fill_color="#1E293B", fill_opacity=0.9, stroke_color="#334155", stroke_width=1)
        badge_txt = Text("B.Tech M3: Linear Algebra & Calculus", font="Helvetica", font_size=13, color="#38BDF8")
        badge = VGroup(badge_box, badge_txt).next_to(subtitle, DOWN, buff=0.45)
        badge_txt.move_to(badge_box.get_center())

        self.play(
            Write(title),
            Create(underline),
            FadeIn(subtitle, shift=UP * 0.2),
            FadeIn(badge, shift=UP * 0.2),
            run_time=2.2
        )
        self.wait(3.5)

        # Transition out
        self.play(
            FadeOut(title),
            FadeOut(underline),
            FadeOut(subtitle),
            FadeOut(badge),
            FadeOut(plane),
            run_time=1.5
        )
        self.wait(0.5)
