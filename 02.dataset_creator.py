import cv2
import numpy as np
import sqlite3

face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# load pre-trained face detection classifier


def insert_update_database(id_, name):
    connection = sqlite3.connect("lmtech_database.db")
    query = "SELECT * FROM Persons WHERE ID=" + str(id_)
    response = connection.execute(query)
    user_exists = 0

    for record in response:
        user_exists = 1   # Record already exists

    if user_exists:
        query = "UPDATE Persons SET Name='" + \
            name + "'" + " WHERE ID=" + str(id_)
        print 'Existing Person Details have been updated!'
    else:
        # following query will create new record in table
        query = "INSERT INTO Persons(ID, Name) Values(" + \
            str(id_) + ", '" + name + "')"
        print query
        print 'New Person added Successfully!!'

    connection.commit()        # save the changes in db
    connection.close()         # Close the connection to the db

id_ = input("*Please Enter your ID: ")
name = raw_input("*Your Name: ")
insert_update_database(id_, name)
# Call the function to create database entry

cap = cv2.VideoCapture(0)  # start the webcam to capture images

dataset_count = 1

while True:
    ret, frame = cap.read()
    grayscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Need to convert into grayscaled to detect faces

    faces = face_detect.detectMultiScale(grayscaled_image, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.imwrite('dataset/user.' + str(id) + '.' + str(dataset_count) +
                    '.jpg', grayscaled_image[y:y + h, x:x + w])
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # frame = image on which we are going to draw a rectangle
        # (x, y) = coordinates of the face
        # (x + w, y + h) = Height and Width
        # Green Color
        # width of the rectangle = 2px

        print 'Completed ', str(float(dataset_count) * 100 / 500.0)[:5], "%"
        dataset_count += 1

    cv2.imshow('Webcam', frame)
    if dataset_count > 500:
        break   # Stop when 20 images has been capturedq

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
