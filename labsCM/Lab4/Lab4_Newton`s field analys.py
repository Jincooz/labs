import os
import math

def dprint(data):
    with open('labsCM\Lab4\Console.txt', 'a') as outfile:
        outfile.write(data)
 
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
 
def task_solution(vector):
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
    residual_vector = [f1(new_vector),f2(new_vector)]
    residual_vector2 =  vector_sum(vector, [-element for element in new_vector])
    residual_vector2 = [abs(element) for element in residual_vector2]
    less_then_eps = True
    for i in range(len(residual_vector)):
        less_then_eps = less_then_eps and (abs(residual_vector[i]) < eps) and (abs(residual_vector2[i]) < eps)
    if less_then_eps:
        return new_vector
    else:
        return task_solution(new_vector)
 
def main():
    dprint("first root search\n")
    vector1 = task_solution([0.5,-0.5])
    dprint("second root search\n")
    vector2 = task_solution([-0.25,0.75])
    vector1 = [round(element*10000) for element in vector1]
    vector2 = [round(element*10000) for element in vector2]
    experiment_steps = [-1.032 + 0.008*i for i in range(259)]
    for y in experiment_steps:
        print = ""
        for x in experiment_steps:
            vector = task_solution([x , y])
            vector = [round(element*10000) for element in vector]
            if(vector[0] == vector1[0] and vector[1] == vector1[1]):
                print += "0  "
            elif (vector[0] == vector2[0] and vector[1] == vector2[1]):
                print += "1  "
            else:
                print += "2  "
        dprint(print + "\n")

eps = 0.00001
main()  
os.remove('labsCM\Lab4\ResultNewton`s field.txt')
os.rename('labsCM\Lab4\Console.txt','labsCM\Lab4\ResultNewton`s field.txt')
 

