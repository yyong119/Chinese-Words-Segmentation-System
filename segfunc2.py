# -*- coding: UTF-8 -*-
#-----------------------------#
#Team Name: MacroHard
#Members: Zhenlin Qi
#         Zheyu Shi
#         Yong Mao
#All Rights Reserved
#It's a demo for CWSS
#-----------------------------#

import os
import __main__
import time
from math import *

global gailv01
global gailv02
global gailv00

gailv01={}
gailv02={}
gailv00={}

def seg2(s):
    yinhanlist=[""]*len(s)
    SBMElist=["S","B","M","E"]
    prelist=[0]*len(s)
    for i in range(len(prelist)):
        prelist[i]=[0]*4
    trylist=[0]*len(s)
    for i in range(len(trylist)):
        trylist[i]=[0]*4
    trylist[0][0]=0
    trylist[0][1]=0
    trylist[0][2]=99999
    trylist[0][3]=99999
    for i in range(1,len(s)):
        p=[0]*16
        p[0]=p[0]+(-log(gailv00["SS"]))
        if ((s[i-1],s[i],"S") in gailv02.keys()) and ((s[i],"S") in gailv01.keys()):
            if gailv01[(s[i],"S")]<gailv02[(s[i-1],s[i],"S")]:
                p[0]+=(-log(gailv02[(s[i-1],s[i],"S")]))
            else:
                p[0]+=(-log(gailv01[(s[i],"S")]))
        elif ((s[i],"S") in gailv01.keys()):
            p[0]+=(-log(gailv01[(s[i],"S")]))
        else:
            p[0]+=99999
        p[1]+=99999
        p[2]+=99999
        p[3]=p[3]+(-log(gailv00["ES"]))
        if ((s[i-1],s[i],"S") in gailv02.keys()) and ((s[i],"S") in gailv01.keys()):
            if gailv01[(s[i],"S")]<gailv02[(s[i-1],s[i],"S")]:
                p[3]+=(-log(gailv02[(s[i-1],s[i],"S")]))
            else:
                p[3]+=(-log(gailv01[(s[i],"S")]))
        elif ((s[i],"S") in gailv01.keys()):
            p[3]+=(-log(gailv01[(s[i],"S")]))
        else:
            p[3]+=99999
        p[4]=p[4]+(-log(gailv00["SB"]))
        if ((s[i-1],s[i],"B") in gailv02.keys()) and ((s[i],"B") in gailv01.keys()):
            if gailv01[(s[i],"B")]<gailv02[(s[i-1],s[i],"B")]:
                p[4]+=(-log(gailv02[(s[i-1],s[i],"B")]))
            else:
                p[4]+=(-log(gailv01[(s[i],"B")]))
        elif ((s[i],"B") in gailv01.keys()):
            p[4]+=(-log(gailv01[(s[i],"B")]))
        else:
            p[4]+=99999
        p[5]+=99999
        p[6]+=99999
        p[7]=p[7]+(-log(gailv00["EB"]))
        if ((s[i-1],s[i],"B") in gailv02.keys()) and ((s[i],"B") in gailv01.keys()):
            if gailv01[(s[i],"B")]<gailv02[(s[i-1],s[i],"B")]:
                p[7]+=(-log(gailv02[(s[i-1],s[i],"B")]))
            else:
                p[7]+=(-log(gailv01[(s[i],"B")]))
        elif ((s[i],"B") in gailv01.keys()):
            p[7]+=(-log(gailv01[(s[i],"B")]))
        else:
            p[7]+=99999
        p[8]+=99999
        p[9]=p[9]+(-log(gailv00["BM"]))
        if ((s[i-1],s[i],"M") in gailv02.keys()) and ((s[i],"M") in gailv01.keys()):
            if gailv01[(s[i],"M")]<gailv02[(s[i-1],s[i],"M")]:
                p[9]+=(-log(gailv02[(s[i-1],s[i],"M")]))
            else:
                p[9]+=(-log(gailv01[(s[i],"M")]))
        elif ((s[i],"M") in gailv01.keys()):
            p[9]+=(-log(gailv01[(s[i],"M")]))
        else:
            p[9]+=99999
        p[10]=p[10]+(-log(gailv00["MM"]))
        if ((s[i-1],s[i],"M") in gailv02.keys()) and ((s[i],"M") in gailv01.keys()):
            if gailv01[(s[i],"M")]<gailv02[(s[i-1],s[i],"M")]:
                p[10]+=(-log(gailv02[(s[i-1],s[i],"M")]))
            else:
                p[10]+=(-log(gailv01[(s[i],"M")]))
        elif ((s[i],"M") in gailv01.keys()):
            p[10]+=(-log(gailv01[(s[i],"M")]))
        else:
            p[10]+=99999
        p[11]+=99999
        p[12]+=99999
        p[13]=p[13]+(-log(gailv00["BE"]))
        if ((s[i-1],s[i],"E") in gailv02.keys()) and ((s[i],"E") in gailv01.keys()):
            if gailv01[(s[i],"E")]<gailv02[(s[i-1],s[i],"E")]:
                p[13]+=(-log(gailv02[(s[i-1],s[i],"E")]))
            else:
                p[13]+=(-log(gailv01[(s[i],"E")]))
        elif ((s[i],"E") in gailv01.keys()):
            p[13]+=(-log(gailv01[(s[i],"E")]))
        else:
            p[13]+=99999
        p[14]=p[14]+(-log(gailv00["ME"]))
        if ((s[i-1],s[i],"E") in gailv02.keys()) and ((s[i],"E") in gailv01.keys()):
            if gailv01[(s[i],"E")]<gailv02[(s[i-1],s[i],"E")]:
                p[14]+=(-log(gailv02[(s[i-1],s[i],"E")]))
            else:
                p[14]+=(-log(gailv01[(s[i],"E")]))
        elif ((s[i],"E") in gailv01.keys()):
            p[14]+=(-log(gailv01[(s[i],"E")]))
        else:
            p[14]+=99999
        p[15]+=99999
        mini=0
        for j in range(1,4):
            if (p[j]+trylist[i-1][j%4])<(p[mini]+trylist[i-1][mini%4]):
                mini=j
        trylist[i][0]=trylist[i][0]+p[mini]+trylist[i-1][mini%4]
        prelist[i][0]=mini%4
        mini=4
        for j in range(5,8):
            if (p[j]+trylist[i-1][j%4])<(p[mini]+trylist[i-1][mini%4]):
                mini=j
        trylist[i][1]=trylist[i][1]+p[mini]+trylist[i-1][mini%4]
        prelist[i][1]=mini%4
        mini=8
        for j in range(9,12):
            if (p[j]+trylist[i-1][j%4])<(p[mini]+trylist[i-1][mini%4]):
                mini=j
        trylist[i][2]=trylist[i][2]+p[mini]+trylist[i-1][mini%4]
        prelist[i][2]=mini%4
        mini=12
        for j in range(13,16):
            if (p[j]+trylist[i-1][j%4])<(p[mini]+trylist[i-1][mini%4]):
                mini=j
        trylist[i][3]=trylist[i][3]+p[mini]+trylist[i-1][mini%4]
        prelist[i][3]=mini%4
    mini=0
    for j in range(1,4):
        if trylist[len(s)-1][j]<trylist[len(s)-1][mini]:
            mini=j
    yinhanlist[-1]=SBMElist[mini]
    count=len(s)-1
    while count>0:
        count-=1
        yinhanlist[count]=SBMElist[prelist[count+1][mini]]
        mini=prelist[count+1][mini]
    resultstr=""
    for i in range(len(s)):
        if yinhanlist[i]=="S":
            resultstr+=s[i]
            resultstr+=" | "
        if yinhanlist[i]=="B":
            resultstr+=s[i]
        if yinhanlist[i]=="M":
            resultstr+=s[i]
        if yinhanlist[i]=="E":
            resultstr+=s[i]
            resultstr+=" | "
    return resultstr

