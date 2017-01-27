#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]
b = []

print a,"\n",b

len = len(a)/2

for i in range(len):
    b.append(a[i])
    b.append(a[len+i])

print b


print 3**10000000000