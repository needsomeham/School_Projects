import math
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
