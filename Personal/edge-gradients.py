import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread("./Photos/park.jpg")
cv.imshow("Boston", img)
img = cv.resize(img, (460, 427))


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# 1. Laplacian
# lap = cv.Laplacian(gray, cv.CV_64F)
# lap = np.uint8(np.absolute(lap))
# cv.imshow("Laplacian", lap)
#


# 2. Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 1)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined = cv.bitwise_or(sobelx, sobely)

cv.imshow("sobelx", sobelx)
cv.imshow("sobely", sobely)
cv.imshow("combined", combined)

#

canny = cv.Canny(gray, 125, 175)
cv.imshow("canny", canny)


cv.waitKey(0)
