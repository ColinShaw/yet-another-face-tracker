from src.capture import Capture
from src.display import Display
from src.scale   import Scale
from src.label   import Label
from src.detect  import Detect


label, scale, detect = Label(), Scale(), Detect()
with Display() as display, Capture() as capture:
    key = ''
    while key != 'q':
        success = False
        image = capture.frame()
        small = scale.image(image)
        locs  = detect.locations(small)
        if len(locs) == 1:
            success = True
            loc = scale.location(locs[0])
            label.set_image(image).set_location(loc)
            image = label.outline().get_image()
        display.show(image)
        key = display.key()
        if key == 'c' and success == True:
            print('Capturing')

