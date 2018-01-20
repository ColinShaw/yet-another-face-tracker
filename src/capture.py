from scipy.misc import imresize
import cv2


class Capture(object):

    def __init__(self, width_max=400, height_max=300, device=0):
        self.__width_max = width_max
        self.__height_max = height_max
        self.__camera = cv2.VideoCapture(device)

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

