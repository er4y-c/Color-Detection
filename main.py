import cv2
import numpy as np

blueLower = np.array([110,85,0])
blueUpper = np.array([168,255,255])
redLower = np.array([136, 87, 111])
redUpper = np.array([180, 255, 255])
greenLower = np.array([25, 52, 72])
greenUpper = np.array([100, 255, 255])
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        blurred = cv2.GaussianBlur(frame,(7,7),0)
        hsvImg = cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
        cv2.imshow("Blurlu Kayit",hsvImg)

        blueMask = cv2.inRange(hsvImg,blueLower,blueUpper)
        contours,hir= cv2.findContours(blueMask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        if len(contours)>0:
            for pic,contour_ in enumerate(contours):
                area = cv2.contourArea(contour_)
                if area>300:
                    x,y,wid,heig = cv2.boundingRect(contour_)
                    s = "x: {}, y: {}, genislik: {}, yukseklik: {}".format(np.round(x),np.round(y),np.round(wid),np.round(heig))
                    print(s)
                    cv2.rectangle(frame,(x,y),(x+wid,y+heig),(255,0,0))
                    cv2.putText(frame, "Mavi Renk", (x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,0,0))

        redMask = cv2.inRange(hsvImg,redLower,redUpper)
        contours,hir= cv2.findContours(redMask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        if len(contours)>0:
            for pic,contour_ in enumerate(contours):
                area = cv2.contourArea(contour_)
                if area>300:
                    x,y,wid,heig = cv2.boundingRect(contour_)
                    s = "x: {}, y: {}, genislik: {}, yukseklik: {}".format(np.round(x),np.round(y),np.round(wid),np.round(heig))
                    print(s)
                    cv2.rectangle(frame,(x,y),(x+wid,y+heig),(0,0,255))
                    cv2.putText(frame, "Kirmizi Renk", (x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255))
        
        greenMask = cv2.inRange(hsvImg,greenLower,greenUpper)
        contours,hir= cv2.findContours(greenMask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        if len(contours)>0:
            for pic,contour_ in enumerate(contours):
                area = cv2.contourArea(contour_)
                if area>300:
                    x,y,wid,heig = cv2.boundingRect(contour_)
                    s = "x: {}, y: {}, genislik: {}, yukseklik: {}".format(np.round(x),np.round(y),np.round(wid),np.round(heig))
                    print(s)
                    cv2.rectangle(frame,(x,y),(x+wid,y+heig),(0,255,))
                    cv2.putText(frame, "Yesil Renk", (x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0))                        
        cv2.imshow("Kayit",frame)            
        if cv2.waitKey(1) == ord("q"):
            break