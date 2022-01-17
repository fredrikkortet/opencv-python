import cv2 as cv

#image = cv.imread("Com/CatPicture.jpg")

#cv.imshow("Cat", image)

capture = cv.VideoCapture("Com/startrek.mkv")

while True:
    isTrue, frame= capture.read()
    cv.imshow("video", frame)

    if cv.waitKey(20) &0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
