import cv2


class Display(object):

    def __enter__(self):
        return self

    def show(self, image, label=''):
        cv2.imshow(label, image)

    def key(self):
        return chr(cv2.waitKey(25) & 0xFF)

    def __exit__(self, exc_type, exc_value, traceback):
        cv2.destroyAllWindows()

