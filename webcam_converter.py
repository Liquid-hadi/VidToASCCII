import cv2
import os
import sys
import time

from ascii_converter import ASCIIConverter


class WebcamConverter(ASCIIConverter):
    def __init__(self, width: int = 120) -> None:
        super().__init__(width)

    def start(self) -> None:
        # 0 tells OpenCV to use the default system webcam
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: cannot access webcam")
            return

        print("Press Ctrl+C to stop")
        # Brief pause so the user can read the message before the ASCII takes over
        time.sleep(1)

        # ANSI escape code to hide the blinking cursor while rendering
        sys.stdout.write("\033[?25l")

        try:
            while True:
                ret, frame = cap.read()
                # ret is False when the webcam stops sending frames
                if not ret:
                    break

                ascii_frame = self.frame_to_ascii(frame)

                # Move cursor to top-left corner instead of clearing the screen — avoids flicker
                sys.stdout.write("\033[H")
                sys.stdout.write(ascii_frame)
                sys.stdout.flush()

        except KeyboardInterrupt:
            pass
        finally:
            cap.release()
            # Restore the cursor before exiting
            sys.stdout.write("\033[?25h")
            os.system("clear")
            print("Stopped.")
