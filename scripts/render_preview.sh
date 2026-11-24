#!/usr/bin/env bash
# Render preview animations (480p, 15fps) for rapid iteration and testing.
set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"
PYTHON_BIN="$PROJECT_DIR/.venv/bin/python"

if [ ! -f "$PYTHON_BIN" ]; then
    echo "Virtual environment not found! Please run setup first."
    exit 1
fi

echo "=========================================================="
echo "Rendering Preview (480p, 15fps)..."
echo "=========================================================="

mkdir -p "$PROJECT_DIR/output"

$PYTHON_BIN -m manim -ql --frame_rate 15 src/full_video.py FullLinearTransformationsVideo -o preview_full.mp4
mv media/videos/full_video/480p15/preview_full.mp4 output/preview_full.mp4

echo "Preview ready at: output/preview_full.mp4"
