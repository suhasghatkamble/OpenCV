import cv2 as cv
import numpy as np 


img = cv.imread('Photos/carone.jpeg')

cv.imshow('image', img)


# OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library



#transformation of image means shifting image to x and y , left right
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y =--> Down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)



# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)

# rotate_anticlockwise
rotated_anticlock = rotate(img, 45)
cv.imshow('Rotated anticlock', rotated_anticlock)

# rotate_clockwise
rotated_clock = rotate(img, -45)
cv.imshow('Rotated clock', rotated_clock)

# rotate rotated clockwise image
rotated_rotated = rotate(rotated_clock, -45)
cv.imshow('Rotated Rotated', rotated_rotated)

# rotate image with clockwise
rotate_image = rotate(img, -90)
cv.imshow('Rotate image', rotate_image)

# Resizing
#INTER_CUBIC gives better images
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping 
# flipCode - 0 (flip image vertically)
#1 - (flip image horizontally )
# -1 (flip image both vertically and horizontally)

#vertically
flip_vertically = cv.flip(img, 0)
cv.imshow('Vertically Flip', flip_vertically)

#horizontally
flip_horizontally = cv.flip(img, 1)
cv.imshow('Horizontally Flipping', flip_horizontally)

#both
flip_both = cv.flip(img, -1)
cv.imshow('image both flip', flip_both)

cv.waitKey(0)