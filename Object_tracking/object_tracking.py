# Importing the libraries
import cv2

# Creating tracker
tracker = cv2.TrackerCSRT_create()

# Reading video
video = cv2.VideoCapture('race.mp4')
##Read first frame of the video
success, frame = video.read()

# Track region on first frame and for drawing bounding box on that frame
bbox = cv2.selectROI(frame)

# Track the first frame
success = tracker.init(frame, bbox)

# Reading and tracking all frames
while True:
    success, frame = video.read()
    if not success:
        break
    sucess, bbox = tracker.update(frame)

    # draw bounding box
    if sucess:
        (x, y, w, h) = [int(i) for i in bbox]  # Copying Information of bbox
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
    else:
        cv2.putText(frame, 'Error', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27:  # ESC key 
        break
