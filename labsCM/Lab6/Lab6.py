import math as mt
import random as rng

def function(x):
    return pow(7,5*x)

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
        divided_differences.append(divided_difference(x_list[0:k+1],y_list))

    def newtons_polynomial(x):
        result = y_list[0]
        for k in range(1, len(x_list)):
            multiplication_result = 1.0
            for i in range(k):
                multiplication_result *= (x-x_list[i])
            result += multiplication_result * divided_differences[k-1]
        return result
    return newtons_polynomial

def main():
    start = float(input("a = "))
    end = float(input("b = "))
    amount_of_dots = 200
    x_list = [ start + i * ((end - start)/(amount_of_dots-1)) for i in range(amount_of_dots)] 
    rng.shuffle(x_list)
    y_list = [function(x_list[i]) for i in range(amount_of_dots)] 
    polinomial1 = create_lagrange_polynomial(x_list, y_list)
    polinomial2 = create_newtons_polynomial(x_list, y_list)
    polinomial3 = create_newtons_polynomial(x_list[::-1], y_list[::-1])
    #TODO fix newtons method (don`t work for big amount of dots or big range end - start)
    #TODO? fix lagranges method (have 100% result dy1 = 0 always) 
    sumdy1 = 0
    sumdy2 = 0
    sumdy3 = 0
    for x in x_list:
        dy1 = abs(polinomial1(x)-function(x))
        dy2 = abs(polinomial2(x)-function(x))
        dy3 = abs(polinomial3(x)-function(x))
        sumdy1 += dy1
        sumdy2 += dy2
        sumdy3 += dy3
        print("x = %f y1 = %s, y2 = %s, y3 = %s" % (x,("yes" if  dy1 < 0.000001 else "no"), ("yes" if dy2 < 0.000001 else "no"), ("yes" if dy3 < 0.000001 else "no")))
    print("dy1 = %.3f, dy2 = %.3f, dy3 = %.3f" % (sumdy1,sumdy2,sumdy3))

main()
