import numpy as np
import matplotlib.pyplot as plt
import time
import random

from addPadding import addPadding
from recurrsiveFFT import recursFFT
from iterativeFFT import iterativeFFT


def graphTimes(timesRecurs:[],timesIter:[],allotedTime):
    # x values to graph against
    powersRecurs = np.arange(len(timesRecurs))
    powersIter = np.arange(len(timesIter))

    # scattering each of the times for comparison
    plt.scatter(powersRecurs,timesRecurs,color = 'red', label = 'Recursive FFT Algo')
    plt.scatter(powersIter,timesIter,color = 'blue', label = 'Iterative FFT Algo')

    # Some general overhead for the graph
    plt.yscale('log')
    plt.xlabel('Size of array, exponent of 2')
    plt.ylabel('Time to complete FFT in nanoseconds')
    plt.title(f'Recursive FFT algorithm vs Iterative algorithm given allotted time of {allotedTime} minutes')

    plt.legend()
    plt.show()
# Simple timer function to time the two FFT algos
# Note that building fftThis is inside of the timer, therefore its not a true test, but a relative test
#
def timer(maxTime,function):
    keepCount = 0
    keepTimes = []
    startTime = time.time()
    while True:
        print(f'current count at {keepCount}')
        # check that the time hasnt expired
        if (time.time() - startTime)/60 > maxTime: break

        fftThis = [random.randint(1, 50) for j in range(2**keepCount)]
        # Running the alg
        startRecurs = time.time_ns()
        function(fftThis,len(fftThis),False)
        deltaHS = time.time_ns() - startRecurs
        keepTimes.append(deltaHS)
        keepCount += 1

    return keepTimes


if __name__ == '__main__':

    # User defined time limit
    timeLimit = 5 #minutes

    # Timing two functions
    timesRecurs = timer(timeLimit,recursFFT)
    timesIter = timer(timeLimit,iterativeFFT)

    # Graphing results
    graphTimes(timesRecurs,timesIter,timeLimit)

