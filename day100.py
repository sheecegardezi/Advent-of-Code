#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
title           :day100.py
description     :Link to problem: http://adventofcode.com/2017/day/10
author          :Sheece Gardezi
date            :2017/30/12
version         :1.0
usage           :python day100.py
python_version  :3.6.1
"""
# Import the modules needed to run the script.
import numpy
import math


dataStructure = []
file = open("input/100.txt", "r")


lengths=[]
for line in file:
    for number in line.strip().split(','):
        lengths.append(int(number.strip(',')))

circularList=[]
for i in range(0,256):
    circularList.append(i)

currentPosition=0
skipSize=0
currentLength=0

#create sub list to be reversed
for currentLength in lengths:


    sublist=[]
    if (currentPosition + currentLength) < len(circularList):

        for i in range(currentPosition, currentPosition+currentLength):
            currentElement=circularList[i]
            sublist.append(currentElement)



    else:
        for i in range(currentPosition, len(circularList)):
            currentElement= circularList[ i]
            sublist.append(currentElement)

        for i in range(0,len(circularList)-currentLength+1):
            currentElement = circularList[i]
            sublist.append(currentElement)


    #reverse list
    reversedSubList=[]
    for i in range(len(sublist)):
        reversedSubList.append(sublist[len(sublist)-1-i])

    #update circular list
    for i in range(len(reversedSubList)):

        if i+currentPosition >= len(circularList):
            circularList[i + currentPosition - len(circularList)] = reversedSubList[i]
        else:
            circularList[i + currentPosition]=reversedSubList[i]


    currentPosition= (currentPosition + skipSize + currentLength) % len(circularList)
    skipSize= skipSize + 1

print(circularList[0]*circularList[1], circularList)
