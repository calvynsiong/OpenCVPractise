# import cv2 as cv
# # %% Images
# img = cv.imread("./Photos/cat_large.jpg")

# cv.imshow("Cat", img)


# # %% Videos
# import cv2 as cv

# # Stores the video as a capture variable
# capture = cv.VideoCapture("./Videos/dog.mp4")

# while True:
#     # Bool that conveys if the video is played and frame for reading each video frame
#     isTrue, frame = capture.read()
#     cv.imshow("Video", frame)  # Show each frame as video
#     # Stops the video when 20s reach or when letter d is pressed
#     if cv.waitKey(20) & 0xFF == ord("d"):
#         break
# capture.release()  # removes the capture
# cv.destroyAllWindows()  # destroys the video

# cv.waitKey(0)

# # %%

# import cv2 as cv

# def changeRes(width,height): #Only works on live video
#     capture.set(3,width) #3 references width
#     capture.set(4,height) #4 references height


# def rescaleFrame(frame, scale=0.75):
#     height = int(frame.shape[0]*scale)
#     width = int(frame.shape[1]*scale)
#     dimensions = (width, height)
# img = rescaleFrame(cv.imread("./Photos/cat_large.jpg"), .2)

# cv.imshow("Cat", img)

#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
# capture = cv.VideoCapture("./Videos/dog.mp4")

# while True:
#     # Bool that conveys if the video is played and frame for reading each video frame
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame, .2)
#     # cv.imshow("Video", frame)  # Show each frame as video

#     cv.imshow("Video", frame)  # Show each frame as video
#     cv.imshow("Video2", frame_resized)  # Show each frame as video
#     # Stops the video when 20s reach or when letter d is pressed
#     if cv.waitKey(20) & 0xFF == ord("d"):
#         break
# capture.release()  # removes the capture
# cv.destroyAllWindows()  # destroys the video

# cv.waitKey(0)

# %%
# import cv2 as cv
# import numpy as np

# 500,500 (height * width) means a 500 by 500 zero array data type = uint8 makes it be recognized as an image
# blank = np.zeros((500, 500, 3), dtype="uint8")
# Painting the entire image a certain color
# (x,y coordinates going right,down)
# cv.rectangle(
#     blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//3), (0, 255, 0), cv.FILLED)
# cv.imshow("Rectangles", blank)

# cv.waitKey(0)

# Drawing a circle

# cv.circle(blank, (250, 250), 50, (0, 0, 255), -1)
# cv.imshow("Circles", blank)
# cv.waitKey(0)

# Drawing a line

# cv.line(blank, (0, 0), (250, 450), (0, 0, 255), 3)
# cv.imshow("Line", blank)
# cv.waitKey(0)

# Writing text
# cv.putText(blank, "LesGo",
#            (blank.shape[1]//2, blank.shape[0]//3), cv.FONT_HERSHEY_TRIPLEX, 1.5, (0, 255, 0), 3)
# cv.imshow("Text", blank)
# cv.waitKey(0)
# %%

# img = cv.imread("./Photos/cat.jpg")

# 1) grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Cat", gray)

# 2) blur
# blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)


# 3) Edge cascading to detect edges
# canny accepts lower and upper thresholds and if the edge is between that then it is detected)
# canny = cv.Canny(img, 125, 275)

# 4) Dilating image
# dilated = cv.dilate(canny, (3, 3), iterations=3)

# 5 Eroding images

# erode = cv.erode(dilated, (3, 3), iterations=3)

# 6) resize and crop

# cv.imshow("Normal", img)
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cropped = img[0:500, 0:500]
# cv.imshow("resized", resized)
# cv.imshow("cropped", cropped)


# cv.waitKey(0)

# %%
import cv2 as cv
import numpy as np

img = cv.imread("./Photos/cats.jpg")


# Translation
# def translate(img, x, y):
#     transMat = np.float32([[1, 0, x], [0, 1, y]])  # Creating a datatype
#     # Creating dimensions with width and height
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMat, dimensions)
# translated = translate(img, -100, 100)
# cv.imshow("translated", translated)
# -x --> left, +x --> right
# -y --> uo, +y --> down

# Rotation
# def rotate(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]

#     if rotPoint is None:
#         rotPoint = (width//2, height//2)
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1)
#     dimensions = (width, height)
#     return cv.warpAffine(img, rotMat, dimensions)
# rotated = rotate(img, -45)
# rotated2 = rotate(img, -90)
# cv.imshow("rotated", rotated)
# cv.imshow("rotated2", rotated2)


# Flipping

# flip = cv.flip(img, 0)  # 0 = x axis, 1 = y axis, 01 - both axis
# cropped = img[200:400, :]


# %%
blank = np.zeros(img.shape, dtype="uint8")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)

# Contours

# contours, hierachies = cv.findContours(
#     canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)  # RETR_LIST returns all the contours/ RETR_EXTERNAL returns external ones, #CHAIN_APPROX_NONE returns all (no approximations, CHAIN_APPROX_SIMPLE compresses the contours line into 2 points-> start and end)

# cv.imshow("blur", blur)
# cv.imshow("canny", canny)


# Turning type into binary
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
contours, hierachies = cv.findContours(
    thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"The contours has a length of {len(contours)}")
# -1 means all contours are drawn
cv.drawContours(blank, contours, -1, (0, 255, 255), 1)
cv.imshow("blank", blank)
cv.imshow("canny", canny)


cv.waitKey(6000)
