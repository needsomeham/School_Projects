'''
AUTHOR @Jacob Neeham
Textbook problem 9.18
This progam takes an input matrix defined by the book and outputs
the solution vector. The method for solving the output vector is 
though forward elimination suplimented by partial pivoting
'''

#setting up matrix from user
matrix = [[1,2,-1],[5,2,2],[-3,5,-1]]
b = [2,9,1]
n=len(matrix)
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
    
    #printing each answer
    w=1
    for element in Xn:
        print("x",w," = ",element,sep="")
        w += 1
main(o,i,j,k,matrix,b,Xn)