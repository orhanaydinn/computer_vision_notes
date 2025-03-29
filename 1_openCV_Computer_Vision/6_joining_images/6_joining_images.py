# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 17:31:39 2025

@author: Orhan
"""

import cv2
import numpy as np

#open picture

img = cv2.imread("Lenna_(test_image).png")
cv2.imshow("Original", img)

# HORIZONTAL 
hor = np.hstack((img,img))
cv2.imshow("Horizontal", hor)


# VERTICAL 
ver = np.vstack((img,img))
cv2.imshow("Vertical", ver)


