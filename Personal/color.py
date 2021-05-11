# %%

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./Photos/park.jpg")
cv.imshow("Boston", img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

# HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("hsv", hsv)

# Lab
# lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
# cv.imshow("lab", lab)

# RGB
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow("rgb", rgb)

# plt.imshow(rgb)
# plt.show()


# %%


# split

b, g, r = cv.split(img)

# cv.imshow("b", b)
# cv.imshow("g", g)
# cv.imshow("r", r)
# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)


# merge
merged = cv.merge([b, g, r])
# cv.imshow("merged", merged)


blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)


cv.waitKey(0)
