#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
import threading


allsock = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9998))
s.listen(10)


def sendprivateinfo(name,info,sock,fromname):       #发送私聊信息
    if(allsock.has_key(name)):
        allsock[name].send(info+" \n------from "+fromname)
    else:
        sock.send("++++++++++++++++++++++\nthis name is not existed!\n+++++++++++++++++++++")


def getallonlinename():            #获取在线名称
    allname = "+++++++++++++++++++++++++++++++++++\n"
    for namex in allsock.keys():
        allname += namex+"\n"
    allname += "+++++++++++++++++++++++++++++++++++\n"
    return allname

def removesock(name):         #移除连接
    del allsock[name]


def sendallinfo(name,data):    #群发信息
    for namex in allsock.keys():
        if(namex == name): continue
        allsock[namex].send(data+" \n------from "+name)


def tcplink(sock, addr,name):
    print 'Accept new connection from %s:%s...' % addr,sock
    while True:
        data = sock.recv(1024)
        if(data == "\exit" or data == ""):break
        elif(data == "\getname"):
            sock.send(getallonlinename())
            continue
        elif(data == "\To"):
            nameandinfo = sock.recv(1024)
            num = nameandinfo.find(chr(32),0,len(nameandinfo))
            privatename = nameandinfo[:num]
            privateinfo = nameandinfo[num+1:]
            sendprivateinfo(privatename,privateinfo,sock,name)
            continue
        sendallinfo(name,data)
    removesock(name)
    sock.close()
    print 'Connection from %s:%s closed.' % addr

while True:
    sock, addr = s.accept()
    data = sock.recv(1024)
    if(allsock.has_key(data)):
        sock.send("501")
        sock.close()
        continue
    else:
        sock.send("401")
    sock.send("welcome " + data)
    allsock[data]=sock
    t = threading.Thread(target=tcplink, args=(sock, addr,data))
    t.start()


