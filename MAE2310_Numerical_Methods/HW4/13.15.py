"""
Homework 4 Problem 13.15
Develop a program using a programming or macro language to implement Newton’s 
method. The subroutine should have the following features:
    -Iterate until the relative error falls below a stopping criterion or
    exceeds a maximum number of iterations.
    -Returns both the optimal x and f(x).
Test your program with the same problem as Example 13.3.

@author: Jacob Needham
"""
print("OUTPUT")
#function equation
def function(x):
    y = -1.5*x**6 - 2*x**4 + 12*x
    return y

#first derivitive
def functionDer(x):
    y = -9*x**5 -8*x**3 + 12
    return y

#second derivitive
def functionDer2(x):
    y = -45*x**4 -24*x**2
    return y


#Newton Raphson technique    
def newtonMethod(x0,es,iMax):
    ea=es
    xR = x0
    iCount = xOld = ea = None
    for iCount in range(0,iMax):
        iCount +=1
        xOld = xR
        xR = xOld - (functionDer(xOld)/functionDer2(xOld))
        if xR != 0:
            ea = abs((xR-xOld)/xR)*100
        if ea<es or iCount > iMax:
            break
    print("The max was found after", iCount,"iterations")
    print("The x value of the max of the function is: ", round(xR,4))
    print("The function evaluated at the max is:", round(function(xR),4))
    print("The error is: ", round(ea*100,4) , "%")

newtonMethod(2, .001, 30)
 