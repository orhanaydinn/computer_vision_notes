# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 14:59:12 2025

@author: Orhan
"""
#import Libraries

import cv2


#Open Photo
img = cv2.imread("messi5.jpg", 0)


cv2.imshow("First Photo", img)


#Keybord function
k = cv2.waitKey(0) &0xFF

if k == 27:
    cv2.destroyAllWindows()
    
elif k == ord('s'):
    cv2.imwrite("messi_gray.png", img)
    cv2.destroyAllWindows()

