from src.capture      import Capture
from src.config       import Config
from src.detect       import Detect
from src.encode       import Encode
from src.kisi         import Kisi
from src.local_camera import LocalCamera
from src.repeat       import Repeat
from src.transform    import Transform
from datetime         import datetime


config  = Config().get()
camera  = LocalCamera(config)
capture = Capture(config, camera)
encode  = Encode(config)
kisi    = Kisi(config)
repeat  = Repeat(config)
trans   = Transform(config)
detect  = Detect()

refs, ref_map = encode.images()

with capture:
    while True:
        image = capture.frame()
        small = trans.scale_image(image)
        _, encs = detect.all(small)
        if len(encs) == 1:
            lbl = False
            cmps = detect.compare(refs, encs[0])
            for i in range(len(cmps)):
                if cmps[i]:
                    lbl = ref_map[i]
            if lbl != False and repeat.test(lbl):
                print('[{}] Detected {}'.format(str(datetime.now()), lbl))
                kisi.unlock()
        else:
            repeat.test('')
                
