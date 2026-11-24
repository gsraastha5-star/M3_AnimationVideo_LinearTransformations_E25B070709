"""
Typst mathematical equation compiler for Manim.
Renders clean vector SVG mathematical equations with proper scaling,
guaranteeing that formulas are crisp, properly proportioned, and never overlap.
"""

import hashlib
import os
import subprocess
from manim import SVGMobject

CACHE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "media", "typst_cache"))
TYPST_BIN = "/opt/homebrew/bin/typst" if os.path.exists("/opt/homebrew/bin/typst") else "typst"

def typst_math(
    expr: str,
    color: str = "#FFFFFF",
    size: str = "24pt",
    preamble: str = "",
    height: float = 0.45,
    width: float = None
) -> SVGMobject:
    """
    Compiles a Typst math expression to SVG and returns a Manim SVGMobject.
    Properly scales the mobject to avoid Manim's default oversized height=2.0.
    """
    os.makedirs(CACHE_DIR, exist_ok=True)
    
    cache_key = hashlib.sha256((expr + color + size + preamble).encode("utf-8")).hexdigest()
    typ_path = os.path.join(CACHE_DIR, f"eq_{cache_key}.typ")
    svg_path = os.path.join(CACHE_DIR, f"eq_{cache_key}.svg")
    
    if not os.path.exists(svg_path):
        source_code = f"""#set page(width: auto, height: auto, margin: 0.15em, fill: none)
#set text(fill: rgb("{color}"), size: {size}, font: "New Computer Modern")
{preamble}
$ {expr} $
"""
        with open(typ_path, "w", encoding="utf-8") as f:
            f.write(source_code)
            
        try:
            subprocess.run([TYPST_BIN, "compile", typ_path, svg_path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as err:
            print(f"Typst compilation error for expr: {expr}")
            print(err.stderr.decode("utf-8"))
            raise err

    svg_mob = SVGMobject(svg_path)
    
    # Scale to proper proportions
    if height is not None:
        svg_mob.set_height(height)
    if width is not None:
        if svg_mob.width > width:
            svg_mob.set_width(width)
            
    return svg_mob
