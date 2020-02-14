'''
Homework 2.4 
Determine the real roots of f(x) = 0.5x^3 − 3x^2 + 6x − 1
(a) Graphically.
(b) Using the Newton-Raphson method to within εs = 0.01%.
'''

import numpy as np
import matplotlib.pyplot as graph

#peramiters defined by the user
x = None
x0 = 5
es = .001
iMax = 50


def function(x):
    y = 0.5*x*x*x - 3*x*x + 6*x - 1
    return y

def functionDer(x):
    y = 1.5*x*x - 6*x + 6
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
    graph.title('Homeowrk 2.4: Wednesdy Jan 14 ') 
    
    #plotting axis
    graph.plot(x, x*0 + 0 , linewidth = .5, color = 'black')
    graph.plot(x*0 +0, y, linewidth =.5, color = 'black')
    
    #grpahing
    graph.show() 

plotSpace()

'''
Part B
Newton Raphson
'''

def newtonRaphson(x0,es,iMax):
    ea=es
    xR = x0
    iCount = xOld = ea = None
    for iCount in range(0,iMax):
        iCount +=1
        xOld = xR
        xR = xOld - (function(xOld)/functionDer(xOld))
        if xR != 0:
            ea = abs((xR-xOld)/xR)*100
        if ea<es or iCount > iMax:
            break
    print("The number of iterations was ", iCount)
    print("The root of the function is: ", xR)
    print("The error is: ", ea*100 , "%")

newtonRaphson(x0, es, iMax)
 