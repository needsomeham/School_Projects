"""
Project 1 Part 1 (a)
This program takes a three-dimensional stress field as specified by the user
and outputs the charicteristic polynomial.
@author: Jacob Needham
"""
print("OUTPUT")

#getting values of matrix
print("Please input the values of the 3x3 matrix one value at a time")
m = []
for row in range(3):
    m.append([0,0,0])
    
for row in range(3):
    for cell in range(3):
        m[row][cell] = int(input())
 
       
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


#Printing the characteristic polynomial
print("For the entered matrix:")
for i in m:
    print(i)
print("The characteristic equation for is:")
print("0 = x^3 - ",I1,"*x^2 + ",I2,"*x - ",I3,sep="")
