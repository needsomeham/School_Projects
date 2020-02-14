"""
Homework 4 Problem 14.10
The grid search is another brute force approach to optimization. The 
two-dimensional version is depicted in Fig. P14.10. The x and y dimensions 
are divided into increments to create a grid. The function is then evaluated 
at each node of the grid. The denser the grid, the more likely it would be to 
locate the optimum.
Develop a program using a programming or macro language to implement the grid 
search method. Design the program so that it is expressly designed to locate a 
maximum. Test it with the same problem as Example 14.1.

@author: Needh
"""
import numpy as np

def function(x,y):
    z = y - x -2*x**2 - 2*x*y - y**2
    return z

#Golden search subroutine
def randomSearch(gridIncrement,xLower,xUpper,yLower,yUpper):
    listOfPoints = []
    xStep = np.arange(xLower,xUpper,gridIncrement)
    yStep = np.arange(yLower,yUpper,gridIncrement)
    
    for x in xStep:
        for y in yStep:
            listOfPoints.append([function(x,y),x,y])
    index = listOfPoints.index(max(listOfPoints))
    domainMax = listOfPoints[index][0]
    xValue = listOfPoints[index][1]
    yValue = listOfPoints[index][2]
    
    print("OUTPUT")
    print("The max of the set")
    print("y - x -2*x^2 - 2*x*y - y^2")
    print("bounded by ",xLower,"<=x<=",xUpper," and ",yLower, "<=y<=",yUpper,\
          " with a grid increment of ", gridIncrement, " is:",sep="")
    print(round(domainMax,3)," located at x=",xValue,", y=",yValue,sep="")

randomSearch(.005,-2,2,1,3)        