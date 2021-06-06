# FortniteAimBot
detect enemies with yolov3 and use aim-assist or auto-fire features 

Fornite object detection using Darknet's YOLOv3 implemented via PyTorch.<br>

Click to view YouTube demo<br>
[![IMAGE ALT TEXT](https://img.youtube.com/vi/Y0Y_G9msqrc/0.jpg)](https://www.youtube.com/watch?v=Y0Y_G9msqrc)

<b>Current functionality:</b><br>
-Read Monitor as PIL.Image then convert to Numpy array<br>
-Run Numpy arrayof monitor through neural network to detect objects<br> 
-Output tensor has all objects detected on monitor 
-Refine tensor: Remove all 'non person' objects 
-To aviod detecting yourself the object at the bottom of the screen is removed
-Draw red rectangle around identifications <br>
-Overlay image on running Fortnite with the ability to click through the image as to not effect gameplay<br>
-Mouse fires when target is in the cross hairs
<br>


TODO:

- change hard coded path names to current folder directory
- impliment `/Aim/Actions.py` functionality

Vision/Detection.py 
- optimize `write()` function to draw bounding boxes at the same time

Vision/TensorRefinement.py
- clean up and remove when yolo model has only 1 class (person)

Aim/Actions.py
- add back to demo version
- find new solution to auto click pressing twice is not ideal

<br><br>
<b>Contact:</b> MichaelRomeroJr1@gmail.com
