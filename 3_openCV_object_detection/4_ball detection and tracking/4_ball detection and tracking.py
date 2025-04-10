# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 13:04:55 2025

@author: Orhan
"""

import cv2
import numpy as np

from collections import deque

buffer_size = 16
pts = deque(maxlen = buffer_size)

# HSV format for BLUE COLOR 

blueLower = (84, 98, 0)
blueUpper = (179, 255, 255)

# CAPTURE

cap = cv2.VideoCapture(0)
cap.set(3,960)
cap.set(4,480)

while True:
    
    success, imgOriginal = cap.read()
    
    if success:
        
        # blur
        blurred = cv2.GaussianBlur(imgOriginal, (11,11), 0)
        
        # hsv 
        
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
           
        cv2.imshow("HSV Image", hsv)
        
        # crate mask for blue 
        
        mask = cv2.inRange(hsv, blueLower, blueUpper)
        cv2.imshow("mask Image", mask)
        
        mask = cv2.erode(mask,None, iterations = 2)
        mask = cv2.dilate(mask, None, iterations = 2)
        cv2.imshow("Mask + Erode", mask)
        
        # find contours
        
        contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        center = None 
        
        if len(contours) > 0:
            
            # find biggiest contours
            
            c = max(contours, key = cv2.contourArea)
            
            # turn the rectangle
            
            rect = cv2.minAreaRect(c)
            ((x, y), (width, height), rotation) = rect
            
            s = "x: {}, y: {}, width: {}, height: {}, rotation: {}".format(np.round(x), np.round(y), np.round(width), np.round(height), np.round(rotation))
            print(s)
            
            # box
            
            box = cv2.boxPoints(rect)
            box = np.int64(box)

            # moments            
            M = cv2.moments(c)
            center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
            
            # draw counter 
            
            cv2.drawContours(imgOriginal, [box], 0, (0, 255, 255), 2)
            
            # draw point in the centers
            
            cv2.circle(imgOriginal, center, 5, (255, 0, 255), -1)
            
            # Write information on the secreen
            
            cv2.putText(imgOriginal, s, (25,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,255), 2)
            
        cv2.imshow("Orijinal Tespit", imgOriginal)
            
        
        
    if cv2.waitKey(1) & 0xFF == ord("q"):break