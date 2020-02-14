
"finding height of rocket as a piecewise function

def timeLess15(time):
    "this function produces a height if time less than 15
    heightBefore15 = 38.1454*t + 0.13743*t*t*t
    return heightBefore15

def timeBetween15and33(time):
    "this function produces a height if time between 15 and 33
    heightBefore33 = 1036 + 130.909*(time-15) + 6.18425*(time-15)*(time-15) - .428*(time-15)*(time-15)*(time-15)
    return heightBefore33

def timeAfter33(time):
    "this function produces a height if time is greater than 33
    heightAfter33 = 2900 - 62.468*(time-33) - 16.9274*(time-33)*(time-33) + .41796*(time-33)*(time-33)*(time-33)
    return heightAfter33

"passing time into correct heigh equation
if time < 0:
    height = 0
    print(height)
else if 0 <= time <15
    height = timeLess15(time)
    print(height)
else if 15 <= time < 33
    height = timeBetween15and33(time)
    print(height)
else 
    height = timeAfter33(time)
    if height < 0:
        height = 0
        return height
    print(height)
    
