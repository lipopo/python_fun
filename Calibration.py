# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:57:00 2017

@author: Lipo
"""

import cv2
import numpy as np 

Capture = cv2.VideoCapture(0)
objq = np.zeros((4*3,3),np.float32)
objq[:,:2] = np.mgrid[0:4,0:3].T.reshape(-1,2)
img_ps = []
obj_ps = []
criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30,0.001)
count = 0
while 1:
    _,img = Capture.read()
    if type(img) == type(None):
        continue
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,corners = cv2.findChessboardCorners(gray,(4,3),None)
    if ret:
        obj_ps.append(objq)
        cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        img_ps.append(corners)
        img = cv2.drawChessboardCorners(img,(4,3),corners,ret)
        count += 1
    cv2.imshow("use",img)
    a = cv2.waitKey(33)
    if a != 255 or count > 10:
        break
#计算相机参数并保存
ret,mtx,dist,rvecs,tvecs = cv2.calibrateCamera(obj_ps,img_ps,gray.shape[::-1],None,None)
np.save("/home/lipo/projects/comres/mtx",mtx)
np.save("/home/lipo/projects/comres/dist",dist)
cv2.destroyAllWindows()

