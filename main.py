import numpy as np
import cv2
from PIL import ImageGrab
import datetime

# def main() -> None:
# specify a unique name for the video
file_name: str = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = "./outputs/"+file_name + ".mp4"
# specify the resolution
# specify the width and height of screen
image = ImageGrab.grab()
width, height = image.size
# specify the video codec
codex = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# specify FPS
fps = 15.0

video = cv2.VideoWriter(file_name, codex, fps, (width, height))

while (True):
    image = ImageGrab.grab(bbox=(0, 0, width, height))
    image_matrix = np.array(image)
    final_image = cv2.cvtColor(image_matrix, cv2.COLOR_BGR2RGB)
    video.write(final_image)

    if (cv2.waitKey(10) == ord('q')):
        break


# if (__name__ == "main"):
#     main()
