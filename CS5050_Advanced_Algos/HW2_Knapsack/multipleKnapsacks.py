import time
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as polyfit
import numpy as np


# Recursive version for filling knapsack
def fill_knap_recurs(K1,K2,i):
    if K1<0:
        return -35
    if K2<0:
        return -35
    if i<0:
        return 0

    return max(fill_knap_recurs(K1 - S[i], K2, i-1) + V[i],     # simply add object to K1
               fill_knap_recurs(K1, K2 - S[i], i-1) + V[i],     # add object to K2
               fill_knap_recurs(K1, K2, i-1))                   # trow object away


# Memoizing version for filling knapsack
def fill_knap_memo(K1,K2,i):
    if K1 < 0:
        return -35
    if K2 < 0:
        return -35
    if i<0:
        return 0

    if isDone[K1][K2][i]:
        return cache[K1][K2][i]
    cache[K1][K2][i] = max(fill_knap_memo(K1 - S[i],K2,i-1)+ V[i],      # add object to K1
                           fill_knap_memo(K1,K2 - S[i],i-1) + V[i],     # add object to K2
                           fill_knap_memo(K1,K2,i-1))                   # throw object away

    isDone[K1][K2][i] = True
    return cache[K1][K2][i]


# DP version for filling knapsack
# Ran out of time :/
def fill_knap_DP():
    return True


# Main control function to help kick off timer function and graph function
def timer_recures_memo(knap1,knap2):
    timeRecurs = []
    timeMemo = []

    # Setting stuff for globals
    global S,V,isDone,cache

    # Running a loop for testing
    for j in range(30):
        S,V = generateSV(j*10+2,j*15+3)
        i = len(S) - 1
        N = len(S) - 1
        isDone = np.full((K1 + 1, K2 + 1, N + 1), False)
        cache = np.zeros((K1 + 1, K2 + 1, N + 1))
        startTimeRecurse = time.time_ns()
        fill_knap_recurs(knap1,knap2,i)
        endTimeRecurse = time.time_ns()
        deltaTimeRecurse = (endTimeRecurse - startTimeRecurse)/1000000000
        timeRecurs.append(deltaTimeRecurse)

        startTimeMemo = time.time_ns()
        fill_knap_memo(knap1,knap2,i)
        endTimeMemo = time.time_ns()
        deltaTimeMemo = (endTimeMemo - startTimeMemo)/1000000000
        timeMemo.append(deltaTimeMemo)
    return timeRecurs,timeMemo


# Helper function to generate random N and aveSize for testing
def generateSV(N,aveSize):
    sizes = np.random.randint(1, aveSize*2, N+1, dtype=int)
    values = np.random.normal(aveSize,1,N+1)
    return sizes,values


# Assignment Test of code, basically a kick off
def knapsack_trial(K1,K2):
    recurseTime,memotime = timer_recures_memo(K1,K2)

    graph(memotime,recurseTime)


# # Testing of my recursive code
# def knapasack_trial_recustive(knap1,knap2,i):
#     times = []
#     # for j in range(19,20):
#     #     S,V = generateSV(j*15+1,j*15+1)
#     times.append(time_recurs_knapsack(knap1,knap2,len(S)-1))
#     for i in range(len(times)):
#         times[i] = times[i]/1000000000
#     graph_recurs(times)

# Testing for my other code, ignore
# def graph_recurs(list):
#     # Setting up scatter plot
#     x = np.arange(0, len(list))
#     fig, ax = plt.subplots()
#     ax.scatter(x, list, color='red', label='Recursive')
#
#     # graphing line for memoList
#     b, m = polyfit.polyfit(x, list, 1)
#     plt.plot(x, b + m * x, '-', color='red', label='Linefit for Recursive Function')
#
#     # Showing Graph and legend
#     plt.legend()
#     plt.show()


# Function to take in multiple lists and plot them
def graph(memoList,recurse):
    # Setting up scatter plot
    x = np.arange(0,len(memoList))
    fig, ax = plt.subplots()
    ax.scatter(x,memoList,color='red',label='Memoized')
    ax.scatter(x,recurse,color='blue',label='Recurse')

    # naming axis
    ax.set_title("Plot of Number of Objects vs Runtime")
    ax.set(xlabel='Number of objects/10', ylabel='Solve Time (nanoseconds)')

    # graphing line for memoList
    b, m = polyfit.polyfit(x,memoList,1)
    plt.plot(x,b+m*x,'-', color='red', label=f'Linefit for Memoized Function, m={round(m,6)}')

    # graphing line for DPList
    b2, m2 = polyfit.polyfit(x,recurse,1)
    plt.plot(x,b2+m2*x,'-',color='blue', label=f'Linefit for Recurse Function, m={round(m2,6)}')

    # Showing Graph and legend
    plt.legend()
    plt.show()


if __name__ == '__main__':

    # Manually setting up knapsack problem for testing and objects to fill them
    K1 = 4
    K2 = 7

    # Assignment Trial for graph
    knapsack_trial(K1,K2)

    # #K1Values = 0
    # #K2Values = 0
    # S = [1, 2, 4, 6, 8, 9]
    # V = [2.654, 3.564, 7.342, 6.76453, 54.7465, 34.265]
    # N = len(S)
