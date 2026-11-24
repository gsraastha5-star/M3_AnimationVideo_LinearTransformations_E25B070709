"""
Generate AI Voice-over for Linear Transformations Animation.
Uses edge-tts (Microsoft Natural Neural Voice) to generate professional,
natural-sounding student-to-student narration synchronized to each scene.
"""

import asyncio
import os
import subprocess
import edge_tts

VOICE = "en-US-ChristopherNeural"  # Professional, articulate, natural student tone
RATE = "+0%"

SCENE_SCRIPTS = [
    {
        "id": 1,
        "name": "scene1_hook",
        "duration": 30.90,
        "text": (
            "Welcome! Today we are exploring one of the most powerful concepts in linear algebra: "
            "Linear Transformations. Usually, we see vectors as simple arrows or coordinate pairs. "
            "But what happens to vectors and coordinate grids when we multiply them by a matrix? "
            "Let's move beyond static spreadsheets of numbers, and discover how matrices act as dynamic machines "
            "that reshape space."
        )
    },
    {
        "id": 2,
        "name": "scene2_concept",
        "duration": 30.80,
        "text": (
            "Let's ground our intuition with three key concepts: a vector with magnitude and direction, "
            "a matrix as a geometric machine, and a linear transformation. "
            "A transformation is linear if the origin stays anchored, and all grid lines remain straight and parallel. "
            "Mathematically, this satisfies additivity: T of u plus v equals T of u plus T of v; "
            "and homogeneity: T of c times v equals c times T of v. "
            "Where basis vectors go, the entire space must follow."
        )
    },
    {
        "id": 3,
        "name": "scene3_visual_intuition",
        "duration": 38.70,
        "text": (
            "Here is our standard Cartesian grid with basis vectors: green is e-one at (1, 0), "
            "red is e-two at (0, 1), framing our unit square. "
            "Now look at our matrix: A equals [[2, 1], [0, 1]]. Notice the columns! "
            "Column one is [2, 0], and column two is [1, 1]. "
            "As the matrix acts on the plane, e-one stretches to (2, 0), e-two leans to (1, 1), "
            "and the square grid shears into a parallelogram grid of area 2. "
            "The columns literally tell us where the basis vectors land!"
        )
    },
    {
        "id": 4,
        "name": "scene4_worked_example",
        "duration": 60.70,
        "text": (
            "Let's test this with a worked example: vector v equals [1, 1]. "
            "Notice that v is simply one times e-one plus one times e-two. "
            "Now, we compute A times v algebraically. "
            "For the top row, the dot product is 2 times 1 plus 1 times 1, which equals 2 plus 1, giving 3. "
            "For the bottom row, 0 times 1 plus 1 times 1 equals 1. "
            "Our calculated result is the vector [3, 1]. "
            "Now watch the geometry! "
            "As the transformation is applied, vector v sweeps across the grid and lands at coordinates (3, 1). "
            "Why? Because T of v equals 1 times T of e-one plus 1 times T of e-two: "
            "[2, 0] plus [1, 1] equals [3, 1]. "
            "Algebra and geometry reveal the exact same truth!"
        )
    },
    {
        "id": 5,
        "name": "scene5_geometric_interpretation",
        "duration": 39.90,
        "text": (
            "Let's look closely at the coordinate equations: x prime equals 2x plus y, and y prime equals y. "
            "Notice that y prime is completely unchanged. Every horizontal line stays at its original height. "
            "Meanwhile, x prime scales by 2, plus an additional shift equal to y. "
            "Points higher up shift further to the right. That progressive displacement is what creates the shear effect. "
            "Yet, the origin remains fixed, straight lines stay straight, and all areas are exactly doubled, "
            "because the determinant of A is 2."
        )
    },
    {
        "id": 6,
        "name": "scene6_summary",
        "duration": 33.80,
        "text": (
            "Here are the three big takeaways: "
            "First: A matrix defines how vectors transform space. "
            "Second: The columns of a matrix describe the transformed basis vectors, determining the entire plane. "
            "Third: Linear transformations preserve straight lines and the origin. "
            "Always remember: One matrix. Two basis vectors. An entire transformed plane. "
            "Good luck with your B-Tech mathematics assessment!"
        )
    }
]


