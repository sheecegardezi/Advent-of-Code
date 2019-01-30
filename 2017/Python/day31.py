#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
title           :day31.py
description     :Link to problem: http://adventofcode.com/2017/day/3
author          :Sheece Gardezi
date            :2017/16/12
version         :1.0
usage           :python day30.py
python_version  :3.6.1
"""
# Import the modules needed to run the script.
import numpy
import math

def findGreaterValue(x,y,dataMatrix,targetValue,currentRectangleDimention):
    """Fill in the matrix till a number greater than target value is generated."""
    
    while True:
        
        #fill in right coloum
        for i in range(1,currentRectangleDimention-1):
            x=x-1
            y=y    
            dataMatrix[x][y]=getValue(dataMatrix,x,y)
            if dataMatrix[x][y] > targetValue:
                return dataMatrix[x][y]
                
            
        #fill in top row
        for i in range(1,currentRectangleDimention):
            x=x
            y=y-1    
            dataMatrix[x][y] = getValue(dataMatrix,x,y)
            if dataMatrix[x][y] > targetValue:
                return dataMatrix[x][y]
            
        #fill in left coloum
        for i in range(1,currentRectangleDimention):
            x=x+1
            y=y    
            dataMatrix[x][y]=getValue(dataMatrix,x,y)
            if dataMatrix[x][y] > targetValue:
                return dataMatrix[x][y]

        #fill in bottom row
        for i in range(1,currentRectangleDimention+1):
            x=x
            y=y+1    
            dataMatrix[x][y] = getValue(dataMatrix,x,y)
            if dataMatrix[x][y] > targetValue:
                return dataMatrix[x][y]
            
        currentRectangleDimention=currentRectangleDimention+2
            
def getValue(dataMatrix,x,y):
    """Return the sum of all the numbers in neighborhood."""
    return dataMatrix[x-1][y-1]+dataMatrix[x-1][y]+dataMatrix[x-1][y+1]+dataMatrix[x][y-1]+dataMatrix[x][y]+dataMatrix[x][y+1]+dataMatrix[x+1][y-1]+dataMatrix[x+1][y]+dataMatrix[x+1][y+1]



dimention=10000
dataMatrix= numpy.zeros((dimention,dimention)).tolist()


#initail data
startValue=1.0
startIndex=math.floor(dimention/2)
currentRectangleDimention=1
x=startIndex
y=startIndex
dataMatrix[x][y]=startValue



targetValue=361527
answer=findGreaterValue(x,y,dataMatrix,targetValue,currentRectangleDimention)
print(answer)
