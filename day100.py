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
    for number in line.strip().split(' '):
        lengths.append(int(number.strip(',')))

circularList=[]
for i in range(0,5):
    circularList.append(i)

currentIndex=0
skip=0
currentLength=0

#create sub list to be reversed
for currentLength in lengths:
    sublist=[]
    for i in range(currentLength):

        if (currentIndex+i) >= len(circularList):
            currentElement=circularList[ int((currentIndex+i) % len(circularList))]
            sublist.append(currentElement)
        else:
            currentElement=circularList[ (currentIndex+i)]
            sublist.append(currentElement)

    #reverse list
    reversedSubList=[]
    for i in range(len(sublist)):
        reversedSubList.append(sublist[len(sublist)-1-i])

    #update circular list
    for i in range(len(reversedSubList)):

        if i+currentIndex >= len(circularList):
            circularList[i + currentIndex-len(circularList)] = reversedSubList[i]
        else:
            circularList[i+currentIndex]=reversedSubList[i]

    print(circularList)