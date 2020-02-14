# Libraries
import matplotlib as mpl
from matplotlib import pyplot
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np
import copy


def is_fourier_stable():
    if fourierNumber<=.25:
        return True
    return False


def make_grid(temp):
    grid = [[temp for i in range(numPoints)] for j in range(numPoints)]
    return grid


def plot_graph(graph):
    cmap = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',['blue','red'],256)
    # bounds = [1,1,numPoints+1,numPoints+1]

    img = pyplot.imshow(graph,interpolation=None,cmap=cmap)

    #pyplot.imshow.extent(0,0,len(graph),len(graph))

    pyplot.colorbar(img,cmap=cmap, label = 'Temp in Celsius ')
    #pyplot.grid(True,color='white')
    pyplot.xticks(range(numPoints), [chr(97 + x) for x in range(numPoints)])
    pyplot.title(f'2D Heat Conduction represented by {numPoints}x{numPoints} points after {iter} iterations \nHeater at C,3 and C,2 at {hotTemp} C \nCooler at E,3 and E,6 at {coldTemp} C \nFourier Number is {fourierNumber}')
    
    pyplot.show()

def heat_cool_grid(grid, isExperimenal:bool):
    gridLength = int(numPoints/6)

    for y in range(gridLength):
        for x in range(gridLength):
            if isExperimenal:
                # processor 1
                grid[gridLength*3+y][x] = 61.66

                # processor 2
                grid[gridLength*4+y][gridLength*2+x] = 58.87

                # cooling fan 1
                grid[y][gridLength*4 + x] = 30.26

                # cooling fan 2
                grid[gridLength*3 + y][gridLength*4 + x] = 35.49

                continue

            # processor 1
            grid[gridLength*3+y][x] = 75

            # processor 2
            grid[gridLength*4+y][gridLength*2+x] = 75

            # cooling fan 1
            grid[y][gridLength*4 + x] = 20

            # cooling fan 2
            grid[gridLength*3 + y][gridLength*4 + x] = 20
    return grid


# should return true if the difference between the two grids is less than 1%
def is_error_good(gridBefore,gridAfter):
    for i in range(numPoints):
        for j in range(numPoints):
            currentError = abs(gridAfter[i][j] - gridBefore[i][j])
            if currentError > error:
                return False
    return True


def twoD_adiabatic(grid, isExperimental:bool):
    gridAfter = grid

    iterationCount = 0
    while True:
        grid = copy.deepcopy(gridAfter)

        for y in range(numPoints):
            for x in range(numPoints):
                # Finite difference model is on page 306
                # Top Left Corner
                if y == 0:
                    if x == 0:
                        gridAfter[y][x] = fourierNumber * ( 2*grid[y + 1][x] + 2*grid[y][x + 1] ) + (1 - 4 * fourierNumber) * grid[y][x]
                # Top Right Corner
                    if x == numPoints-1:
                        gridAfter[y][x] = fourierNumber * ( 2*grid[y + 1][x] + 2*grid[y][x - 1] ) + (1 - 4 * fourierNumber) * grid[y][x]
                # Top Row
                    else:
                       gridAfter[y][x] = fourierNumber*(2*grid[y+1][x] + grid[y][x+1] + grid[y][x-1] ) + (1-4*fourierNumber)*grid[y][x] 
                
                # Bottom Left Corner        
                if y == numPoints-1:
                    if x == 0:
                        gridAfter[y][x] = fourierNumber * ( 2*grid[y - 1][x] + 2*grid[y][x + 1] ) + (1 - 4 * fourierNumber) * grid[y][x]
                # Bottom Right Corner
                    if x == numPoints-1:
                        gridAfter[y][x] = fourierNumber * ( 2*grid[y - 1][x] + 2*grid[y][x - 1] ) + (1 - 4 * fourierNumber) * grid[y][x]
                # Bottom Row
                    else:
                        gridAfter[y][x] = fourierNumber * ( 2*grid[y - 1][x] + grid[y][x + 1] + grid[y][x - 1] ) + (1 - 4 * fourierNumber) *grid[y][x]

                # Exclude the first and last rows
                if y>0 and y<numPoints-1:   
                    # Left Column
                    if x == 0:
                        gridAfter[y][x] = fourierNumber*(grid[y+1][x]+grid[y-1][x]+2*grid[y][x+1])+(1-4*fourierNumber)*grid[y][x]
                    # Right Column
                    if x == numPoints-1:
                        gridAfter[y][x] = fourierNumber*(grid[y+1][x]+grid[y-1][x]+2*grid[y][x-1])+(1-4*fourierNumber)*grid[y][x]
                    # Middle block 
                    else:
                       gridAfter[y][x] = fourierNumber*(grid[y+1][x]+grid[y-1][x]+grid[y][x+1]+grid[y][x-1] ) + (1-4*fourierNumber)*grid[y][x]

        # Incremetning and heating/cooling the grid back to the state
        iterationCount += 1
        heat_cool_grid(gridAfter,isExperimental)

        # ensuring the error is less than the prescribed ammount
        if is_error_good(grid,gridAfter):
            return iterationCount, gridAfter


if __name__ == '__main__':
    global numPoints, hotTemp, coldTemp, fourierNumber, error, iter
    # Setting up constants defined from lab
    alpha = 117/1000000         # 117 is thermal diffusivity of copper
    timeStep = 0.1               # 3.1773
    physicalGridLength = .03669   # distance between nodes in meters
    numPoints = 6              # number of points in grid
    deltaX = physicalGridLength/numPoints
    ambientTemp = 20.5            # Ambient temp of plate when test was started
    hotTemp = 75
    coldTemp = 20
    error = 0.01                 # Acceptable resolution change for steady state in lab

    # Building grid and setting to the initial temps of the heating and cooling
    grid = make_grid(ambientTemp)
    fourierNumber = ((alpha)*(timeStep))/(physicalGridLength**2)

    # Heating an cooling initial grid
    grid = heat_cool_grid(grid, True)

    # Running code
    iter, finalGrid = twoD_adiabatic(grid, True)

    # quick check to make sure we are stable
    if(is_fourier_stable()):
        plot_graph(finalGrid)
    else:
        print("Fourier Numner unstable. Pick a new time step.")