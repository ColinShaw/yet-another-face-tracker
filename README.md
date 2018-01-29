# Yet Another Face Tracker

This is a face tracking system built around the
`face_detection` library, which is built around
`dlib`.  The point of it is to be able to easily
add new people to a library of detectable people
by providing an interactive live video feed from
which screenshots can be taken with known 
detections, and then take actions based on these,
for example marking live video and controlling
door locks.  The detected faces are saved to a 
directory specified by the name of the 
individual.  Run this:

```
python capture.py Colin
```

This will make a `Colin` directory under `/images/`
that contains images captured from the live 
video feed if you press the `c` key while there is
an affirmative face identification.

There is another utility, `preview.py` that simply
reads all of the images from `/images/` and
associates the images with the directory name as a
label (e.g. the `Colin` directory).  It validates
the detection to the extent of making sure that a
face is detected.  If not, the training example
is deleted.  All detected faces in the live 
video are compared against the known faces and 
labeled.  Invoke it like this:

```
python preview.py
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
use this.  Nothing fancy going on here with
regard to stopping and starting, it just
runs in your terminal until you quit.  To get the
desired automation around it you can just control
the launch of the program.  You might have to change
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
requires an object to fetch images.  One such class
is the `LocalCamera` class that is an interface to
the `OpenCV` `VideoCapture` interface for local 
video devices.  You can easily add new functionality
for things like IP cameras by simply implementing
the image fetch in a new class.

