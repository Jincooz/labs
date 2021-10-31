import os
import math

def number_to_string(number, max_length):
    if(number >= 0): presymbol = '+'
    else: presymbol = '-'
    return presymbol + str(round(abs(number), int(-math.log10(eps)))).ljust(max_length, '0')

def dprint(data):
    global outfile
    if(type(data) == str):
        pass
    elif (type(data) == complex and data.imag == 0):
        data = str(data.real)
    elif (type(data) == int or type(data) == float):
        data = str(data)
    elif (type(data) == list and type(data[0])==list and type(data[0][0]) == complex):
        is_complex = True
        max_length = 0
        have_negative = False
        for row in data:
            for x in row:
                is_complex = is_complex and x.imag == 0
                if(x.real > 0 and max_length < math.ceil(math.log10(x.real))):
                    max_length = math.ceil(math.log10(x.real))
                if(x.imag > 0 and max_length < math.ceil(math.log10(x.imag))):
                    max_length = math.ceil(math.log10(x.imag))
                if(x.real < 0 or x.imag < 0):
                    have_negative = True
        max_length = int(-math.log10(eps)) + max_length + 1
        datacopy = data.copy()
        data = ''
        if(is_complex):
            for i in range(len(datacopy)):
                data += '['
                for j in range(len(datacopy[0])-1):
                    data += number_to_string(datacopy[i][j].real, max_length)  + ', '
                data += number_to_string(datacopy[i][len(datacopy[0])-1].real, max_length) + ']\n'
        else:
            for i in range(len(datacopy)):
                data += '['
                for j in range(len(datacopy[0])-1):
                    data += number_to_string(datacopy[i][j].real, max_length) + number_to_string(datacopy[i][j].imag, max_length) + 'i, '
                data +=  number_to_string(datacopy[i][len(datacopy[0])-1].real, max_length) + number_to_string(datacopy[len(datacopy)-1][len(datacopy[0])-1].imag, max_length) + 'i]\n'
    elif (type(data) == list and type(data[0]) == complex):
        is_complex = True
        max_length = 1
        have_negative = False
        for x in data:
            is_complex = is_complex and x.imag == 0
            if(x.real > 0 and max_length < math.ceil(math.log10(x.real))):
                max_length = math.ceil(math.log10(x.real))
            if(x.imag > 0 and max_length < math.ceil(math.log10(x.imag))):
                max_length = math.ceil(math.log10(x.imag))
            if(x.real < 0 or x.imag < 0):
                have_negative = True
        max_length = int(-math.log10(eps)) + max_length + 1
        datacopy = data.copy()
        data = '['
        if(is_complex):
            for i in range(len(datacopy) - 1):
                data += number_to_string(datacopy[i].real, max_length) + ', '
            data += number_to_string(datacopy[len(datacopy)-1].real, max_length) + ']\n'
        else:
            for i in range(len(datacopy) - 1):
                data += number_to_string(datacopy[i].real, max_length) + number_to_string(datacopy[i].imag, max_length) + 'i, '
            data +=  number_to_string(datacopy[len(datacopy)-1].real, max_length) + number_to_string(datacopy[len(datacopy)-1].imag, max_length) + 'i]\n'
    else:
        data = "Error with data type"
    with open('labsCM\Lab2\Console.txt', 'a') as outfile:
        outfile.write(data + '\n')
    print(data)

def MM_multiplication(matrix1, matrix2):
    if(matrix1[0].__len__()!=matrix2.__len__()):
        return -1
    n =  matrix2.__len__()
    ResultMatrix = [[complex(0,0) for element in matrix2[0]] for row in matrix1]
    for i in range(ResultMatrix.__len__()):
        for j in range(ResultMatrix.__len__()):
            for l in range(n):
                ResultMatrix[i][j] += matrix1[i][l]*matrix2[l][j] 
    return ResultMatrix

def MV_multiplication(matrix, vector):
    result_vector = [complex(0,0) for x in vector]
    for i in range(vector.__len__()):
        for j in range(matrix[0].__len__()):
            result_vector[i] += matrix[i][j] * vector[j]
    return result_vector

def vector_subtraction(matrix1, matrix2):
    for i in range(len(matrix1)):
            matrix1[i] -= matrix2[i]
    return matrix1

def transpose(matrix):
    return [[matrix[j][i] for j in range(matrix.__len__())] for i in range(matrix.__len__())]

def determinant(matrix):
    result = 1
    for i in range(matrix.__len__()):
        result *= matrix[i][i]
    matrix = transpose(matrix)
    for i in range(matrix.__len__()):
        result *= matrix[i][i]
    return result

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
            U[i][j] = (complex(matrix[i][j],0) - sum) / U[i][i]
    return U

def straight_run(Tmatrix, vector):
    result_vector = [x for x in vector]
    for i in range(Tmatrix.__len__()):
        sum = 0
        for j in range(i):
            sum += result_vector[j] * Tmatrix[i][j]
        result_vector[i] = (vector[i] - sum) / Tmatrix[i][i]
    return result_vector

def reverse_run(matrix, vector):
    result_vector = [x for x in vector]
    for i in range(0, matrix.__len__())[::-1]: 
        sum = 0
        for j in range(i+1,matrix.__len__()):
            sum += result_vector[j] * matrix[i][j]
        result_vector[i] = (vector[i] - sum) / matrix[i][i]
    return result_vector

def sole_sulution(matrix, vector):
    Umatrix = U(matrix)    
    U_multiply_resultvector = straight_run(transpose(Umatrix), vector)    
    resultvector = reverse_run(Umatrix, U_multiply_resultvector)    
    residual_vector = vector_subtraction(vector, MV_multiplication(matrix, resultvector))
    return resultvector, Umatrix, U_multiply_resultvector, residual_vector
    
def task_solution(matrix):
    vector = []
    for row in matrix:
        vector.append(row.pop(-1))
    resultvector, Umatrix, U_multiply_resultvector, residual_vector = sole_sulution(matrix, vector)
    dprint("U matrix : ")
    dprint(Umatrix)
    if (determinant(Umatrix) == 0):
        dprint("Matrx is singular")
    else:
        dprint("U multiply SOLE solution vector :")
        dprint(U_multiply_resultvector)
        dprint("SOLE solution vector :")
        dprint(resultvector)
        dprint("Residual vector :")
        dprint(residual_vector)
        dprint("Determinant of matrix :")
        dprint(determinant(Umatrix))
        reverse_matrix = [[0 for x in row] for row in matrix]
        for i in range(len(vector)):
            vector = [(1 if i == j else 0) for j in range(len(vector))]
            resultvector,trash,trash,trash = sole_sulution(matrix, vector)
            for j in range(len(resultvector)):
                reverse_matrix[j][i] = resultvector[j]
        dprint("Reverse matrix :")
        dprint(reverse_matrix)
        dprint("Start matrix multiply reversematrix:")
        dprint(MM_multiplication(reverse_matrix,matrix))
        

def main():
    with open('labsCM\Lab2\Input.txt', 'r') as infile:
        Idata = [[float(element) for element in line.replace('\n','').split(' ')] for line in infile.readlines()]
    if (Idata.__len__() + 1 == Idata[0].__len__()):
        task_solution(Idata)
    else:
        dprint("Error, with input data")
        return
    pass

os.remove('labsCM\Lab2\Console.txt')
eps = 0.000001
main()