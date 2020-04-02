import numpy as np

# High School version. Simply the distributive property
def highschoolMult(int1:[],int2:[]):
    # Finding the size of the larger array
    if int1 >= int2:
        size = len(int1)
    else: size = len(int2)

    # Solution array
    PQ = np.zeros(size)

    # Multiplying each number against the others
    for i in range(int1):
        for j in range(int2):
            PQ[i+j] += int1[i] * int2[j]
    return PQ
