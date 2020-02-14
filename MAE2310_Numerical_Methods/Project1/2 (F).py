"""
Project 1 Part 2 (f)
This section of code finds a numerical approximation to the finite difference
approximation equation with a spacing of n intervals between boundary
conditions at x=0 and x=12.
@author: Jacob Needham
"""
#Getting user input for number of nodes
n = int(input("How many nodes would you like?\n"))

#Initializing finite difference approximation matrix of size n.
matrix = []
for i in range(n):                     #empty matrix
    matrix.append([0]*n)
    
for i in range(n-1):                   #the 1/(deltaX/n)^2 term (Ti-1 and Ti+1)
    matrix[i][i+1] = 1/((12/n)**2)
    matrix[i+1][i] = 1/((12/n)**2)
for i in range(n):                     #the current term - solution matrix term 
    matrix[i][i] = -2/(12/n)**2-.02    #(Ti -.2Ti)
    
b=[None]*n
for i in range(1,n-1):
    b[i] = -.2
b[0] = -.2-20/((12/n)**2)
b[n-1] = -.2-160/((12/n)**2) 

#Creating the necessary matricies to use Gauss Elimination
o=None
Xn = [None]*n   #solution space
theMax = [None]*n #lists to hold the maxes and ratios of each row
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
    #calling Gauss Elimination
    forwardElim(k,i,j,matrix)
    backwardSub(Xn,b,matrix)
    
    #printing each answer
    w=12/(n+1)
    print()
    print("The finite difference approximation with",n,"nodes is:" )
    for element in range(len(Xn)):
        print("T(",round(w*(element+1),2),") = ",Xn[element],sep="")
main(o,i,j,k,matrix,b,Xn)