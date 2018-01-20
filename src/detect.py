import face_recognition as fr


class Detect(object):

    def locations(self, image):
        return fr.face_locations(image, model='cnn')

    def encodings(self, image):
        return fr.face_encodings(image)

    def all(self, image):
        locs = fr.face_locations(image, model='cnn')
        encs = fr.face_encodings(image, locs)
        return locs, encs

    def compare(self, refs, encs):
        return fr.compare_faces(refs, encs)

