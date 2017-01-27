#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
A = [12,7,33,23,1,4,2,5,6,3]


for i in range(len(A)):
    key = A[i]
    j = i-1
    while j>=0 and A[j]>key:
        A[j+1] = A[j]
        j = j - 1
    A[j+1] = key

print A