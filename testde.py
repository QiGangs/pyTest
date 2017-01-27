#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Car:
    no = 1

    def __init__(self,name):
        self.name = name

    def getname(self):
        return self.name



def getabs( x ):
    y = x * x
    return y


def setx( x ):
    x = 14
    return

print getabs(12)

a = 0

setx(a)

print a

car = Car("test")
print car.getname()