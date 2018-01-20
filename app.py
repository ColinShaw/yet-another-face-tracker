from scipy.misc import imresize
from os.path    import splitext
from os         import listdir
import face_recognition as fr
import cv2


SCALE = 4


refs, ref_map = [], []

image_names = [f for f in listdir('images') if 'jpg' in f]

for image_name in image_names:
    file_name = 'images/{}'.format(image_name)
    image = fr.load_image_file(file_name)
    refs.append(fr.face_encodings(image)[0])
    ref_map.append(splitext(image_name)[0])

cam = cv2.VideoCapture(0)

while True:
    ret, image = cam.read()
    w,h = image.shape[1], image.shape[0]
    small = imresize(image, (h/SCALE,w/SCALE))
    if ret:
        locations = fr.face_locations(small, model='cnn')
        encodings = fr.face_encodings(small, locations)
        for i in range(len(locations)):
            enc = encodings[i]
            loc = locations[i]
            cmps, label = fr.compare_faces(refs, enc), False
            for j in range(len(cmps)):
                if cmps[j]:
                    label = ref_map[j]
            if label:
                cv2.rectangle(
                    image,
                    (loc[1]*SCALE,loc[0]*SCALE),
                    (loc[3]*SCALE,loc[2]*SCALE),
                    (0,255,0),
                    2
                )
                cv2.rectangle(
                    image,
                    (loc[1]*SCALE+1,loc[0]*SCALE-20),
                    (loc[3]*SCALE-1,loc[0]*SCALE),
                    (0,255,0),
                    cv2.FILLED
                )
                cv2.putText(
                    image,
                    label,
                    (loc[3]*SCALE+2,loc[0]*SCALE-2),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0,0,0)
                )
        cv2.imshow('Image Detection', image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()

