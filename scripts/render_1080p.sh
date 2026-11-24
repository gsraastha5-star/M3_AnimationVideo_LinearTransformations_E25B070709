#!/usr/bin/env bash
# Production High-Definition Render (1080p, 60fps, 16:9)
set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"
PYTHON_BIN="$PROJECT_DIR/.venv/bin/python"

if [ ! -f "$PYTHON_BIN" ]; then
    echo "Virtual environment not found! Please create .venv first."
    exit 1
fi

mkdir -p "$PROJECT_DIR/output"
mkdir -p "$PROJECT_DIR/media/videos/1080p60"

echo "=========================================================="
echo "Rendering High-Quality 1080p Scenes (1920x1080 @ 60fps)..."
echo "=========================================================="

echo "Rendering Scene 1: Hook and Introduction..."
$PYTHON_BIN -m manim -qh src/scene1_hook.py Scene1Hook -o scene1_1080p.mp4

echo "Rendering Scene 2: Understanding the Concept..."
$PYTHON_BIN -m manim -qh src/scene2_concept.py Scene2Concept -o scene2_1080p.mp4

echo "Rendering Scene 3: Visual Intuition..."
$PYTHON_BIN -m manim -qh src/scene3_visual_intuition.py Scene3VisualIntuition -o scene3_1080p.mp4

echo "Rendering Scene 4: Step-by-Step Worked Example..."
$PYTHON_BIN -m manim -qh src/scene4_worked_example.py Scene4WorkedExample -o scene4_1080p.mp4

echo "Rendering Scene 5: Geometric Interpretation..."
$PYTHON_BIN -m manim -qh src/scene5_geometric_interpretation.py Scene5GeometricInterpretation -o scene5_1080p.mp4

echo "Rendering Scene 6: Summary and Credits..."
$PYTHON_BIN -m manim -qh src/scene6_summary.py Scene6Summary -o scene6_1080p.mp4

echo "=========================================================="
echo "Concatenating scenes into final 1080p master video..."
echo "=========================================================="

bash "$PROJECT_DIR/scripts/concatenate_scenes.sh"

echo "=========================================================="
echo "FINAL 1080p DELIVERABLE READY:"
echo "output/final_linear_transformations_1080p.mp4"
echo "=========================================================="
