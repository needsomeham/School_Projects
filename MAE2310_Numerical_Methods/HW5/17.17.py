'''
Homework 5 Problem 17.17
Fit the cubic equation to the following data:

x | 3    4    5    7    8    9    11   12
------------------------------------------
y | 1.6  3.6  4.4  3.4  2.2  2.8  3.8  4.6

along with the coefficients, determine r^2 and Sy/x.

@author Jacob Needhm
'''

import numpy as np
import math

x = np.matrix([3,4,5,7,8,9,11,12], dtype = 'float')
y = np.matrix([1.6,3.6,4.4,3.4,2.2,2.8,3.8,4.6], dtype = 'float')
m = 4                            #number of basis functions plus a constant
n = 8                            #height of matrix
z = np.matrix([[None for x in range(n)] for y in range(m)],dtype='float')


#Hard coding each part of the basis function
def a0(x):
    y = 1
    return y

def a1(x):
    y = x
    return y

def a2(x):
    y = x**2
    return y

def a3(x):
    y = x**3
    return y


#This populates the z matrix
for row in range(m):
    for column in range(n):
        if row == 0:
            z[0,column] = a0(x[0,column])
        if row == 1:
            z[1,column] = a1(x[0,column])
        if row == 2:
            z[2,column] = a2(x[0,column])
        if row == 3:
            z[3,column] = a3(x[0,column])

#orients matrix for output        
z=z.transpose()
y=y.transpose()

#this solves for the solution vector that contains coefficients a1-an
#solution vector A = (z(t)*z)^-1 * z(t) * y
A = np.dot(np.dot(np.linalg.inv(np.dot(z.transpose(),z)),z.transpose()),y)

a0 = A[0,0]
a1 = A[1,0]
a2 = A[2,0]
a3 = A[3,0]

#Printing solution equation
print('OUTPUT')
print("The cubic function that most accuratly pass though the points is:")
print("y= ",round(a0,4)," + ",round(a1,4),"*x + ",round(a2,4),"*x^2 + ",
      round(a3,4),"*x^3",sep = '')


def function(x):
    y = a0 + a1*x + a2*x**2 + a3*x**3
    return y

'''
Finding Correlaton Coefficient and Standard Error
'''

Sr = 0
for i in range(n):
    Sr += (+y.item(i)-a0-a1*function(x.item(i))-a2*function(x.item(i)))**2
Sr = math.sqrt(Sr/(n-m+3))

print("The standard error is:")
print(round(Sr,3))

#Correlation Coefficient
yBar = y.sum()/n
St = 0
for i in range(n):
    St += ((y.item(i)-yBar))**2

r = math.sqrt((St-Sr)/St)
print("The standard correlation coefficient is:")
print(round(r,3))

