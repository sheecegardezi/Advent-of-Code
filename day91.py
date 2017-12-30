#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
title           :day91.py
description     :Link to problem: http://adventofcode.com/2017/day/9
author          :Sheece Gardezi
date            :2017/30/12
version         :1.0
usage           :python day91.py
python_version  :3.6.1
"""
# Import the modules needed to run the script.
import numpy
import math

dataStructure = []
file = open("input/91.txt", "r")


for line in file:

    ignore=False
    garbage=False
    garbageLetters=0
    groupLevel=0
    groupCount=0
    for letter in line.strip():

        if not ignore:

            if letter == '!':
                ignore = True


            elif garbage:
                if letter=='>':
                    garbage=False
                else:
                    garbageLetters=garbageLetters+1

            elif letter == '<':
                garbage= True

            elif letter == '}':
                groupLevel=groupLevel-1

            elif letter == '{':
                groupLevel=groupLevel+1
                groupCount= groupCount + groupLevel
        else:
            ignore=False

    print(line.strip(),garbageLetters)

print(garbageLetters)