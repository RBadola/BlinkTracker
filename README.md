# Eye Blink Detection and Alert System
This is a Python application that uses OpenCV, dlib, and win10toast libraries to detect eye blinks and send a notification if the user has not blinked frequently enough. The application works by capturing the video feed from the user's webcam and detecting the user's eyes. It then calculates the eye aspect ratio (EAR) for both eyes and if the EAR falls below a certain threshold, it considers it a blink. If the user has not blinked frequently enough, it sends a notification to remind them to blink.
# Requirements To Run On Your Device
you would need the follwing libraries
* Python 3
* OpenCV
* dlib
* win10toast

To make it into a executable file pyinstaller can be used by running the following command:
`pip install pyinstaller`

Navigate to the directory containing the file.
Run the following command to create a standalone executable file:

`pyinstaller --onefile blink.py`
