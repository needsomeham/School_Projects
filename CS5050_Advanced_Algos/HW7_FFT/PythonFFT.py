import cmath
import numpy as np
import matplotlib.pyplot as plt
import time
import random

# Small function to ensure that the string is of length 2^something
# If not, pad the end till it is
def addPadding(x):
    # Finds the smallest power of 2 that is larger than the len(x)
    power = 0
    while 2**power < len(x):
        power +=1
    if len(x) == 2**power:
        return x

    # Creating new string and padding it
    fullX = [0 for i in range(2**power)]
    for i in range(len(x)):
        fullX[i] = x[i]
    return fullX


# A helper function to kick off the recursive FFT function
def FFThelper(x):
    finalX = addPadding(x)
    answer = FFT(finalX,len(finalX))
    return answer


# Main FFT function
# Based off of the Cooley and Tukey exploitation of the discrete Fourier Transform
# Works based on symmetry in the function to exploti the fact that you can split even and odd parts of the function
# based on a small algebraic trick. Basically without the algebra the function is O(n^2), but with the trick
# it becomes O(nlogn + n) but the final +n falls off.
# You could also get rid of the the passed N and just take the size of the array on the first step reducing the need
# for a recursive kick off function.
# Based on: https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm
def FFT(x:[],N:int):
    # Base case
    if N <= 1:
        return x

    else:
        # Splitting the lists into even and odd bins
        listEven = FFT(x[::2], int(N/2))
        listOdd = FFT(x[1::2], int(N/2))

        # Making an array for to hold the solution
        ans = [0 for i in range(N)]

        # Populating the array where one half of the complex conjugate goes in the first position while the second half
        # goes in the N/2 th position.
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
    # Some containers to hold the data
    pows = []
    timeNumpy = []
    timeMyFFT = []

    # Largest power user would like to run to
    largestPow = 24

    # Timing various lengths of strings
    for pow in range(largestPow + 1):
        print(f'Working on string length of 2^{pow}')

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