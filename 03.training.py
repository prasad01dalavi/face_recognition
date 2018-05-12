import os
import cv2
import numpy as np
from PIL import Image  # Python Image Library
import time
recognizer = cv2.createLBPHFaceRecognizer()


def get_images_with_ids():
    image_paths = [os.path.join('dataset', file_name)
                   for file_name in os.listdir('dataset')]
    # image_paths list

    faces = []  # stores list of numpy array of face images
    ids = []    # stores id associated with each image

    for image_path in image_paths:
        face_image = Image.open(image_path).convert('L')
        # open the image with PIL

        face_np = np.array(face_image, 'uint8')
        # convert PIL image to numpy array of that image
        faces.append(face_np)
        cv2.imshow('img', face_np)

        id_ = int(os.path.split(image_path)[-1].split('.')[1])
        ids.append(id_)
    return faces, ids

faces, ids = get_images_with_ids()
# get the numpy array of list of face images and ids

recognizer.train(faces, np.array(ids))  # training
recognizer.save('recognizer/training_data.yml')
# Save the training data, note the format of file
print 'Training Success!'
