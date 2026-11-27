#!/usr/bin/env bash
# Script to merge your real human voice recording with the silent 1080p video.
# Usage: bash scripts/add_user_voiceover.sh /path/to/your_recording.mp3 (or .m4a / .wav)
set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"
export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"

AUDIO_INPUT="$1"

if [ -z "$AUDIO_INPUT" ]; then
    # Auto-detect if audio file is placed in math_video folder
    for ext in mp3 m4a wav aac; do
        found=$(find . -maxdepth 2 -iname "*voice*" -name "*.$ext" ! -path "./media/*" | head -n 1)
        if [ -n "$found" ]; then
            AUDIO_INPUT="$found"
            break
        fi
    done
fi

if [ -z "$AUDIO_INPUT" ] || [ ! -f "$AUDIO_INPUT" ]; then
    echo "Usage: bash scripts/add_user_voiceover.sh <path_to_audio_file>"
    echo "Example: bash scripts/add_user_voiceover.sh ~/Desktop/my_recording.m4a"
    exit 1
fi

echo "=========================================================="
echo "Replacing AI audio with your voice recording: $AUDIO_INPUT"
echo "=========================================================="

VIDEO_SILENT="$PROJECT_DIR/output/final_linear_transformations_silent_1080p.mp4"
FINAL_OUTPUT="$PROJECT_DIR/output/final_linear_transformations_1080p.mp4"

# Mux audio with silent video
ffmpeg -y \
  -i "$VIDEO_SILENT" \
  -i "$AUDIO_INPUT" \
  -c:v copy \
  -c:a aac -b:a 192k \
  -map 0:v:0 \
  -map 1:a:0 \
  -shortest \
  "$FINAL_OUTPUT"

echo "=========================================================="
echo "SUCCESS: Your voice recording has been added to the video!"
echo "Video saved at: $FINAL_OUTPUT"
echo "=========================================================="
