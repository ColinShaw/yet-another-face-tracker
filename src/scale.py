from scipy.misc import imresize


class Scale(object):

    def __init__(self, scale=2):
        self.__scale = scale

    def image(self, image):
        w,h = image.shape[0], image.shape[1]
        return imresize(image, (w/self.__scale, h/self.__scale))

    def location(self, loc):
        return (
            loc[0] * self.__scale,
            loc[1] * self.__scale,
            loc[2] * self.__scale,
            loc[3] * self.__scale
        )

