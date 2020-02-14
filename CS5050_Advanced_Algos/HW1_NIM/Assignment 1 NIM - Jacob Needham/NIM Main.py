import matplotlib.pyplot as plt
import numpy as np
import time


class NIM:

    # Constructor
    def __init__(self, stones):
        self.n = stones
        # list of states that have already been checked
        self.done = [False for i in range(self.n+1)]
        self.win_list_recursive = [False for i in range(self.n)]
        self.win_list_memoize = [False for i in range(self.n)]

    # Getters
    def get_win_list_recursive(self):
        return self.win_list_recursive

    def get_win_list_memorize(self):
        return self.win_list_memoize

    # Dynamic method for finding solutions
    def win_memoize(self,n):
        if n == 0:
            return True
        if n == 1:
            return False
        if self.done[n]:
            return self.win_list_memoize[n]
        self.done[n] = True
        self.win_list_memoize[n] = not(self.win_memoize(n-1) and self.win_memoize(n-2))
        return self.win_list_memoize[n]

    # Recursive method for finding win
    def win_recursion(self, n):
        if n == 0:
            return True
        if n == 1:
            return False
        self.win_list_recursive[n] = not(self.win_recursion(n-1) and self.win_recursion(n-2))
        return self.win_list_recursive[n]

    def num_stones_to_take(self,n):
        if n <= 0:
            return -1
        # returning the number of stones to take based on the next win/loss of removing that stone
        if not(self.win_recursion(n-1)):
            return 1
        else:
            return 2

    def num_stones_to_take_memoize(self,n):
        if n <= 0:
            return -1
        # returning the number of stones to take based on the next win/loss of removing that stone
        if not (self.win_memoize(n-1)):
            return 1
        else:
            return 2

    def win(self):
        return True

    def print_NIM(self):
        print()#some solution)


def play_NIM():
    print("Welcome to NIM! How many stones would you like to play with?")
    n = int(input())         # this should have exception handling
    computer_win = False

    # Main turn based player options to ask how many
    while n>0:

        # Computer's turn
        currentNIM = NIM(n)
        taken_stones = currentNIM.num_stones_to_take(n)
        print("There are", n, "stones left.")
        print("The computer took", taken_stones, "stones.")
        n -= taken_stones
        if is_winner(n):
            print("you won")
            break

        # User's turn
        print("There are",n,"stones left.")
        print("Its your turn. How many stones would you like to take? (1-2)")
        usertake = int(input())
        n = n - usertake
        if is_winner(n):
            print("Sorry, the computer won. Better luck next time")
            break

def is_winner(n):
    if n <= 0:
        return True
    else:
        return False

# Mathematical function for Fibonacci Sequence
def function(x):
    y = 1.6182**(x-40)   # adjusted to start with computer
    return y


# Graphing function of n vs log time
def make_graph(x,y):

    # Setting up the graph
    plt.xlabel("Number of NIM tiles")
    plt.ylabel("Log Time (s)")
    plt.yscale("log")
    plt.title("NIM Game \n Solved Recursively with Fibonacci Sequence Implementation")

    # Plotting NIM points
    x = np.arange(0,x)
    plt.plot(x,y, label = "NIM Solve Time")

    # plotting an "ideal" comparison
    x_ideal = np.arange(20,x.size)
    y_ideal = []
    for i in range(20,x.size):
        y_ideal.append(function(i))

    plt.plot(x_ideal,np.array(y_ideal),label = "Ideal Mathematical Solve Time")

    # Showing Graph
    plt.legend()
    plt.show()


# Code run time for recursive NIM
def timer_and_list_recursive(n):
    time_difference = []
    NIMGame = NIM(n)
    for i in range(n):
        start_time = time.time()
        NIMGame.num_stones_to_take(i)
        finish_time = time.time()
        time_difference.append((finish_time - start_time))

    return time_difference


# Code run time for memorized NIM
def timer_and_list_memoize(n):
    time_difference = []
    NIMGame = NIM(n)
    for i in range(n):
        start_time = time.time()
        NIMGame.num_stones_to_take_memoize(i)
        finish_time = time.time()
        time_difference.append((finish_time - start_time))

    return time_difference


# Master call to make true/false table and a graph
def timer_table_and_plot(iterations):

    # Runtime for each implimentation
    runtime_recursive = timer_and_list_recursive(iterations)
    runtime_memorize = timer_and_list_memoize(iterations)

    # checking if the lists are the output between the recursion and memozation are the same
    mastertable = [[i,False,False] for i in range(iterations+1)]
    NIMgame = NIM(iterations)
    for i in range(iterations):
        mastertable[i][1] = NIMgame.win_recursion(i)
        mastertable[i][2] = NIMgame.win_memoize(i)
    check_output(mastertable)

    # Creating the Graph
    make_graph(iterations,np.array(runtime_recursive))


def check_output(mastertable):
    for i in range(len(mastertable)):
        if mastertable[i][1] != mastertable[i][2]:
            print("The lists are not the same")
            break
    print("The lists are the same")


if __name__ == '__main__':

    # Data comparison
    number_stones = 40                   # Select the number of stones in the game, above 45 takes quite a while
    timer_table_and_plot(number_stones)  # Functions to plot comparison of ideal time, real time, and if the memorized
                                         # version and recursive version yeld the same output.

    # Play NIM vs computer
    play_NIM()                           # A fun game to see if you can beat the computer at NIM