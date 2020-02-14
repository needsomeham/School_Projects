"""
Project 1 Part 1 (b)
This program takes the three-dimensional stress field provided by the project
and outputs the eigenvalues of the matrix. Both the modified secant method and
the fixed point method are employed to find the roots of the characteristic 
equation x^3 - I1*x^2 + I2*x - I3
@author: Jacob Needham
"""
import numpy as np
import matplotlib.pyplot as graph
print("OUTPUT")

#Matrix given in problem statement
m = [[9,13,24],
     [13,6,14],
     [24,14,15]]

#Invarients of the 3x3 matrix
# I1 = trace(matrix)
I1 = m[0][0] + m[1][1] + m[2][2]
# I2 = 1/2*(trace(matrix)^2+trace(matrix^2))
I2 = m[0][0]*m[1][1] +m[1][1]*m[2][2] + m[0][0]*m[2][2] \
- m[0][1]*m[1][0] - m[1][2]*m[2][1] - m[0][2]*m[2][0]
# I3 = determinat(matrix)
I3 = -m[0][2]*m[1][1]*m[2][0] + m[0][1]*m[1][2]*m[2][0] \
+ m[0][2]*m[1][0]*m[2][1] - m[0][0]*m[1][2]*m[2][1] - m[0][1]*m[1][0]*m[2][2] \
+ m[0][0]*m[1][1]*m[2][2]


#Charicteristic polynomial to solve for eigenvalues
#the most important thing for this project is noticing that the fixed point
#method will diverge if, roughly speaking, the funtion is too steep
#around a aroot. Dividing the equation by a value larger than the largest
#eigenvalue will squash the funciton and potntiallal allow it to converge to a
#point.
def function(x):
    y = abs((x**3 - I1*x**2 + I2*x - I3)/ (-3*I3))
    return y


#Creating a graph of the function
def plotSpace():
    #setting up function
    x = np.arange(-10000,10000,.01)
    y = function(x)
    graph.ylim(-20,20)
    graph.xlim(-15,50)
    #plotting function  
    graph.plot(x, y) 
    
    #setting up graph
    graph.xlabel('x - axis') 
    graph.ylabel('y - axis') 
    graph.title('Project 1 Problem 1 B') 
    
    #plotting axis
    graph.plot(x, x*0 + 0 , linewidth = .5, color = 'black')
    graph.plot(x*0 + 0, x, linewidth =.5, color = 'black')
    
    #grpahing
    graph.show() 

plotSpace()


#The modified secant method takes an inital guess x0 and evaluates the
#function a small distance, d, away. It solves for the intercept of the 
#line created and then chooses that value for the new input.
def modSecant(x0,es,iMax):
    ea=es
    xR = x0
    iCount = None
    d=.01
    for iCount in range(0,iMax):
        iCount +=1
        xR = x0 - (d*xR*function(x0))/(function(x0 + (d*x0))-function(x0))
        if xR != 0:
            ea = abs((xR-x0)/xR)*100
        if ea<es or iCount > iMax:
            break
        x0 = xR
        
    print("Number of iterations: ", iCount)
    print("An eigenvalue is: ", xR)
    print("The error is: ", ea*100 , "%")
    print("")
    
modSecant(1,.001,300)
modSecant(-15,.001,300)
modSecant(40,.001,300)

#to create space between modified secant and fixed point
print()
print()


#The fixed point method evaluates the funtion at an inital guess x0 and 
#adds to the solution the inital guess. This process is repeated until 
#the root is found.
def fixedPoint(x0,es,iMax):
    xR = x0
    iCount = 0
    ea = es
    #eaOLD = None
    for iCount in range(iMax):
        iCount += 1
        xROld = xR
        xR = xROld + function(xROld)
        #print(xR)                      #helpful for making cobwebs
        #eaOLD = ea
        if xR != 0:
            ea = abs((xR-xROld)/xR)
        #if (eaOLD - ea)/ea < 1000:     #catches a diverging function
         #   print("Its diverging!")
          #  break
        if ea<es or iCount > iMax:
            break

    print("Number of iterations: ", iCount)
    print("An eigenvalue is: ", xR)
    print("The error is: ", ea*100 , "%")
    print("")

fixedPoint(-4,.001,300)    
fixedPoint(-40,.001,300)    
fixedPoint(40,.0001,300)

