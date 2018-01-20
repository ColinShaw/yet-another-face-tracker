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
label (e.g. the `Colin` directory).  This simply 
runs live video with the detections.


### Future plans

The goal is to have a simple to use collection of
programs for generating training data easily, testing
with live video, and ultimately integrating with
the Kisi door locks.  Idea with this is you can capture
new people with door access easily, then run a 
daemon that evaluates who is near the door, and when 
there is adequate confidence in the capture (ten
consecutive frames detected appropriately), trigger
the door to unlock.

