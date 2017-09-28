import cv2
cap = cv2.VideoCapture(0)

while True:
    ret = False
    while ret == False:
        ret,frame = cap.read()
    frame = cv2.flip(frame,flipCode=1)
    cv2.imshow("frame",frame)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
