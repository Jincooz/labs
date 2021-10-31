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
    with open('labsCM\Lab3\Console.txt', 'a') as outfile:
        outfile.write(data + '\n')
    print(data)

def recursive_method(B, d, x, k):
    for i in range(len(B)):
        x[i] = 

def task_solution(matrix):
    vector = []
    for row in matrix:
        vector.append(row.pop(-1))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(i==j):
                matrix[i][j] -= 1
            matrix[i][j] = -matrix[i][j]
    solution_vectror = recursive_method(matrix, vector, x= [0 for i in range(len(vector))], k=0)

def MV_multiplication(matrix, vector):
    result_vector = [complex(0,0) for x in vector]
    for i in range(vector.__len__()):
        for j in range(matrix[0].__len__()):
            result_vector[i] += matrix[i][j] * vector[j]
    return result_vector

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