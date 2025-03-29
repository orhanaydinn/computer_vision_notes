# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 19:47:29 2025

@author: Orhan
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("datai_team.jpg", 0)
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Original")

"""
    Erosion

"""

kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 1) # iteration = 1 demek bunu 1 kere yap demek
plt.figure()
plt.imshow(result, cmap="gray")
plt.axis("off")
plt.title("Erosion")


"""
# dilation 
# erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. 
# So we dilate it. Since noise is gone, they won't come back, but our object area increases.
result = cv2.dilate(img, kernel, iterations = 1) # iteration = 1 demek bunu 1 kere yap demek

"""

plt.figure()
plt.imshow(result, cmap="gray")
plt.axis("off")
plt.title("Dilation")


"""
    white noise

"""
whiteNoise = np.random.randint(low = 0, high = 2, size = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure()
plt.imshow(whiteNoise, cmap = "gray")
plt.axis("off")
plt.title("whiteNoise")

noise_img = whiteNoise + img
plt.figure()
plt.imshow(noise_img,cmap = "gray")
plt.axis("off")
plt.title("Img and whiteNoise")

"""
    Opening
    
"""
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure()
plt.imshow(opening,cmap = "gray")
plt.axis("off")
plt.title("Opening")

"""
# kapatma

"""
blackNoise = np.random.randint(low = 0, high = 2, size = img.shape[:2])
blackNoise = blackNoise*-255
black_noise_img = blackNoise + img
plt.figure()
plt.imshow(black_noise_img, cmap = "gray")
plt.axis("off")
plt.title("blackNoise")

black_noise_img[black_noise_img <= -245] = 0
plt.figure()
plt.imshow(black_noise_img, cmap = "gray")
plt.axis("off")
plt.title("Img and blackNoise")


closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure()
plt.imshow(closing,cmap = "gray")
plt.axis("off")
plt.title("closing")

# Morphological Gradient it is edge detection
# It is the difference between dilation and erosion of an image.
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure()
plt.imshow(gradient,cmap = "gray")
plt.axis("off")
plt.title("Morfolojik  Gradyan")

