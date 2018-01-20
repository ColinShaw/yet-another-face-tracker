from scipy.misc import imread
from os.path    import isdir
from os         import listdir
import face_recognition as fr


class Encode(object):

    def __init__(self, base_dir='images'):
        self.__base_dir = base_dir
       
    def images(self):
        refs, ref_map = [], []
        b = self.__base_dir
        dir_names = [d for d in listdir(b) if isdir('{}/{}'.format(b,d))]
        for dir_name in dir_names:
            b = '{}/{}'.format(self.__base_dir,dir_name)
            image_names = [i for i in listdir(b) if 'jpg' in i]
            for image_name in image_names:
                file_name = '{}/{}'.format(b,image_name)
                image = imread(file_name)
                encs = fr.face_encodings(image)
                if len(encs) == 1:
                    refs.append(encs[0])
                    ref_map.append(dir_name)
                    print('{}... detected'.format(file_name))
                else:
                    print('{}... not detected'.format(file_name))
        return refs, ref_map 

