import cv2


class Label(object):

    def set_image(self, image):
        self.__image = image
        return self

    def set_location(self, location):
        self.__loc = location
        return self

    def get_image(self):
        return self.__image

    def outline(self):
        cv2.rectangle(
            self.__image,
            (self.__loc[1],self.__loc[0]),
            (self.__loc[3],self.__loc[2]),
            (0,255,0),
            2
        )
        return self

    def header(self, label):
        cv2.rectangle(
            image,
            (self.__loc[1]+1,self.__loc[0]-20),
            (self.__loc[3]-1,self.__loc[0]),
            (0,255,0),
            cv2.FILLED
        )
        cv2.putText(
            image,
            label,
            (self.__loc[3]+2,self.__loc[0]-2),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,0,0)
        )
        return self

