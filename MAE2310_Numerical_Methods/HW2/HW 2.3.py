'''
Homework 2.3
Textbook problem 5.13.
Velocity given by funcion. Constants are defined. Find mass m.
'''

import numpy as np
import matplotlib.pyplot as graph


#peramiters defined by the user
mass = None
xL = 55
xU = 65
es = .001
iMax = 50

def function(mass):
    y = (9.81 * mass)/15 * (1 - 2.7182818284590452353602874**(-(15/mass)*10)) - 36
    return y

def plotSpace ():
    #setting up function
    x = np.arange(-10000,10000,.01)
    y = function(x)
    graph.ylim(-10,20)
    graph.xlim(25,75)
    #plotting function  
    graph.plot(x, y) 
    
    #setting up graph
    graph.xlabel('x - axis') 
    graph.ylabel('y - axis') 
    graph.title('Homeowrk 2.3: Monday Jan 14 ') 
    
    #plotting axis
    graph.plot(x, x*0 + 0 , linewidth = .5, color = 'black')
    graph.plot(x*0 +0, y, linewidth =.5, color = 'black')
    
    #grpahing
    graph.show() 

plotSpace()


def falsePosition(xL,xU,es,iMax):
    iCount = 0
    xR = xL
    ea = es
    xOld = None
    
    for iCount in range(0,iMax):
        xOld = xR
        xR = xU - (function(xU)*(xL-xU)/(function(xL)-function(xU)))
        iCount +=1
        if xR != 0:
            ea = abs((xR-xOld)/xR)
        test = function(xL)*function(xR)
        if test < 0:
            xU = xR
        elif test > 0:
            xL = xR
        else :
            ea = 0
        
        if ea<es or iCount >= iMax:
            break
    print("The number of iterations was: ", iCount)
    print("The root is: ", xR)
    print("The error is: ", ea*100 , "%")


falsePosition(xL,xU,es,iMax)
