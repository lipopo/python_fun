# -*- coding: utf-8 -*-
"""
Created on Wed Aug 09 23:26:05 2017

@author: Lipo
"""
import cv2
import numpy as np

#deal用于响应按键的操作
deal = {}
Capture0 = cv2.VideoCapture(0)
Capture1 = cv2.VideoCapture(1)
cv2.namedWindow("fun~")

while 1:
    if not (Capture1.isOpened() and Capture0.isOpened()):
        break
    _,img0 = Capture0.read()
    _,img1 = Capture1.read()
    #灰度化
    img0_g = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
    img1_g = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    #局部二值化
    img0_a = cv2.adaptiveThreshold(img0_g,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,0)
    img1_a = cv2.adaptiveThreshold(img1_g,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,0)
    #形态学运算
    img0_c = cv2.morphologyEx(img0_a,cv2.MORPH_CLOSE,np.ones((7,7)))
    img1_c = cv2.morphologyEx(img1_a,cv2.MORPH_CLOSE,np.ones((7,7)))
    #边缘检测
    img0_c = cv2.Canny(img0_c,0,100)
    img1_c = cv2.Canny(img1_c,0,100)
    img0_t = cv2.resize(img0,(img0.shape[1]/3,img0.shape[0]))
    img1_t = cv2.resize(img1,(img1.shape[1]/3,img1.shape[0]))
    img_ = np.concatenate((img0_t,img1_t),axis=1)
    cv2.imshow("fun~",img_)
    key = cv2.waitKey(22)
    if key != -1:
        break


Capture.release()