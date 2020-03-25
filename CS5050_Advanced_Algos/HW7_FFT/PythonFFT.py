import cmath
import numpy as np
import matplotlib.pyplot as plt
import time
import random

def buffer(x):
    #finds the smallest power of 2 that is larger than the len(x)
    power = 0
    while 2**power < len(x):
        power +=1
    if len(x) == 2**power:
        return x

    fullX = [0 for i in range(2**power)]
    for i in range(len(x)):
        fullX[i] = x[i]
    return fullX

# A helper function to kick off the recursive FFT function
def FFThelper(x):
    finalX = buffer(x)
    answer = FFT(finalX,len(finalX))
    return answer

def FFT(x:[],N:int):
    if N <= 1:
        return x

    else:
        listEven = FFT(x[::2], int(N/2))
        listOdd = FFT(x[1::2], int(N/2))
        ans = [0 for i in range(N)]

        for k in range(int(N/2)):
            ans[k] = listEven[k] + cmath.exp(-2j*cmath.pi*k/N)*listOdd[k]
            ans[k+int(N/2)] = listEven[k] - cmath.exp(-2j*cmath.pi*k/N)*listOdd[k]
        return ans


# Just a little safety net just in case the program crashes or something
def printToFile(pow:int,npFFT,stFFT):
    file = open('dataCache.txt','a')
    file.write(f"pow:{pow}\n")
    file.write(f"n:{npFFT}\n")
    file.write(f"s:{stFFT}\n\n")
    file.close()


# Function to graph the time comparison of my FFT vs community numpy FFT
def graphTimes(powers:[],studentTimes:[],numpyTimes:[]):

    # Scattering each of the datasets
    plt.scatter(powers,studentTimes, color = 'red', label = 'Student FFT times')
    plt.scatter(powers,numpyTimes, color = 'blue', label = 'Numpy FFT times')

    # Some general overhead for the graph
    plt.yscale('log')
    plt.xlabel('Size of array, exponent of 2')
    plt.ylabel('Time to complete FFT in nanoseconds')
    plt.title('Time to solve FFT for various sized arrays')

    # Showing the graph
    plt.legend()
    plt.show()


if __name__ == '__main__':
    pows = []
    timeNumpy = []
    timeMyFFT = []

    #making the timing sequence
    for pow in range(25):
        print(pow)

        # Generating a randomly filled array
        FFTthis = [random.randint(0,50) for i in range(2**pow)]

        # Timing my FFT
        start = time.time_ns()
        FFThelper(FFTthis)
        end = time.time_ns()
        deltaMyFFT = end - start

        # Timing numpy FFT
        startNP = time.time_ns()
        np.fft.fft(FFTthis)
        endNP = time.time_ns()
        deltaNP = endNP - startNP

        # Adding results to both the safety file and also to the graph
        printToFile(pow,deltaNP,deltaMyFFT)
        pows.append(pow)
        timeNumpy.append(deltaNP)
        timeMyFFT.append(deltaMyFFT)

    # Graphing the results
    graphTimes(pows,timeMyFFT,timeNumpy)