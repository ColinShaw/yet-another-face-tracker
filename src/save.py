from os.path    import exists
from os         import makedirs
from uuid       import uuid4
from scipy.misc import imsave


class Save(object):

    @staticmethod
    def image(image, name, folder='images'):
        if not exists(folder):
            makedirs(folder)
        if not exists('{}/{}'.format(folder,name)):
            makedirs('{}/{}'.format(folder,name))
        imsave('{}/{}/{}.jpg'.format(folder,name,uuid4().hex),image)

