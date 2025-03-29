# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 21:35:20 2025

@author: Orhan
"""

import cv2
import mediapipe as mp

cap = cv2.VideoCapture("video3.mp4")




mpFaceDetection = mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection(0.25)

mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = faceDetection.process(imgRGB)
    #print(results.detections)
    
    
    if results.detections:
        for id, detections in enumerate(results.detections):
            bboxC = detections.location_data.relative_bounding_box
            #print(bboxC)
            h, w, c = img.shape
            bbox = int(bboxC.xmin*w), int(bboxC.ymin*h), int(bboxC.width*w), int(bboxC.height*h)
            #print(bbox)
            cv2.rectangle(img, bbox, (0,255,255),2)
            
            
            
    cv2.imshow("img", img)
    cv2.waitKey(10)