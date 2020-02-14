###########################
from random import random, randint

N = 7       # number of items in the sizes
K = 100     # size of the knapsack

def knapsackBool(i, size):
    if size == 0:           # if the knapsack is full, there is a combination of objects that fit in it
        return True
    if size < 0:            # if the object is larger than knapsack, the knapsack will be negative. Reject
        return False
    if i == 0:              # you have gone through all the possible objects, no combination exists
        return False
    return knapsackBool(i-1, size) or knapsackBool(i-1, size - S[i])    # either put the object in the knapsack or
                                                                        # or throw it away. Investigate the result
for _ in range(0,100):
    S = [randint(1,K/2) for _ in range(0,N + 1)]        # random object generating function to fit in knapsack
    if knapsackBool(N, K):                              # test if there is a solution in the array
        print("Solution exists")
    else:
        print("Solution does not exist")
        
    
    
N = 5
K = 10
S = [None, 11,12,23,435,44,4,20]
print(knapsackBool(N, K))
        
