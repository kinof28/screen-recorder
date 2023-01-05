import numpy as np
import cv2
from PIL import ImageGrab
import time

# def main() -> None:
# specify a unique name for the video
file_name: str = time.localtime+"-record.mp4"
# specify the width and height of screen
width: int = 900
height: int = 700
# specify the resolution
resolution = (width, height)
# specify the video codec
codex = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter(file_name, codex, 20.0, resolution)

while (True):
    image = ImageGrab.grab()
    image_matrix = np.array(image)
    final_image = cv2.cvtColor(image_matrix, cv2.COLOR_BGR2RGB)
    cv2.imshow("screen record", final_image)
    video.write(final_image)

    if (cv2.waitKey(10) == ord('q')):
        break


# if (__name__ == "main"):
#     main()
