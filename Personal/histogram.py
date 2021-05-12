
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# # Creating a mask
blank = np.zeros(img.shape[:2], dtype="uint8")
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("circle", circle)


mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow("mask", mask)
# # Grayscale histogram

# # Array of images, color channels, size, range
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

# plt.figure()  # Initializes figure
# plt.title("GrayScale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")

# # plt.plot(gray_hist)
# plt.xlim([0, 256])  # Creates limit
# plt.show()

# --------------------------
# Colored histograms

plt.figure()  # Initializes figure
plt.title("Colored Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

colors = ("b", 'g', 'r')
for i, col in enumerate(colors):  # Enumerate to use index for color channel
    # Tacks on blue, green and red on histogram
    # (Only focuses on overlap between mask and image)
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)  # Channel is red, green, and blue
    plt.xlim([0, 256])
plt.show()


cv.waitKey(0)
