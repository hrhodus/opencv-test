import cv2
cap = cv2.VideoCapture(0)
print ("Input even for Color livefeed")
print ("Input odd for Grayscale livefeed")
a = int(raw_input())

while True:
    ret = False
    while ret == False:
        ret,frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if a % 2 == 0:
        frame = cv2.flip(frame,flipCode=1)
        cv2.imshow("frame",frame)
        cv2.waitKey(1)
    else:
        gray = cv2.flip(gray,flipCode=1)
        cv2.imshow("frame",gray)
        cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
