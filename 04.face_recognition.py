import cv2
import numpy as np
import sqlite3     # for database operations

face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# load pre-trained face detection classifier

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('recognizer/training_data.yml')

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX


def get_profile(id_):  # Returns all data from the database for that id
    profile = None
    connection = sqlite3.connect("lmtech_database.db")
    query = "SELECT * FROM Persons WHERE ID=" + str(id_)
    response = connection.execute(query)  # run the query
    for record in response:
        profile = record
    connection.close()
    return profile


def show_profile(profile_id):  # shows id related information on image
    cv2.putText(frame, 'Name: ' + get_profile(profile_id)[1], (x, y + h + 30),
                font, 0.5, (0, 200, 0), 1)
    cv2.putText(frame, 'Age: ' + str(get_profile(profile_id)[2]), (x, y + h + 50),
                font, 0.5, (0, 200, 0), 1)
    cv2.putText(frame, 'Gender: ' + str(get_profile(profile_id)[3]), (x, y + h + 70),
                font, 0.5, (0, 200, 0), 1)
    cv2.putText(frame, 'Designation: ' + str(get_profile(profile_id)[4]), (x, y + h + 90),
                font, 0.5, (0, 200, 0), 1)


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

        id_, confidence = recognizer.predict(
            grayscaled_image[y:y + h, x:x + w])
        # here confidence is relatively opposite
        # means lesser the value, more will be the accuracy

        if id_ == 1 and confidence < 50:
            show_profile(1)

        elif id_ == 2 and confidence < 50:
            show_profile(2)

        elif id_ == 3 and confidence < 50:
            show_profile(3)

    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
