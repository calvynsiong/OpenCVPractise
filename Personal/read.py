import cv2 as cv
# %% Images
# # img = cv.imread("./Photos/cat_large.jpg")

# # cv.imshow("Cat", img)


# %% Videos
import cv2 as cv

capture = cv.VideoCapture("./Videos/dog.mp4")  # Stores the video as a capture variable

while True:
    # Bool that conveys if the video is played and frame for reading each video frame
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)  # Show each frame as video
    if cv.waitKey(20) & 0xFF == ord("d"):  # Stops the video when 20s reach or when letter d is pressed
        break
capture.release() #removes the capture
cv.destroyAllWindows() #destroys the video

cv.waitKey(0)

# %%
