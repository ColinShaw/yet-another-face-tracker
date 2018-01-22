from src.capture   import Capture
from src.config    import Config
from src.detect    import Detect
from src.display   import Display
from src.label     import Label
from src.save      import Save
from src.transform import Transform
from sys           import argv


if len(argv) < 2:
    print('You must specify a name argument.')

else:
    config  = Config().get()
    capture = Capture(config)
    trans   = Transform(config)
    display = Display()
    detect  = Detect()
    label   = Label()

    with capture, display:
        key = ''
        while key != 'q':
            success = False
            image = capture.frame()
            disk  = trans.image_copy(image)
            disk  = trans.image_color_flip(disk)
            small = trans.scale_image(image)
            locs  = detect.locations(small)
            if len(locs) == 1:
                success = True
                loc = trans.scale_location(locs[0])
                label.set_image(image).set_location(loc)
                image = label.outline().header(argv[1]).get_image()
            display.show(image)
            key = display.key()
            if key == 'c' and success == True:
                print('Capturing {}...'.format(argv[1]))
                Save().image(disk, argv[1])

