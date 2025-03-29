# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 15:10:22 2025

@author: Orhan
"""

import cv2

#capture
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

#Record Video
writer = cv2.VideoWriter("record_video.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20,(width, height))

while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    
    # Save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break


cap.release()
writer.release()
cv2.destroyAllWindows()