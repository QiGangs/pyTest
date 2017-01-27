#!/usr/bin/python

from Crypto.Cipher import AES
name = "lxl"
num = len(name)
for i in range(16-num):
    name +="0"

print len(name)

print AES.block_size