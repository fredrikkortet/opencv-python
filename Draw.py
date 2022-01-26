import  cv2 as cv 
import numpy as np

#Create blank image 
blank = np.zeros((500,500,3), dtype="uint8")
cv.imshow("blank",blank)

# draw color on the picture
#blank[:] = 0,255,0
#cv.imshow("green", blank)

# draw figures
#rectangle
cv.rectangle(blank, (10,10), (250,250), (0,255,0), thickness=-1)
#circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40,(0,30,255),thickness=-1)
#line
cv.line(blank, (100,280), (23,400), (255,255,255),thickness=2)
# text
cv.putText(blank, "Star trek", (300,300), cv.FONT_HERSHEY_DUPLEX, 1.0, (255,0,0),2)
cv.imshow("blank",blank)
cv.waitKey(0)
