import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True:
    success,img = cap.read()
    
    code = decode(img)
    for i in code:
        mytext = i.data.decode('utf-8')
        points = np.array([i.polygon],np.int32)
        rect_points = i.rect
        cv2.polylines(img,[points],True,(0,255,0),3)
        cv2.putText(img,mytext,(rect_points[0],rect_points[1]),cv2.FONT_HERSHEY_PLAIN,0.9,(0,255,0),1)
        print(mytext)

    cv2.imshow('result',img)
    cv2.waitKey(2)




