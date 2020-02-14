'''
Homework 2.5
Determine all roots of f(x) = −3x^3 + 19x^2 − 21x − 12
(a) Using the Secant method to a value of εs corresponding to three significant
figures.
'''

import numpy as np
import matplotlib.pyplot as graph


#peramiters defined by the user
x = None
iMax = 50
es = .001

#Rroot 1
R1x0 = 3
R1x1 = 6
#root 2
R2x0 = 0
R2x1 = 3
#root 3
R3x0 = -1
R3x1 = 1

def function(x):
    y = -3*x**3 + 19*x**2 - 21*x - 12
    return y


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
    graph.title('Homeowrk 2.5: Wednesday Jan 16 ') 
    
    #plotting axis
    graph.plot(x, x*0 + 0 , linewidth = .5, color = 'black')
    graph.plot(x*0 +0, y, linewidth =.5, color = 'black')
    
    #grpahing
    graph.show() 

plotSpace()

def secant(x0,x1,es,iMax):
    ea=es
    iCount = None
    for iCount in range(0,iMax):
        iCount +=1
        xR = x1 - (function(x1)*(x0 - x1))/((function(x0) - function(x1)))
        if xR != 0:
            ea = abs((xR-x1)/xR)*100
        if ea<es or iCount > iMax:
            break
        x0 = x1
        x1 = xR
        
    print("The number of iterations was ", iCount)
    print("A root of the function is: ", xR)
    print("The error is: ", ea*100 , "%")
    print("")

secant(R1x0, R1x1, es, iMax)
secant(R2x0, R2x1, es, iMax)
secant(R3x0, R3x1, es, iMax)