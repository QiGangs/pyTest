#!/usr/bin/python
# -*- coding: UTF-8 -*-

import testhf

print "祁";

if False:
    print "this is true"
    print "hello"
else:
    print "this is false"
    print "cao"


#a = raw_input("please input\n")
#print a


var1 = 10
var2 = 20
var3 = "this is python"
var4 = var3[2:3]
print var3,var4
print var3[2:]

b = ["ads","bsd",1,2,3,'a','b']
print b[0],b[1],b[4]
b[2] = "test"
print b

c = ("qwer","dfb",12,24,48,'z','x'',xc')
print c,"\n",c[1],"\n",c[4]



d = {'name': 'john','code':6734, 'dept': 'sales',2:"qwe"}
print d[2],d['name']
print d.keys()
print d.values()

'''
print 2**1000
'''


e = 1
f = 2
if e <= f:
    print "e<=f"

if 'names' not in d:
    print "hehehehehe"
if 'qwer' in c:
    print "yes"

for g in "im qi":
    print g
for h in range(len(['1',"qwe",2,'sd',123])):
    print h


i = [1,2,3,4,5,6]
del i[1]
print i,i[1]

j = testhf.get(10)
print j