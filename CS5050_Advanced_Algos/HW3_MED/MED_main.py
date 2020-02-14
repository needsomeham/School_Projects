import numpy as np
import copy


def MED_DP(i,j):
    # initializing cache
    cache = np.zeros([i+1,j+1],dtype=int)
    for row in range(i+1):
        cache[row][0] = row
    for column in range(j+1):
        cache[0][column] = column

    # filling cache with answers
    for row in range(1,i+1):
        for column in range(1,j+1):
            cache[row][column] = min( cache[row-1][column] + 1, cache[row][column-1] + 1, cache[row-1][column-1] + (A[row] != B[column]))

    # returning the answer asked for
    return cache[i,j]


def MED_recursive(i: int, j: int):
    if i == 0:
        return j
    if j == 0:
        return i
    return min(MED_recursive(i-1,j) + 1,
               MED_recursive(i,j-1) + 1,
               MED_recursive(i-1,j-1) + (A[i]!=B[j]))


# Kicks off either the recursive version or the DP of MED
def MED_helper(Ain: str, Bin: str):
    global A,B
    A = Ain
    B = Bin
    if not A.startswith(" "):
        A = " " + A
    if not B.startswith(" "):
        B = " " + B

    #editDistanceRecurs = MED_recursive(len(A)-1,len(B)-1)
    editDistance = MED_DP(len(A)-1,len(B)-1)

    if editDistance > largestEdit[0]:
        largestEdit[0] = editDistance
        largestEdit[1] = Ain + ' and ' + Bin

    return editDistance

def find_max_len():
    #finding the length of the longest word
    maxLen = 0
    for line in fullText:
        for word in line:
            if maxLen < len(word):
                maxLen = len(word)
    return maxLen

# printing the output for the number of edits for a given number of words
def write_file(histogram,lagestEdit):
    fileOut = open('MED Output.txt','w')
    fileOut.truncate(0)     # deleting all left over data
    fileOut.write('A histogram of the number of edits vs the count of word pairs of that edit:\n')
    for line in range(1,len(histogram)):
        fileOut.write(f'{line} edits with {histogram[line]} words\n')
    fileOut.write(f'The word pairs with the largest pair were:\n{largestEdit[1]} with {largestEdit[0]} edits')
    fileOut.close()

# reading in a specific file :)
def read_file():
    allText = []
    # reading in the file into fullText
    fileIn = open("allNames.txt", 'r')
    for line in fileIn:
        lineHolder = []
        editLine = line.split('->')
        lineHolder.append(editLine[0])
        otherWords = editLine[1].split(',')
        for word in otherWords:
            editWord = word.strip()
            finalWord = editWord.replace('\n', '')
            lineHolder.append(finalWord)
        allText.append(lineHolder)
    fileIn.close()
    return allText


if __name__ == '__main__':
    # creating global strings and a list to hold the largest edits
    global A, B
    largestEdit = [0,'none']

    # getting the full text with all spacing removed
    fullText = copy.deepcopy(read_file())

    # find longest word just in case that needs to be completely deleted
    longestWord = find_max_len()
    histogram = [0 for i in range(find_max_len()+1)]

    # for each of the lines in text, compare the the entry with each of the following entries
    for line in fullText:
        for i in range(1,len(line)):
            histogram[MED_helper(line[0], line[i])] += 1

    # print the output to MED Output.txt
    write_file(histogram,largestEdit)
