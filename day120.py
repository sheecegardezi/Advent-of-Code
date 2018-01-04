#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
title           :day120.py
description     :Link to problem: http://adventofcode.com/2017/day/12
author          :Sheece Gardezi
date            :2018/1/4
version         :1.0
usage           :python day120.py
python_version  :3.6.1
"""

startposition=[0,0]
file = open("input/120.txt", "r")


imputData={}
for line in file:



    basePipe = int(line.strip().split('<->')[0].strip())
    imputData[basePipe]=[]

    for connectedPipes in line.strip().split('<->')[1].strip().split(','):

        imputData[basePipe].append(int(connectedPipes.strip()))


listOfConnectedPipes=[]

for pipe in imputData[0]:
    listOfConnectedPipes.append(pipe)

runningIndex=0
while runningIndex < len(listOfConnectedPipes):

    currentPipe=listOfConnectedPipes[runningIndex]

    for pipe in imputData[currentPipe]:
        if pipe not in listOfConnectedPipes:
            listOfConnectedPipes.append(pipe)

    runningIndex=runningIndex+1

print(len(listOfConnectedPipes))