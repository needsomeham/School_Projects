import cmath
import math
import numpy as np
import matplotlib.pyplot as plt
import time
import random

# Importing the other versions of the distribution alg
from highschool import highschoolMult
from threeMultiply import threeMult

# Function to ensure that the string is of length 2^something
# If not, pad the end till it is
# *kwargs picks up two extra cases: one; you know the power
#                                   two; you have two arrays you want the same padding on
def addPadding(x,**kwargs):
    # Case were you know the length of the array you want to pad to
    try:
        power = kwargs.get('power',None)
        if power > 0:
            paddedArray = [0 for i in range(2**power)]
            for i in range(len(x)):
                paddedArray[i] = x[i]
            return paddedArray
    except: pass

    # Case for two arrays to make them the same length
    try:
        if kwargs.get('array2') != None:
            array2 = kwargs.get('array2', None)
            if len(x) >= len(array2):
                padded1 = addPadding(x)
                padded2 = addPadding(array2,power=int(math.log2(len(padded1))))
                return padded1,padded2

            else:
                padded2 = addPadding(array2)
                padded1 = addPadding(x,power=int(math.log2(len(padded2))))
                return padded1, padded2
    except: pass

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

# Function that takes two numbers FFT's them, multiples them in phase space, and returns them from phase space
def FFTHelperMult(num1:[],num2:[]):
    pad1, pad2 = addPadding(num1, array2=num2)

    # Transferring the numbers into phase space
    fftNum1 = FFT(pad1, len(pad1), False)
    fftNum2 = FFT(pad2, len(pad2), False)

    # Multiplying the numbers
    for i in range(len(fftNum1)):
        fftNum1[i] = fftNum1[i] * fftNum2[i]

    # Taking the numbers out of phase space
    ans = FFT(fftNum1, len(fftNum1), True)

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
        listOdd = FFT(x[(direction*1)::2], int(N/2), isInverse)

        # Making an array for to hold the solution
        ans = [0 for i in range(N)]

        # Populating the array where one half of the complex conjugate goes in the first position while the second half
        # goes in the N/2 th position.

        # Easy way to split the code based on if its the inverse or not
        for k in range(int(N/2)):
            ans[k] = listEven[k] + cmath.exp(-2j*cmath.pi*k/N)*listOdd[k]
            ans[k+int(N/2)] = listEven[k] - (direction)*cmath.exp(-2j*cmath.pi*k/N)*listOdd[k]
        return ans


def printToFile(name:str,power:int,times):
    def printToFile(pow: int, npFFT, stFFT):
        file = open('dataCache.txt', 'a')
        file.write(f"pow:{pow}\n")
        file.write(f"n:{npFFT}\n")
        file.write(f"s:{stFFT}\n\n")
        file.close()

# Setting a timer for a designated amount of time and seeing how far each gets
def timeFunctions(numblist:[],timeLimitMin:int):
    # Counts for how many each algo ran
    countHighschool = 0
    countThreeMult = 0
    countFFT = 0

    # Because I dont have time to figure out how to multithread, just break up the timing 3 ways

    # Timing the high school alg
    startTime = time.time()
    havntReachedTimeLimit = True
    while havntReachedTimeLimit:
        # check that the time hasnt expired
        if (time.time() - startTime)/60 > timeLimitMin:
            havntReachedTimeLimit = False
            break

        # try to get numbers from master list. If we build psudo numbers, it will mess up timing
        try:
            num1 = numblist[countHighschool]
            num2 = numblist[countHighschool+1]
        except:
            print('Ran out of numbers. Voided test')
            countHighschool = 0
            break

        # Running the alg
        highschoolMult(num1,num2)

        countHighschool += 1


    # Timing the faster 3 multiply version
    startTime = time.time()
    while havntReachedTimeLimit:
        # check that the time hasnt expired
        if (time.time() - startTime) / 60 > timeLimitMin: break

        # try to get numbers from master list. If we build psudo numbers, it will mess up timing
        try:
            num1 = numblist[countHighschool]
            num2 = numblist[countHighschool + 1]
        except:
            print('ran out of numbers, void test')
            countThreeMult = 0
            break

        # Running the alg
        threeMult(num1, num2, len(num1))

        countThreeMult += 1

    # Timing the FFT version
    startTime = time.time()
    while havntReachedTimeLimit:
        # check that the time hasnt expired
        if (time.time() - startTime) / 60 > timeLimitMin: break

        # try to get numbers from master list. If we build psudo numbers, it will mess up timing
        try:
            num1 = numblist[countHighschool]
            num2 = numblist[countHighschool + 1]
        except:
            print('Ran out of numbers. Voided test.')
            countFFT = 0
            break



        countFFT += 1






if __name__ == '__main__':
    number1 = [1,2,3,4,5]
    number2 = [54,356,7,23]
    fftThis = [1,2,3,4,5,6,7,8]

    phaseAns = FFT(fftThis,len(fftThis),False)
    print(phaseAns)
    print(FFT(phaseAns,len(fftThis),True))

    print(np.fft.fft(fftThis))
    print(np.fft.ifft(np.fft.fft(fftThis)))

    # # Testing out the padding
    # array = [1,2,3]
    # arrayfour = [1,2,5,6,5]
    #
    # print(addPadding(array))
    # print(addPadding(array,power=4))
    # print(addPadding(array,array2=arrayfour))


