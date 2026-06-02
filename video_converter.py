import cv2
import os
import sys
import time

from ascii_converter import ASCIIConverter


class VideoConverter(ASCIIConverter):
    def __init__(self, width: int = 120, fps_cap: int = 30) -> None:
        super().__init__(width)
        # fps_cap so the terminal handles fast vids
        self.fps_cap = fps_cap

    def play(self, path: str) -> None:
        cap = cv2.VideoCapture(path)

        if not cap.isOpened():
            print(f"Error: cannot open {path}")
            return

        video_fps = cap.get(cv2.CAP_PROP_FPS)

        # Use the lower of the video's actual FPS and our cap to set the sleep time between frames
        delay = 1 / min(video_fps, self.fps_cap)

        # ANSI escape code to hide the blinking cursor while rendering
        sys.stdout.write("\033[?25l")

        try:
            while True:
                ret, frame = cap.read()
                # ret is False when there are no more frames (end of video)
                if not ret:
                    break

                ascii_frame = self.frame_to_ascii(frame)

                # Move cursor to top-left corner instead of clearing the screen — avoids flicker
                sys.stdout.write("\033[H")
                sys.stdout.write(ascii_frame)
                sys.stdout.flush()

                # Wait to match the original video's frame rate
                time.sleep(delay)

        except KeyboardInterrupt:
            pass
        finally:
            cap.release()
            # Restore the cursor before exiting
            sys.stdout.write("\033[?25h")
            os.system("clear")
