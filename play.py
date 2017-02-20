"""
Created on Mon Sep 12 22:43:55 2016

@author: JP
"""

import numpy as np
import cv2

try:
    cap = cv2.VideoCapture(0)
except:
    cap.release()
    cap = cv2.VideoCapture(0)

cap.set(3,800)
cap.set(4,600)

Detect_bool = False

Play_array = np.zeros([1,2], dtype=tuple)

def Detect(img_c):
    img_hsv = cv2.cvtColor(img_c, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", img_hsv)

    rows, cols, chan = img_hsv.shape

    lower = np.array([104, 50, 50], dtype = "uint8")
    upper = np.array([108, 255, 255], dtype = "uint8")

    mask = cv2.inRange(img_hsv, lower, upper)

    contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

    max_cnt = []
    max_cnt_area = 0
    for h, cnt in enumerate(contours):
        area = int(np.ceil(cv2.contourArea(cnt)))
        if area > max_cnt_area:
            max_cnt = cnt
            max_cnt_area = area

    if max_cnt != []:
        M = cv2.moments(max_cnt)
        cx = int(M["m10"]/M["m00"])
        cy = int(M["m01"]/M["m00"])
    else:
        return tuple([0, 0])

    return tuple([cx, cy])


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    img = np.copy(frame)

    if Detect_bool:
        D = Detect(img)
        Play_array = np.vstack((D, Play_array))
        for i, p in enumerate(Play_array):
            if i <= 25 and p[0] != 0 and p[1] != 0 and Play_array[i+1, 0] != 0 and Play_array[i+1, 1] != 0:
                cv2.line(img, tuple(p), tuple(Play_array[i+1]), (0,0,0), 100-i*4+10)
        for i, p in enumerate(Play_array):
            if i <= 25 and p[0] != 0 and p[1] != 0 and Play_array[i+1, 0] != 0 and Play_array[i+1, 1] != 0:
                cv2.line(img, tuple(p), tuple(Play_array[i+1]), (255,0,0), 100-i*4)

    # Display the resulting frame
    cv2.imshow("Image",img)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break
    elif k == ord("d"): # Recalc pts
        Detect_bool = not Detect_bool


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()