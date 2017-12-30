#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
title           :day90.py
description     :Link to problem: http://adventofcode.com/2017/day/9
author          :Sheece Gardezi
date            :2017/30/12
version         :1.0
usage           :python day90.py
python_version  :3.6.1
"""
# Import the modules needed to run the script.
import numpy
import math

dataStructure = []
file = open("input/90.txt", "r")


for line in file:
    groupCount = 0
    ignore=False
    garbage=False
    groupLevel=0
    for letter in line.strip():

        if not ignore:

            if letter == '!':
                ignore = True

            elif letter == '<':
                garbage= True

            elif garbage:
                if letter=='>':
                    garbage=False

            elif letter == '}':
                groupLevel=groupLevel-1

            elif letter == '{':
                groupLevel=groupLevel+1
                groupCount= groupCount + groupLevel
        else:
            ignore=False

    print(groupCount)