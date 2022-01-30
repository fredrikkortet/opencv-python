import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255,-1)
circle = cv.circle(blank.copy(), (200,200), 200, 255,-1)

cv.imshow("circle",circle)
cv.imshow("rectangle", rectangle)

#bitwise AND
bitAnd = cv.bitwise_and(rectangle, circle)
cv.imshow("AND", bitAnd)
#bitwise OR
bitOr = cv.bitwise_or(rectangle, circle)
cv.imshow("OR", bitOr)
#bitwise XOR
bitXor = cv.bitwise_xor(rectangle, circle)
cv.imshow("XOR", bitXor)
#bitwise NOT
bitNot = cv.bitwise_not(rectangle)
cv.imshow("NOT", bitNot)

cv.waitKey(0)