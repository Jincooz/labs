import math as mt
import random as rng
from tkinter import E
import numpy as np
from matplotlib import pyplot as plt

#TODO changee function to pow(7,5*x)
def function(x):
    return pow(7,x)

def create_basic_polynomial(x_list, i):
    def basic_polynomial(x):
        result = 1.0
        for j in range(len(x_list)):
            if (i != j):
                result *= (x-x_list[j])/(x_list[i]-x_list[j])
        return result
    return basic_polynomial

def create_lagrange_polynomial(x_list, y_list):
    basic_polynomial_list = []
    for i in range(len(x_list)):
        basic_polynomial_list.append(create_basic_polynomial(x_list,i))
    
    def lagrange_polynomial(x):
        result = 0.0
        for i in range(len(x_list)):
            result += y_list[i] * basic_polynomial_list[i](x)
        return result
    return lagrange_polynomial

def divided_difference(x_list, y_list):
    function_result = 0.0
    for j in range(len(x_list)):
        multipliation_result = 1.0
        for i in range(len(x_list)):
            if ( j != i ):
                multipliation_result *= x_list[j] - x_list[i]
        function_result += y_list[j]/multipliation_result
    return function_result

def create_newtons_polynomial(x_list, y_list):
    divided_differences = []
    for k in range(1,len(x_list)):
        divided_differences.append(divided_difference(x_list[0:k+1],y_list[0:k+1]))
        if(abs(divided_differences[k-1])<1E-6):
            divided_differences[k-1] = 0
        if(divided_differences[k-1] != 0):
            pass

    def newtons_polynomial(x):
        result = y_list[0]
        for k in range(1, len(x_list)):
            multiplication_result = divided_differences[k-1]
            for i in range(k):
                multiplication_result *= (x-x_list[i])
            result += multiplication_result
        return result
    return newtons_polynomial

def create_spline(x_list, y_list):
    h = np.zeros(len(x_list) - 1)
    n = np.zeros(len(y_list) - 1)
    for i in range(len(x_list) - 1):
        h[i] = x_list[i+1] - x_list[i]
        n[i] = y_list[i+1] - y_list[i]
    matrix = np.zeros((len(x_list)-2,len(x_list)-2))
    result_vector = np.zeros((len(x_list))-2)
    matrix[0][0] = 2 * (h[0] + h[1])
    matrix[0][1] = h[1]
    result_vector[0] = 6 * (n[1]/h[1] - n[0]/h[0])
    for i in range(1,len(h)-2):
        matrix[i][i-1] = h[i]
        matrix[i][i] = 2 * (h[i] + h[i+1])
        matrix[i][i+1] = h[i+1]
        result_vector[i] = 6 * (n[i+1]/h[i+1]-n[i]/h[i])
    matrix[len(h) - 2][len(h) - 2] = 2 * (h[len(h)-2] + h[len(h)-1])
    matrix[len(h) - 2][len(h) - 3] = h[len(h)-1]
    result_vector[len(h) - 2] = 6 * (n[len(h) - 1]/h[len(h) - 1]-n[len(h) - 2]/h[len(h) - 2])
    c = np.linalg.solve(matrix, result_vector)
    c = np.insert(c, 0, 0)
    d= np.zeros(len(h))
    b = np.zeros(len(h))
    a = np.zeros(len(h))
    for i in range(len(x_list) - 2):
        a[i] = y_list[i]
        d[i] = ((c[i+1] - c[i])/(3*h[i]))
        b[i] = ((y_list[i+1]-y_list[i])/h[i] - c[i]*h[i] - d[i]*h[i]*h[i])
    a[len(h)-1] = y_list[len(h)-1]
    d[len(h)-1] = (-1*c[len(h)-1]/(3*h[len(h)-1]))
    b[len(h)-1] = (-2*h[len(h)-1]*c[len(h)-1]/3 + (y_list[len(h)]-y_list[len(h)-1])/h[len(h)-1])
    def spline(x):
        i = 0
        while x_list[i+1]+0.00000001 < x:
            i += 1
        dx = x-x_list[i]
        return a[i] + b[i] * dx + c[i] * dx * dx + d[i] * dx * dx * dx
    return spline

