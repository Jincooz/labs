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
    with open('labsCM\Lab4\Console.txt', 'a') as outfile:
        outfile.write(data + '\n')
    print(data)
 
def vector_sum(vector1, vector2):
    result_vector = vector1.copy()
    for i in range(len(result_vector)):
            result_vector[i] += vector2[i]
    return result_vector
 
def transpose(matrix):
    return [[matrix[j][i] for j in range(matrix.__len__())] for i in range(matrix.__len__())]
 
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
    U_multiply_resultvector = straight_run(transpose(U(matrix)), vector)    
    resultvector = reverse_run(U(matrix), U_multiply_resultvector)
    return resultvector
 
def f1(vector):
    return (math.sin(vector[0]+vector[1])+1.302*vector[0] - 0.793)
 
def f2(vector):
    return (vector[0]*vector[0] + vector[1]*vector[1] - 1)
 
def f00(vector):
    return (math.cos(vector[0]+vector[1]) + 1.302)
 
def f01(vector):
    return (math.cos(vector[0]+vector[1]))
 
def f10(vector):
    return (2*vector[0])
 
def f11(vector):
    return (2*vector[1])
 
def task_solution(vector, itteration):
    new_vector = vector.copy()
    matrix = [[0, 0], [0, 0]]
    matrix[0][0] = f00(vector)
    matrix[0][1] = f01(vector)
    matrix[1][0] = f10(vector)
    matrix[1][1] = f11(vector)
    Fm = vector.copy()
    Fm[0] = -f1(vector)
    Fm[1] = -f2(vector)
    new_vector = sole_sulution(matrix, Fm)
    new_vector = [float(new_vector[i].real)+vector[i] for i in range(len(new_vector))]
    dprint("Itteration " + str(itteration + 1) + ":")
    dprint(new_vector)
    residual_vector = [f1(new_vector),f2(new_vector)]
    dprint("Residual vector")
    dprint(residual_vector)
    residual_vector2 =  vector_sum(vector, [-element for element in new_vector])
    residual_vector2 = [abs(element) for element in residual_vector2]
    dprint("Residual vector2 :")
    dprint(residual_vector2)
    less_then_eps = True
    for i in range(len(residual_vector)):
        less_then_eps = less_then_eps and (abs(residual_vector[i]) < eps) and (abs(residual_vector2[i]) < eps)
    if less_then_eps:
        return new_vector
    else:
        return task_solution(new_vector, itteration+1)
 
def main():
    dprint("first root search\n")
    vector1 = task_solution([0.5,-0.5], 0)
    dprint("second root search\n")
    vector2 = task_solution([-0.25,0.75], 0)

eps = 0.00001
main()
os.remove('labsCM\Lab4\ResultNewton`s.txt')
os.rename('labsCM\Lab4\Console.txt','labsCM\Lab4\ResultNewton`s.txt')
 

