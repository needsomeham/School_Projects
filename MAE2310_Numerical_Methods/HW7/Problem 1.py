"""
Homework 7 Problem 1
Develop an algorithm which, for a given function f(x), interval bounds a and b with a < b,
and a prescribed number of subintervals n, applies the multiple application trapezoidal 
rule to approximate integrating f(x) dx from a to b.

@author: Jacob Needham
"""
import math

def function(x):
    y = x**0.1 * (1.2 - x)*(1 - math.exp(20*(x-1)))
    return y

def multiTrap(a,b,n):
    h = (b-a)/n
    x = a
    total = function(x)
    for i in range(1,n):
        x += h
        total += 2*function(x)
    total += function(b)
    I =(b-a)* total/(2*n)
    return I

def main():
    print("The value found for 600 iterations:",multiTrap(0,1,600))
    
main()