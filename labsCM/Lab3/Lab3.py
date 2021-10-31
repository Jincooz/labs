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
    elif (type(data) == list and type(data[0])==list and (type(data[0][0]) == float or  type(data[0][0]) == int)):
        max_length = 0
        have_negative = False
        for row in data:
            for x in row:
                if(x.real > 0 and max_length < math.ceil(math.log10(x.real))):
                    max_length = math.ceil(math.log10(x.real))
                if(x.imag > 0 and max_length < math.ceil(math.log10(x.imag))):
                    max_length = math.ceil(math.log10(x.imag))
                if(x.real < 0 or x.imag < 0):
                    have_negative = True
        max_length = int(-math.log10(eps)) + max_length + 1
        datacopy = data.copy()
        data = ''
        for i in range(len(datacopy)):
            data += '['
            for j in range(len(datacopy[0])-1):
                data += number_to_string(datacopy[i][j], max_length)  + ', '
            data += number_to_string(datacopy[i][len(datacopy[0])-1], max_length) + ']\n'
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
    elif (type(data) == list and (type(data[0]) == float or type(data[0]) == int)):
        datacopy = data.copy()
        data = '['
        for i in range(len(datacopy) - 1):
            data += str(datacopy[i]) + ', '
        data += str(datacopy[len(datacopy)-1]) + ']\n'
    else:
        data = "Error with data type"
    with open('labsCM\Lab3\Console.txt', 'a') as outfile:
        outfile.write(data + '\n')
    print(data)

def transpose(matrix):
    return [[matrix[j][i] for j in range(matrix.__len__())] for i in range(matrix.__len__())]

def MM_multiplication(matrix1, matrix2):
    if(matrix1[0].__len__()!=matrix2.__len__()):
        return -1
    n =  matrix2.__len__()
    ResultMatrix = [[0 for element in matrix2[0]] for row in matrix1]
    for i in range(ResultMatrix.__len__()):
        for j in range(ResultMatrix.__len__()):
            for l in range(n):
                ResultMatrix[i][j] += matrix1[i][l]*matrix2[l][j] 
    return ResultMatrix
    
def MV_multiplication(matrix, vector):
    result_vector = [0 for x in vector]
    for i in range(vector.__len__()):
        for j in range(matrix[0].__len__()):
            result_vector[i] += matrix[i][j] * vector[j]
    return result_vector

def vector_sum(vector1, vector2):
    result_vector = vector1.copy()
    for i in range(len(result_vector)):
            result_vector[i] += vector2[i]
    return result_vector

def recursive_method(B, d, x_kn, k, A, b):
    x_kn1 = x_kn.copy()
    for i in range(len(x_kn1)):
        x_kn1[i] = 0
        for j in range(len(B[0])):
            x_kn1[i] += B[i][j] * x_kn1[j]
        x_kn1[i] += d[i]
    residual_vector = vector_sum(b, [-element for element in MV_multiplication(A, x_kn1)])
    less_then_eps = True
    dprint("Iteration " + str(k+1))
    dprint("X" + str(k+1) + " = ")
    dprint(x_kn1)
    dprint("Residual vector")
    dprint(residual_vector)
    for element in residual_vector:
        less_then_eps = less_then_eps and (abs(element) < eps)
    if less_then_eps:
        return x_kn1
    else:
        return recursive_method(B, d, x_kn1, k + 1, A, b)

def task_solution(matrix):
    vector = []
    for row in matrix:
        vector.append(row.pop(-1))
    #matrix = MM_multiplication(matrix1 = matrix, matrix2 = matrix)
    #vector = MV_multiplication(matrix, vector)
    B = [[element for element in row] for row in matrix]
    d = [element for element in vector]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(j!=i) : B[i][j] = -B[i][j] / B[i][i]
        d[i] = d[i] / B[i][i]
        B[i][i]=0
    solution_vectror = recursive_method(B, d, x_kn = [0 for i in range(len(vector))], k=0, A=matrix, b = vector)

def main():
    with open('labsCM\Lab3\Input.txt', 'r') as infile:
        Idata = [[float(element) for element in line.replace('\n','').split(' ')] for line in infile.readlines()]
    if (Idata.__len__() + 1 == Idata[0].__len__()):
        task_solution(Idata)
    else:
        dprint("Error, with input data")
        return
    pass

os.remove('labsCM\Lab3\Console.txt')
eps = 0.000001
main()