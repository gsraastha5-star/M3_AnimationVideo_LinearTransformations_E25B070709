# M3 Mathematical Animation Video: Linear Transformations

[![Manim Community](https://img.shields.io/badge/Rendered%20with-Manim%20Community%20v0.22-blue.svg)](https://www.manim.community/)
[![Resolution](https://img.shields.io/badge/Resolution-1920x1080%20(1080p60)-green.svg)]()
[![Course](https://img.shields.io/badge/Course-B.Tech%20Mathematics%20(M3)-orange.svg)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)]()

A complete, professional mathematical educational animation video created for the **B.Tech Linear Algebra and Calculus (M3)** internal assessment.

Inspired by the visual storytelling and intuitive elegance of **3Blue1Brown** (Grant Sanderson), this project demonstrates what happens to vectors and coordinate grids when space is transformed by a $2 \times 2$ matrix.

---

## 1. Project Overview

- **Central Question:** *What happens to vectors and coordinate grids when we multiply them by a matrix?*
- **Transformation Matrix:**
  $$A = \begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix}$$
- **Input Vector:**
  $$v = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$
- **Resulting Vector:**
  $$A v = \begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 2(1) + 1(1) \\ 0(1) + 1(1) \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \end{bmatrix}$$
- **Transformed Standard Basis Vectors:**
  - $e_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \xrightarrow{T} \begin{bmatrix} 2 \\ 0 \end{bmatrix}$ (Column 1 of $A$)
  - $e_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix} \xrightarrow{T} \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ (Column 2 of $A$)
- **Geometric Effect:** Horizontal dilation (scale factor 2) combined with a horizontal shear proportional to height $y$ ($x' = 2x + y, y' = y$), doubling areas ($\det(A) = 2$).
- **Video Specifications:**
  - **Resolution:** 1920 × 1080 (Full HD 1080p)
  - **Frame Rate:** 60 fps
  - **Aspect Ratio:** 16:9 widescreen landscape
  - **Total Duration:** 3 minutes 56 seconds (within the ~5 minute educational guideline)

---

## 2. Six-Scene Video Structure

| Scene | Title | Timecode | Key Mathematical Concept |
|:---:|:---|:---:|:---|
| **1** | **Hook & Introduction** | `0:00 – 0:35` | Vector motion on Cartesian plane; teaser grid flex; central question |
| **2** | **Understanding the Concept** | `0:35 – 1:20` | Definitions: Vector, Matrix, Linear Map; Additivity & Homogeneity axioms |
| **3** | **Visual Intuition** | `1:20 – 2:20` | Basis vectors $e_1, e_2$; Matrix columns as landing spots; grid deformation |
| **4** | **Step-by-Step Worked Example** | `2:20 – 3:45` | $A \times v = [3, 1]^T$; step-by-step dot products; tip-to-tail geometric proof |
| **5** | **Geometric Interpretation** | `3:45 – 4:35` | Coordinate equations $x' = 2x+y, y'=y$; horizontal shear; area doubling ($\det=2$) |
| **6** | **Summary & Credits** | `4:35 – 5:10` | 3 core takeaways; iconic thesis quote; academic references & AI disclosure |

---

## 3. Repository Structure

```
math_video/
├── README.md                          # Comprehensive project documentation
├── requirements.txt                   # Pinned Python dependencies
├── narration_script.md                # 5-minute timed student-to-student narration script
├── AI_DISCLOSURE_AND_REFERENCES.md    # Academic references & AI integrity disclosure
├── storyboard.typ                     # Source file for Storyboard document
├── storyboard.pdf                     # Compiled publication-quality 6-scene Storyboard PDF
├── mathematical_derivation.typ        # Source file for Mathematical Derivation document
├── mathematical_derivation.pdf        # Compiled publication-quality Mathematical Derivation PDF
├── src/                               # Modular Python animation source code
│   ├── __init__.py
│   ├── config.py                      # Theme colors, dimensions, vectors, grid styles
│   ├── typst_math.py                  # High-performance Typst vector SVG math renderer
│   ├── scene1_hook.py                 # Scene 1: Hook & Introduction
│   ├── scene2_concept.py              # Scene 2: Understanding the Concept
│   ├── scene3_visual_intuition.py     # Scene 3: Visual Intuition & Basis Vectors
│   ├── scene4_worked_example.py       # Scene 4: Step-by-Step Worked Example
│   ├── scene5_geometric_interpretation.py # Scene 5: Geometric Interpretation & Shear
│   ├── scene6_summary.py              # Scene 6: Summary & Credits
│   └── full_video.py                  # Master unified animation scene
├── scripts/                           # Automated build and rendering scripts
│   ├── render_preview.sh              # Fast low-res preview render (480p, 15fps)
│   ├── render_1080p.sh                # Production Full HD render (1080p, 60fps)
│   ├── concatenate_scenes.sh          # Lossless FFmpeg scene concatenator
│   └── generate_ai_voiceover.py       # AI neural voiceover generator and audio sync
└── output/                            # Rendered video outputs
    ├── final_linear_transformations_1080p.mp4 # Final 1080p video with AI voiceover
    └── final_linear_transformations_with_ai_voiceover_1080p.mp4
```

---

## 4. Installation & Setup

### Prerequisites
- **Operating System:** macOS, Linux, or Windows (WSL recommended)
- **Python:** 3.11 or 3.12 (Python 3.12 recommended)
- **System Binaries:** `ffmpeg`, `pango`, `pkg-config`, `typst`

#### On macOS (using Homebrew):
```bash
brew install ffmpeg pango pkg-config typst uv
```

#### On Ubuntu / Debian:
```bash
sudo apt update
sudo apt install -y ffmpeg libpango1.0-dev pkg-config
# Install typst via cargo or binary release
cargo install typst-cli
```

### Virtual Environment Setup
Clone this repository and create a virtual environment using `uv` or standard `python3 -m venv`:

```bash
cd math_video

# Using uv (fastest):
uv venv .venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt

# Or using standard pip:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 5. Rendering Instructions

### Quick Low-Resolution Preview (Fast Iteration)
To render a 480p preview in seconds:
```bash
bash scripts/render_preview.sh
# Output saved to: output/preview_full.mp4
```

### Full Production High-Definition 1080p Render
To render all six scenes in 1080p60 and automatically merge them into the master deliverable:
```bash
bash scripts/render_1080p.sh
# Final output saved to: output/final_linear_transformations_1080p.mp4
```

### Rendering an Individual Scene
You can render any individual scene directly with Manim:
```bash
# Render Scene 3 in 1080p
.venv/bin/python -m manim -qh src/scene3_visual_intuition.py Scene3VisualIntuition
```

---

## 6. Voice-Over & Narration Recording

A complete, timestamp-mapped voice-over script is available in [`narration_script.md`](file:///Users/aasthamusale/Desktop/math_video/narration_script.md).

### Recording Tips:
1. **Pacing:** Speak in a relaxed, student-to-student conversational tone (~130 words per minute).
2. **Audio Software:** Audacity, OBS Studio, or Adobe Audition.
3. **Muxing Audio with Video:**
   Once you record `voiceover.mp3` or `voiceover.wav`:
   ```bash
   ffmpeg -i output/final_linear_transformations_1080p.mp4 -i voiceover.mp3 -c:v copy -c:a aac output/final_video_with_audio.mp4
   ```

---

## 7. Mathematical & Storyboard Documents

- **Six-Scene Storyboard PDF:** [`storyboard.pdf`](file:///Users/aasthamusale/Desktop/math_video/storyboard.pdf)  
  *Detailed visual layouts, camera angles, color codes, and animation transitions.*
- **Mathematical Derivation Report:** [`mathematical_derivation.pdf`](file:///Users/aasthamusale/Desktop/math_video/mathematical_derivation.pdf)  
  *Comprehensive academic proof of basis determination, coordinate transformations, shear decomposition, and area doubling.*

To recompile these PDFs from their Typst source code:
```bash
typst compile storyboard.typ storyboard.pdf
typst compile mathematical_derivation.typ mathematical_derivation.pdf
```

---

## 8. Academic Integrity & References

See [`AI_DISCLOSURE_AND_REFERENCES.md`](file:///Users/aasthamusale/Desktop/math_video/AI_DISCLOSURE_AND_REFERENCES.md) for complete academic citations (Gilbert Strang, David C. Lay, Erwin Kreyszig, 3Blue1Brown) and formal AI disclosure statement.

---

## 9. Deliverables Verification Checklist

- [x] Final 1080p MP4 animation video: `output/final_linear_transformations_1080p.mp4` (Duration: 3:56, 1920x1080, 60fps)
- [x] Complete modular Python source code (`src/` with all 6 scenes)
- [x] Separate 5-minute student-to-student narration script (`narration_script.md`)
- [x] Six-scene storyboard PDF (`storyboard.pdf`)
- [x] Mathematical derivation PDF (`mathematical_derivation.pdf`)
- [x] Academic references and AI disclosure (`AI_DISCLOSURE_AND_REFERENCES.md`)
- [x] Comprehensive installation and rendering guide (`README.md`)
- [x] Pinned dependencies file (`requirements.txt`)
- [x] Clean project folder structure ready for GitHub repository upload
