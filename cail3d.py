# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 16:20:00 2017

@author: Lipo
"""

import cv2 
import numpy as np

def draw(img,pts):
    #print pts
    cv2.line(img,tuple(pts[0].ravel()),tuple(pts[1].ravel()),(0,0,255),5)
    cv2.line(img,tuple(pts[0].ravel()),tuple(pts[2].ravel()),(0,0,255),5)
    cv2.line(img,tuple(pts[3].ravel()),tuple(pts[2].ravel()),(0,0,255),5)
    cv2.line(img,tuple(pts[3].ravel()),tuple(pts[1].ravel()),(0,0,255),5)

    cv2.line(img,tuple(pts[-1].ravel()),tuple(pts[3].ravel()),(0,255,0),5)
    cv2.line(img,tuple(pts[0].ravel()),tuple(pts[4].ravel()),(0,255,0),5)
    cv2.line(img,tuple(pts[1].ravel()),tuple(pts[5].ravel()),(0,255,0),5)
    cv2.line(img,tuple(pts[2].ravel()),tuple(pts[6].ravel()),(0,255,0),5)

    cv2.line(img,tuple(pts[-1].ravel()),tuple(pts[-2].ravel()),(255,0,0),5)
    cv2.line(img,tuple(pts[-1].ravel()),tuple(pts[-3].ravel()),(255,0,0),5)
    cv2.line(img,tuple(pts[4].ravel()),tuple(pts[5].ravel()),(255,0,0),5)
    cv2.line(img,tuple(pts[4].ravel()),tuple(pts[6].ravel()),(255,0,0),5)
    
    return img
dist = np.load("/home/lipo/projects/comres/dist.npy")
mtx = np.load("/home/lipo/projects/comres/mtx.npy")

objps = np.zeros((4*3,3),np.float32)
objps[:,:2] = np.mgrid[0:4,0:3].T.reshape(-1,2)
#draw_ps = np.float32([[3,0,0],[0,3,0],[0,0,3]])
all_ps = np.float32([[0,0,0],[0,3,0],[3,0,0],[3,3,0],[0,0,3],[0,3,3],[3,0,3],[3,3,3]])
Capture = cv2.VideoCapture(0)
cv2.namedWindow("use")
while 1:
    _,img = Capture.read()
    if type(img) == type(None):
        continue
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,corners = cv2.findChessboardCorners(gray,(4,3),None)
    if ret:
        cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30,0.001))
        _,rvec,tvec,inliers = cv2.solvePnPRansac(objps,corners,mtx,dist,None,None)
        img_ps,_ = cv2.projectPoints(all_ps,rvec,tvec,mtx,dist)
        img = draw(img,img_ps)
    cv2.imshow("use",img)
    a = cv2.waitKey(33)
    if a != 255:
        break
cv2.destroyAllWindows()