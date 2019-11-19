import scipy as sp
import numpy as np
import random


def matrixExpander(m):
    matrix=m.copy()
    #expanding horizontally
    for i in range (len(matrix)):
        matrix[i]=matrix[i]+matrix[i][::-1]
    #exexpanding vertically
    for i in range(len(matrix)):
        inverseMatrix=matrix.copy()[::-1]
    matrix+=inverseMatrix
    return matrix

def randonGraphGen(width = 1000, height = 1000, locations):

    num_locs = len(locations)
    location_map  = dict()

    for loc in locations:
        rand_pos = random.randint(width), random.randint(height)
        locations_map.add(loc, rand_pos)





def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(m[i][j],end=' ')
        print('\n')

matrix5=matrixExpander([[0,1,3,5,5],[1,0,2,4,5],[3,2,0,3,6],[5,4,3,0,4],[5,5,6,4,0]])
matrix10=matrixExpander(matrix5)
matrix20=matrixExpander(matrix10)
matrix40=matrixExpander(matrix20)
for i in range(len(matrix20)):
    for j in range(len(matrix20)):
        if matrix20[i][j] == 0:
            matrix20[i][j] = 'x'
print(len(matrix20))
print(len(matrix20[1]))
printMatrix(matrix20)
