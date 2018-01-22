import yaml


class Config(object):

    def __init__(self, filename='config.yaml'):
        with open(filename) as f:
            self.__config = yaml.safe_load(f)

    def get(self):
        return self.__config

