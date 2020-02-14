'''
Monday Jan 14 class:
Homework 2.1
Determine the real root off(x) = 0.8x5−8x4+ 46x3−90x2+ 83x−26
(a)  Graphically.
(b)  Using the bisection method to determine the root withεs= 10%.  
Employthe initial guesses of xl= 0.5 and xu= 1.0.
(c)  Perform the same computation as in (b) but use the false position methodandεs= 0.2%.
'''

import matplotlib.pyplot as graph
import numpy as np

#Peramiters defined by the user
xL = .05
xU = 1.0
es = .001
iMax = 50

#creating a function class to be called later
def function(x):
    y = .8*x*x*x*x*x - 8*x*x*x*x + 46*x*x*x - 90*x*x + 83*x - 26 #often python struggles to raise to a power
    return y

'''
Part A
Graphically
'''

#building a graph
def plotSpace ():
    #imporitng function
    x = np.arange(-10,10,.01)
    y = function(x)
    graph.ylim(-20,20)
    graph.xlim(-1, 6)
    
    #plotting function  
    graph.plot(x, y) 
    
    #setting up graph
    graph.xlabel('x - axis') 
    graph.ylabel('y - axis') 
    graph.title('Homeowrk 2.1: Monday Jan 14 ') 
    
    #plotting axis
    graph.plot(x, x*0 + 0 , linewidth = .5, color = 'black')
    graph.plot(x*0 +0, y, linewidth =.5, color = 'black')
    
    #grpahing
    graph.show() 

plotSpace()


''' 
Part B 
Using the bisection method to determine the root with εs = 10%. Employ
the initial guesses of xl = 0.5 and xu = 1.0.
'''

#buiding the bisection method
def bisectionMethod(xL,xU,es,iMax):
    iCount = 0
    xR = xL
    ea = es
    xOld = None

    for iCount in range(0,iMax):
        xOld = xR
        xR = (xL + xU) / 2 #this averages the function over a range and narrows on the root
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
    print("The numner of iterations was: ", iCount)
    print("Using bisection, the root is: " , xR)
    print("The error was: " , ea*100 , "%")


bisectionMethod(xL,xU,es,iMax)
print("")

'''
Part C
Perform the same computation as in (b) but using the false position method.
'''

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
    print("Using fasle postion, the root is: ", xR)
    print("The error is: ", ea*100 , "%")
        
falsePosition(xL,xU,es,iMax)
        
        
        
