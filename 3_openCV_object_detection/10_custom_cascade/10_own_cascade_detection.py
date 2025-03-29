# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 16:48:03 2025

@author: Orhan
"""

import cv2

path = "cascade.xml"
objectName = "Pencil"
frameWidth = 280
frameHeight = 360
color = (255, 0,0)

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):pass

# trackbar 

cv2.namedWindow("Result")
cv2.resizeWindow("Result", frameWidth, frameHeight + 100)

cv2.createTrackbar("Scale", "Result", 400, 1000, empty)
cv2.createTrackbar("Neighbor", "Result", 4, 50, empty)

cascade = cv2.CascadeClassifier(path)

while True:
    success, img = cap.read()
    
    if success:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        scaleVal = 1 + (cv2.getTrackbarPos("Scale", "Result")/1000)
        
        neighbor = cv2.getTrackbarPos("Neighbor", "Result")
        
        # Detection
        
        rects = cascade.detectMultiScale(gray, scaleVal, neighbor)
        
        for (x,y,w,h) in rects:
            
            cv2.rectangle(img, (x,y), (x+w, y+h), color, 3)
            cv2.putText(img, objectName, (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            
            cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord("q"): break
        