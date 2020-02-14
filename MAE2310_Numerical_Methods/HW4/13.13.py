"""
Homework 4 Problem 13.13
Develop a progrom using a programing or macro language to implement the
golden-section serach algorithm. Design teh program so that it is expressly 
designed to locate a maximum or minimum based on user preference. The 
subroutine should have the following features:
    -iterate untill the relative error falls below a stopping criterion or 
    exceeds a maximum number of iterations.
    -return both the otimal x and f(x)
    -minimize the number of function evaluations

@author: Jacob Needham
"""

#getting user decision on max or min
def wantMaxOrMin():
    count = 0
    answer = False
    while answer != True and count<5:
        print("Type \"MAX\" if you would like to find the max or \"MIN\" \
              to find the minimum of the function")
        user = input()
        count +=1
        if user == "MAX":
            return True
            break
        if user == "MIN":
            return False
            break
        elif user != "MAX" or user != "MIN":
            print("\nInvalid input, try again")
        

#function equation, in a real problem the function would come from the user
def function(x):
    y = (x**3 - 30*x**2 - 661*x -1791)/1791
    return y


#Golden search subroutine
def goldenSearchMax(es,iMax,L,U):
    iCount = 0
    ea = es
    R = ((5**.5)-1)/2
    xL = L
    xU = U
    d = R *(xU - xL)
    x1 = xL + d
    x2 = xU - d
    f1 = function(x1)
    f2 = function(x2)
    if f1>f2 :
        xopt = x1
        fx = f1
    else:
        xopt = x2
        fx = f2
    for iCount in range(iMax):
        d = R*d
        xinit = xU - xL
        if f1 > f2:
            xL = x2
            x2 = x1
            x1 = xL + d
            f2 = f1
            f1 = function(x1)
        else:
            xU = x1
            x1 = x2
            x2 = xU - d
            f1 = f2
            f2 = function(x2)
        iCount += 1
        if f1 > f2:
            xopt = x1
            fx = f1
        else:
            xopt = x2
            fx = f2
        if xopt != 0:
            ea = (1-R)* abs(xinit/xopt)*100
        if ea < es:
            break
    print("\nNumber of iterations to convergence:", iCount)
    print("The optimal value is:", round(fx,4))
    print("The x value for the optimal value is:",round(xopt,4))
    

def goldenSearchMin(es,iMax,L,U):
    iCount = 0
    ea = es
    R = ((5**.5)-1)/2
    xL = L
    xU = U
    d = R *(xU - xL)
    x1 = xL + d
    x2 = xU - d
    f1 = function(x1)
    f2 = function(x2)
    if f1<f2 :
        xopt = x1
        fx = f1
    else:
        xopt = x2
        fx = f2
    for iCount in range(iMax):
        d = R*d
        xinit = xU - xL
        if f1 < f2:
            xL = x2
            x2 = x1
            x1 = xL + d
            f2 = f1
            f1 = function(x1)
        else:
            xU = x1
            x1 = x2
            x2 = xU - d
            f1 = f2
            f2 = function(x2)
        iCount += 1
        if f1 < f2:
            xopt = x1
            fx = f1
        else:
            xopt = x2
            fx = f2
        if xopt != 0:
            ea = (1-R)* abs(xinit/xopt)*100
        if ea < es:
            break
    print("\nNumber of iterations to convergence:", iCount)
    print("The minimal value is:", round(fx,4))
    print("The x value for the minimal value is:",round(xopt,4))


def main():
    answer = wantMaxOrMin()
    
    if answer == True:
        goldenSearchMax(.001,200,-20,0)
    else:
        goldenSearchMin(.001,200,-20,0)
main()