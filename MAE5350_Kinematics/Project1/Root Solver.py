from matplotlib import pyplot
import math
import copy
from scipy import optimize

functions = {'one': 'math.sqrt(math.exp(x*2)) - 45',
             'two': '2*x**2 - 15',
             'three': '4 -15*x + x**4'}


# def function(name,x):
#     y = eval(functions[name])
#     return y


def function(x):
    y = math.sqrt(math.exp(x*2)) - 45
    return y

def function2(x):
    y = (math.exp(2*x)/x)-56
    return y

def secant(method):
    # Threshold for quitting
    error_max = .0000001

    # Not running the iterations more than 1000 times
    iter_max = 1000

    # Overhead
    current_error = 1
    count = 0
    values = []

    # Secant requires two points to start
    root_old = 5
    root = 1

    # finding all roots to a given function
    while current_error > error_max:
        # following the secant line to its intercept and making that the next root
        root_new = root - (method(root)*(root_old - root))/(method(root_old)-method(root))
        values.append(root_new)
        current_error = abs((root_new - root_old)/(root_new))*100

        # Checking if the max iterations has been exceeded
        if count > iter_max:
            return values
        count += 1
        root_old = root
        root = root_new

    return values

# Built in solver that uses Newtons method to find a solution based on a starting point
def built_in_solver(guess):
    return optimize.newton(function,guess)

def secant_root_solver(functions):

    all_roots = []
    for equation in functions.keys():
        root = secant(function)
        print(f"{equation}'s root is {root}")

        # Putting all roots into a list
        all_roots.append([equation,root])

    return all_roots

def semilog_plot(real:[],img:[],title):
    pyplot.plot(real,color = 'red', label = 'Real')
    pyplot.plot(img, color = 'blue', label = 'Imaginary')

    pyplot.title(f"Finding real and imaginary root of {title} using Secant Method \n "
                 f"Real Root ({real[len(real)-1]}) vs Number of Iteration ({len(real)}) \n"
                 f"Imaginary Root ({img[len(img)-1]}) vs Number of Iterations ({len(img)})")
    pyplot.ylabel("Root Value")
    pyplot.xlabel("Number of iterations (log)")
    pyplot.xscale('log')
    pyplot.legend()
    pyplot.show()



if __name__ == '__main__':
    # This is a comparision of the secant method root solver with a scipy built in function

    gamma_real = 2
    gamma_img = 2
    all_functions = {'beta real': function,
                      'beta img': function2,
                      'gamma real': gamma_real,
                      'gamma img': gamma_img}

    # Returning arrays of all root values as it converges
    beta_real = copy.deepcopy(secant(all_functions['beta real']))
    beta_img = copy.deepcopy(secant(all_functions['beta img']))
    # gamma_real = copy.deepcopy(secant(all_functions['gamma real']))
    # gamma_img = copy.deepcopy(secant(all_functions['gamma img']))

    # Plotting betta and gamma
    semilog_plot(beta_real, beta_img, "Beta")
    # semilog_plot(gamma_real, gamma_img, "Gamma")


