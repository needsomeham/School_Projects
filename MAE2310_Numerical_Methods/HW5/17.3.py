'''
Homework 5 Problem 17.3
Use a least-squares regression to fit a straight line to:
    
x | 0  2  4  6  9  11  12  15  17  19
---------------------------------------
y | 5  6  7  6  9  8   7   10  12  12

along with the slope and intercept, compute the standard error of the the 
estimate and the correlation coefficient. Plot the data and the regression 
line. Then repeat the problem, but regress x vs y - that is, switch the 
varibles. Interpret your results.

@author: Jacob Needham
'''

'''
Finding best fit function
'''
import math
import numpy as np
import matplotlib.pyplot as graph

#data from problem statement
x = np.matrix([0,2,4,6,9,11,12,15,17,19],dtype='float')
y = np.matrix([5,6,7,6,9,8,7,10,12,12],dtype='float')
m = 2                             #number of basis functions plus a constant
n = 10                            #height of matrix
z = np.matrix([[None for x in range(n)] for y in range(m)],dtype='float')


#Hard coding each part of the basis function
def a0(x):
    y = 1
    return y

def a1(x):
    y = x
    return y


#This populates the z matrix
for row in range(m):
    for column in range(n):
        if row == 0:
            z[0,column] = a0(x[0,column])
        if row == 1:
            z[1,column] = a1(x[0,column])

#orients matrix for output
z=z.transpose()
y=y.transpose()

#this solves for the solution vector that contains coefficients a1-an
#solution vector A = (z(t)*z)^-1 * z(t) * y
A = np.dot(np.dot(np.linalg.inv(np.dot(z.transpose(),z)),z.transpose()),y)


a0 = A[0,0]
a1 = A[1,0]

#Printing the solution equation
print("The equation of the line passing through the points is:")
print("y=",round(a1,3),"x + ",round(a0,3),sep="")

#line of best fit function 
def function(x):
    y = a0 + a1*x
    return y


'''
Finding standard error and correlation coefficient
'''
#Standard Error
Sr = 0
for i in range(n):
    Sr += (function(y.item(i)-a0-a1*x.item(i)))**2
Sy = math.sqrt(Sr/(n-2))

print("The standard error is:")
print(round(Sy,3))

#Correlation Coefficient
yBar = y.sum()/n
St = 0
for i in range(n):
    St += (function(y.item(i)-yBar))**2
r = math.sqrt((St-Sr)/St)
print("The standard correlation coefficient is:")
print(round(r,3))



'''
Plot
'''

#graph
def plotSpace ():
    #setting up function
    x = np.arange(-100,100,.01)
    y = function(x)
    graph.ylim(0,20)
    graph.xlim(0, 20)
    #plotting function  
    graph.plot(x, y)
    #plotting data series
    graph.plot([0,2,4,6,9,11,12,15,17,19],[5,6,7,6,9,8,7,10,12,12],'ro')
    
    #setting up graph
    graph.xlabel('x - axis') 
    graph.ylabel('y - axis') 
    graph.title('Homeowrk 5 Problem 3') 
    
    #plotting axis
    graph.plot(x, x*0 + 0 , linewidth = .5, color = 'black')
    graph.plot(x*0 +0, y, linewidth =.5, color = 'black')
    
    #grpahing
    graph.show() 

plotSpace()




'''
DISCUSSION
The second half of the assingment is identical, however x and y are flipped.
It is intreting to note that beacuse the correlation coefficient measures
the difference between the average y of the points and the current point, it
is much more sensative to the relative height of the points. The line may be
just as 'tightly' fitted to the data, but becaue the point are more spread in
the part of the assignment, it may not be represented in the coefficients.
'''