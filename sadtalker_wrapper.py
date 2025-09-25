import os
import subprocess
import sys

def generate_educational_video(
    audio_path: str,
    image_path: str,
    output_dir: str = "results",
    enhancer: str = "gfpgan"
):
    """
    Wrapper to call SadTalker's inference.py to create a talking-head video.

    Parameters
    ----------
    audio_path : str
        Path to the input audio file (e.g. 'audio/test.wav')
    image_path : str
        Path to the source image (e.g. 'images/source.jpg')
    output_dir : str
        Directory where the result will be saved (default: 'results')
    enhancer : str
        Optional enhancer (default: 'gfpgan')
    """

    # Locate the SadTalker directory and inference script
    sadtalker_dir = os.path.dirname(__file__)
    inference_script = os.path.join(sadtalker_dir, "inference.py")

    if not os.path.isfile(inference_script):
        raise FileNotFoundError(
            f"inference.py not found at {inference_script}. "
            "Check that SadTalker was cloned correctly."
        )

    os.makedirs(output_dir, exist_ok=True)

    # Build the command
    cmd = [
        sys.executable,  # use current venv's python
        inference_script,
        "--driven_audio", audio_path,
        "--source_image", image_path,
        "--result_dir", output_dir,
        "--enhancer", enhancer
    ]

    print(f"Running SadTalker:\n{' '.join(cmd)}\n")
    subprocess.run(cmd, check=True)
    print(f"✅ Video generated inside: {output_dir}")
