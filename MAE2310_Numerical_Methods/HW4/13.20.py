# -*- coding: utf-8 -*-
"""
Homework 4 Problem 13.20
The normal distribution is a bell-shaped curve defined by y=e^(-x^2).
Use the golden-section search to determine the location of the inflection 
point of this curve for positive x.

@author: Jacob Needham
"""
import math

#function equation
def function(x):
    y = math.exp(-x**2)
    return y

def functionDer(x):
    y = -2*x*math.exp(-x**2)
    return y

def functionDer2(x):
    y = (4*x**2-2)*math.exp(-x**2)
    return y

    
def goldenSearchMin(es,iMax,L,U):
    iCount = 0
    ea = es
    R = ((5**.5)-1)/2
    xL = L
    xU = U
    d = R *(xU - xL)
    x1 = xL + d
    x2 = xU - d
    f1 = functionDer(x1)
    f2 = functionDer(x2)
    if f1<f2 :
        xopt = x1
        fx = f1
    else:
        xopt = x2
        fx = f2
    for iCount in range(iMax):
        d = R*d
        xinit = xU - xL
        if f1 < f2:
            xL = x2
            x2 = x1
            x1 = xL + d
            f2 = f1
            f1 = functionDer(x1)
        else:
            xU = x1
            x1 = x2
            x2 = xU - d
            f1 = f2
            f2 = functionDer(x2)
        iCount += 1
        if f1 < f2:
            xopt = x1
            fx = f1
        else:
            xopt = x2
            fx = f2
        if xopt != 0:
            ea = (1-R)* abs(xinit/xopt)*100
        if ea < es:
            break
    print("OUTPUT")
    print("The x value for the inflection point is:",round(function(fx),4))
    print("Number of iterations to convergence:", iCount)
    

goldenSearchMin(.001,100,-20,20)