# -*- coding: utf-8 -*-
# http://docs.gimp.org/en/plug-in-convmatrix.html
import cv2
import numpy

im=cv2.imread('jpg/origin.jpg')
b,g,r=cv2.split(im)
a1=numpy.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
a2=numpy.array([[-2,-1,0],[-1,1,1],[0,1,2]])
a3=numpy.array([[0,0,0],[-1,1,0],[0,0,0]])

def cnn(x):
    result =numpy.empty((297,297),dtype=numpy.float)
    for i in range(0, 297):
        for j in range(0, 297):
            temp = x[i:i + 3, j:j + 3] * a3
            result[i][j]=(temp.sum())
    return result

b1=cnn(b)
g1=cnn(g)
r1=cnn(r)

result=cv2.merge([b1,g1,r1])
print result
cv2.imwrite("jpg/cnn_4.jpg",result)

