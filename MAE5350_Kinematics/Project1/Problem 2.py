import math
import numpy as np
import random

# Constants for the thing
# NOTE ordered list of locations [x,y,z]
pt1 = [0, 0]
pt2 = [25, -25]
pt3 = [25, -20]

thetaPt1 = math.pi / 2
thetaPt2 = math.pi / 4
thetaPt3 = 0

alpha2 = thetaPt1 - thetaPt2
alpha3 = thetaPt1 - thetaPt3

def random_point_in_box():
    randx = random.randint(-5,15)
    randy = random.randint(-30,-10)

    return randx, randy

def is_grashof(links: []):
    links.sort()
    if links[0] + links[3] <= links[1] + links[2]:
        return True
    return False

def to_degrees(angle_rad):
    return (angle_rad*180)/math.pi

def distance_two_points(point1:[], point2:[]):
    dist = math.sqrt( (point1[0] + point2[0])**2 + (point1[1] + point2[1])**2 )
    return dist

def pythag(pt1,pt2):
    return math.sqrt(pt1**2 + pt2**2)

def is_in_box(point:[]):
    if point[0] < - 5 or point[0] > 15:
        return False
    if point[1] > -10 or point[1] < -30:
        return False
    return True

def is_in_little_box(point:[]):
    if point[0] < 0 or point[0] > 10:
        return False
    if point[1] > 0 or point[1] < -10:
        return False
    return True

def find_vectors(var2,var3,alpha2,alpha3,delta2,delta3,p21,p31):
    # Creating a simplified version for the linear algebra
    a = math.cos(var2) - 1
    b = math.sin(var2)
    c = math.cos(alpha2) - 1
    d = math.sin(alpha2)
    e = p21 * math.cos(delta2)
    f = math.cos(var3) - 1
    g = math.sin(var3)
    h = math.cos(alpha3) - 1
    k = math.sin(alpha3)
    l = p31 * math.cos(delta3)
    m = p21 * math.sin(delta2)
    n = p31 * math.sin(delta3)

    # Where the matrix would look like:
    #    a*w1x - b*w1y + c*z1x - d*z1y = e
    #    f*w1x - g*w1y + h*z1x - k*z1y = l
    #    b*w1x + a*w1y + d*z1x + c*z1y = m
    #    g*w1x + f*w1y + k*z1x + h*z1y = n

    # Therefore:
    matrixA = np.array([[a, -b, c, -d], [f, -g, h, -k], [b, a, d, c], [g, f, k, h]])
    matrixB = np.array([e, l, m, n])

    # Check if the matrix is invertable
    try:
        np.linalg.det(matrixA)
    except:
        print("Matrix not invertable")
        # Probably put more information about what the user could fix to make sure its invertable

    # Solving linear system of equations
    x = np.linalg.solve(matrixA, matrixB)

    # Defining W and Z or U and S vector components
    wx = x[0]
    wy = x[1]
    zx = x[2]
    zy = x[3]

    return wx, wy, zx, zy

def solve_problem1(pt1,pt2,pt3,beta2,beta3,gamma2,gamma3,thetaPt1,thetaPt2,thetaPt3):
    """Part B"""
    # Distance between point 1-2 and 1-3
    p21 = distance_two_points(pt2,pt1)
    p31 = distance_two_points(pt3,pt1)

    # Angles for delta2 and delta3
    delta2 = np.arctan2(pt2[1], pt2[0])
    delta3 = np.arctan2(pt3[1], pt3[0])

    # Solving for alpha 2 and 3
    alpha2 = thetaPt1 - thetaPt2
    alpha3 = thetaPt1 - thetaPt3

    """Part C and D"""
    # Find beta2, beta3, gamma2, gamma3
    # Find vectors W Z U S

    Wx, Wy, Zx, Zy = find_vectors(beta2,beta3,alpha2,alpha3,delta2,delta3,p21,p31)
    Ux, Uy, Sx, Sy = find_vectors(gamma2,gamma3,alpha2,alpha3,delta2,delta3,p21,p31)

    # Finding the length of vector u and s

    return Wx,Wy,Zx,Zy,Ux,Uy,Sx,Sy
    # """Part E"""
    #
    # # Printing solution to W, Z, U, S in complex form
    # #print(f'Vector W in complex notation: {Wx}, {Wy}j units')
    #
    # # Solving for length of link V
    # # Finding vector v which lies in between point A and point B
    # Vx = Zx - Sx
    # Vy = Zy - Sy
    # V = math.sqrt(Vx ** 2 + Vy ** 2)
    #
    # # Finding vector g (the ground vector)
    # Gx = Wx - Ux + Vx
    # Gy = Wy - Uy + Vy
    # G = math.sqrt(Gx ** 2 + Gy ** 2)
    #
    # links = [W,U,V,G]
    #
    # # Finding points C and D
    # C = [-Zx - Wx, -Zy - Wy]
    # D = [-Sx - Ux, -Sy - Uy]
    #
    # return is_in_box(C), is_in_box(D)


