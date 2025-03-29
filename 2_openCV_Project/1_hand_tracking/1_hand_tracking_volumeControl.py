# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 16:45:36 2025

@author: Orhan
"""

import cv2
import time
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Ses kontrolü için pycaw ayarları
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Minimum ve maksimum ses seviyeleri belirle
vol_min, vol_max, _ = volume.GetVolumeRange()

cap = cv2.VideoCapture(0)

mpHand = mp.solutions.hands
hands = mpHand.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

# Mesafe için min ve max sınırlar belirle
MIN_DISTANCE = 30
MAX_DISTANCE = 200

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHand.HAND_CONNECTIONS)
            
            h, w, c = img.shape
            thumb_tip = None
            index_tip = None
            
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                if id == 4:  # Başparmak ucu
                    thumb_tip = (cx, cy)
                    cv2.circle(img, (cx, cy), 9, (255, 0, 0), cv2.FILLED)
                
                if id == 8:  # İşaret parmağı ucu
                    index_tip = (cx, cy)
                    cv2.circle(img, (cx, cy), 9, (255, 0, 0), cv2.FILLED)
            
            # Eğer iki nokta tespit edildiyse mesafeyi hesapla
            if thumb_tip and index_tip:
                x1, y1 = thumb_tip
                x2, y2 = index_tip
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                
                # Çizgi çiz ve mesafeyi ekrana yaz
                cv2.line(img, thumb_tip, index_tip, (0, 255, 0), 3)
                cv2.putText(img, f'{int(distance)} px', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                
                # Mesafeyi 0-1 arasında normalize et
                distance = max(MIN_DISTANCE, min(distance, MAX_DISTANCE))
                volume_level = ((distance - MIN_DISTANCE) / (MAX_DISTANCE - MIN_DISTANCE)) * (vol_max - vol_min) + vol_min
                
                # Ses seviyesini ayarla
                volume.SetMasterVolumeLevel(volume_level, None)
    
    # FPS hesapla ve ekrana yazdır
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    cv2.putText(img, f"FPS: {int(fps)}", (10, 75),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
    
    cv2.imshow("img", img)
    cv2.waitKey(1)
