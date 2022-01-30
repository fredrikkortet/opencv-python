import cv2 as cv

img = cv.imread("Com/CatPicture.jpg")
cv.imshow("cat", img)

#normal blur
normal = cv.blur(img,(3,3))
cv.imshow("normal blur",normal)

#gaussian Blur 
gauss = cv.GaussianBlur(img, (3,3),0)
cv.imshow("gaussian",gauss)

# median blur
median = cv.medianBlur(img,3)
cv.imshow("median blur", median)

#bilateral blur
bilateral = cv.bilateralFilter(img, 3, 15, 15)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)