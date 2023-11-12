"""
Taking images with the camera on the Raspberry Pi
"""
import sys
import time

import cv2


CAMERA_NAME = 0
# TODO: Move this to configuration file
CAMERA_WIDTH = 1920
CAMERA_HEIGHT = 1200

SAVE_PREFIX = "log_record_" + str(int(time.time())) + "_"
DELAY = 1  # seconds

if __name__ == "__main__":

    camera = cv2.VideoCapture(CAMERA_NAME)
    if not camera.isOpened():
        with open(SAVE_PREFIX + "error.txt", "w") as f:
            f.write(SAVE_PREFIX + "\n" + "ERROR: Failed to open camera")
        assert False

    result = camera.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
    assert result
    result = camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
    assert result

    width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
    assert width == CAMERA_WIDTH
    height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
    assert height == CAMERA_HEIGHT

    i = 0
    while True:
        result, image = camera.read()
        if not result:
            continue

        cv2.imwrite(SAVE_PREFIX + str(i) + ".png", image)
        i += 1

        time.sleep(DELAY)

    camera.release()
