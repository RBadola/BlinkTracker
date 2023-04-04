import dlib
import cv2
import time
from win10toast import ToastNotifier

# Load the face detector and predictor
detector = dlib.get_frontal_face_detector()

# Initialize the eye aspect ratio variables
leftEAR = rightEAR = 0
EYE_AR_THRESH = 0.2
EYE_AR_CONSEC_FRAMES = 3
COUNTER = 0
TOTAL = 0
BLINK_TIME = 60  # set the blink time in seconds
ALERT_THRESHOLD= 15
# Initialize the blink count variables
blink_count = 0
last_blink_time = time.time()

# Initialize the alert notifier
toaster = ToastNotifier()

while True:
    # Capture the video frame
    cap = cv2.VideoCapture(0)

    # Loop over each frame
    while True:
        # Read the video frame
        _, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = detector(gray, 0)

        # Loop over each face
        for face in faces:
            # Detect the eyes in the face
            shape = detector(gray, face)
            left_eye = shape.part(36,42)
            right_eye = shape.part(42,48)

            # Compute the eye aspect ratio for the left and right eye
            leftEAR = eye_aspect_ratio(left_eye)
            rightEAR = eye_aspect_ratio(right_eye)

            # Average the eye aspect ratio together for both eyes
            ear = (leftEAR + rightEAR) / 2.0

            # Check if the eye aspect ratio is below the blink threshold
            if ear < EYE_AR_THRESH:
                COUNTER += 1

            # Otherwise, the eye aspect ratio is not below the blink threshold
            else:
                # If the eyes were closed for a sufficient number of consecutive frames,
                # consider it a blink and increment the blink count
                if COUNTER >= EYE_AR_CONSEC_FRAMES:
                    blink_count += 1
                    last_blink_time = time.time()

                # Reset the consecutive frames counter
                COUNTER = 0

        # Display the blink count and last blink time
        if time.time() - last_blink_time > BLINK_TIME:
            TOTAL = blink_count
            blink_count = 0
            last_blink_time = time.time()

            if TOTAL < ALERT_THRESHOLD:
                message = "You haven't blinked enough. Please blink more frequently!"
                toaster.show_toast("Blink Alert!", message, duration=10)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and destroy the window
    cap.release()
    cv2.destroyAllWindows()
