import cmath
import numpy

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

# A helper function to take the input
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

if __name__ == '__main__':
    test = [0,1,2,3,4,5,6,7]

    print(numpy.fft.fft(test))
    print()
    print(FFThelper(test))