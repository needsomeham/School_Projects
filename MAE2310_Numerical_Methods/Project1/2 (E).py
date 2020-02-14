"""
Project 1 Part 2 (e)
This section of code finds a numerical approximation to the finite difference
approximation equation with a spacing of 5 intervals (ranging from 2 to 10).
@author: Jacob Needham
"""

#Creating the matrix to solve the
n=5
matrix = [[-2/(12/n)**2-.02,1/(12/n)**2,0,0,0],
           [1/(12/n)**2,-2/(12/n)**2-.02,1/(12/n)**2,0,0],
           [0,1/(12/n)**2,-2/(12/n)**2-.02,1/(12/n)**2,0],
           [0,0,1/(12/n)**2,-2/(12/n)**2-.02,1/(12/n)**2],
           [0,0,0,1/(12/n)**2,-2/(12/n)**2-.02]]
b = [-.2-20/((12/n)**2),
     -.2,
     -.2,
     -.2,
     -.2-160/((12/n)**2)]


#Creating necessary vectors to use Gauss Elimation
o=None 
Xn = [None]*n
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
    
    #printing an answer
    print("OUTPUT")
    print("The finite difference approximation with 5 nodes is:" )
    w=1
    for element in Xn:
        print("T(",w*2,") = ",element,sep="")
        w += 1
main(o,i,j,k,matrix,b,Xn)