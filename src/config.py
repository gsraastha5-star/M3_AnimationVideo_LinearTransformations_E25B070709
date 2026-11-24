"""
Configuration, constants, and styling for M3 Mathematical Animation Video.
Topic: Linear Transformations.
Follows 3Blue1Brown aesthetic: clean dark background, vibrant contrasting colors,
readable typography, and mathematically grounded visuals.
"""

import numpy as np
from manim import *

# -----------------------------------------------------------------------------
# Color Palette
# -----------------------------------------------------------------------------
COLOR_BG = "#0B0F19"             # Deep slate dark background
COLOR_GRID_BG = "#1E293B"        # Subtle background grid lines
COLOR_GRID_TRANS = "#334155"     # Transformed grid lines (accented)
COLOR_AXES = "#64748B"           # Axis lines

COLOR_E1 = "#2ECC71"             # Emerald Green for standard basis e1 / i_hat
COLOR_E2 = "#E74C3C"             # Ruby Red for standard basis e2 / j_hat
COLOR_V = "#F1C40F"              # Amber Gold for input vector v = (1, 1)
COLOR_AV = "#00E5FF"             # Electric Cyan for transformed vector Av = (3, 1)
COLOR_SUM = "#BB86FC"            # Lavender purple for sum / linear combinations

COLOR_TEXT_PRIMARY = "#FFFFFF"   # Bright white for titles and primary labels
COLOR_TEXT_SECONDARY = "#94A3B8" # Muted slate for subtitles and explanations
COLOR_TEXT_HIGHLIGHT = "#38BDF8" # Light sky blue for emphasis

# -----------------------------------------------------------------------------
# Mathematical Matrix & Vectors
# -----------------------------------------------------------------------------
# Transformation Matrix A = [[2, 1], [0, 1]]
MATRIX_A = np.array([[2.0, 1.0],
                     [0.0, 1.0]])

# Standard basis vectors
VEC_E1 = np.array([1.0, 0.0, 0.0])
VEC_E2 = np.array([0.0, 1.0, 0.0])

# Transformed basis vectors: A * e1 = [2, 0], A * e2 = [1, 1]
VEC_TE1 = np.array([2.0, 0.0, 0.0])
VEC_TE2 = np.array([1.0, 1.0, 0.0])

# Input vector v = [1, 1]
VEC_V = np.array([1.0, 1.0, 0.0])

# Transformed vector Av = [3, 1]
VEC_AV = np.array([3.0, 1.0, 0.0])

# Matrix 3x3 representation for Manim coordinate transformations
# Manim 3D vectors have [x, y, z]. Transformation affects x, y while z=0.
MATRIX_A_3D = np.array([[2.0, 1.0, 0.0],
                        [0.0, 1.0, 0.0],
                        [0.0, 0.0, 1.0]])

# -----------------------------------------------------------------------------
# Layout and Display Constants
# -----------------------------------------------------------------------------
FONT_HEADING = "Helvetica"
FONT_BODY = "Helvetica"

def get_styled_plane(x_range=(-6, 6, 1), y_range=(-4, 4, 1), x_length=12, y_length=8):
    """
    Returns a beautifully styled NumberPlane matching the 3B1B dark theme.
    """
    plane = NumberPlane(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        background_line_style={
            "stroke_color": COLOR_GRID_BG,
            "stroke_width": 1.5,
            "stroke_opacity": 0.55,
        },
        faded_line_style={
            "stroke_color": COLOR_GRID_BG,
            "stroke_width": 0.8,
            "stroke_opacity": 0.25,
        },
        axis_config={
            "stroke_color": COLOR_AXES,
            "stroke_width": 2.2,
            "include_numbers": False,
        }
    )
    return plane

def make_vector_arrow(plane, coords, color, stroke_width=4.5, buff=0):
    """
    Creates a styled Arrow vector originating from the plane's origin.
    """
    start_pt = plane.c2p(0, 0)
    end_pt = plane.c2p(coords[0], coords[1])
    arrow = Arrow(
        start=start_pt,
        end=end_pt,
        color=color,
        buff=buff,
        stroke_width=stroke_width,
        max_tip_length_to_length_ratio=0.25,
        max_stroke_width_to_length_ratio=5.0
    )
    return arrow
