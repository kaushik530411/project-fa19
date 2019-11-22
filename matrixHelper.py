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
def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(m[i][j],end=' ')
        print('\n')

def writeMatrix(matrix, f):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j != len(matrix) - 1:
                f.write(str(matrix[i][j]) + ' ')
            else:
                f.write(str(matrix[i][j]))
        if i != len(matrix) - 1:
            f.write('\n')

def writeRandomHouses(f, maxTA, matrixOrder):
    homes=''
    numHomes=0

    for i in range(0,matrixOrder,6):
        if(numHomes+4>=maxTA):
            break
        homes+=str(i+2)+' '+str(i+4)+' '+str(i+5)+' '+str(i+6)+' '
        numHomes+=4
    f.write(str(numHomes))
    f.write('\n')

    for i in range(1, matrixOrder+1):
        if i != matrixOrder:
            f.write(str(i)+" ")
        else:
            f.write(str(i))
            f.write('\n')
    f.write(str(homes))

def writeInputFile(matrixOrder, matrix, f, maxTA, source):
    f.write(str(matrixOrder))
    f.write('\n')
    writeRandomHouses(f, maxTA, matrixOrder)
    f.write('\n')
    f.write(str(source))
    f.write('\n')
    writeMatrix(matrix, f)








matrix12=matrixExpander([[0,10,14,12,16,28],[10,0,20,0,0,34],[14,20,0,8,12,0],[12,0,8,0,0,38],[16,0,12,0,0,18],[28,34,0,38,18,0]])
matrix24=matrixExpander(matrix12)
matrix48=matrixExpander(matrix24)
# matrix96=matrixExpander(matrix48)
#
# matrix192=matrixExpander(matrix96)
""""matrix10=matrixExpander(matrix5)
matrix20=matrixExpander(matrix10)
matrix40=matrixExpander(matrix20)
matrix80=matrixExpander(matrix40)
matrix160=matrixExpander(matrix80)"""

for i in range(len(matrix48)):
    for j in range(len(matrix48)):
        if matrix48[i][j] == 0:
            matrix48[i][j] = 'x'

f = open("50x.in", "w+")
writeInputFile(48, matrix48, f, 25, 1)
f.close()
