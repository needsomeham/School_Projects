import math
import numpy as np
from numpy import linalg




# step 2
# w1X = w*math.cos(theta)
# w1Y = w*math.sin(theta)
# z1X = z*math.cos(phi)
# z1Y = z*math.sin(phi)


# Part B --> Finding p12,p13, alpha2, alpha3, delta2, delta3

# Defining Positions with respect to Point 1
# Original Values: pt1(5,30)  pt2(30,27.5)  pt3(30,10)
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def to_degrees(angle_rad):
    return angle_rad*180/math.pi

pt1 = Point(0, 0)
pt2 = Point(25, -2.5)
pt3 = Point(25, -20)
print('pt1:', pt1)
print('pt2:', pt2)
print('pt3:', pt3)

# Finding Magnitude of p12 and p13
p21 = math.sqrt((pt1.x + pt2.x) ** 2 + (pt1.y + pt2.y) ** 2)
p31 = math.sqrt((pt1.x + pt3.x) ** 2 + (pt1.y + pt3.y) ** 2)
print('p21:', p21)
print('p31:', p31)

# Given angles of body in radians
thetaPt1 = math.pi / 2
thetaPt2 = math.pi / 4
thetaPt3 = 0
# print('thetaPt1:',thetaPt1*(180/math.pi))
# print('thetaPt2:',thetaPt2*(180/math.pi))
# print('thetaPt3:',thetaPt3*(180/math.pi))


# Finding alpha2 and alpha3 in radians
alpha2 = thetaPt1 - thetaPt2
alpha3 = thetaPt1 - thetaPt3
print('alpha2:', to_degrees(alpha2))
print('alpha3:', to_degrees(alpha3))

# Finding delta2 and delta3 in radians
# When entering values: y then x
delta2 = np.arctan2(pt2.y, pt2.x)
delta3 = np.arctan2(pt3.y, pt3.x)
print('delta2:', to_degrees(delta2))
print('delta3:', to_degrees(delta3))

# Part C --> Solving for W and Z
# Using equations 5.23 through 5.27

#TODO: find the actual values for beta2 and beta3

# Assuming values for beta2 and beta3
beta2 = -60 * math.pi / 180
beta3 = -120 * math.pi / 180

# Obtaining the x and y components for the unknown vectors
# w1x = w*math.cos(theta)
# w1y = w*math.sin(theta)
# z1x = z*math.cos(phi)
# z1y = z*math.sin(phi)


# Creating a simplified notation
a = math.cos(beta2) - 1
b = math.sin(beta2)
c = math.cos(alpha2) - 1
d = math.sin(alpha2)
e = p21 * math.cos(delta2)
f = math.cos(beta3) - 1
g = math.sin(beta3)
h = math.cos(alpha3) - 1
k = math.sin(alpha3)
l = p31 * math.cos(delta3)
m = p21 * math.sin(delta2)
n = p31 * math.sin(delta3)

# Using the variables above, the equation are:
# a*w1x - b*w1y + c*z1x - d*z1y = e
# f*w1x - g*w1y + h*z1x - k*z1y = l
# b*w1x + a*w1y + d*z1x + c*z1y = m
# g*w1x + f*w1y + k*z1x + h*z1y = n


# Defining matrix A:
matrixA = np.array([[a, -b, c, -d], [f, -g, h, -k], [b, a, d, c], [g, f, k, h]])
# print("matrixA: \n", matrixA)


# Checking the determinant
if np.linalg.det(matrixA) == 0:
    print("matrixA is non invertable")

# Defining matrix B:
matrixB = np.array([e, l, m, n])

# Solving the linear equations for matrix x
x = np.linalg.solve(matrixA, matrixB)
print("\nBeta Solutions: \n", np.linalg.solve(matrixA, matrixB))

# Defining W and Z vector components
w1x = x[0]
w1y = x[1]
z1x = x[2]
z1y = x[3]

# Finding the length of vector u and s
w = math.sqrt(w1x ** 2 + w1y ** 2)
z = math.sqrt(z1x ** 2 + z1y ** 2)
print("|w|: ", w)
print("|z|: ", z)

# Part C --> Solving for U and S

# Assuming values for gamma2 and gamma3
gamma2 = -30 * math.pi / 180
gamma3 = -70 * math.pi / 180

# Obtaining the x and y components for the unknown vectors
# u1x = u*math.cos(theta)
# u1y = u*math.sin(theta)
# s1x = s*math.cos(phi)
# s1y = s*math.sin(phi)


# Creating a simplified notation
a = math.cos(gamma2) - 1
b = math.sin(gamma2)
c = math.cos(alpha2) - 1
d = math.sin(alpha2)
e = p21 * math.cos(delta2)
f = math.cos(gamma3) - 1
g = math.sin(gamma3)
h = math.cos(alpha3) - 1
k = math.sin(alpha3)
l = p31 * math.cos(delta3)
m = p21 * math.sin(delta2)
n = p31 * math.sin(delta3)

# Using the variables above, the equation are:
# a*u1x - b*u1y + c*s1x - d*s1y = e
# f*u1x - g*u1y + h*s1x - k*s1y = l
# b*u1x + a*u1y + d*s1x + c*s1y = m
# g*u1x + f*u1y + k*s1x + h*s1y = n


# Defining matrix A:
matrixA = np.array([[a, -b, c, -d], [f, -g, h, -k], [b, a, d, c], [g, f, k, h]])

# Chekcing the determinant
if np.linalg.det(matrixA) == 0:
    print("error")

# Defining matrix B:
matrixB = np.array([e, l, m, n])

# Solving the linear equations for matrix x
x = np.linalg.solve(matrixA, matrixB)
print("Gamma Solutions: \n", np.linalg.solve(matrixA, matrixB))

# Defining U and S vector components
u1x = x[0]
u1y = x[1]
s1x = x[2]
s1y = x[3]

# Finding the length of vector u and s
u = math.sqrt(u1x ** 2 + u1y ** 2)
s = math.sqrt(s1x ** 2 + s1y ** 2)
print("|u|: ", u)
print("|s|: ", s)

# Part D --> Finding points A and B (where the nodes connect
#  coupler with input and coupler with output)

# Finding vector v which lies in between point A and point B
v1x = z1x - s1x
v1y = z1y - s1y
v = math.sqrt(v1x ** 2 + v1y ** 2)
print("\n|v|: ", v)

# Finding vector g (the ground vector)
g1x = w1x - u1x + v1x
g1y = w1y - u1y + v1y
g = math.sqrt(g1x ** 2 + g1y ** 2)
print("|g|:", g)

# Determining if it is Fourbar Grashof