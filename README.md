# Yet Another Face Tracker

This is a face tracking system built around the
`face_detection` library, which is built around
`dlib`.  The point of it is to be able to easily
add new people to a library of detectable people
by providing an interactive live video feed from
which screenshots can be taken with known 
detections.  These are saved to a folder by
the specified name of the individual.  Run this 
in this way:

```
python capture.py Colin
```

This will make a `Colin` directory under `/images/`
that contains images captured from the live 
video feed if you press the `c` key while there is
an affirmative face identification.

There is another utility, `live.py` that simply
reads all of the images from `/images/` and
associates the images with the directory name as a
label (e.g. the `Colin` directory).  It validates
the detection to the extent of making sure that a
face is detected.  If not, the training example
is deleted.  All detected faces in the live 
video are compared against the known faces and 
labeled.  Invoke it like this:

```
python live.py
```

The last utility, `door.py` is an interface with 
Kisi door locks.  This does not have a display,
so you won't physically see who is in the frame.  In
this application, if one and only one known face is
identified for a number of consecutive frames, the
door is unlocked.  Regardless of other logging that
may or may not occur, you probably want to log what
is being done.  This can be done like this:

```
python door.py > log.txt 2>&1
```

Obviously you need to have Kisi door locks to 
use this aspect.  Nothing fancy going on here with
regard to stopping and starting this thing, it just
runs in your terminal until you quit.  To get the
desired automation around it you can just control
the launch of the program.  You might have to the 
the `KeyboardInterrupt` condition for quitting if 
the situation warrants it.

You will need to copy the example configuration,
`config.yaml.example` to a real configuration,
`config.yaml`.  If you are using Kisi door locks
you will need to fill in credentials and which
door to unlock.  The rest of the configurations
shouldn't need messing with.

One thing to note about the implementation is the
abstraction for image input.  The `Capture` class
makes some assumptions about a class that is
passed to the constructor having to do with being
able to obtain images.  The sample here uses the
`OpenCV` `VideoCapture` class for obtaining images
from local capture devices.  This needs to be 
changed to a different mechanism for obtaining
images if you are wanting to use something like
an IP camera.
