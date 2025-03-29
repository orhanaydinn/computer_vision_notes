# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 14:36:35 2025

@author: Orhan
"""

import cv2
import matplotlib.pyplot as plt 

# open main photo

chos = cv2.imread("chocolates.jpg", 0)
plt.figure()
plt.imshow(chos, cmap= "gray")
plt.axis("off")

# open key photo 

cho = cv2.imread("nestle.jpg", 0)
plt.figure()
plt.imshow(cho, cmap= "gray")
plt.axis("off")


# orb 
# corner - edge 
orb = cv2.ORB_create()

# key point detector

kp1, des1 = orb.detectAndCompute(cho, None)
kp2, des2 = orb.detectAndCompute(chos, None)

# bf matcher 
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

# match point 
matches = bf.match(des1, des2)

# sort by distance
matches = sorted(matches, key = lambda x: x.distance)

# show the matches image 
plt.figure()
img_match = cv2.drawMatches(cho, kp1, chos, kp2, matches[:20], None, flags = 2)
plt.imshow(img_match)
plt.axis("off")

# sift 
sift = cv2.xfeatures2d.SIFT_create()

#bf 

bf = cv2.BFMatcher()

# key point detector with SIFT 
kp1, des1 = sift.detectAndCompute(cho, None)
kp2, des2 = sift.detectAndCompute(chos, None)

matches = bf.knnMatch(des1, des2, k = 2)

best_estimator = []

for match1, match2 in matches:
    
    if match1.distance < 0.75*match2.distance:
        best_estimator.append([match1])
        
plt.figure()
sift_matches = cv2.drawMatchesKnn(cho, kp1, chos, kp2, best_estimator, None, flags = 2)
plt.imshow(sift_matches)
plt.axis("off")





