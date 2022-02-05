import math as mt
import random as rng

#TODO changee function to pow(7,5*x)
def function(x):
    return x

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
    return polinomial_list

def test_print(x_list, polinomial_list):
    sumdy = [0 for i in range(len(polinomial_list))]
    for x in x_list:
        dy = [abs(polinomial_list[i](x)-function(x)) for i in range(len(polinomial_list))]
        for i in range(len(polinomial_list)):
            sumdy[i] += dy[i]
        print("x = %.5f" % (x), end="")
        for i in range(len(polinomial_list)):
            print(" y%i = %s" % (i, ("yes" if  dy[i] < 0.000001 else "no")), end="")
        print("")
    for i in range(len(polinomial_list)):
        print("y%i = %.5f " % (i, sumdy[i]), end="")
    print("")

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
    test_print(x_list2, polinomial_list)

main()
