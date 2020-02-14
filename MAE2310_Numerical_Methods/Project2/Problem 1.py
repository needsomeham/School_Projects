"""
Numerical Methods Project 2

Problem 1

@author: Jacob Needham
"""
import math

'''
One function to rule them all #LOTR 
'''
def Main():
    a,b,Ea = getEa()
    n = numberOfIterations(Ea,a,b)
    goldenSearchMin(Ea,n,a,b)
    
    
'''
Function takes in lower and upper limits, and absolute error from user and
returns a tuple with answered data.
'''
def getEa():
    a = float(input("What is the lower limit to search?\n"))
    b = float(input("What is the upper limit to search?\n"))
    Ea = float(input("What is the desired absolute error?\n"))
    print() #blank line to add space
    return a,b,Ea

'''
function to find min of
'''
def function(x):
    y = 2*x + 3/x
    return y

'''
Rounded function to find number of iterations to guarantee a desired error. Over rounds
to ensure that the error is on the low side
'''
def numberOfIterations(Ea,a,b):
    n = int(math.ceil(math.log2((abs(b-a))/Ea)))
    return n

'''
Function finds the min of a function based on upper limit, lower limit, and numer of 
iterations
'''
def goldenSearchMin(Ea,n,L,U):
    iCount = 0
    R = ((5**.5)-1)/2
    xL = L
    xU = U
    d = R *(xU - xL)
    x1 = xL + d
    x2 = xU - d
    f1 = function(x1)
    f2 = function(x2)
    if f1<f2 :
        xopt = x1
        fx = f1
    else:
        xopt = x2
        fx = f2
    for iCount in range(n):
        d = R*d
        xinit = xU - xL
        if f1 < f2:
            xL = x2
            x2 = x1
            x1 = xL + d
            f2 = f1
            f1 = function(x1)
        else:
            xU = x1
            x1 = x2
            x2 = xU - d
            f1 = f2
            f2 = function(x2)
        iCount += 1
        if f1 < f2:
            xopt = x1
            fx = f1
        else:
            xopt = x2
            fx = f2
        if xopt == 0:
            printStatement(n,Ea,fx,xopt)
            print("And in this particular case the root has zero error")
            exit
    printStatement(n,Ea,fx,xopt)

''' 
Generic print statment           
'''
def printStatement(n, Ea, fx, xopt):
    print("The program ran for", n, 'iterations with less than', Ea, 'error.')
    print("The minimal value found was:", round(fx,5))
    print("The x value for the minimal value is:",round(xopt,5))

Main()
