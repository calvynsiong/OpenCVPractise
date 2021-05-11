import cv2 as cv
import numpy as np


blank = np.zeros((400, 400), dtype="uint8")
rectangle = cv.rectangle(blank.copy(), (30, 30),
                         (370, 370), (255, 221, 244), -1)
circle = cv.circle(
    blank.copy(), (blank.shape[1]//2, blank.shape[0]//2), 200, (255, 221, 244), -1)

cv.imshow("rectangle", rectangle)
# cv.imshow("circle", circle)

# bitwise and (returns intersecting regions only)
# bitwise_and = cv.bitwise_and(circle, rectangle)
# cv.imshow("bitwise_and", bitwise_and)

# bitwise or (returns intersecting regions and non intersecting regions)
# bitwise_or = cv.bitwise_or(circle, rectangle)
# cv.imshow("bitwise_or", bitwise_or)


# bitwise xor (returns non intersecting regions only) or OR - AND
# bitwise_xor = cv.bitwise_xor(circle, rectangle)
# cv.imshow("bitwise_xor", bitwise_xor)

# bitwise not (returns not the image)
bitwise_not = cv.bitwise_not(circle)
cv.imshow("bitwise_not", bitwise_not)


cv.waitKey(0)
