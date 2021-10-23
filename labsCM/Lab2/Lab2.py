import os
import math

def dprint(string):
    global outfile
    print(string)
    outfile.write(string)
    pass

def U(matrix):
    U = [[complex(0,0) for element in row] for row in matrix]
    for i in range(matrix.__len__()):
        sum = 0
        for k in range(0,matrix.__len__()):
            sum += U[k][i] * U[k][i]
        if(matrix[i][i] >= sum.real):
            U[i][i] = complex(math.sqrt(matrix[i][i] - sum.real),0)
        else:
            U[i][i] = complex(0,math.sqrt( - matrix[i][i] + sum.real))
        for j in range(matrix.__len__()):
            sum = 0
            for k in range(0,i):
                sum += U[k][i] * U[k][j]
            U[i][j] = (matrix[i][j] - sum) / U[i][i]
    return U

def transpose(matrix):
    return [[matrix[j][i] for j in range(matrix.__len__())] for i in range(matrix.__len__())]

def determinant(matrix):
    result = 1
    for i in range(matrix.__len__()):
        result *= matrix[i][i]
    return result

def multiply(matrix1, matrix2):
    if(matrix1[0].__len__()!=matrix2.__len__()):
        return -1
    n =  matrix2.__len__()
    ResultMatrix = [[complex(0,0) for element in matrix2[0]] for row in matrix1]
    for i in range(ResultMatrix.__len__()):
        for j in range(ResultMatrix.__len__()):
            for l in range(n):
                ResultMatrix[i][j] += matrix1[i][l]*matrix2[l][j] 
    return ResultMatrix


def main():
    with open('labsCM\Lab2\Input.txt', 'r') as infile:
        matrix = [[float(element) for element in line.replace('\n','').split(' ')] for line in infile.readlines()]
    if(matrix.__len__() + 1 != matrix[0].__len__()):
        dprint("Error, with input data")
        return
    vector = []
    for row in matrix:
        vector.append(row.pop(-1))        
    print(vector)
    print(matrix)
    Umatrix = U(matrix)
    print(Umatrix)
    TUmatrix = transpose(Umatrix)
    print(TUmatrix)
    multipy_result = multiply(TUmatrix,Umatrix)
    pass

os.remove('labsCM\Lab2\Console.txt')
with open('labsCM\Lab2\Console.txt', 'w') as outfile:
    main()