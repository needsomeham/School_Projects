"""
Textbook problem 18.23

Develop, debug, and test a program in either a high-level language or macro 
language of your choice to implement cubic spline interpolation based on 
Fig. 18.18. Test the program by duplicating
Example 18.10. (table 18.1)

@author: Jacob Needham
"""

import numpy as np

'''
Main function defines data series of points and what X is to be found and calls
the cubic spline interpolation to find corresponding Y value.
'''
def Main():    
    #put data here:
    x = np.matrix([3,4.5,7,9], dtype = 'float')
    y = np.matrix([2.5,1,2.5,.5], dtype = 'float')
    n = x.size 
    
    find_x = 5
    CubicSplineInt(x,y,n,find_x)

'''
Function takes data series x,y and the length of the data set, n, and finds a
coresponding Y value (y_eval) for an input X value (x_eval).
'''
def CubicSplineInt(x,y,n,x_eval):
    #initilzing matrix A, solution vector b, and 2nd derivates vector Fpp
    A = np.matrix([[0 for x in range(n)] for y in range(n)], dtype = 'float')
    A[0,0] = 1
    A[n-1,n-1] = 1
    
    Fpp = np.matrix([None]*n, dtype = 'float')
    
    b = np.matrix([None]*n, dtype = 'float')
    b[0,0] = 0
    b[0,n-1] = 0
    
    #Populating the A matrix with left hand side of equation 18.37 from book
    #and b matrix with right hand side of same equation.
    for i in range(1,n-1):
        A[i,i-1] = x[0,i] - x[0,i-1]
        A[i,i] = 2*(x[0,i+1] - x[0,i-1])
        A[i,i+1] = x[0,i+1] - x[0,i]
        b[0,i] = (6*(y[0,i+1]-y[0,i]))/(x[0,i+1]-x[0,i]) \
                 + (6*(y[0,i-1]-y[0,i]))/(x[0,i]-x[0,i-1])
    
    #linear algebra to solve for Fpp vector using Fpp = A^-1*b
    Fpp = np.dot(np.linalg.inv(A),np.transpose(b))
    
    #calculating the interpolated point for the chosen x value x_eval
    for i in range(n-1):
        if (x[0,i-1] <= x_eval and x[0,i] >= x_eval):
            y_eval = (Fpp[i-1,0]*(x[0,i]-x_eval)**3)/(6*(x[0,i]-x[0,i-1])) \
                    + (Fpp[i,0]*(x_eval - x[0,i-1])**3)/(6*(x[0,i]-x[0,i-1])) \
                    + ((y[0,i-1]/(x[0,i]-x[0,i-1]))-(Fpp[i-1,0]*(x[0,i]-x[0,i-1]))/6)*\
                    (x[0,i]-x_eval) 
                    + ((y[0,i]/(x[0,i]-x[0,i-1]))-(Fpp[i,0]*(x[0,i]-x[0,i-1]))/6)*\
                    (x_eval-x[0,i-1])
    print('OUTPUT')
    print('For the given data set and x value=',x_eval,', the interpolated y value is: ',\
          round(y_eval,4), sep = '')

Main()