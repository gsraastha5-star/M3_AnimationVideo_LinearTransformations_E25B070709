#!/usr/bin/env bash
# Concatenate individual 1080p scene renders into a single seamless movie.
set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"

mkdir -p "$PROJECT_DIR/output"

S1=$(find "$PROJECT_DIR/media/videos" -name "scene1_1080p.mp4" | head -n 1)
S2=$(find "$PROJECT_DIR/media/videos" -name "scene2_1080p.mp4" | head -n 1)
S3=$(find "$PROJECT_DIR/media/videos" -name "scene3_1080p.mp4" | head -n 1)
S4=$(find "$PROJECT_DIR/media/videos" -name "scene4_1080p.mp4" | head -n 1)
S5=$(find "$PROJECT_DIR/media/videos" -name "scene5_1080p.mp4" | head -n 1)
S6=$(find "$PROJECT_DIR/media/videos" -name "scene6_1080p.mp4" | head -n 1)

if [ -z "$S1" ] || [ -z "$S2" ] || [ -z "$S3" ] || [ -z "$S4" ] || [ -z "$S5" ] || [ -z "$S6" ]; then
    echo "Error: One or more 1080p scene videos not found. Make sure all 6 scenes rendered."
    exit 1
fi

echo "Scene files detected:"
echo "1: $S1"
echo "2: $S2"
echo "3: $S3"
echo "4: $S4"
echo "5: $S5"
echo "6: $S6"

CONCAT_LIST="$PROJECT_DIR/media/concat_list.txt"
cat << EOF > "$CONCAT_LIST"
file '$S1'
file '$S2'
file '$S3'
file '$S4'
file '$S5'
file '$S6'
EOF

OUTPUT_FINAL="$PROJECT_DIR/output/final_linear_transformations_1080p.mp4"

ffmpeg -y -f concat -safe 0 -i "$CONCAT_LIST" -c copy "$OUTPUT_FINAL"

echo "Successfully merged 6 scenes into: $OUTPUT_FINAL"
