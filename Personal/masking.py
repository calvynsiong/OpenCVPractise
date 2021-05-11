import cv2 as cv
import numpy as np


img = cv.imread("./Photos/cats.jpg")
blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Base", img)
cv.imshow("blank", blank)


# Mask
# mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2+45,), 100, 255, -1)
mask = cv.rectangle(blank, (30, 30), (300, 300), 255, -1)
cv.imshow("mask", mask)

masked = cv.bitwise_or(img, img, mask=mask)
cv.imshow("Masked", masked)

cv.waitKey(0)
