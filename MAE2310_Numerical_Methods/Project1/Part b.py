"""
Project 1 Part 2 (c)
A solution to constants B and C from the system of equations found solving the
heat equation using ODE techniques.
@author: Jacob Needham
"""
import math
#System of equations from solution to ODE:
# 30 = B + C
# 170 = B * e^(sqrt(.02)*12) + e^(-sqrt(.02)*12)

#Loading a matrix and solution vector with above equations
matrix = [[1,1],
          [math.exp(math.sqrt(.02)*12),math.exp(-math.sqrt(.02)*12)]]
b = [30,170]


#Creating necessary vectors to use Gauss Elimation
n=2
o=None
#solution space
Xn = [None]*n
#lists to hold the maxes and ratios of each row
theMax = [None]*n
ratio = [None]*n
k = i = j = 0

def partialPivoting(o,matrix,i):
    for row in matrix:
        theMax[o] = max(row, key=abs)
        o += 1    
    for m in range(len(matrix)):
        ratio[m] = abs(matrix[m][m]/theMax[m])    
    if i < n:
        if ratio[i-1] < max(ratio[i:], key=abs):
            swapIndex = max(ratio[i:])
            matrix[i-1] = matrix[swapIndex]

def forwardElim(k,i,j,matrix):
    for k in range(1,n):
        for i in range(k+1,n+1):
            
            #partial pivoting
            o=0
            partialPivoting(o,matrix,i)
            
            #forward elimination
            factor = matrix[i-1][k-1]/matrix[k-1][k-1]
            for j in range(k+1,n+1):
                matrix[i-1][j-1] = matrix[i-1][j-1] - factor * matrix[k-1][j-1]
            b[i-1] = b[i-1] - factor * b[k-1]
 
def backwardSub(Xn,b,matrix):       
    Xn[n-1] = b[n-1]/matrix[n-1][n-1]
    for i in range(n-1,0,-1):
        Sum = b[i-1]
        for j in range(i+1,n+1):
            Sum = Sum - matrix[i-1][j-1] * Xn[j-1]
        Xn[i-1] = Sum/matrix[i-1][i-1]

def main(o,i,j,k,matrix,b,Xn):
    #calling each function
    forwardElim(k,i,j,matrix)
    backwardSub(Xn,b,matrix)
    
    #printing answers
    print("OUTPUT:")
    print("Coefficients A and B are:")
    print("A:", Xn[0])
    print("B:", Xn[1])
    
main(o,i,j,k,matrix,b,Xn)