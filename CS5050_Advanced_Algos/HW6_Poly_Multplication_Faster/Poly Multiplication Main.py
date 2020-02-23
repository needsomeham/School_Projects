import numpy as np
import random
import time
import copy
import matplotlib.pyplot as plt


# High School version. Simply the distributive property
def distribution(P,Q):
    PQ = np.zeros((2* len(P)))
    for i in range(len(P)):
        for j in range(len(Q)):
            PQ[i+j] += P[i] * Q[j]
    return PQ


def divide_conquer_recurs(P:[], Q:[],n):
    # Need to make a new PQ each time, because it only needs to be filled on the last step
    PQ = np.zeros((2*n))
    half = int(n/2)

    # Base case
    if n == 1:
        PQ[0] = P[0]*Q[0]
        return PQ

    # Work of breaking up the lists
    PQLL = copy.deepcopy(divide_conquer_recurs(P[0:half],Q[0:half],half))
    PQLH = copy.deepcopy(divide_conquer_recurs(P[0:half],Q[half:],half))
    PQHL = copy.deepcopy(divide_conquer_recurs(P[half:],Q[0:half],half))
    PQHH = copy.deepcopy(divide_conquer_recurs(P[half:],Q[half:],half))

    # Solution construction
    for i in range(n):
        PQ[i] += PQLL[i]
        PQ[i+half] += PQLH[i]
        PQ[i+half] += PQHL[i]
        PQ[i+n] += PQHH[i]

    # Return the solution matrix
    return PQ

# def divide_fast_add_help()
#
def divide_conquer_faster(P:[],Q:[],n):
    PQ = np.zeros((2*n))
    half = int(n/2)

    # Base Case
    if n == 1:
        PQ[0] = P[0]*Q[0]
        return PQ

    # Working on breaking up the lists. Big difference is that this version
    # only takes 3 calls rather than 4. Looking at the math this is much faster
    PQLL = copy.deepcopy(divide_conquer_recurs(P[0:half],Q[0:half],half))
    PMID = np.zeros(half)
    QMID = np.zeros(half)
    for i in range(half):
        PMID[i] = P[i] + P[i+half]
        QMID[i] = Q[i] + Q[i+half]
    PQMID = copy.deepcopy(divide_conquer_faster(PMID, QMID, half))
    PQHH = copy.deepcopy(divide_conquer_faster(P[half:], Q[half:], half))

    # Solution construction
    for i in range(n):
        PQ[i] += PQLL[i]
        PQ[i+n] += PQHH[i]
    for i in range(n):
        PQ[i+half] += PQMID[i] - PQLL[i] - PQHH[i]

    # Returning the solution matrix
    return PQ

def graph(dataHS,dataDC,dataFaster):
    print(dataHS)
    print(dataDC)
    # Unfortunately you have to manually unpack the data :/
    xHS = []
    yHS = []
    for point in dataHS:
        xHS.append(point[0])
        yHS.append(point[1])

    xDC = []
    yDC = []
    for point in dataDC:
        xDC.append(point[0])
        yDC.append(point[1])

    xFast = []
    yFast = []
    for point in dataFaster:
        xFast.append(point[0])
        yFast.append(point[1])

    # Setting up overhead
    plt.title('Comparing High School Distribution vs Divide and Conquer Algorithms vs Faster Divide and Conquer')
    plt.xlabel('Exponent of 2')
    plt.ylabel('Log Time in Nanoseconds')

    # Making lines for each of the data sets


    # Scattering the data
    plt.scatter(xHS,yHS, c = 'red', label = 'High School')
    plt.scatter(xDC,yDC, c = 'blue', label = 'Divide and Conquer')
    plt.scatter(xFast,yFast, c = 'green', label = 'Divide and Conquer Fast')
    plt.yscale('log')

    plt.legend()
    plt.show()

if __name__ == '__main__':
    # Overhead to hold the power and its respective solve time times
    # Also I know from class that 2^15 takes an hour, and if I want
    # multiple data points then I can only let it run till 2^12 with the
    # time I have left.

    # One big note is that this function requires that each of the function calls
    # are of the power 2*CONST. Else when you have it each time you wont have an int
    # to mesh the strings back together. Therefore this is a more general study and not
    # applicable to any sized polynomial.

    dataHS = []
    dataDC = []
    dataFaster = []
    upperLimit = 10     # max array size 2^12

    # Timing each of the multiplication methods 5 times each
    for n in range(2,upperLimit+1):
        # Timing each method 5 times
        for round in range(5):
            # Making new P and Q for each time
            P = [random.random()*2-1 for i in range(2**n)]
            Q = [random.random()*2-1 for j in range(2**n)]

            # Timing High School algo
            start = time.time_ns()
            distribution(P,Q)
            end = time.time_ns()
            deltaHS = end - start
            dataHS.append([n,deltaHS])

            # Timing DC
            start = time.time_ns()
            divide_conquer_recurs(P,Q,len(P))
            end = time.time_ns()
            deltaDC = end - start
            dataDC.append([n,deltaDC])

            # Timing Fast DC
            start = time.time_ns()
            divide_conquer_faster(P,Q,len(P))
            end = time.time_ns()
            deltaFast = end - start
            dataFaster.append([n,deltaFast])
    graph(dataHS,dataDC,dataFaster)
