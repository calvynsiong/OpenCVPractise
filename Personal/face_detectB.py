import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread("./Photos/group 1.jpg")
# img = cv.resize(img, (460, 427))
# cv.imshow("Lady", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
print(img.shape)
# crop = img[136:(136+266), 175:(175+266)]
# cv.imshow("gray", crop)


# Casecade
haar_Cascade = cv.CascadeClassifier("./haar_face.xml")


faces_rect = haar_Cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=1)
print(f"The number of faces is {len(faces_rect)}")

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv.imshow("faces", img)


cv.waitKey(0)
