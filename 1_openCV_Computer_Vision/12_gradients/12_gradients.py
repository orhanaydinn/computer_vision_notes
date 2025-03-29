# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 20:01:55 2025

@author: Orhan
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("sudoku.jpg", 0)
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")
plt.title("Orijinal Image")

"""
X Gradyan
"""
sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 1, dy = 0, ksize = 5) # depth is precision of each pixel
plt.figure()
plt.imshow(sobelx, cmap = "gray")
plt.axis("off")
plt.title("Sobel X")

"""
Y gradyan 
"""

sobely = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 0, dy = 1, ksize = 5) # depth is precision of each pixel
plt.figure()
plt.imshow(sobely, cmap = "gray")
plt.axis("off")
plt.title("Sobel Y")


"""
Laplacian  gradyan
"""

laplacian = cv2.Laplacian(img, ddepth = cv2.CV_16S)
plt.figure()
plt.imshow(laplacian, cmap = "gray")
plt.axis("off")
plt.title("Laplacian")
