import os
import math
from typing import Match

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

def fy(vector):
    return (math.cos(vector[0]+0.812) - 1.302)/1.522

def fx(vector):
    return 0.793-math.sin(vector[1]-1.791)

def f1(vector):
    return (math.cos(vector[0]+0.812) - 1.302 - 1.522 * vector[1])

def f2(vector):
    return (0.793-math.sin(vector[1]-1.791) - vector[0])

def task_solution(vector, k):
    new_vector = vector.copy()
    new_vector[0] = fx(vector)
    new_vector[1] = fy(vector)
    residual_vector = [f1(new_vector),f2(new_vector)]
    residual_vector2 =  vector_sum(vector, [-element for element in new_vector])
    residual_vector2 = [abs(element) for element in residual_vector2]
    dprint("Iteration " + str(k+1))
    dprint("X" + str(k+1) + " = ")
    dprint(new_vector)
    dprint("Residual vector")
    dprint(residual_vector)
    dprint("Residual vector2")
    dprint(residual_vector2)
    less_then_eps = True
    for i in range(len(residual_vector)):
        less_then_eps = less_then_eps and (abs(residual_vector[i]) < eps) and (abs(residual_vector2[i]) < eps)
    if less_then_eps:
        return 0
    else:
        return task_solution(new_vector, k+1)

def main():
    task_solution([1.0771,-1.0625],0)
    

os.remove('labsCM\Lab4\Console.txt')
eps = 0.00001
main()