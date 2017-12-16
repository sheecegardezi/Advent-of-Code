"""
link to problem: http://adventofcode.com/2017/day/3
author: sheece gardezi
"""
import math

def getDimentionOfGrid(number):
    i = 1
    while number > math.pow(i, 2):
        i=i+2
    return i
#x=361527
x=12

dimentions=getDimentionOfGrid(x)
halfOfDimention=math.floor((dimentions)/2)
print(dimentions)

corner0=math.pow(dimentions,2)
corner1=corner0+1*(1-dimentions)
corner2=corner0+2*(1-dimentions)
corner3=corner0+3*(1-dimentions)
corner4s=corner0+4*(1-dimentions)+1

print("x: ",x)
print("Corner0: ",corner0)
print("Corner1: ",corner1)
print("Corner2: ",corner2)
print("Corner2: ",corner3)
print("corner4s: ",corner4s)

#down row
if x >= corner0:
    ySteps=halfOfDimention-(x-corner1)
    print("c1_ySteps: ",ySteps)

if x >= corner1:
    ySteps=halfOfDimention-(x-corner1)
    print("c1_ySteps: ",ySteps)
#left coloum
elif x >= corner2:
    ySteps=halfOfDimention-(x-corner2)
    print("c2_ySteps: ",ySteps)
#up row
elif x >= corner3 :
    ySteps=halfOfDimention-(x-corner3)
    print("c3_ySteps: ",ySteps)
#right coloum
elif x+1 >= corner4s:
    ySteps = halfOfDimention+(x-corner4s)-1
    print("c4_ySteps: ",ySteps)

xSteps=halfOfDimention
print("xSteps: ",xSteps)

print(abs(xSteps)+abs(ySteps))

#if number in right/left coloum, horizontal sets are as follows
#print(math.floor((dimentions)/2))

#if number in right/left coloum,vertical steps are
#print(math.floor((dimentions)/2)-(temparyValue-x))