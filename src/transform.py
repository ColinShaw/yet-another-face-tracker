from scipy.misc import imresize
import numpy as np
import cv2


class Transform(object):

    def __init__(self, config):
        self.__scale = config['scale_factor']

    def scale_image(self, image):
        w,h = image.shape[0], image.shape[1]
        return imresize(image, (w/self.__scale,h/self.__scale))

    def scale_location(self, loc):
        return (
            loc[0] * self.__scale,
            loc[1] * self.__scale,
            loc[2] * self.__scale,
            loc[3] * self.__scale
        )

    def image_copy(self, data):
        return np.copy(data)

    def image_color_flip(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

