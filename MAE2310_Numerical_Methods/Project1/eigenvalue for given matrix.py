"""
This code will take the example matrix given and find
the eigenvalues associated with it.

@author: Jacob Neehdam
"""

#importing libraries to be used later
import numpy as np
import matplotlib.pyplot as graph
import sympy.parsing.sympy_parser as parse
from sympy import * 
import ast
#loading the matrix from the assignment
m = [[9,13,24],
     [13,6,14],
     [24,14,15]]

#subtracting an x from each pivot
Open = '('
Close = ')'
x = str('-x')
for row in range(3):
    hold = str(m[row][row])
    m[row][row] = Open + hold + x + Close

for row in m:
    print(row)

#finding each term of the eigenvalue problem
#x = None
term1 = str(m[0][0]) + "*(" + str(m[1][1]) + "*" + str(m[2][2]) + "-" + str(m[1][2]) + "*" + str(m[2][1]) + ")"
term2 = "-" + str(m[0][1]) + "*(" + str(m[1][0]) + "*" + str(m[2][2]) + "-" + str(m[1][2]) + "*" + str(m[2][0]) + ")"
term3 = "+" + str(m[0][2]) + "*(" + str(m[1][0]) + "*" + str(m[2][1]) + "-" + str(m[1][1]) + "*" + str(m[2][0]) + ")"
equals0 = " = 0"
finalEquation = term1 + term2 + term3   #this is the final eigenvalue equation to solve
print("Eigenvalues found by solving:")
print(finalEquation)
nextTry = ast.parse(finalEquation)
print(type(nextTry))
print('nextTry', nextTry)
FINALEquation = parse.parse_expr(finalEquation,evaluate=False)
print(type(FINALEquation))

def function(x):
    y = (9-x)*((6-x)*(15-x)-14*14)-13*(13*(15-x)-14*24)+24*(13*14-(6-x)*24)
    return y

def plotSpace ():
    #setting up function
    x = np.arange(-10000,10000,.01)
    y = function(x)
    graph.ylim(-10000,20000)
    graph.xlim(-15,50)
    #plotting function  
    graph.plot(x, y) 
    
    #setting up graph
    graph.xlabel('x - axis') 
    graph.ylabel('y - axis') 
    graph.title('Project 1 Problme 1 B') 
    
    #plotting axis
    graph.plot(x, x*0 + 0 , linewidth = .5, color = 'black')
    graph.plot(x*0 +0, y, linewidth =.5, color = 'black')
    
    #grpahing
    graph.show() 

plotSpace()

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
        
    print("The number of iterations was ", iCount)
    print("A root of the function is: ", xR)
    print("The error is: ", ea*100 , "%")
    print("")
'''    
modSecant(-10,.001,30)
modSecant(-15,.001,30)
modSecant(40,.001,30)
'''

def fixedPoint(x0,es,iMax):
    xR = x0
    iCount = 0
    ea = es
    for iCount in range(iMax):
        iCount += 1
        xROld = xR
        xR = xROld + function(xROld)
        print(xR)
        if xR != 0:
            ea = abs((xR-xROld)/xR)
        if ea<es or iCount > iMax:
            break

    print("The number of iterations was ", iCount)
    print("A root of the function is: ", xR)
    print("The error is: ", ea*100 , "%")
    print("")
'''
fixedPoint(-10,.001,30)
fixedPoint(-15,.001,30)    
fixedPoint(-40,.001,30)    
'''    
    
    
    
    
    
    
    