def daoru_gailv():
    ts=time.time()
    print('daoru starts at ',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    __main__.logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'Qi\'s algorithm begins to load' + '\n')

    global gailv00
    global gailv01
    global gailv02
    ff01=open("gailv_out01.txt","r")
    line=ff01.readline()
    while line:
        gailv00[line[:2]]=float(line[4:])
        line=ff01.readline()
    ff01.close()

    ff02=open("biaozhu_dic01.txt","r")
    line=ff02.readline()
    while line:
        for i in range(len(line)):
            if line[i]==")":
                num=i+1
        gailv01[(line[2],line[7])]=float(line[num:])
        line=ff02.readline()
    ff02.close()

    with open('biaozhu_dic02.txt') as file:
        for line in file:
            for i in range(len(line)):
                if line[i]==")":
                    num=i+1
            if float(line[num:])>=1.0:
                pass
            else:
                gailv02[(line[2],line[7],line[12])]=float(line[num:])
    
    # ff03=open("biaozhu_dic02.txt","r")
    # line=ff03.readline()
    # while line:
    #     for i in range(len(line)):
    #         if line[i]==")":
    #             num=i+1
    #     if float(line[num:])>=1.0:
    #         pass
    #     else:
    #         gailv02[(line[2],line[7],line[12])]=float(line[num:])
    #     line=ff03.readline()
    # ff03.close()
    te=time.time()
    tc=str(te-ts)
    print()
    print('*'*20)
    print('daoru ends at ',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    # __main__.logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'Qi\'s algorithm loads OK' + '\n')

    print('daoru costs',tc[0:5],'s')
    __main__.logfile.write('        Time cost '+ tc[0:5] + '\n')

    print('*'*20)
