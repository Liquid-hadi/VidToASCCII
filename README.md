# VidToASCII

Converts video or a live webcam feed into ASCII art and plays it in the terminal in real time.

Each frame is resized, converted to grayscale, and every pixel's brightness is mapped to a character from a ramp that goes from dark (space) to light (`@`).

```
ASCII_CHARS = " .,:;i1tfLCG08@"
```

---

## Requirements

- Python 3.x
- OpenCV (`cv2`)

Install the dependency:

```bash
pip install opencv-python
```

---

## Usage

```bash
python main.py
```

You'll see a menu:

```
=== Video to ASCII ===
1. Webcam
2. Video file
q. Quit
```

### Option 1 — Webcam

Streams your default webcam live as ASCII art. Press `Ctrl+C` to stop.

### Option 2 — Video file

Enter the path to a video file (e.g. `video.mp4`) and it will play it as ASCII art at the original frame rate (capped at 30 FPS). Press `Ctrl+C` to stop early.

---

## Project Structure

```
VidToASCII/
├── main.py               # Entry point — terminal menu
├── ascii_converter.py    # Base class with frame-to-ASCII conversion logic
├── webcam_converter.py   # Reads from webcam and renders ASCII
└── video_converter.py    # Reads from a video file and renders ASCII
```
