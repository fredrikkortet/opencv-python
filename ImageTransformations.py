import cv2 as cv
import numpy as np
image = cv.imread("Com/CatPicture.jpg")

#cv.imshow("cat", image)
#move picture 
# -x -> left -y -> up
# x -> right y -> down
def translate(image, x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, transMat, dimensions)

translated = translate(image,100,100)
#cv.imshow("translated",translated)
# Rotate picture
def rotate(image, angle,rotPoint=None):
    (height,width) = image.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)  
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(image, rotMat, dimensions)

rotated = rotate(image, -45)
#cv.imshow("Rotated", rotated)
#resize
flip = cv.flip(image,0)
cv.imshow("flip", flip)
cv.waitKey(0)
