# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 17:08:00 2017

@author: Lipo
"""
#这段代码用于演示如何使用matplotlib 绘制三维散点图 并使用自定义marker
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#这里新建一个图形x,y,z随机生成
figure = plt.figure(1)
#创建三维图形
#ax = plt.subplot(111,projection='3d')
#初始化数据
x = np.random.randint(0,255,100)
y = np.random.randint(0,255,100)
z = np.random.randint(0,255,100)
marker = np.random.randint(0,10,100)
for i in range(10):
    ax = plt.subplot2grid((5,2),(i/2,0),projection='3d') if i%2 == 0 else plt.subplot2grid((5,2),((i-1)/2,1),projection='3d')
    dw = np.where(marker==i)[0]
    ax.scatter3D(x[dw],y[dw],z[dw],marker=".$%d$"%i)
    ax.plot3D(x[dw],y[dw],z[dw])

plt.show()