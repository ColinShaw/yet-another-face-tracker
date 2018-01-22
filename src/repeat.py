class Repeat(object):

    def __init__(self, config):
        self.__times = config['repeat_times']
        self.__last_value = ''
        self.__count = 0

    def test(self, value):
        if self.__last_value == value:
            self.__count += 1
            if self.__count == self.__times:
                self.__last_value = ''
                self.__count = 0
                return True
        else:
            self.__last_value = value
            self.__count = 0
        return False

