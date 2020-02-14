'''
Homework 2.6
Müller’s method. Test it by:
duplicating Example 7.2.
Divide a polynomial f(x) = x**5 - 5*x**4 + x**3 - 6*x +10 by the monomial factor x-2.
'''

import numpy as np
import matplotlib.pyplot as graph
import cmath


#peramiters defined by the user
x = None
iMax = 50
es = .001

#Rroot 1
x0 = 6
x1 = 8
x2 = -5


def function(x):
    y = (x**5 - 5*x**4 + x**3 - 6*x +10) / (x-2)
    return y


def plotSpace ():
    #setting up function
    x = np.arange(-10,10,.01)
    y = function(x)
    graph.ylim(-150,25)
    graph.xlim(-10, 10)
    #plotting function  
    graph.plot(x, y) 
    
    #setting up graph
    graph.xlabel('x - axis') 
    graph.ylabel('y - axis') 
    graph.title('Homeowrk 2.6: Friday Jan 18 ') 
    
    #plotting axis
    graph.plot(x, x*0 + 0 , linewidth = .5, color = 'black')
    graph.plot(x*0 +0, y, linewidth =.5, color = 'black')
    
    #grpahing
    graph.show() 

plotSpace()


def Muller (x0,x1,x2,es,iMax):
    ea = es
    iCount = None
    for iCount in range(0,iMax):
        iCount += 1
        h0 = x1 - x0
        h1 = x2 - x1
        if h1 ==0:
            break
        d0 = (function(x1)- function(x0))/h0
        d1 = (function(x2)- function(x1))/h1
        if (h1+h0) == 0:
            break
        a = (d1-d0)/(h1+h0)
        b = a*h1 + d1
        c = function(x2)
        rad = cmath.sqrt(b**2 - 4*a*c)
        if abs(b + rad) > abs(b - rad):
            den = b + rad
        else:
            den = b - rad
        xR = x2 + (-2*c)/den
        if xR != 0:
            ea = abs((xR-x2)/xR)*100
        if ea <es or iCount >= iMax:
            exit 
        x0 = x1
        x1 = x2
        x2 = xR
    print("A root is: ", xR)
    print("The number of iterations was: ", iCount)
    print("The error is: ", ea*100 , "%")
    
Muller(x0,x1,x2,es,iMax)
        
    