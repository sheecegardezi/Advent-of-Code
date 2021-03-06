#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
title           :day30.py
description     :Link to problem: http://adventofcode.com/2017/day/3
author          :Sheece Gardezi
date            :2017/16/12
version         :1.0
usage           :python day30.py
python_version  :3.6.1
"""

# Import the modules needed to run the script.
import math

def getDimentionOfGrid(number):
    """Return the length of side of rectangle."""
    """
    find the length of side of recangle in which the number exists 
    using the fact that max number in each rectange will be square of odd number 
    """
    
    i = 1
    while number > math.pow(i, 2):
        i=i+2
    return i

#main program
input=361527

dimentions=getDimentionOfGrid(input)

#calaculte the corner value of the rectangle
corner0=math.pow(dimentions,2)
corner1=corner0+1*(1-dimentions)
corner2=corner0+2*(1-dimentions)
corner3=corner0+3*(1-dimentions)
corner0alis=corner0+4*(1-dimentions)

#check if number exist at right-bottom corner
if input in [corner0,corner1,corner2,corner3] :
    answer= dimentions-1

#check if number exist at bottom row    
if input > corner1:
    ySteps=math.floor(dimentions/2)
    xSteps=((corner0-corner1)/2+corner1)-input
    
    answer=abs(xSteps)+abs(ySteps)

#check if number exist at left row     
elif input > corner2:

    xSteps=math.floor(dimentions/2)
    ySteps=((corner1-corner2)/2+corner2)-input
    
    answer=abs(xSteps)+abs(ySteps)
    

#check if number exist at top row   
elif input > corner3:
    ySteps=math.floor(dimentions/2)
    xSteps=((corner2-corner3)/2+corner3)-input
    
    answer=abs(xSteps)+abs(ySteps)
    
#check if number exist at right row   
elif input > corner0alis :
    
    xSteps=math.floor(dimentions/2)
    ySteps=((corner3-corner0alis)/2+corner0alis)-input
    
    answer=abs(xSteps)+abs(ySteps)
    
print(answer)