import cmath
import math

def rbs(i: int, size: int):
    N = 1 << size
    iter = i
    for j in range(1, size):
        i >>= 1
        iter <<= 1
        iter |= (i & 1)
    iter &= N-1
    return iter

def iterativeFFT(x:[],N:int, isInverse:bool):
    # Building the cache
    size = int(math.log2(N))
    cache = [[0 for i in range(N)] for j in range(size + 1)]

    # Filling in the base cases with the exponential
    for position in range(N):
        cache[0][position] = x[rbs(position,size)]

    # Populating the cache
    for i in range(1, size + 1):

        width = 1 << i
        for j in range(0, N, width):
            jCount = 0
            for k in range(width//2):
                omega = cmath.exp(-2j*cmath.pi*(2*(i*(size)))*jCount/N)
                cache[i][j+k] = cache[i-1][j+k] + omega*cache[i-1][j+k+width//2]
                cache[i][j+k+width//2] = cache[i-1][j+k] - omega*cache[i-1][j+k+width//2]
                jCount += 1

    return cache[size]