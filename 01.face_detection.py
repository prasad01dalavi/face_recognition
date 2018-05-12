import cv2
import numpy as np

face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# load pre-trained face detection classifier
# For other pre-trained classifiers, visit the following link:
# https://github.com/opencv/opencv/tree/master/data/haarcascades

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    grayscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Need to convert into grayscaled to detect faces

    faces = face_detect.detectMultiScale(grayscaled_image, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # frame = image on which we are going to draw a rectangle
        # (x, y) = coordinates of the face
        # (x + w, y + h) = Height and Width
        # Green Color
        # width of the rectangle = 2px

    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
