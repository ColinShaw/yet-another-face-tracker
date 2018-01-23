from scipy.misc import imresize


class Capture(object):

    def __init__(self, source, config):
        self.__width_max = config['preview_width']
        self.__height_max = config['preview_height']
        self.__source = source

    def __enter__(self):
        return self

    def frame(self):
        image = self.__source.frame()
        aspect = float(image.shape[1]) / float(image.shape[0])
        w,h = self.__width_max, self.__height_max
        if aspect > 1.0:
            h = float(self.__width_max) / aspect
        else:
            w = float(self.__height_max) / aspect
        return imresize(image, (int(h),int(w)))

    def __exit__(self, exc_type, exc_value, traceback):
        self.__source.cleanup()

