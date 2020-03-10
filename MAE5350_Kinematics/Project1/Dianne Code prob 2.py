
import math
import numpy as np
from numpy import linalg


# Part A --> Determine r1, r2, r3, zeta1, zeta2, and zeta3

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


pt1 = Point(0, 0)
pt2 = Point(25, -2.5)
pt3 = Point(25, -20)
print('pt1:', pt1)
print('pt2:', pt2)
print('pt3:', pt3)

# Function to randomly choose two fixed pivot
# points in the base: oC and oD
# Base: x(-5,15)  y(-5,-30)


# -->need an x and y for each point
# --> oC.x,oC.y and oD.x,oD.y


# READ ME!!
# First we will solve for the left side of the problem.
# This uses oC (the left pivot) to solve for both betas.
# The next bunch of lines will then be repeated for the right side.
# BUT the right side will use oD (not oC) and solve for both gammas.
# I will make a note at the end of all the lines of code
# that will be repeated so you know where to stop the loop:)


# Finding r1, r2, and r3
r1x = -oCx
r1y = -oCy
r2x = pt2.x
r2y = pt2.y
r3x = pt3.x
r3y = pt3.y

r1 = math.sqrt(r1x ** 2 + r1y ** 2)
r2 = math.sqrt(r2x ** 2 + r2y ** 2)
r3 = math.sqrt(r3x ** 2 + r3y ** 2)
print("|r1|: ", r1)
print("|r2|: ", r2)
print("|r3|: ", r3)

# Finding zeta1, zeta2, and zeta3
# When entering values: y then x
zeta1 = np.arctan2(r1y, r1x)
zeta2 = np.arctan2(r2y, r2x)
zeta3 = np.arctan2(r3y, r3x)
print("zeta1: ", zeta1)
print("zeta2: ", zeta2)
print("zeta3: ", zeta3)

# Part B --> Finding beta2, beta3, gamma2, and gamma3
# using equations 34a-d


# First, we need to find alpha (from part 1)
thetaPt1 = math.pi / 2
thetaPt2 = math.pi / 4
thetaPt3 = 0
print('thetaPt1:', thetaPt1 * (180 / math.pi))
print('thetaPt2:', thetaPt2 * (180 / math.pi))
print('thetaPt3:', thetaPt3 * (180 / math.pi))

# Finding alpha2 and alpha3 in radians
alpha2 = thetaPt1 - thetaPt2
alpha3 = thetaPt1 - thetaPt3
print('alpha2:', alpha2 * (180 / math.pi))
print('alpha3:', alpha3 * (180 / math.pi))

# Creating an easier way to solve for Beta/Gamma
c1 = r3 * math.cos(alpha2 + zeta3) - r2 * math.cos(alpha3 + zeta2)
c2 = r3 * math.sin(alpha2 + zeta3) - r2 * math.sin(alpha3 + zeta2)
c3 = r1 * math.cos(alpha3 + zeta1) - r3 * math.cos(zeta3)
c4 = -r1 * math.sin(alpha3 + zeta1) + r3 * math.sin(zeta3)
c5 = r1 * math.cos(alpha2 + zeta1) - r2 * math.cos(zeta2)
c6 = -r1 * math.sin(alpha2 + zeta1) + r2 * math.sin(zeta2)

a1 = -c3 ** 2 - c4 ** 2
a2 = c3 * c6 - c4 * c5
a3 = -c4 * c6 - c3 * c5
a4 = c2 * c3 + c1 * c4
a5 = c4 * c5 - c3 * c6
a6 = c1 * c3 - c2 * c4

k1 = a2 * a4 + a3 * a6
k2 = a3 * a4 + a5 * a6
k3 = (a1 ** 2 - a2 ** 2 - a3 ** 3 - a4 ** 4 - a6 ** 2) / 2

# simply compare the betas against alphas and take the unique beta
beta31 = 2 * math.atan((k2 + math.sqrt(k1 ** 2 + k2 ** 2 - k3 ** 2)) / (k1 + k3))
beta32 = 2 * math.atan((k2 - math.sqrt(k1 ** 2 + k2 ** 2 - k3 ** 2)) / (k1 + k3))

beta2 = math.atan(-(a3 * math.sin(beta3) + a2 * math.cos(beta3) + a4) /
                  -(a5 * math.sin(beta3) + a3 * math.cos(beta3) + a6))

# END OF REPEATING CODE!!
# END OF REPEATING CODE!!
# END OF REPEATING CODE!!
# END OF REPEATING CODE!!


# Part C --> Finding W, Z, U, and S
#  We are using the code from part one but the
#  beta and zeta angles we just solved for.


# Part D --> Are points A and B located on the box? Is it a fourbar Grashof?




