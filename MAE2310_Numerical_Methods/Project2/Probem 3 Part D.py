"""
Numerical Methods Project 2 Problem 3 Part D

Use your cubic spline interpolation algorithm (from homework 6) to predict u at 
T = 2.5 C. Generate a plot comparing the data points to your cubic spline interpolation.

@author: Jacob Needham
"""

import matplotlib.pyplot as graph
import numpy as np

'''
Main function defines data series of points and what X is to be found and calls
the cubic spline interpolation to find corresponding Y value.
'''
def Main():    
    #put data here:
    x = np.matrix([0,5,10,20,30,40], dtype = 'float')
    y = np.matrix([1.787,1.519,1.307,1.002,.7957,.6529], dtype = 'float')
    n = x.size 
    
    find_x = 2.5
    plotSpace(x,y,n)
    ans = CubicSplineInt(x,y,n,find_x)
    print('For the given data set and x value=',find_x,', the interpolated y value is: ',\
          round(ans,4), sep = '')

'''
Function takes data series x,y and the length of the data set, n, and finds a
coresponding Y value (y_eval) for an input X value (x_eval).
'''
def CubicSplineInt(x,y,n,x_eval):
    #initilzing matrix A, solution vector b, and 2nd derivates vector Fpp
    A = np.matrix([[0 for x in range(n)] for y in range(n)], dtype = 'float')
    A[0,0] = 1
    A[n-1,n-1] = 1
    
    Fpp = np.matrix([None]*n, dtype = 'float')
    
    b = np.matrix([None]*n, dtype = 'float')
    b[0,0] = 0
    b[0,n-1] = 0
    
    #Populating the A matrix with left hand side of equation 18.37 from book
    #and b matrix with right hand side of same equation.
    for i in range(1,n-1):
        A[i,i-1] = x[0,i] - x[0,i-1]
        A[i,i] = 2*(x[0,i+1] - x[0,i-1])
        A[i,i+1] = x[0,i+1] - x[0,i]
        b[0,i] = (6*(y[0,i+1]-y[0,i]))/(x[0,i+1]-x[0,i]) \
                 + (6*(y[0,i-1]-y[0,i]))/(x[0,i]-x[0,i-1])
    
    #linear algebra to solve for Fpp vector using Fpp = A^-1*b
    Fpp = np.dot(np.linalg.inv(A),np.transpose(b))
    
    #calculating the interpolated point for the chosen x value x_eval
    for i in range(n-1):
        if (x[0,i-1] <= x_eval and x[0,i] >= x_eval):
            y_eval = (Fpp[i-1,0]*(x[0,i]-x_eval)**3)/(6*(x[0,i]-x[0,i-1])) \
                    + (Fpp[i,0]*(x_eval - x[0,i-1])**3)/(6*(x[0,i]-x[0,i-1])) \
                    + ((y[0,i-1]/(x[0,i]-x[0,i-1]))-(Fpp[i-1,0]*(x[0,i]-x[0,i-1]))/6)*\
                    (x[0,i]-x_eval) \
                    + ((y[0,i]/(x[0,i]-x[0,i-1]))-(Fpp[i,0]*(x[0,i]-x[0,i-1]))/6)*\
                    (x_eval-x[0,i-1])
            return y_eval
    
#This function is ONLY to plot axis in graph
def function2(x):
    y = x
    return y

def plotSpace (x,y,n):
    #plotting alot of points to approximate a function for output
    for i in range(0,3000):
        graph.plot(i/100,CubicSplineInt(x,y,n,i/100),',')

    #setting up function
    x = np.arange(-100,100,.001)
    #y = function(x)
    y2 = function2(x)  #this is used to get the full range of y values for the axis lines
    graph.ylim(0,2)
    graph.xlim(-5, 45)
    
    #plotting function  
    #graph.plot(x, y)     #ignore
    
    #plotting data set
    xSeries  = [0,5,10,20,30,40]
    ySeries  = [1.787,1.519,1.307,1.002,.7957,.6529]
    graph.plot(xSeries,ySeries,'ro')
    
    #setting up graph
    graph.xlabel('x - axis') 
    graph.ylabel('y - axis') 
    graph.title('Project 2 Problem 3 Part D') 
    
    #plotting axis
    graph.plot(x, x*0 + 0 , linewidth = .5, color = 'black')
    graph.plot(x*0 +0, y2, linewidth =.5, color = 'black')
    
    #grpahing
    graph.show() 


Main()  