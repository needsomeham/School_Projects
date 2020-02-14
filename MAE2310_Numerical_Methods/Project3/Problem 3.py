# -*- coding: utf-8 -*-
"""
Project 3 Problem 3

The drag force Fd (N) exerted on a falling object can be modeled as proportional to the 
square of the objects downward velocity v (m/s), with a constant of proportionality
cd (kg/m).
(a) Assume that a falling object has mass m = 100 (kg) with a drag coefficient of 
cd = 0.25 kg/m, and let g = 9.81 (m/s2) denote the constant downward acceleration due to 
gravity near the surface of the earth. Starting from Newton’s second law, explain the 
derivation of the following ODE for the downward velocity v = v(t) of the falling object:
dv/dt = 9.81 − 0.0025v^2
(b) Suppose that this same object is dropped from an initial height of y0 = 2 km. 
Determine when the object hits the ground by solving the ODE you derived in question 3(a) 
using:
(i) Euler’s method.
(ii) the standard 4th order Runge-Kutta method.

@author: Jacob Needham
"""

import matplotlib.pyplot as graph
import numpy as np

def Main():
    #input perameters from user
    x0 = 0        #initial time
    xF = 37       #final time guess
    y10 = 0       #intiial veloctiy
    y20 = 2000    #initial y position
    h1 = .01      #step size
    
    #RK
    #retrns velocity vector, position vector, and time vector
    RK1_h1, RK2_h1, x_values = RK4_2D(x0,y10,y20,xF,h1)
    plotSpace(x_values, RK1_h1, RK2_h1, 'Runge-Kutta falling body problem h=.01')
    
    print()
    print()
    
    #Euler 
    #retrns velocity vector, position vector, and time vector
    euler1_h1, euler2_h1, x_values = eulerMethod(x0,xF,y10,y20,h1)
    plotSpace(x_values, euler1_h1, euler2_h1, 'Euler Method  falling body problem h=.01')
    

#differential velocity function
def f1(t,v,x):
    y = 9.81 - 0.0025*v**2
    return y


#differential position function
def f2(t,v,x):
    y = -v
    return y

      
def RK4_2D (x0,y10,y20,xF,h):
    
    #Creating vector holding all x variables to be iterated on
    x_values = np.arange(x0,xF+h,h)
    
    #initilizing velocity and position solution vectors 
    y1 = [0 for i in range(len(x_values))]
    y2 = [0 for i in range(len(x_values))]
    y1[0] = y10
    y2[0] = y20
    
    #main for loop to RK4 the function
    for i in range(len(x_values)-1): 
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
        
        #testing to see of the position is less than 0, or hit the ground
        if y2[i+1] <= 0:
            print('Using RK-4, the time at which the object ' \
                  'hits the ground is:',x_values[i],'seconds.')
            break
        
    return y1, y2, x_values
    
def eulerMethod (x0,xF,y10,y20,h):
    
   #Creating vector holding all x variables to be iterated on
    x_values = np.arange(x0,xF+h,h)
    
    #initilizing velocity and position solution vectors 
    y_euler1 = [0 for i in range(len(x_values))]
    y_euler2 = [0 for i in range(len(x_values))]
    y_euler1[0] = y10
    y_euler2[0] = y20

    #main Euler function
    for i in range(len(x_values)-1):
        y_euler1[i+1] = y_euler1[i] + f1(x_values[i],y_euler1[i],y_euler2[i])*h
        y_euler2[i+1] = y_euler2[i] + f2(x_values[i],y_euler1[i],y_euler2[i])*h
        
        #testing to see of the position is less than 0, or hit the ground
        if y_euler2[i+1] <= 0:
            print('Using Euler\'s Method, the time at which the object ' \
                  'hits the ground is:',x_values[i],'seconds.')
            break
        
    return y_euler1, y_euler2, x_values


#simple function to graph axis
def function(x):
    y = x
    return y

#fFunction to graph
def plotSpace (timeSeries,yVelocity,yPosition,title):
    
    #setting up graph
    graph.xlabel('Time (s)') 
    graph.ylabel('Velocity (m/s) or Postion (m)') 
    graph.title('Project 3 Problem 3 \n' + title) 
    
    #graphing velocity           
    graph.scatter(timeSeries,yVelocity, color = 'blue', marker = '.')
    graph.plot(timeSeries,yVelocity, color = 'blue', label = 'Velocity vs Time')
    
    #graphing postion
    graph.scatter(timeSeries,yPosition, color = 'red', marker = '.')
    graph.plot(timeSeries,yPosition, color = 'red', label = 'Position vs Time')
    
    #showing legend
    graph.legend()
    
    #plotting axis
    x = np.arange(min(timeSeries),max(timeSeries),.01)
    y = function(x)
    graph.plot(x, x*0 + 0 , linewidth = .5, color = 'black')
    #graph.plot(x*0 +0, y, linewidth =.5, color = 'black')
    
    #grpahing
    graph.show() 


Main()