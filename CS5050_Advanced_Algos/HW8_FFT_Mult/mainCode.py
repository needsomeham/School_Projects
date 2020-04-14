import cmath
import math
import numpy as np
import matplotlib.pyplot as plt
import time
import random


# Importing the other versions of the distribution alg
from highschool import highschoolMult
from threeMultiply import threeMult
from addPadding import addPadding


# Function that takes two numbers FFT's them, multiples them in phase space, and returns them from phase space
def FFTHelperMult(num1:[],num2:[]):
    pad1, pad2 = addPadding(num1, array2=num2)

    # Transferring the numbers into phase space
    fftNum1 = FFT(pad1, len(pad1), False)
    fftNum2 = FFT(pad2, len(pad2), False)

    phaseAns = [fftNum1[i]*fftNum2[i] for i in range(2*len(fftNum1))]
    # Multiplying the numbers

    # Taking the numbers out of phase space
    ans = FFT(phaseAns, len(phaseAns), True)

    for i in range(len(ans)):
        ans[i] /= len(ans)
    return ans

# Main FFT function
# Based off of the Cooley and Tukey exploitation of the discrete Fourier Transform
# Works based on symmetry in the function to exploti the fact that you can split even and odd parts of the function
# based on a small algebraic trick. Basically without the algebra the function is O(n^2), but with the trick
# it becomes O(nlogn + n) but the final +n falls off.
# You could also get rid of the the passed N and just take the size of the array on the first step reducing the need
# for a recursive kick off function.
def FFT(x:[],N:int, isInverse:bool):
    # Base case
    if N <= 1:
        return x

    else:
        # indexes backwards if the inverse
        if isInverse:
            direction = -1
        else:
            direction = 1

        # Splitting the lists into even and odd bins
        listEven = FFT(x[::2], int(N/2), isInverse)
        listOdd = FFT(x[1::2], int(N/2), isInverse)

        # Making an array for to hold the solution
        ans = [0 for i in range(N)]

        # Populating the array where one half of the complex conjugate goes in the first position while the second half
        # goes in the N/2 th position.
        for k in range(int(N/2)):
            ans[k] = listEven[k] + cmath.exp(-2j*cmath.pi*direction*k/N)*listOdd[k]
            ans[k+int(N/2)] = listEven[k] - cmath.exp(-2j*cmath.pi*k*direction/N)*listOdd[k]
        return ans


def printToFile(name:str,power:int,times):
    def printToFile(pow: int, npFFT, stFFT):
        file = open('dataCache.txt', 'a')
        file.write(f"pow:{pow}\n")
        file.write(f"n:{npFFT}\n")
        file.write(f"s:{stFFT}\n\n")
        file.close()

# Setting a timer for a designated amount of time and seeing how far each gets
def timeFunctions(timeLimitMin:int):
    # Because I dont have time to figure out how to multithread, just break up the timing 3 ways

    # Timing the high school alg
    countHighschool = 0
    timesHighschool = []
    startTime = time.time()
    while True:
        print(f'in hs {countHighschool}')
        # check that the time hasnt expired
        if (time.time() - startTime)/60 > timeLimitMin: break

        fftThis = [random.randint(1, 50) for j in range(2**countHighschool)]
        # Running the alg
        startHS = time.time_ns()
        highschoolMult(fftThis,fftThis)
        deltaHS = time.time_ns() - startHS
        timesHighschool.append(deltaHS)
        countHighschool += 1


    # Timing the faster 3 multiply version
    countThreeMult = 0
    timesThreeMult = []
    startTimeThree = time.time()
    while True:
        print(f'in 3 mult {countThreeMult}')
        # check that the time hasnt expired
        if (time.time() - startTimeThree) / 60 > timeLimitMin: break

        fftThis = [random.randint(1, 50) for j in range(2**countThreeMult)]

        # Running the alg
        startThree = time.time_ns()
        threeMult(fftThis, fftThis, len(fftThis))
        deltaThree = time.time_ns() - startThree
        timesThreeMult.append(deltaThree)
        countThreeMult += 1


    # Timing the FFT version
    countFFT = 0
    timesFFT = []
    startTimeFFT = time.time()
    while True:
        print(f'in FFT {countFFT}')
        # check that the time hasnt expired
        if (time.time() - startTimeFFT) / 60 > timeLimitMin: break

        fftThis = [random.randint(1, 50) for j in range(2**countFFT)]

        # Running the alg
        startFFT = time.time_ns()
        FFTHelperMult(fftThis,fftThis)
        delatFFT = time.time_ns() - startFFT
        timesFFT.append(delatFFT)
        countFFT += 1

    graphTimes(timesHighschool,timesThreeMult,timesFFT,timeLimitMin)

# Small graphing function to make a chart of the graph times
def graphTimes(timesHS:[],times3Mult:[],timesFFT:[],totalTime):
    # Xvalues to graph against
    powersHS = np.arange(len(timesHS))
    powers3Mult = np.arange(len(times3Mult))
    powersFFT = np.arange(len(timesFFT))

    # Scattering each of the data sets
    plt.scatter(powersHS,timesHS, color = 'red', label = 'High School Algorithm')
    plt.scatter(powers3Mult,times3Mult, color = 'blue', label = '3 Multiplication Algorithm')
    plt.scatter(powersFFT,timesFFT, color='green', label='FFT Algorithm')

    # Some general overhead for the graph
    plt.yscale('log')
    plt.xlabel('Size of array, exponent of 2')
    plt.ylabel('Time to complete FFT in nanoseconds')
    plt.title(f'Given {totalTime} minutes to solve exponentially increasing sized arrays \n'
              f'High School algo solved problems up to and including 2^{len(timesHS)} sized arrays\n'
              f'3 Sub Multiply solved problems upto an including 2^{len(times3Mult)} sized arrays \n'
              f'FFT solved problems up to and including 2^{len(timesFFT)} sized arrays')

    # Showing the graph
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # Testing the graph function
    setone = [1,2,3,4,5,6]
    settwo = [1,4,8,6,2,4]
    setthree = [1,2,3,5,8]

    paddedOne, paddedTwo = addPadding(setthree,array2=settwo)
    # print(highschoolMult(setthree,settwo))
    # print(threeMult(paddedOne,paddedTwo,len(paddedOne)))
    # print(FFTHelperMult(setthree,settwo))
    # fft1 = np.fft.fft(setthree)
    # fft2 = np.fft.fft(settwo)
    # ansfft = fft1*fft2
    # ans = np.fft.ifft(ansfft)
    # print(ans)

    # Proving the FFT and inverse FFT works
    testSet = [1,2,3,4,5,6,7]
    fftSetOne = FFT(testSet,len(testSet),False)
    answer = FFT(fftSetOne,len(fftSetOne),True)

    # Proving the multplication works for a small set
    testMult1 = [1,2]
    testMult2 = [5,7]
    ansHS = highschoolMult(testMult1,testMult2)
    padTest1, padTest2 = addPadding(testMult1,array2=testMult2)
    ans3sub = threeMult(padTest1,padTest2,len(padTest1))
    ansFFT = FFTHelperMult(testMult1,testMult2)
    print(f'For a quick test, lets distribute {testMult1} against {testMult2}.')
    print(f'The highschool algo yields: {ansHS}')
    print(f'The 3 sub multiply yields:  {ans3sub}')
    print(f'The FFT code yields:        {ansFFT} ')

    # Timing the functions to see how long they take against each other with psudo random generated list elements
    timeFunctions(10)