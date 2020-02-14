"""
Numerical Methods Project 2

Problem 3 Part A
Use your polynomial regression algorithm (from homework 5) to 
fit a parabola to these 
data points in order to predict u at T = 2.5 C. What is the value you obtained for r^2? 
Generate a plot comparing the data points to your polynomial 
t.

x | 0     5     10    20   30      40
-----------------------------------------
y | 1.787 1.519 1.307 1.002 0.7975 0.6529

@author: Jacob Needham
"""
import matplotlib.pyplot as graph
import numpy as np
import math

x = np.matrix([0,5,10,20,30,40], dtype = 'float')
y = np.matrix([1.787,1.519,1.307,1.002,.7957,.6529], dtype = 'float')
m = 3                            #number of basis functions plus a constant
n = 6                            #height of matrix
z = np.matrix([[None for x in range(n)] for y in range(m)],dtype='float')


#Hard coding each part of the basis function
def a0(x):
    y = 1
    return y

def a1(x):
    y = x
    return y

def a2(x):
    y = x**2
    return y


#This populates the z matrix
for row in range(m):
    for column in range(n):
        if row == 0:
            z[0,column] = a0(x[0,column])
        if row == 1:
            z[1,column] = a1(x[0,column])
        if row == 2:
            z[2,column] = a2(x[0,column])
        
#orients matrix for output        
z=z.transpose()
y=y.transpose()

#this solves for the solution vector that contains coefficients a1-an
#solution vector A = (z(t)*z)^-1 * z(t) * y
A = np.dot(np.dot(np.linalg.inv(np.dot(z.transpose(),z)),z.transpose()),y)

a0 = A[0,0]
a1 = A[1,0]
a2 = A[2,0]


#Printing solution equation
print('OUTPUT')
print("The quadratic function that most accuratly pass though the points is:")
print("y= ",round(a0,4)," + ",round(a1,4),"*x + ",round(a2,4),"*x^2 + ",sep = '')


def function(x):
    y = a0 + a1*x + a2*x**2
    return y
'''
Interpolating quadratic function to find temperature at T = 2.5 C
'''
print("The interpolated value at 2.5 C is", round(function(2.5),4))


'''
Finding Correlaton Coefficient and Standard Error
'''
#Standard Error
Sr = 0
for i in range(n):
    Sr += (+y.item(i)-a0-a1*function(x.item(i))-a2*function(x.item(i)))**2
Sr = math.sqrt(Sr/(n-m+3))

#Correlation Coefficient
yBar = y.sum()/n
St = 0
for i in range(n):
    St += ((y.item(i)-yBar))**2
r = math.sqrt((St-Sr)/St)

print("The coefficient of determination is:",round(r,4))

'''
Building a plot to grpah points and the function
'''
def function2(x):
    y = x
    return y

def plotSpace ():
    #setting up function
    x = np.arange(-100,100,.001)
    y = function(x)
    y2 = function2(x)  #this is used to get the full range of y values for the axis lines
    graph.ylim(0,2)
    graph.xlim(-5, 45)
    #plotting function  
    graph.plot(x, y) 
    
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

plotSpace()


