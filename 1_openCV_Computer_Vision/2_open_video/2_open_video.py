# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 14:58:15 2025

@author: Orhan
"""

import cv2
import time

#Add video name
video_name = "MOT17-04-DPM.mp4"


cap = cv2.VideoCapture(video_name)


print("Genislik: ", cap.get(3))
print("Genislik: ", cap.get(4))

if cap.isOpened() == False:
    print("Hata")
  
    
while True:
    ret, frame = cap.read()

    if ret == True:
        time.sleep(0.01) # If dont use time.sleep(), The video play very fast
    
        cv2.imshow("Video", frame)
    
    else: break 
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release() # stop capture
cv2.destroyAllWindows()
