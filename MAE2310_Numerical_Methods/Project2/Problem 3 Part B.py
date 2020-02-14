"""
Numerical Methods Project 2 Problem 3 Part B

Andrade's equation has been proposed as a model for this relationship, which claims that 
(see equation) where Ta = absolute temperature of the water (K), and D and B are 
constants. Apply a mathematical transformation to (1) that will allow you to solve for 
B and D by applying the general regression algorithm you developed
for homework 5. Use Andrade's equation to predict u at T = 2.5 C. Generate a plot 
comparing the data points to your 
t using Andrade's equation.

@author: Jacob Needham
"""

import matplotlib.pyplot as graph
import numpy as np
import math

def Main():
        
    x = np.matrix([0,5,10,20,30,40], dtype = 'float')
    y = np.matrix([math.log(1.787),math.log(1.519),math.log(1.307),math.log(1.002),\
                   math.log(.7957),math.log(.6529)], dtype = 'float')
    m = 2                             #number of basis functions plus a constant
    n = 6                             #height of matrix
    z = np.matrix([[None for x in range(n)] for y in range(m)],dtype='float')
    
    coef1,coef2 = genRegAlg(m,n,x,y,z,a0,a1)
    
    plotSpace(coef1,coef2)
    
    print("The interpolated value at x = 2.5 C =",round(function(2.5,coef1,coef2),4))

#Hard coding each part of the basis function
def a0(x):
    y = 1
    return y

def a1(x):
    y = 1/(x+273.15)
    return y

def genRegAlg(m,n,x,y,z,a0,a1):

    #Populating the z matrix
    for row in range(m):
        for column in range(n):
            if row == 0:
                z[0,column] = a0(x[0,column])
            if row == 1:
                z[1,column] = a1(x[0,column])
            
    #orients matrix for output        
    z=z.transpose()
    y=y.transpose()
    
    #this solves for the solution vector that contains coefficients a1-an
    #solution vector A = (z(t)*z)^-1 * z(t) * y
    A = np.dot(np.dot(np.linalg.inv(np.dot(z.transpose(),z)),z.transpose()),y)
    
    coef1 = A[0,0]
    coef2 = A[1,0]
    
    return coef1, coef2
#Printing solution equation
#print("The base funtion that most accuratly pass though the points is:")
#print("y= ",round(a0,4)," + ",round(a1,4),"*x + ", sep = '')

def function(x,a0,a1):
    y = math.exp(a0) * math.exp( a1/(x+273.15))
    return y

def function2(x):
    y = x
    return y

def plotSpace (coef1,coef2):

    for i in range(0,4500):
        graph.plot(i/100,function(i/100,coef1,coef2),',')

    #setting up function
    x = np.arange(-100,100,.001)
    #y = function(x)
    y2 = function2(x)  #this is used to get the full range of y values for the axis lines
    graph.ylim(0,2)
    graph.xlim(-5, 45)
    
    #plotting function  
    #graph.plot(x, y) 
    
    #plotting data set
    xSeries  = [0,5,10,20,30,40]
    ySeries  = [1.787,1.519,1.307,1.002,.7957,.6529]
    graph.plot(xSeries,ySeries,'ro')
    
    #setting up graph
    graph.xlabel('x - axis') 
    graph.ylabel('y - axis') 
    graph.title('Project 2 Problem 3 Part A') 
    
    #plotting axis
    graph.plot(x, x*0 + 0 , linewidth = .5, color = 'black')
    graph.plot(x*0 +0, y2, linewidth =.5, color = 'black')
    
    #grpahing
    graph.show() 


Main()  