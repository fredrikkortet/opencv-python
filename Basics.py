import cv2 as cv

image = cv.imread("Com/CatPicture.jpg")
# grey scale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

#blur
blur = cv.GaussianBlur(image, (3,3), cv.BORDER_DEFAULT)

#edge cascade
canny = cv.Canny(blur, 125,175)
#dilating the image
dilated = cv.dilate(canny, (3,3),iterations=3)
#Eroding
eroded = cv.erode(dilated, (3,3),iterations=3)

#Resize
resized = cv.resize(image, (500,500),interpolation=cv.INTER_CUBIC)

#cropping
crop = image[400:600, 500:700]

#cv.imshow("Cat", image)
#cv.imshow("Cat gray", gray)
#cv.imshow("Cat blur", blur)
#cv.imshow("Cat canny edges",canny)
#cv.imshow("Dilated cat",dilated)
#cv.imshow("Eroding Cat",eroded)
#cv.imshow("resized cat", resized)
cv.imshow("cropped",crop)
cv.waitKey(0)