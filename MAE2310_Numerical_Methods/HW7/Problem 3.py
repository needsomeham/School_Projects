"""
Homework 7 Problem 3
Develop an algorithm which, for a given function f(x), interval bounds a and b with a < b,
and error tolerance per subinterval tol, applies adaptive quadrature to approximate the 
integration of f(x) dx from a to b based on the pseudocode that was presented in class 
and can be found on page 642 of the textbook.

@author: Jacob Needham
"""
import math

def function(x):
    y = x**0.1 * (1.2 - x)*(1 - math.exp(20*(x-1)))
    return y

def quadapt(a,b,tol):
    c = (a+b)/2
    Fa = function(a)
    Fb = function(b)
    Fc = function(c)
    quadap = qStep(a,b,tol,Fa,Fb,Fc)
    return quadap
    
def qStep(a,b,tol,Fa,Fb,Fc):
    h1 = b-a
    h2 = h1/2
    c = (a+b)/2
    Fd = function((a+c)/2)
    Fe = function((c + b)/2)
    I1 = h1/6*(Fa +4*Fc + Fb)
    I2 = h2/6*(Fa + 4*Fd + 2*Fc + 4*Fe + Fb)
    if abs(I2 -I1) <= tol:
        I = I2 + (I2 - I1)/15
    else :
        Ia = qStep(a,c,tol,Fa,Fc,Fd)
        Ib = qStep(c,b,tol,Fc,Fb,Fe)
        I = Ia + Ib
    return I

def main():
    a=0
    b=1
    tol = .00001
    print("The value found for a tolerance of .0001:",quadapt(a,b,tol))
    
main()