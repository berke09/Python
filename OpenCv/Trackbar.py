import cv2
import numpy as np

def nothing(x):
    pass
cv2.namedWindow("berke") # trackbar pencere ismi
cam = cv2.VideoCapture(0)
cv2.createTrackbar("h1","berke",0,255,nothing) # first trackbar
cv2.createTrackbar("s1","berke",0,255,nothing) # second trackbar
cv2.createTrackbar("v1","berke",0,255,nothing) # third trackbar
cv2.createTrackbar("h2","berke",0,255,nothing) # first trackbar
cv2.createTrackbar("s2","berke",0,255,nothing) # second trackbar
cv2.createTrackbar("v2","berke",0,255,nothing) # third trackbar
cv2.createTrackbar("switch","berke",0,1,nothing)

kernel = np.ones((5,5),dtype=np.uint8)



while(cam.isOpened()):
    _,frame = cam.read()
    new = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("berke",new)
    H1 = cv2.getTrackbarPos("h1","berke")
    S1 = cv2.getTrackbarPos("s1","berke")
    V1 = cv2.getTrackbarPos("v1","berke")
    H2 = cv2.getTrackbarPos("h2","berke")
    S2 = cv2.getTrackbarPos("s2","berke")
    V2 = cv2.getTrackbarPos("v2","berke")
    switch = cv2.getTrackbarPos("switch","berke")

    if switch == 1:
        lower = np.array([H1,S1,V1])
        upper = np.array([H2,S2,V2])

    else :
        lower = np.array([0,0,0])
        upper = np.array([0,0,0])

    cv2.erode(frame,kernel,iterations=1)
    cv2.dilate(frame,kernel,iterations=1)
    mask = cv2.inRange(new,lower,upper)
    res = cv2.bitwise_and(new,new,mask=mask)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.waitKey(0)
cv2.destroyAllWindows()