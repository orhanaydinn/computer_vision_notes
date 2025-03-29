# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 16:29:50 2025

@author: Orhan
"""

import cv2



# Resized
img = cv2.imread("Lenna_(test_image).png")
print("Picture Size: ", img.shape) # 512x512

cv2.imshow("Original", img)

imgResized = cv2.resize(img,(800,800))
print("Resized Img Shape: ", imgResized.shape)

cv2.imshow("Img Resized", imgResized)

# Crop

imgCropped = img[:200,0:300]   # width height -> height width
cv2.imshow("Cropped Picture", imgCropped)