# -*- coding: utf-8 -*-
"""
Project 3 Problem 4 part B
The motion of a damped mass spring is described by the following ODE : 
m * d2x/dt2 + c * dx/dt + kx = 0,
where x = displacement from equilibrium position (m), t = time (s), m = mass (kg), 
k = stiffness constant (N/m) and c = damping coefficient (N·s/m).

Part B:
Assume that the mass is m = 10 kg, the stiffness k = 12 N/m, the damping coefficient 
is c = 3 N·s/m, the initial velocity of the mass is zero (v(0) = 0), and the initial 
displacement is x = 1 m (x(0) = 1). Solve for the displacement and velocity of the mass 
over the time period 0 ≤ t ≤ 15, and plot your results for the displacement x = x(t),
(i) using Euler’s method with step size h = 0.5, and then with step size h = 0.01.
(ii) using the standard 4th order Runge-Kutta method with step size h = 0.5, and 
then with step size h = 0.01.

@author: Jacob Neehdam
"""

import matplotlib.pyplot as graph
import numpy as np

def Main():
    #input perameters from user
    x0 = 0
    xF = 15
    y10 = 0
    y20 = 1
    h1 = .5
    h2 = .01
    
    #plot of RK for c=3 and h=.5
    RK1_h1, RK2_h1, x_values = RK4_2D(x0,y10,y20,xF,h1)
    plotSpace(x_values, RK1_h1, RK2_h1, 'Runge-Kutta  c=3, m=10, k=12, h=.5')
    
    #Plot of Euler for c=3 and h=.5
    euler1_h1, euler2_h1, x_values = eulerMethod(x0,xF,y10,y20,h1)
    plotSpace(x_values, euler1_h1, euler2_h1, 'Euler Method  c=3, m=10, k=12, h=.5')
    
    #Plot of RK for c=3 and h=1    
    RK1_h2, RK2_h2, x_values = RK4_2D(x0,y10,y20,xF,h2)
    plotSpace(x_values, RK1_h2, RK2_h2, 'Runge-Kutta  c=3, m=10, k=12, h=.01')
    
    #Plot of Euler for c=3 and h=1    
    euler1_h2, euler2_h2, x_values = eulerMethod(x0,xF,y10,y20,h2)
    plotSpace(x_values, euler1_h2, euler2_h2, 'Euler Method  c=3, m=10, k=12, h=.01')

#funciton really is dv/dt
def f1(t,v,x):
    c = 3
    k = 12
    m = 10
    y = -((c/m)*v)-((k/m)*x)
    return y


#function really is d2y/dt2
def f2(t,v,x):
    y = v
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



#Function to graph
def plotSpace (timeSeries,yVelocity,yPosition,title):
    
    #setting up graph
    graph.xlabel('Time (s)') 
    graph.ylabel('Velocity (m/s) or Postion (m)') 
    graph.title('Project 3 Problem 5 \n' + title) 
    
    #graphing velocity           
    graph.scatter(timeSeries,yVelocity, color = 'blue', marker = '.')
    graph.plot(timeSeries,yVelocity, color = 'blue', label = 'Velocity vs Time')
    
    #graphing postion
    graph.scatter(timeSeries,yPosition, color = 'red', marker = '.')
    graph.plot(timeSeries,yPosition, color = 'red', label = 'Position vs Time')
    
    #showing legend
    graph.legend()
    
    #plotting axis
    #x = np.arange(min(timeSeries),max(timeSeries),.01)
    #y = function(x)
    graph.plot(x, x*0 + 0 , linewidth = .5, color = 'black')
    #graph.plot(x*0 +0, y, linewidth =.5, color = 'black')
    
    #grpahing
    graph.show() 


Main()