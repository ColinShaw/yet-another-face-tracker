import cv2
import numpy as np


class LocalCamera(object):

    def __init__(self, config):
        self.__camera = cv2.VideoCapture(config['video_device'])

    def frame(self):
        status, image = self.__camera.read()
        if status:
            return image
        else:
            return np.zeros((1,1,3), dtype=np.uint8)

    def cleanup(self):
        self.__camera.release()

