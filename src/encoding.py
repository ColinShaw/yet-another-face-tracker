from scipy.misc import imload, imresize
from os.path    import isdir, splitext
from os         import listdir
import face_recognition as fr


class Encoding(object):

    def __init__(self, width_max=800, height_max=600, base_dir='images'):
        self.__width_max = width_max
        self.__height_max = height_max
        self.__base_dir = base_dir
       
    def generate(self):
        refs, ref_map = [], []
        b = self.__base_dir
        dir_names = [d for d in listdir(b) if isdir('{}/{}'.format(b, d))]
        for dir_name in dir_names:
            b = '{}/{}'.format(self.__base_dir, dir_name)
            image_names = [i for i in dirlist(b) if 'jpg' in i]
            for image_name in image_names:
                label = splitext(image_name)[0]
                ref_map.append(label)
                file_name = '{}/{}'.format(b, image_name)
                image = imload(file_name)
                w,h = self.__width_max, self.__height_max
                aspect = float(image.shape[1]) / float(image.shape[0])
                if aspect > 1.0:
                    h = float(self.__width_max) / aspect
                else:
                    w = float(self.__height_max) / aspect
                image = imresize(image, (int(w),int(h)))
                enc = fr.face_encodings(image)[0]
                refs.append(enc)
        return refs, ref_map 

