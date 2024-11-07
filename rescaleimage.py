import cv2 as cv









def rescaleFrame(frame, scale=0.75):  #scale by default is 0.75    resized by 0.75
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



#image resized
img = cv.imread('Photos/carone.jpeg')
cv.imshow('Car', img)


resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)




# Resizing and rescaling images
# Resize video

capture = cv.VideoCapture('Videos/car_video.mp4')

while True:
    isTrue, frame = capture.read() # this reads a video frame by frame, isTrue says whether the frame successful come
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video', frame) # to display each frame of video imshow used
    
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'): # if d is press then break the video
        break

capture.release() # release the video of capture
cv.destroyAllWindows() # destroy the video of capture
    
