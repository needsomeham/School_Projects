import math
import numpy as np


# Useful functions for the rest of the program
def is_grashof(links: []):
    links.sort()
    if links[0] + links[3] <= links[1] + links[2]:
        return True
    return False

def to_degrees(angle_rad):
    return (angle_rad*180)/math.pi

def distance(point1:[], point2:[]):
    dist = math.sqrt( (point1[0] + point2[0])**2 + (point1[1] + point2[1])**2 )
    return dist

def is_in_box(point:[]):
    if point[0] < - 5 or point[0] > 15:
        return False
    if point[1] > -10 or point[1] < -30:
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

    """Part A"""
    # Ignore red pivot points
    #print("Part A, \nWe ignored pivot points\n")

    """Part B"""
    # Find p21, p31, del2, del3, alpha2, alpha3

    #print("Part B")
    # Distance between point 1-2 and 1-3
    p21 = distance(pt2,pt1)
    p31 = distance(pt3,pt1)
    #print(f'Distance from 1 to 2: {p21} units')
    #print(f'Distance from 1 to 3: {p31} units')

    # Angles for delta2 and delta3
    delta2 = np.arctan2(pt2[1], pt2[0])
    delta3 = np.arctan2(pt3[1], pt3[0])
    #print(f'Delta 2: {delta2} degreees')
    #print(f'Delta 3: {delta3} degrees')

    # Solving for alpha 2 and 3
    alpha2 = thetaPt1 - thetaPt2
    alpha3 = thetaPt1 - thetaPt3
    #print(f'Alpha 2: {to_degrees(alpha2)} degrees')
    #print(f'Alpha 3: {to_degrees(alpha3)} degrees')

    #print()


    """Part C and D"""
    # Find beta2, beta3, gamma2, gamma3
    # Find vectors W Z U S
    #print('Part C')
    #print(f'Beta 2: {beta2} degrees')
    #print(f'Beta 3: {beta3} degrees')
    #print(f'Gamma 2: {gamma2} degrees')
    #print(f'Gamma 3: {gamma3} degrees')


    Wx, Wy, Zx, Zy = find_vectors(beta2,beta3,alpha2,alpha3,delta2,delta3,p21,p31)
    Ux, Uy, Sx, Sy = find_vectors(gamma2,gamma3,alpha2,alpha3,delta2,delta3,p21,p31)

    # Finding the length of vector u and s
    W = math.sqrt(Wx ** 2 + Wy ** 2)
    Z = math.sqrt(Zx ** 2 + Zy ** 2)
    U = math.sqrt(Ux ** 2 + Uy ** 2)
    S = math.sqrt(Sx ** 2 + Sy ** 2)

    #print(f'Magnitude of W: {W} units')
    #print(f'Magnitude of Z: {Z} units')
    #print(f'Magnitude of U: {U} units')
    #print(f'Magnitude of S: {S} units')

    #print()


    """Part E"""
    # Find points A and B
    # TODO: Is it grashof?
    #print('Part E')

    #print('NOTE that A is the position of the vector head Z')
    #print('NOTE that B is the position of the vector head S')

    # Printing solution to W, Z, U, S in complex form
    #print(f'Vector W in complex notation: {Wx}, {Wy}j units')
    #print(f'Vector Z in complex notation: {Zx}, {Zy}j units')
    #print(f'Vector U in complex notation: {Ux}, {Uy}j units')
    #print(f'Vector S in complex notation: {Sx}, {Sy}j units')

    # Solving for length of link V
    # Finding vector v which lies in between point A and point B
    Vx = Zx - Sx
    Vy = Zy - Sy
    V = math.sqrt(Vx ** 2 + Vy ** 2)

    # Finding vector g (the ground vector)
    Gx = Wx - Ux + Vx
    Gy = Wy - Uy + Vy
    G = math.sqrt(Gx ** 2 + Gy ** 2)

    links = [W,U,V,G]

    #print(f'Is the fourbar grashof? {is_grashof(links)}')

    # Finding points C and D
    C = [Zx + Wx, Zy + Wy]
    D = [Sx + Ux, Sy + Uy]
    print(C,' ',D)

    #print('Are base points C and D in the box?')
    #print(f'    C is in box: {is_in_box(C)}')
    #print(f'    D is in box: {is_in_box(D)}')

    return is_in_box(C), is_in_box(D)


if __name__ == '__main__':
    """General overhead for the fourbar"""
    # Defining locations of point 1,2,3
    # NOTE ordered list of locations [x,y,z]
    pt1 = [0, 0]
    pt2 = [25, -25]
    pt3 = [25, -20]

    # Angles for point 1
    thetaPt1 = math.pi / 2
    thetaPt2 = math.pi / 4
    thetaPt3 = 0

    # Picking betas and gammas for part c and e

    possible_solutions = []
    for i in range(1,360):
        for j in range(1,360):
            beta2 = i
            gamma2 = j
            beta3 = i
            gamma3 = j
            loc1, loc2 = solve_problem1(pt1,pt2,pt3,beta2,beta3,gamma2,gamma3,thetaPt1,thetaPt2,thetaPt3)
            if loc1 and loc2:
                possible_solutions.append([i,j])

    f = open('solutions.txt','w')
    for line in possible_solutions:
        f.write(f'{line}')
    f.close()
    print(possible_solutions)
