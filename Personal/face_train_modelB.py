import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt


# people = ["Ben Affleck","Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]


people = []
for folder in os.listdir(r"./Faces/train"):
    people.append(folder)
print(people)

DIR = r"./Faces/train"
haar_Cascade = cv.CascadeClassifier("./haar_face.xml")


features = []  # image arrays of faces
labels = []  # labels who the faces belong to


def create_train():
    for person in people:
        path = os.path.join(DIR, person)  # creates path to each celebrity
        label = people.index(person)  # label to classify different celebs

        for image in os.listdir(path):
            # connects each image in the celebrity folder to a path
            img_path = os.path.join(path, image)

            img_array = cv.imread(img_path)
            # Reads each image and grayscales it

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # Creates rectangles that detects faces
            faces_rect = haar_Cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                # faces region of interest will be the cropped faces
                faces_roi = gray[y:y+h, x:x+w]
                # Adds cropped faces to features list with corresponding labels
                features.append(faces_roi)
                labels.append(label)


create_train()
print(f"The length of features is {len(features)}")
print(f"The length of labels is {len(labels)}")
print("Training done------")

# Convery features and labels to numpy arrays
features = np.array(features, dtype="object")
labels = np.array(labels)


face_recognizer = cv.face.LBPHFaceRecognizer_create()  # face_recognizer training
face_recognizer.save("face_trained.yml")

# Trains the features and labels together
face_recognizer.train(features, labels)

np.save("features.npy", features)  # Saves numpy files
np.save("labels.npy", labels)
