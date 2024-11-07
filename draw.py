import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') # creating a dummy image , uint8 is datatype of image
# height , width, number of color channels .....np.zeros((500,500,3)

cv.imshow('Blank', blank) # it creates a blank image



# 1.Paint a image in certain color

# green image
blank[:] = 0, 255, 0     # blank[:] -- all pixels    , 0,255,0 is green color
cv.imshow('Green', blank)


# red image
blank[:] = 0, 0, 255  
cv.imshow('Red', blank)





# to color some part of image
blank1 = np.zeros((500,500,3), dtype='uint8')
blank1[200:300, 300:400] = 0,0,255
cv.imshow('somered', blank1)


# 2. Draw a Rectangle 
# method used rectangle(origin pixel, destination pixel, color, thickness=2)
blank2 = np.zeros((500, 500, 3), dtype='uint8')
cv.rectangle(blank2, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow('Rectanglegreenborder', blank2)

# method used rectangle(origin pixel, destination pixel, color, thickness=fill color of any)
#blank.shape[0] -- x axis, blank.shape[1] -- y axis
# fill the rectangle with color
blank3 = np.zeros((500, 500, 3), dtype='uint8')
cv.rectangle(blank3, (0,0), (250,400), (0,255,0), thickness=cv.FILLED) 
cv.imshow('Rectanglefilledgreen', blank3)

blank4 = np.zeros((500, 500, 3), dtype='uint8')
cv.rectangle(blank4, (0,0), (blank4.shape[1]//2, blank4.shape[0]//2), (0,255,0), thickness=-1) # instead of cv.FILLED use -1
cv.imshow('Rectanglegreenhalfscreen', blank4)


# 4. Draw circle
# use cv.circle(img, center, radius, color, thickness) method
blank5 = np.zeros((500, 500, 3), dtype='uint8')
cv.circle(blank5, (blank5.shape[1]//2, blank5.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank5)


# 5. Draw a line
# cv.line(img, starting, destination, color, thickness) method
blank6 = np.zeros((500, 500, 3), dtype='uint8')
cv.line(blank6, (0,0), (blank6.shape[1]//2, blank6.shape[0]//2), (255,255,255), thickness=3)
#cv.line(blank6, (164,90), (270,100), (255,255,255), thickness=3)
cv.imshow('Line', blank6)


# 5. Draw a text
# cv.putText(img, text, starting, fontFace, fontScale, color, thickness) method
blank7 = np.zeros((500, 500, 3), dtype='uint8')
cv.putText(blank7, 'Helloz', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Textonimage', blank7)

cv.waitKey(0)