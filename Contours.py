import cv2 as cv
import numpy as np

image = cv.imread("Com/CatPicture.jpg")
cv.imshow("Cat",image)
blank = np.zeros(image.shape, dtype="uint8")
cv.imshow("blank",blank)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Gray cat",gray)

#blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
#cv.imshow("blur", blur)

#canny = cv.Canny(blur, 125, 175)
#cv.imshow("canny Cat", canny)

#threshold 
ret, thresh = cv.threshold(gray, 125, 255,cv.THRESH_BINARY)
cv.imshow("thresh", thresh)

contours , hierarchies  = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contour(s) found!")

cv.drawContours(blank, contours, -1, (0,0,255),1)
cv.imshow("Contours", blank)
cv.waitKey(0)