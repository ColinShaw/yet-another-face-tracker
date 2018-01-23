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
door is unlocked.  Invoke it like this:

```
python door.py
```

Obviously you need to have Kisi door locks to 
use that.

