"""
Textbook problem 18.17

Develop, debug, and test a program in either a high-level language or macro
language of your choice to implement Newton’s interpolating polynomial based 
on Fig. 18.7.

@author: Jacob Needham
"""
#necessary libaries
import numpy as np

'''
Main fucntion takes input data from table with x and y values and runs Fdd function.
'''
def Main():
    #put numbers here
    x = []
    y = []
    n = len(x)
    
    Xi = 2              #input x value to solve for here
    FddMatrix(x,y,n,Xi)  
    
'''
FddMatrix takes in vectors x, y from table and solves for linear fit between points
'''
def FddMatrix(x,y,n,Xi):
    #initilizing Fdd matrix and placeholder matrix for y
    Fdd = np.matrix([[0 for x in range(n)] for y in range(n)],dtype = 'float') 
    y_working = np.zeros((n,1), dtype = 'float')
    for i in range(n):                            #For loop coppies y value into first 
        Fdd[i,0] = y[i]                           #column.
    for j in range(1,n):                          #For loop fills A matrix using modified  
        for i in range(0,n-j):                    #Eq. 18.2 for linear interpolation from 
            Fdd[i,j] = (Fdd[i+1,j-1] - Fdd[i,j-1])/(x[i+j]-x[i])           #the book.
    
    #initializing necessary place-holding matricies        
    x_temp = [1]
    y_working[0] = Fdd[0,0]
    for order in range(1,n):
        x_temp.append(x_temp[order-1]*(Xi - x[order-1]))
        y_working[order] = y_working[order-1] + Fdd[0,order]*x_temp[order]
    
    #formating output and printing solution
    final_y = str(y_working[n-1])
    final_y = final_y.strip(' /[/]')
    print('At x =',Xi,' the interpolated y value is: ', final_y, sep = '')
    
Main()  