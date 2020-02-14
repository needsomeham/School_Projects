'''
AUTHOR @Jacob Neeham
Textbook problem 9.18
This progam takes an input matrix defined by the user and outputs an inverted
matrix and a solution vector based using LU decompostion. The method for 
solving the output vector is naive forward elimination. 
'''
#creating base matrix
import np
matrix = np.array([])

#asking user for size of matrix, values to populate matrix, and solution matrix
n = int(input("How many rows and columns would you like in your square matrix? "))
matrix = []*n
for row in range(n): 
    matrix.append([input("Values for row {} ".format(row+1)).split(",")])

b = np.array([input("Input the solution vector seperated by commas").split(",")])
b = b.transpose()

#unit vectors to find inverse
b0 = [1,0,0]
b1 = [0,1,0]
b2 = [0,0,1]

#blank vectors for inverse solution
d  = [None]*n
d0 = [None]*n
d1 = [None]*n
d2 = [None]*n

X0 = [None]*n
X1 = [None]*n
X2 = [None]*n

#blank Upper matrix
U = []
for row in range(n):
    U.append([0,0,0])

#blank Lower matrix
L = []
for row in range(n):
    L.append([0,0,0])
for cell in range(n):     #this 
    L[cell][cell] = 1
            
#creating decompose matrix
def decompose(matrix, n):
    for k in range(1,n):
        for i in range(k+1,n+1):
            factor = matrix[k-1][k-1]/matrix[i-1][k-1]
            print('factor', factor)
            matrix[i-1][k-1] = factor
            for j in range(k+1,n+1):
                matrix[i-1][j-1] = matrix[i-1][j-1] - factor*matrix[k-1][j-1]
                
#making U matrix                        
def upper(matrix, n, U):
    for row in range(n):
        for counter in range(row,n):
            U[row][counter] = matrix[row][counter]

#making L matrix
def lower(matrix, n, L):
    for row in range(n):
        for counter in range(row):
            L[row][counter] = matrix[row][counter]            
  
#solving the [L]*d = b
def forwardSub(b,d,L):
    d[0] = b[0]
    Sum = d[0]
    for row in range(1,n):
        d[row] = b[row]-Sum
        Sum = d[row]        
    
    Sum = b[0]
    for row in range(0,n):
        d[row] =  b[row]/(L[row][row-1]+ 1 + Sum)
        Sum = d[row]
#solving [U]*b = x
def backwardSub(Xn,b,matrix):       
    Xn[n-1] = b[n-1]/matrix[n-1][n-1]
    for i in range(n-1,0,-1):
        Sum = b[i-1]
        for j in range(i+1,n+1):
            Sum = Sum - matrix[i-1][j-1] * Xn[j-1]
        Xn[i-1] = Sum/matrix[i-1][i-1]

#calling all functions necessary to invert matrix
def inverse(matrix,n,U,L,b0,b1,b2,X0,X1,X2):
    decompose(matrix, n)
    upper(matrix, n, U)        
    lower(matrix, n, L)        
    forwardSub(b0,d0,L)
    forwardSub(b1,d1,L)
    forwardSub(b2,d2,L)
    backwardSub(X0,d0,U)
    backwardSub(X1,d1,U)
    backwardSub(X2,d2,U)
    
    #transposing Xn solution vectors in matrix
    Transpose = np.array([X0,X1,X2])
    Transpose.transpose()
    
    #printing inverse matrix
    print('Input Matrix')
    for row in matrix:
        print(row)
    print("Inverse Matrix")
    for row in Transpose:
        print(row)

def printLUDecomposition(U,L):
    print('U:')
    for row in U:
        print(row)
    print('L:')  
    for row in L:
        print(row) 
        
def solution(matrix,n,U,L,b0,b1,b2,X0,X1,X2):
    decompose(matrix, n)
    upper(matrix, n, U)        
    lower(matrix, n, L)        
    forwardSub(b,d,L)

          
def main(matrix,n,U,L,b0,b1,b2,X0,X1,X2):
    inverse(matrix,n,U,L,b0,b1,b2,X0,X1,X2)
    printLUDecomposition(U,L)
    
