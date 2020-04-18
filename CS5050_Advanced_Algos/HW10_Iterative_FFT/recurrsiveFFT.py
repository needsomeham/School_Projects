import cmath


# Main FFT function
# Based off of the Cooley and Tukey exploitation of the discrete Fourier Transform
# Works based on symmetry in the function to exploti the fact that you can split even and odd parts of the function
# based on a small algebraic trick. Basically without the algebra the function is O(n^2), but with the trick
# it becomes O(nlogn + n) but the final +n falls off.
# You could also get rid of the the passed N and just take the size of the array on the first step reducing the need
# for a recursive kick off function.
def recursFFT(x:[],N:int, isInverse:bool):
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
        listEven = recursFFT(x[::2], int(N/2), isInverse)
        listOdd = recursFFT(x[1::2], int(N/2), isInverse)

        # Making an array for to hold the solution
        ans = [0 for i in range(N)]

        # Populating the array where one half of the complex conjugate goes in the first position while the second half
        # goes in the N/2 th position.
        for k in range(int(N/2)):
            ans[k] = listEven[k] + cmath.exp(-2j*cmath.pi*direction*k/N)*listOdd[k]
            ans[k+int(N/2)] = listEven[k] - cmath.exp(-2j*cmath.pi*k*direction/N)*listOdd[k]
        return ans