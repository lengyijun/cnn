# -*- coding: utf-8 -*-
import cv2
import numpy

im=cv2.imread('jpg/origin.jpg')
b,g,r=cv2.split(im)
a1=numpy.array([[0,0,0,0,0],[0,0,-1,0,0],[0,-1,5,-1,0],[0,0,-1,0,0],[0,0,0,0,0]])

def cnn(x):
    result =numpy.empty((295,295),dtype=numpy.float)
    for i in range(0, 295):
        for j in range(0, 295):
            temp = x[i:i + 5, j:j + 5] * a1
            result[i][j]=(temp.sum())
    return result

b1=cnn(b)
g1=cnn(g)
r1=cnn(r)

result=cv2.merge([b1,g1,r1])
print result
cv2.imwrite("jpg/cnn.jpg",result)

