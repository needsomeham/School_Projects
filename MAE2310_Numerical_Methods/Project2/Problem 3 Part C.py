# -*- coding: utf-8 -*-
"""
Numerical Methods Project 2 Problem 3 Part C

Use your Newton's interpolating polynomial algorithm (from homework 6) to predict u at 
T = 2.5 C. Generate a plot comparing the data points to your polynomial interpolation.

@author: Jacob Needham
"""
import matplotlib.pyplot as graph
import numpy as np

'''
Main fucntion takes input data from table with x and y values and runs Fdd function.
'''
def Main():
    #put numbers here
    x = [0,5,10,20,30,40]
    y = [1.787,1.519,1.307,1.002,.7957,.6529]
    n = len(x)
    
    Xi = 2.5              #input x value to solve for here
    q = FddMatrix(x,y,n,Xi) 
    
    plotSpace(x,y,n)
    
    print("Interpolating at 2.5 C yields:",q)
    
'''
FddMatrix takes in vectors x, y from table and solves for linear fit between points
'''
def FddMatrix(x,y,n,Xi):
    #initilizing Fdd matrix and placeholder matrix for y
    Fdd = np.matrix([[0 for x in range(n)] for y in range(n)],dtype = 'float') 
    y_working = np.zeros((n,1), dtype = 'float')
    for i in range(n):                            #For loop coppies y value into first 
        Fdd[i,0] = y[i]                           #column.
    for j in range(1,n):                          #For loop fills A matrix using modified  
        for i in range(0,n-j):                    #Eq. 18.2 for linear interpolation from 
            Fdd[i,j] = (Fdd[i+1,j-1] - Fdd[i,j-1])/(x[i+j]-x[i])           #the book.
    
    #initializing necessary place-holding matricies        
    x_temp = [1]
    y_working[0] = Fdd[0,0]
    for order in range(1,n):
        x_temp.append(x_temp[order-1]*(Xi - x[order-1]))
        y_working[order] = y_working[order-1] + Fdd[0,order]*x_temp[order]
    
    return y_working[n-1]
    #formating output and printing solution
    #final_y = str(y_working[n-1])
    #final_y = final_y.strip(' /[/]')
    #print('At x = ',Xi,' the interpolated y value is: ', final_y, sep = '')


def function2(x):
    y = x
    return y
    
def plotSpace (x,y,n):

    for i in range(0,3000):
        graph.plot(i/100,FddMatrix(x,y,n,i/100),',')

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