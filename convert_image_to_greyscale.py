import cv2 as cv


img = cv.imread('Photos/carone.jpeg')

cv.imshow('Car', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Blur 
#blurring an mimage essentially removes some of the noise that exists in an image
#cv.GaussianBlur(img, kernel size odd number--more blur then more number here) method used

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade -- displays edges of image 
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image 
# increase the border of images created after edge Canny

dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# eroding - to get it back the image like edge cascade canny by dilated imag
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


# Cropping
cropped = img[10:20, 20:40]
cv.imshow('Cropped', cropped)

cv.waitKey(0)