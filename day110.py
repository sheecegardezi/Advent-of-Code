#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
title           :day110.py
description     :Link to problem: http://adventofcode.com/2017/day/11
author          :Sheece Gardezi
date            :2018/1/4
version         :1.0
usage           :python day110.py
python_version  :3.6.1
"""



startposition=[0,0]
file = open("input/110.txt", "r")


steps=[]
for line in file:
    for step in line.strip().split(','):
        steps.append(step)


for step in steps:

    if step == "n":

        startposition[0] = startposition[0]
        startposition[1] = startposition[1]+2

    elif step == "ne":

        startposition[0] = startposition[0]+2
        startposition[1] = startposition[1]+1

    elif step == "se":

        startposition[0] = startposition[0]+2
        startposition[1] = startposition[1]-1

    elif step == "s":

        startposition[0] = startposition[0]
        startposition[1] = startposition[1]-2

    elif step == "sw":

        startposition[0] = startposition[0]-2
        startposition[1] = startposition[1]-1

    elif step == "nw":

        startposition[0] = startposition[0]-2
        startposition[1] = startposition[1]+1



distance=0

while startposition[0] != 0 or startposition[1] != 0 :

    #north
    if startposition[0] == 0 and startposition[1] > 0 :
        startposition[0] = startposition[0]
        startposition[1] = startposition[1] - 2

        distance = distance + 1


    #north east
    elif startposition[0] > 0 and startposition[1] > 0 :
        startposition[0] = startposition[0] - 2
        startposition[1] = startposition[1] - 1

        distance = distance + 1

    #south east
    elif startposition[0] > 0 and startposition[1] < 0 :
        startposition[0] = startposition[0] - 2
        startposition[1] = startposition[1] + 1

        distance = distance + 1


    #south
    elif startposition[0] == 0 and startposition[1] < 0 :
        startposition[0] = startposition[0]
        startposition[1] = startposition[1] + 2

        distance = distance + 1

    #south west
    elif startposition[0] < 0 and startposition[1] < 0 :
        startposition[0] = startposition[0] + 2
        startposition[1] = startposition[1] + 1

        distance = distance + 1

    #north west
    elif startposition[0] < 0 and startposition[1] > 0 :
        startposition[0] = startposition[0] + 2
        startposition[1] = startposition[1] - 1

        distance = distance + 1



print(distance)