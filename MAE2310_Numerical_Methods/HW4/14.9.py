"""
Homework 4 Problem 14.9
Develop a program using a programming or macro language to implement the 
random search method. Design the subprogram so that it is expressly designed 
to locate a maximum. Test the program with f(x, y) from Prob. 14.7. Use a 
range of -2 to 2 for both x and y.

@author: Jacob Needham
"""

import random

#function equation
def function(x,y):
    z = 4*x + 2*y + x**2 - 2*x**4 +2*x*y - 3*y**2
    return z

#Random Search takes in a number of points and finds the max value of a function 
def randomSearch(maxNumPoints):
    listOfPoints = []
    for i in range(maxNumPoints):
        randPointX = random.uniform(-2,2)
        randPointY = random.uniform(-2,2)
        listOfPoints.append ([function(randPointX,randPointY),randPointX,randPointY])
    index = listOfPoints.index(max(listOfPoints))
    domainMax = listOfPoints[index][0]
    xValue = listOfPoints[index][1]
    yValue = listOfPoints[index][2]

    print("OUTPUT")
    print("The max of the set")
    print("4*x + 2*y + x^2 - 2*x^4 + 2*x*y - 3*y^2")
    print("bounded by -2<=x<=2 and -2<=y<=2 and with", maxNumPoints, "searches is:")
    print(round(domainMax,3), 
          " at x=", round(xValue,3), 
          ", y=", round(yValue,3),sep="")

randomSearch(1000)