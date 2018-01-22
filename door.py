from src.capture   import Capture
from src.transform import Transform
from src.detect    import Detect
from src.encode    import Encode
from src.repeat    import Repeat
from src.kisi      import Kisi


detect = Detect()
encode = Encode()
kisi = Kisi()
repeat = Repeat()
transform = Transform()

refs, ref_map = encode.images()

with Capture() as capture:
    image = capture.frame()
    small = trans.scale_image(image)
    _, encs = detect.all(small)
    for i in range(len(encs)):
        lbl = False
        enc = encs[i]
        cmps = detect.compare(refs, enc)
        for j in range(len(cmps)):
            if cmps[j]:
                lbl = ref_map[j]
        if lbl:
            if repeat.test(lbl):
                kisi.unlock()
                
