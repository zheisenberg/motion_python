#!/usr/bin/python
# coding: utf-8
#this is a python program for motionloft
#

import numpy as np
import cv2


######
import kmeans
######
print '*****************here is the main program**************'
print ' '
print ' ' 
print ' '
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("1.mp4")

fgbg = cv2.BackgroundSubtractorMOG()


while(1):
    
    ret,frame = cap.read()  #frame is BGR, all processing from here
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #total 190, change to GRAY
    # print frame.dtype #frame is unit8
    
    ret, thresh = cv2.threshold(frame, 127, 255, 0)
    frame, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[4]
    cv2.drawContours(frame, contours, 0, [cnt], 0, (0,255,0), 3)
    print "step 1: background segmentation"
    fgmask = fgbg.apply(frame)
    fgmask_inv = ~fgmask
    #res2 = kmeans.kmeans(fgmask_inv, 2) #kmeans
#
    cv2.imshow("current camera", fgmask)
    
    k = cv2.waitKey(60) & 0xff
    if k == 27:
       break
            
cv2.destroyAllWindows()
cap.release()

