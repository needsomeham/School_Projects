"""
Homework 7 Problem 2
Develop an algorithm which, for a given function f(x), interval bounds a and b with 
a < b, and a prescribed number of subintervals n, approximates integrating f(x) dx from 
a to b according to the following procedure:
(a) If n = 1, it applies the trapezoidal rule.
(b) If n is even, it applies the multiple application Simpson’s 1/3 rule.
(c) If n ≥ 3 and n is odd, it applies the multiple application Simpson’s 1/3 rule
on the first n − 3 subintervals, and applies the Simpson’s 3/8 rule on the
last three subintervals.

@author: Jacob Needham
"""
import math

def function(x):
    y = x**0.1 * (1.2 - x)*(1 - math.exp(20*(x-1)))
    return y

def multiTrap(n,a,b):
    h = (b-a)/n
    x = a
    total = function(x)
    for i in range(1,n):
        x += h
        total += 2*function(x)
    total += function(b)
    I =(b-a)* total/(2*n)
    return I

def simp13(a,b,n,h):
    x=a
    total = function(x)
    #h=(b-a)/n
    for i in range(2,n-1,2):
        x += h
        total = total + 4*function(x)
        x += h
        total = total + 2*function(x)
    x += h
    total = total + 4*function(x)
    x += h
    total = total + function(x)
    I = (b-a)*total/(3*n)
    return I
    
def simp38(a,b,n,h):
    x=a
    dx = (b-a)/n
    total = function(x)
    x += dx
    total += 3*function(x)
    x += dx
    total += 3*function(x)
    x += dx
    total += function(x)
    ans = (b-a)*total/8    
    return ans

def printF(area):
    print("The approximate area under the curve is", area)
    
def main():
    a = 0
    b = 1
    n = 700
    h = (b-a)/n
    
    if n == 1:
        area = multiTrap(n,a,b)
        printF(area)
        
    if n%2 ==0:
        area = simp13(a,b,n,h)
        printF(area)
        
    if n%2 != 0:
        areaA = simp13(a,b-2*h,n,h)
        areaB = simp38(b-2*h,b,n,h)
        printF(areaA+areaB)

main()