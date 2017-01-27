#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

#定义节点
class Node:
    def __init__(self,char='',weight=0,left=None,right=None):
        self.weight=weight
        self.left=left
        self.right=right
        self.char = char
fo = open("foo.txt", "wb+")
dict = {}
list = []

#随机生成字符写入文件
for i in range(1000):
    a = random.randint(32,126)
    aa = chr(a)
    fo.write(aa)

#生成字典统计频率
for i in range(32,127):
    dict[chr(i)] = 0

fo.seek(0, 0);
for i in range(1000):
    b = fo.read(1)
    num = dict[b]
    dict[b] = num + 1
fo.close()

listx =  sorted(dict.items(), key=lambda kv: (-kv[1], kv[0]))
#print listx
#listx = list(reversed(listx))
for i in range(0,126-32):
    new = Node()
    new.char = listx[i][0]
    new.weight = listx[i][1]
    list.append(new)

#按值排序
def sort(list):
    return sorted(list,key=lambda node:node.weight)
#生成哈夫曼树
def Huffman(list):
    while len(list)!=1:
        a,b=list[0],list[1]
        new=Node()
        new.weight=a.weight+b.weight
        new.left,new.right=a,b
        list.remove(a)
        list.remove(b)
        list.append(new)
        list=sort(list)
    return list

list =  Huffman(list)
res = list[0]

def traval(one):
    if one == None: return
    traval(one.left)
    print one.char,
    traval(one.right)

print traval(res)
