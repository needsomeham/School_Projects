# -*- coding: utf-8 -*-
"""
Project 3 Problem 4
Write code for two separate algorithms to implement (a) Euler’s method and (b) the 
standard 4th order Runge-Kutta method, for solving a given first-order two-dimensional 
system of ODEs.  Design the code to solve the system of ODEs over a prescribed interval 
with a prescribed step size.

@author: Jacob Needham
"""

import matplotlib.pyplot as graph
import numpy as np

def Main():
    #input perameters from user
    x0  =        #inital x value
    xF  =        #final x value
    y10 =        #boundary condition for variable 1
    y20 =        #boundary condition for variable 2 
    h1  =        #step size
    
    #RK
    #returns velocity vectors, position vector, possible x locations vector
    RK1_h1, RK2_h1, x_values = RK4_2D(x0,y10,y20,xF,h1)
    
    #Euler
    #returns velocity vectors, position vector, possible x locations vector
    euler1_h1, euler2_h1, x_values = eulerMethod(x0,xF,y10,y20,h1)
    

#differential velocity function
def f1(t,v,x):
    y = FUNCTION
    return y


#differential position funciton
def f2(t,v,x):
    y = FUNCTION
    return y

      
def RK4_2D (x0,y10,y20,xF,h):
    
    #this section creates an array with all x value spacing by h
    x_values = np.arange(x0,xF+h,h)
    
    #initilizing solution vectors 
    y1 = [0 for i in range(len(x_values))]
    y2 = [0 for i in range(len(x_values))]
    y1[0] = y10
    y2[0] = y20
    
    #main for loop to RK4 the function
    for i in range(len(x_values)-1): #end case is not include, in matlab it would be len-1
        K11 = f1(x_values[i],y1[i],y2[i])
        K12 = f2(x_values[i],y1[i],y2[i])
        
        K21 = f1(x_values[i]+.5*h,y1[i]+.5*K11*h,y2[i]+.5*K12*h)
        K22 = f2(x_values[i]+.5*h,y1[i]+.5*K11*h,y2[i]+.5*K12*h)
        
        K31 = f1(x_values[i]+.5*h,y1[i]+.5*K21*h,y2[i]+.5*K22*h)
        K32 = f2(x_values[i]+.5*h,y1[i]+.5*K21*h,y2[i]+.5*K22*h)
        
        K41 = f1(x_values[i]+h,y1[i]+K31*h,y2[i]+K32*h)
        K42 = f2(x_values[i]+h,y1[i]+K31*h,y2[i]+K32*h)
        
        y1[i+1] = (y1[i]+(1/6)*(K11+2*K21+2*K31+K41)*h)
        y2[i+1] = (y2[i]+(1/6)*(K12+2*K22+2*K32+K42)*h)
        
    return y1, y2, x_values
    

def eulerMethod (x0,xF,y10,y20,h):
    x_values = np.arange(x0,xF+h,h)
    y_euler1 = [0 for i in range(len(x_values))]
    y_euler2 = [0 for i in range(len(x_values))]
    
    y_euler1[0] = y10
    y_euler2[0] = y20

    for i in range(len(x_values)-1):
        y_euler1[i+1] = y_euler1[i] + f1(x_values[i],y_euler1[i],y_euler2[i])*h
        y_euler2[i+1] = y_euler2[i] + f2(x_values[i],y_euler1[i],y_euler2[i])*h
        
    return y_euler1, y_euler2, x_values

Main()