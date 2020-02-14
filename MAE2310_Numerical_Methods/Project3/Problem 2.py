# -*- coding: utf-8 -*-
"""
Project 3 Problem 2

Write code for two separate algorithms to implement (a) Euler’s method and(b) the 
standard 4th order Runge-Kutta method, for solving a given first-orderone-dimensional ODE.
Design the code to solve the ODE over a prescribed interval with a prescribed step size, 
taking the initial condition at the left endpoint of the interval as an input variable.

@author: Jacob Needham
"""

def Main():
    #user input to define variables
    x0 =       #inital x value
    xF =       #final x value
    y0 =       #boundary condition 
    h  =       #step size
    
    #RK
    #returning vectors for variable 1, variable 2, and x values
    RK_y1, x_values = RK4_2D(x0,y10,y20,xF,h)
    
    #Euler
    #returning vectors for variable 1, variable 2, and x values
    euler_y1, x_values = eulerMethod(x0,xF,y10,y20,h)
    
    
#differential function
def f1(x,y2):
    y = FUNCTION
    return y

#Runge-Kutte function for integrating based on a boundary condition. 
def RK4_1D (x0,y10,y20,xF,h):
    
    #Creating vector holding all x variables to be iterated on
    x_values = np.arange(x0,xF+h,h)
    
    #initilizing solution vectors 
    y1 = [0 for i in range(len(x_values))]
    y1[0] = y10
    
    #main RK4 loop
    for i in range(len(x_values)-1):
        K11 = f1(x_values[i],y1[i])
        
        K21 = f1(x_values[i]+.5*h,y1[i]+.5*K11*h)
        
        K31 = f1(x_values[i]+.5*h,y1[i]+.5*K21*h)
        
        K41 = f1(x_values[i]+h,y1[i]+K31*h)
        
        y1[i+1] = (y1[i]+(1/6)*(K11+2*K21+2*K31+K41)*h)
        
    return y1, x_values
    

def eulerMethod (x0,xF,y10,y20,h):
    x_values = np.arange(x0,xF+h,h)
    y_euler = [0 for i in range(len(x_values))]
    
    y_euler1[0] = y10

    for i in range(len(x_values)-1):
        y_euler[i+1] = y_euler[i] + f1(x_values[i],y_euler[i])*h
        
    return y_euler, x_values