def function(r1, r2, r3, zeta1, zeta2, zeta3, alpha2, alpha3):
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
    k3 = (a1 ** 2 - a2 ** 2 - a3 ** 2 - a4 ** 2 - a6 ** 2) / 2
    print('k1',k1)
    print('k2',k2)
    print('k3',k3)
    beta31 = 2 * math.atan2((k2 + math.sqrt(k1 ** 2 + k2 ** 2 - k3 ** 2)) , (k1 + k3))
    beta32 = 2 * math.atan2((k2 - math.sqrt(k1 ** 2 + k2 ** 2 - k3 ** 2)) , (k1 + k3))

    beta21 = math.atan2(-(a3 * math.sin(beta31) + a2 * math.cos(beta31) + a4) , -(a5 * math.sin(beta31) + a3 * math.cos(beta31) + a6))
    beta22 = math.atan2(-(a3 * math.sin(beta32) + a2 * math.cos(beta32) + a4) , -(a5 * math.sin(beta32) + a3 * math.cos(beta32) + a6))

    # Taking non trivial betas
    if beta21 == alpha2:
        beta2 = beta22
    else:
        beta2 = beta21

    if beta31 == alpha3:
        beta3 = beta32
    else:
        beta3 = beta31

    return beta2, beta3

def solve_problem2():
    """Part A"""
    # Choose two random points in base
    #TODO: find R1,2,3, zeta1,2,3,

    oCx, oCy = random_point_in_box()
    oDx, oDy = random_point_in_box()
    print(oCx,oCy)
    print(oDx,oDy)
    r2x = pt2[0]
    r2y = pt2[1]
    r3x = pt3[0]
    r3y = pt3[1]

    R1 = pythag(oCx,oCy)
    R2 = pythag(r2x,r2y)
    R3 = pythag(r3x,r3y)

    zeta1C = np.arctan2(oCy, oCx)
    zeta1D = np.arctan2(oDy, oDx)
    zeta2 = np.arctan2(r2y, r2x)
    zeta3 = np.arctan2(r3y, r3x)


    """Part B"""
    #TODO: find beta2,3, gamma2,3

    beta2, beta3 = function(R1,R2,R3,zeta1C,zeta2,zeta3,alpha2,alpha3)
    gamma2, gamma3 = function(R1,R2,R3,zeta1D,zeta2,zeta3,alpha2,alpha3)


    """Part C"""
    #TODO: Use functions from the first problem to sovle W,Z,U,S

    Wx, Wy, Zx, Zy, Ux, Uy, Sx, Sy = solve_problem1(pt1,pt2,pt3,beta2,beta3,gamma2,gamma3,thetaPt1,thetaPt2,thetaPt3)
    W = math.sqrt(Wx ** 2 + Wy ** 2)
    Z = math.sqrt(Zx ** 2 + Zy ** 2)
    U = math.sqrt(Ux ** 2 + Uy ** 2)
    S = math.sqrt(Sx ** 2 + Sy ** 2)

    """Part D"""
    #TODO: Report W,Z,U,S
    #TODO: Find A and B
    #TODO: Is grashof?

    A = [Zx,Zy]
    B = [Sx,Sy]

    a_in_box = is_in_little_box(A)
    b_in_box = is_in_little_box(B)

    # Solving for length of link V
    # Finding vector v which lies in between point A and point B
    Vx = Zx - Sx
    Vy = Zy - Sy
    V = math.sqrt(Vx ** 2 + Vy ** 2)

    # Finding vector g (the ground vector)
    Gx = Wx - Ux + Vx
    Gy = Wy - Uy + Vy
    G = math.sqrt(Gx ** 2 + Gy ** 2)

    links = [W, U, V, G]

    print(is_grashof(links))

solve_problem2()