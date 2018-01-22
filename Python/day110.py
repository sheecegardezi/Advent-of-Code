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


maxDistance=0

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

    tempStartposition = startposition

    distance = 0
    while tempStartposition[0] != 0 or tempStartposition[1] != 0 :
        #north
        if tempStartposition[0] == 0 and tempStartposition[1] > 0 :
            tempStartposition[0] = tempStartposition[0]
            tempStartposition[1] = tempStartposition[1] - 2

            distance = distance + 1


        #north east
        elif tempStartposition[0] > 0 and tempStartposition[1] > 0 :
            tempStartposition[0] = tempStartposition[0] - 2
            tempStartposition[1] = tempStartposition[1] - 1

            distance = distance + 1

        #south east
        elif tempStartposition[0] > 0 and tempStartposition[1] < 0 :
            tempStartposition[0] = tempStartposition[0] - 2
            tempStartposition[1] = tempStartposition[1] + 1

            distance = distance + 1


        #south
        elif tempStartposition[0] == 0 and tempStartposition[1] < 0 :
            tempStartposition[0] = tempStartposition[0]
            tempStartposition[1] = tempStartposition[1] + 2

            distance = distance + 1

        #south west
        elif tempStartposition[0] < 0 and tempStartposition[1] < 0 :
            startposition[0] = startposition[0] + 2
            startposition[1] = startposition[1] + 1

            distance = distance + 1

        #north west
        elif startposition[0] < 0 and startposition[1] > 0 :
            startposition[0] = startposition[0] + 2
            startposition[1] = startposition[1] - 1

            distance = distance + 1

    print(distance)
    if distance > maxDistance:
        maxDistance = distance


print(maxDistance)