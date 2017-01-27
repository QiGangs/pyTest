#!/usr/bin/python
# -*- coding: UTF-8 -*-


def a(x):
    x = x + 12
    return x

def b(x):
    x = x - 11
    return x

def c(q,w,x):
    res = q(x) + w(x)
    return res

print c(a,b,0)
