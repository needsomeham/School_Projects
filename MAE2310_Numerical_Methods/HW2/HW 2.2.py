'''
Homeowork 2.2
 Determine the lowest real root of f(x) = −3x^3 + 19x^2 − 21x − 12
(a) Graphically.
(b) Using the bisection method to determine the lowest root with εs = 2%.
Employ the initial guesses of xl = −1 and xu = 0.
(c) Perform the same computation as in (b) but using the false position method.
'''

import matplotlib.pyplot as graph
import numpy as np

#peramiters defined by the user
xL = -1.0
xU = 0
es = .002
iMax = 50

def function(x):
    y = -3*x*x*x + 19*x*x -21*x-12
    return y

'''
Part A
Graphically
'''

def plotSpace ():
    #setting up function
    x = np.arange(-10,10,.01)
    y = function(x)
    graph.ylim(-25,25)
    graph.xlim(-10, 10)
    #plotting function  
    graph.plot(x, y) 
    
    #setting up graph
    graph.xlabel('x - axis') 
    graph.ylabel('y - axis') 
    graph.title('Homeowrk 2.2: Monday Jan 14 ') 
    
    #plotting axis
    graph.plot(x, x*0 + 0 , linewidth = .5, color = 'black')
    graph.plot(x*0 +0, y, linewidth =.5, color = 'black')
    
    #grpahing
    graph.show() 

plotSpace()

'''
Part B
Bisection Method
'''

def bisectionMethod(xL,xU,es,iMax):
    iCount = 0
    xR = xL
    ea = es
    xOld = None

    for iCount in range(0,iMax):
        xOld = xR
        xR = (xL + xU) / 2
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
    print("The root is: " , xR)
    print("The error was: " , ea*100 , "%")

bisectionMethod(xL,xU,es,iMax)
print("")

'''
Part C
False Postion Method
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
    print("The root is: ", xR)
    print("The error is: ", ea*100 , "%")
        
falsePosition(xL,xU,es,iMax)
        
