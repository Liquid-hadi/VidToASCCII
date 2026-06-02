import cv2

# Characters ordered from darkest to lightest
ASCII_CHARS = " .,:;i1tfLCG08@"


class ASCIIConverter:
    def __init__(self, width: int = 120) -> None:
        self.width = width

    def frame_to_ascii(self, frame) -> str:
        h, w = frame.shape[:2]
        aspect = h / w

        # Multiply by 0.45 to make chars wider
        height = int(self.width * aspect * 0.45)

        # Shrink the frame 
        resized = cv2.resize(frame, (self.width, height))

        # Convert to grayscale so each pixel is a single brightness value (0–255)
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

        ascii_frame = ""
        for row in gray:
            for pixel in row:
                # Map brightness (0–255) to an index in ASCII_CHARS
                index = int(pixel / 255 * (len(ASCII_CHARS) - 1))
                ascii_frame += ASCII_CHARS[index]
            ascii_frame += "\n"

        return ascii_frame
