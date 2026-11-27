#!/usr/bin/env bash
# Mux normalized user voice recording with 1080p video
set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"

VIDEO_INPUT="$PROJECT_DIR/output/final_linear_transformations_1080p.mp4"
AUDIO_RAW="$PROJECT_DIR/fibal.m4a"
AUDIO_PROCESSED="$PROJECT_DIR/media/audio/user_voice_normalized.wav"
OUTPUT_FINAL="$PROJECT_DIR/Linear_Transformations_Final_MyVoice.mp4"

mkdir -p "$PROJECT_DIR/media/audio"
mkdir -p "$PROJECT_DIR/output"

echo "1. Filtering and normalizing user recording..."
# - highpass=f=75: cuts sub-bass rumble/table thumps
# - lowpass=f=12000: eliminates high frequency hiss
# - loudnorm=I=-16:TP=-1.5:LRA=11: standard broadcast loudness for crystal clear speech
ffmpeg -y -i "$AUDIO_RAW" -af "highpass=f=75,lowpass=f=12000,loudnorm=I=-16:TP=-1.5:LRA=11" "$AUDIO_PROCESSED"

echo "2. Muxing video and user audio into final deliverable: $OUTPUT_FINAL"
ffmpeg -y -i "$VIDEO_INPUT" -i "$AUDIO_PROCESSED" \
    -map 0:v:0 -map 1:a:0 \
    -c:v copy \
    -c:a aac -b:a 192k \
    -shortest \
    "$OUTPUT_FINAL"

echo "=========================================================="
echo "Successfully created: $OUTPUT_FINAL"
echo "=========================================================="
