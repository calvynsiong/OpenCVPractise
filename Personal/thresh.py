import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# 1. Simple thresholding
# threshold, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)
# cv.imshow("thresh", thresh)

# Inverse thresh
# threshold, thresh_inv = cv.threshold(gray, 200, 255, cv.THRESH_BINARY_INV)
# cv.imshow("thresh_inv", thresh_inv)
#


# 2. Adaptive thresholding
adaptive = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 10)
cv.imshow("adaptive", adaptive)



cv.waitKey(0)
