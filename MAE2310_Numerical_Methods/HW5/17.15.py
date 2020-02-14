'''
Homework 5 Problem 17.15
The following data are provided:
    
x | 1    2    3    4    5
-----------------------------
y | 2.2  2.8  3.6  4.5  5.5

You want to use leat-squares regression to fit these data with the following
model, y = a + bx + c/x. Determine the coefficients by setting up and solving 
Eq. (17.25). 

@author: Jacob Needham
'''

import numpy as np

x = np.matrix([1,2,3,4,5], dtype = 'float')
y = np.matrix([2.2,2.8,3.6,4.5,5.5], dtype = 'float')
m = 3                             #number of basis functions plus a constant
n = 5                             #height of matrix
z = np.matrix([[None for x in range(n)] for y in range(m)],dtype='float')


#Hard coding each part of the basis function
def a0(x):
    y = 1
    return y

def a1(x):
    y = x
    return y

def a2(x):
    y = 1/x
    return y

#Populating the z matrix
for row in range(m):
    for column in range(n):
        if row == 0:
            z[0,column] = a0(x[0,column])
        if row == 1:
            z[1,column] = a1(x[0,column])
        if row == 2:
            z[2,column] = a2(x[0,column])
            
#orients matrix for output        
z=z.transpose()
y=y.transpose()

#this solves for the solution vector that contains coefficients a1-an
#solution vector A = (z(t)*z)^-1 * z(t) * y
A = np.dot(np.dot(np.linalg.inv(np.dot(z.transpose(),z)),z.transpose()),y)

a0 = A[0,0]
a1 = A[1,0]
a2 = A[2,0]

#Printing solution equation
print("The base funtion that most accuratly pass though the points is:")
print("y= ",round(a0,4)," + ",round(a1,4),"*x + ",round(a2,4),"/x",sep = '')
