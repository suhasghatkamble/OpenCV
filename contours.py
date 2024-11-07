#
# contours meaning an outline representing or bounding the shape or form of something

import cv2 as cv

img = cv.imread('Photos/carone.jpeg')

cv.imshow('Car', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)


cv.waitKey(0)