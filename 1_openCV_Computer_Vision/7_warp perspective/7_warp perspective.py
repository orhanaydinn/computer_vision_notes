# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 17:36:29 2025

@author: Orhan
"""

import cv2
import numpy as np

# Open Picture

img = cv2.imread("kart.png")
cv2.imshow("Original", img)

width = 400
height = 500

pts1 = np.float32([[203,1], [1,472], [540,150], [338,617]])
pts2 = np.float32([[0,0], [0, height], [width,0], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)



imgOutput = cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("Rotate Picture", imgOutput)