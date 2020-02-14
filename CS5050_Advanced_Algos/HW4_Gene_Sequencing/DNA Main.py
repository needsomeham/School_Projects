import numpy as np
import copy
import sys

sys.setrecursionlimit(100000)

DNA_Dictionary = {
    'a': {'a': 5, 'c': -1, 'g': -2, 't': -1, ' ': -3},
    'c': {'a': -1, 'c': 5, 'g': -3, 't': -2, ' ': -4},
    'g': {'a': -2, 'c': -3, 'g': 5, 't': -2, ' ': -2},
    't': {'a': -1, 'c': -2, 'g': -2, 't': 5, ' ': -1},
    ' ': {'a': -3, 'c': -4, 'g': -2, 't': -1, ' ': 0},
}

def read_file(file: str):
    fileIn = open(file,'r')
    readIn = fileIn.read()
    DNA = ' '
    for line in readIn:
        segment = line.strip("0,1,2,3,4,5,6,7,8,9,b,d,e,f,h,i,j,k,l,m,n,o,p,q,r,s,u,v,w,x,y,z").strip()
        DNA += segment

    return DNA

def write_file(name: str,message,score):
    file = open ( f'{name}.txt','w')
    file.truncate(0)
    file.write(f"{name}\nScore: {score}\n\nEdits that need to be made: \n{message}")
    return True

def trace_helper(cache):
    row = len(DNA1)-1
    column = len(DNA2)-1
    edits = traceback(row,column,cache)

    return edits
    #return edits[len(edits)::-1]

def traceback(i,j,cache):
    if i== 0 and j== 0:
        return ''
    elif i == 0:
        for k in range(j,0,-1):
            return f'_ >= {DNA2[k]}\n'
    elif j == 0:
        for k in range(i,0,-1):
            return f'{DNA1[k]} >= _'
    elif cache[i][j] == cache[i][j-1] + DNA_Dictionary[DNA1[i]][' ']:
        return f'_ >= {DNA2[j-1]}\n{traceback(i,j-1,cache)}'
    elif cache[i][j] == cache[i-1][j] + DNA_Dictionary[' '][DNA2[j]]:
        return f'{DNA1[i-1]} >= _\n{traceback(i-1,j,cache)}'
    elif cache[i][j] == cache[i-1][j-1] + DNA_Dictionary[DNA1[i]][DNA2[j]]:
        if DNA1[i-1] == DNA2[j-1]:
            return f'{DNA1[i-1]} = {DNA2[j-1]}\n{traceback(i-1,j-1,cache)}'
        else:
            return f'{DNA1[i-1]} >= {DNA2[j-1]}\n{traceback(i-1,j-1,cache)}'


def DNA_dp(i, j, returnCache: bool):
    # Building a cache
    cache = np.zeros((i+1,j+1), dtype=int)
    for row in range(1,i+1):
        cache[row][0] = cache[row-1][0] + DNA_Dictionary[' '][DNA1[row]]
    for column in range(1,j+1):
        cache[0][column] = cache[0][column-1] + DNA_Dictionary[DNA2[column]][' ']

    # Filling in the cache
    for row in range(1, i + 1):
        for column in range(1, j + 1):
            cache[row][column] = max(cache[row][column-1] + DNA_Dictionary[' '][DNA1[row]],
                                     cache[row-1][column] + DNA_Dictionary[DNA2[column]][' '],
                                     cache[row - 1][column - 1] + DNA_Dictionary[DNA1[row]][DNA2[column]])

    # either cache or val based on bool
    if returnCache:
        return cache
    else:
        return cache[i,j]


def DNA_recurs(i,j):
    if i == 0:
        return j
    if j == 0:
        return i
    return max(DNA_recurs(i-1,j) + DNA_Dictionary[' '][DNA1[i]],
               DNA_recurs(i,j-1) + DNA_Dictionary[DNA2[j]][' '],
               DNA_recurs(i-1,j-1) + DNA_Dictionary[DNA1[i]][DNA2[j]])

def len_check(str1,str2):
    if len(str1) < len(str2):
        return str2,str1
    return str1,str2


if __name__ == '__main__':
    # These globals are the strings that will be compared in the functions
    global DNA1, DNA2


    gorilla = read_file('Gorilla DNA 1000 lines.txt')
    homoSapian = read_file('Homo Sapien DNA 1000 lines.txt')
    neanderthal = read_file('Neanderthal DNA 1000 lines.txt')

    # Test Case
    # DNA2 = ' aa'
    # DNA1 = ' gg'
    # DNA1,DNA2 = len_check(DNA1,DNA2)
    # print(DNA1,DNA2)
    # testCache = copy.deepcopy(DNA_dp(len(DNA1) - 1, len(DNA2) - 1, True))
    # print(testCache)
    # score = testCache[len(DNA1)-1][len(DNA2)-1]
    # print(score)
    # msg = trace_helper(testCache)
    # print(msg)
    # write_file('test',msg,score)

    # Homosapien v Neanderthal'
    DNA1 = 'oanvd zkkjd'
    DNA2 = ' iaondlva '

    DNA1 = homoSapian
    DNA2 = neanderthal
    homoNeandCache = copy.deepcopy(DNA_dp(len(DNA1)-1,len(DNA2)-1,True))
    homoNeandScore = homoNeandCache[len(DNA1)-1][len(DNA2)-1]
    homoNeandMSG = traceback(len(DNA1)-1,len(DNA2)-1,homoNeandCache)
    write_file('Homosapian v Neanderthal 1000 lines',homoNeandMSG,homoNeandScore)

    # Homosapien v Gorilla
    DNA1 = 'balienal e'
    DNA2 = 'iauehaad'
    DNA1 = homoSapian
    DNA2 = gorilla
    homoGorCache = copy.deepcopy(DNA_dp(len(DNA1) - 1, len(DNA2) - 1, True))
    homoGorScore = homoGorCache[len(DNA1) - 1][len(DNA2) - 1]
    homoGorMSG = traceback(len(DNA1) - 1, len(DNA2)-1, homoGorCache)
    write_file('Homossapien v Gorilla',homoGorMSG,homoGorScore)


    # Gorilla v Neanderthal
    DNA1 = 'iaoeifajoefia '
    DNA2 = ' l;aieaoeijfa '
    DNA1 = gorilla
    DNA2 = neanderthal
    gorNeandCache = copy.deepcopy(DNA_dp(len(DNA1) - 1, len(DNA2) - 1, True))
    gorNeandScore = gorNeandCache[len(DNA1) - 1][len(DNA2) - 1]
    gorNeandMSG = traceback(len(DNA1) - 1, len(DNA2)-1, homoNeandCache)
    write_file('Gorilla v Neanderthal',gorNeandMSG,gorNeandScore)


    '''
    Reference of DNA edit values
        A  |  C |  G | T  |  -
    A |  5 | -1 | -2 | -1 | -3
    C | -1 |  5 | -3 | -2 | -4
    G | -2 | -3 |  5 | -2 | -2
    T | -1 | -2 | -2 | -5 | -1
    - | -3 | -4 | -2 | -1 | **
    '''
