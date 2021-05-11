# %%

import cv2 as cv
import numpy as np

img = cv.imread("./Photos/cats.jpg")
cv.imshow("Base", img)
# Averaging (Applying the average pixel density to a kernal)
# blur = cv.blur(img, (3, 3))
# cv.imshow("blur", blur)


# # Gaussian
# Gblur = cv.GaussianBlur(img, (3, 3), 0)
# cv.imshow("Gblur", Gblur)

# # Median blur
# Mblur = cv.medianBlur(img, 3, 0)
# cv.imshow("Mblur", Mblur)

# Bilateral blurring
Bblur = cv.bilateralFilter(img, 10, 55, 55)
cv.imshow("Bblur", Bblur)


cv.waitKey(0)