async def generate_speech(text: str, output_path: str):
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
    await communicate.save(output_path)


def get_audio_duration(file_path: str) -> float:
    cmd = [
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", file_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, check=True)
    return float(res.stdout.strip())


def pad_or_fit_audio(input_path: str, output_path: str, target_duration: float):
    """
    Pads audio with initial lead-in (0.5s) and trailing silence to match exact target duration.
    """
    actual_dur = get_audio_duration(input_path)
    print(f"  Speech audio length: {actual_dur:.2f}s | Target scene length: {target_duration:.2f}s")
    
    if actual_dur > target_duration:
        # Slight speedup if speech slightly exceeds target duration
        speed_factor = actual_dur / (target_duration - 0.5)
        print(f"  Adjusting tempo: {speed_factor:.2f}x to fit scene")
        filter_str = f"atempo={speed_factor},apad=whole_dur={target_duration}"
    else:
        # Pad with 0.5s delay at start, then pad rest with silence to match exact duration
        delay_ms = 400
        pad_dur = target_duration
        filter_str = f"adelay={delay_ms}|{delay_ms},apad=whole_dur={target_duration}"

    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-af", filter_str,
        "-t", str(target_duration),
        "-c:a", "libmp3lame", "-b:a", "192k",
        output_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, check=True)


async def main():
    os.makedirs("media/audio", exist_ok=True)
    padded_files = []

    print("==========================================================")
    print("Generating AI Neural Narration for 6 Scenes...")
    print("==========================================================")

    for item in SCENE_SCRIPTS:
        sid = item["id"]
        raw_mp3 = f"media/audio/raw_scene{sid}.mp3"
        padded_mp3 = f"media/audio/scene{sid}_synced.mp3"
        
        print(f"\n[Scene {sid}] Generating speech ({item['name']})...")
        await generate_speech(item["text"], raw_mp3)
        pad_or_fit_audio(raw_mp3, padded_mp3, item["duration"])
        padded_files.append(padded_mp3)

    # Concat all scene audios into one master voiceover track
    concat_list_file = "media/audio/concat_audio_list.txt"
    with open(concat_list_file, "w") as f:
        for pf in padded_files:
            abs_pf = os.path.abspath(pf)
            f.write(f"file '{abs_pf}'\n")

    full_voiceover = "media/audio/full_voiceover.mp3"
    print("\nMerging all scene audio into master voiceover track...")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_list_file,
        "-c:a", "libmp3lame", "-b:a", "192k",
        full_voiceover
    ], check=True, stdout=subprocess.DEVNULL)

    full_dur = get_audio_duration(full_voiceover)
    print(f"Master voiceover generated: {full_voiceover} (Total duration: {full_dur:.2f}s)")

    # Multiplex with video
    video_in = "output/final_linear_transformations_1080p.mp4"
    video_out = "output/final_linear_transformations_with_ai_voiceover_1080p.mp4"

    print("\nMuxing synchronized audio with 1080p video...")
    subprocess.run([
        "ffmpeg", "-y",
        "-i", video_in,
        "-i", full_voiceover,
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k",
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-shortest",
        video_out
    ], check=True, stdout=subprocess.DEVNULL)

    # Also overwrite final_linear_transformations_1080p.mp4 so it has the voiceover embedded by default
    subprocess.run(["cp", video_out, video_in], check=True)

    print("\n==========================================================")
    print("SUCCESS: AI Voiceover generated and embedded!")
    print(f"Master video with AI Voiceover ready at:")
    print(f"  {video_out}")
    print(f"  {video_in}")
    print("==========================================================")


if __name__ == "__main__":
    asyncio.run(main())