def console_input_get_x_lists_console():
    amount_of_dots = int(input("Amount of dots : "))
    x_list = []
    for i in range(amount_of_dots):
        x_list.append(float(input("Dot" + str(i) + ": ")))
    x_list2 = []
    for i in range(len(x_list) - 1):
        for j in range(6):
            x_list2.append((x_list[i] + (j) * (x_list[i+1] - x_list[i])/6))
    x_list2.append(x_list[len(x_list)-1])
    return x_list, x_list2    

def console_input_get_x_lists_automatic(menu_pick):
    start = float(input("Enter the start x coordinate of the segment. a = "))
    end = float(input("Enter the end x coordinate of the segment. b = "))
    amount_of_dots = int(input("Enter the number of dots. amount = "))
    if menu_pick == "2":
        x_list = [ start + i * ((end - start)/(amount_of_dots-1)) for i in range(amount_of_dots)] 
        amount_of_dots *= 5
        x_list2 = [ start + i * ((end - start)/(amount_of_dots-1)) for i in range(amount_of_dots)]
    elif menu_pick == "3":
        x_list = [ (start * pow(pow(end/start,1/amount_of_dots), (i+1))) for i in range(amount_of_dots)]
        amount_of_dots *= 5
        x_list2 = [ (start * pow(pow(end/start,1/amount_of_dots), (i+1))) for i in range(amount_of_dots)]
    menu_pick = input("Shuffle x list?(y/n): ")
    if menu_pick == "y":
        rng.shuffle(x_list)
    elif menu_pick != "n":
        print("Invalid input. List won't be shuffled.")
    return x_list, x_list2

def polinomial_list_initialize(x_list, y_list):
    polinomial_list = []
    polinomial_list.append(create_lagrange_polynomial(x_list, y_list))
    polinomial_list.append(create_newtons_polynomial(x_list, y_list))
    polinomial_list.append(create_newtons_polynomial(x_list[::-1], y_list[::-1]))
    polinomial_list.append(create_spline(x_list, y_list))
    return polinomial_list

def test_print(x_list, polinomial_list):
    sumdy = [0 for i in range(len(polinomial_list))]
    e = np.zeros((len(polinomial_list),len(x_list)))
    for i,x in enumerate(x_list):
        dy = [interpol_func(x)-function(x) for interpol_func in polinomial_list]
        for j in range(len(polinomial_list)):
            sumdy[j] += abs(dy[j])
            e[j][i] = abs(dy[j])
        print("x = %.5f" % (x), end="")
        for j in range(len(polinomial_list)):
            print(" y%i = %s" % (j, ("yes" if  abs(dy[j]) < 0.000001 else "no")), end="")
        print("")
    for i in range(len(polinomial_list)):
        print("y%i = %.5f " % (i, sumdy[i]), end="")
    print("")
    return e

def main():
    print("How to get x list?\n1. Hand input of dots coordinates\n2. Linear automatic\n3. Power automatic\n4. Exit")
    menu_pick = input("Choose and enter number: ")
    if menu_pick == "1":
        x_list, x_list2 = console_input_get_x_lists_console()
    elif menu_pick == "2" or menu_pick == "3":
       x_list, x_list2 = console_input_get_x_lists_automatic(menu_pick)
    elif menu_pick == "4":
        return 0
    else:
        print("Invalid input. Try again later." )
        return
    y_list = [function(x) for x in x_list]
    polinomial_list = polinomial_list_initialize(x_list, y_list)
    test_print(x_list, polinomial_list)
    e = test_print(x_list2, polinomial_list)
    plt.rcParams['figure.figsize'] = [20, 5]
    plt.plot(x_list2, e[0])
    plt.plot(x_list2, e[1])
    plt.plot(x_list2, e[2])
    plt.plot(x_list2, e[3])
    plt.legend(['lagrange',"newton","reverse newton", "spline"])
    plt.ylabel("e")
    plt.xlabel("x")
    plt.yscale("log")
    plt.tick_params(axis = 'x', labelrotation = 90, labelsize = 9)
    plt.show()


main()
