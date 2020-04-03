import numpy as np

def threeMult(P:[],Q:[],n):
    PQ = np.zeros((2*n))
    half = int(n/2)

    # Base Case
    if n == 1:
        PQ[0] = P[0]*Q[0]
        return PQ

    # Working on breaking up the lists. Big difference is that this version
    # only takes 3 calls rather than 4. Looking at the math this is much faster
    PQLL = threeMult(P[0:half],Q[0:half],half)
    PMID = np.zeros(half)
    QMID = np.zeros(half)
    for i in range(half):
        PMID[i] = P[i] + P[i+half]
        QMID[i] = Q[i] + Q[i+half]
    PQMID = threeMult(PMID, QMID, half)
    PQHH = threeMult(P[half:], Q[half:], half)

    # Solution construction
    for i in range(n):
        PQ[i] += PQLL[i]
        PQ[i+n] += PQHH[i]
    for i in range(n):
        PQ[i+half] += PQMID[i] - PQLL[i] - PQHH[i]

    # Returning the solution matrix
    return PQ

