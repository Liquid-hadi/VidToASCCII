import os
import sys

from webcam_converter import WebcamConverter
from video_converter import VideoConverter


def main() -> None:
    os.system("clear")
    print("=== Video to ASCII ===")
    print("1. Webcam")
    print("2. Video file")
    print("q. Quit")
    print()

    choice = input("Choose an option: ").strip().lower()

    if choice == "1":
        WebcamConverter(width=120).start()

    elif choice == "2":
        path = input("Enter video file path: ").strip()
        if not path:
            print("No path provided.")
            return
        if not os.path.exists(path):
            print(f"Error: file not found: {path}")
            return
        VideoConverter(width=120, fps_cap=30).play(path)

    elif choice == "q":
        print("Bye!")
        sys.exit(0)

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
