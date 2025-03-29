# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 17:12:47 2025

@author: Orhan
"""

import cv2
import numpy as np


# Create Picture

img = np.zeros((512,512,3), np.uint8)
print(img.shape)

cv2.imshow("Siyah", img)

# line

# Picture start point
cv2.line(img, (100,100), (100,300),(0,255,0), 3) # BGR = (0,255,0)
cv2.imshow("Line", img)

#Create rectangle
#(img, start point, color )
cv2.rectangle(img, (0,0), (256,256), (255, 0, 0))
cv2.imshow("Rectangle", img)

cv2.rectangle(img, (0,0), (256,256), (255, 0, 0), cv2.FILLED)
cv2.imshow("Rectangle", img)


#Circle
#(img, center, radius, color)
cv2.circle(img, (300,300), 45, (0,0,255))
cv2.imshow("Circle", img)

cv2.circle(img, (300,300), 45, (0,0,255), cv2.FILLED)
cv2.imshow("Circle", img)

#Text
#(img, start point, font, thickness, color)
cv2.putText(img, "Picture", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Text", img)