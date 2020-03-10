from scipy import optimize
import  math


def function(x):
    y = math.sqrt(math.exp(x*2)) - 45
    return y

sol = optimize.newton(function, 3)

print(sol)