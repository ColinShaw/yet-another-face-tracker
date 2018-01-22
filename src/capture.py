from scipy.misc import imresize
import cv2


class Capture(object):

    def __init__(self, config):
        self.__width_max = config['preview_width']
        self.__height_max = config['preview_height']
        self.__camera = cv2.VideoCapture(config['video_device'])

    def __enter__(self):
        return self

    def frame(self):
        status, image = self.__camera.read()
        if status:
            aspect = float(image.shape[1]) / float(image.shape[0])
            w,h = self.__width_max, self.__height_max
            if aspect > 1.0:
                h = float(self.__width_max) / aspect
            else:
                w = float(self.__height_max) / aspect
            image = imresize(image, (int(h),int(w)))
        else:
            image = np.zeros((self.__width_max, self.__height_max, 3))
        return image

    def __exit__(self, exc_type, exc_value, traceback):
        self.__camera.release()

