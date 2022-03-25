import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os
import math_part

class results:
    def __init__(self):
        S = 0.0
        R2 = 0.0
        IKA = 0.0

#interface 1

error_text = ""

def read_var_from_file(file_dir):
    try:
        file = open(file_dir, 'r')
    except FileNotFoundError:
        error_text = "File not found"
        return False, error_text, None
    var_str = file.readlines()
    amount_of_var = len(var_str)
    if(amount_of_var == 0):
        error_text = "File is empty"
        return False, error_text, None
    var = np.zeros((amount_of_var,1))
    for i in range(len(var_str)):
        try:
            var[i] = float(var_str[i])
        except ValueError:
            error_text = "Data in file is not readable"
            return False, error_text, None
    file.close()
    return True, amount_of_var, var

def coefficients_string(coefficients):
    string = ''
    for element in coefficients:
        string += str(element) + ' '
    return string

def input_AR_coef(AR, AR_coefficients):
    result = np.zeros((AR + 1,1))
    for i in range(AR+1):
        try:
            result[i] = float(input("a%d = " % (i)))
        except ValueError:
            return False, AR_coefficients
    return True, result

def input_MA_coef(MA, MA_coefficients):
    result = np.zeros((MA,1))
    for i in range(MA):
        try:
            result[i] = float(input("b%d = " % (i+1)))
        except ValueError:
            return False, MA_coefficients
    return True, result

def input_coef(AR, MA, coefficients):
    success, AR_coefficients = input_AR_coef(AR, None)
    if not success:
        return False, coefficients
    success, MA_coefficients = input_MA_coef(MA, None)
    if not success:
        return False, coefficients
    return True, make_coefficients(AR_coefficients, MA_coefficients)

def make_coefficients(AR, MA):
    result = np.zeros((len(AR)+len(MA)+1,1))
    for i in range(len(AR)):
        result[i] = AR[i]
    result[len(AR)] = 1
    for i in range(len(MA)):
        result[i+len(AR)+1] = MA[i]
    return result.T

def input_y_amount(number_of_y):
    result = 0
    try:
        result = int(input("number of y = "))
    except ValueError:
        return False, number_of_y
    return True, result

def input_dir(string):
    try: 
        return True, input(string)
    except:
        return False, None

def show_menu(taked_data_from_file, AR, MA, coefficients, number_of_y, some_text_about_errors = ''):
    print(  "Configurate ARMA\n"+
            "1. Autoregression : %d\n" % (AR) +
            "2. Moving avarage : %d\n" % (MA) +
            "3. Coefficients : %s\n" % (coefficients_string(coefficients)) +
            "4. Amount of y : %s\n" % (str(number_of_y) if not taked_data_from_file else str(number_of_y) + "lock") +
            "5. Taked v from file : %s\n" % ("yes lock" if taked_data_from_file else "no") +
            "6. End configuration\n" + 
            some_text_about_errors)
    return input()

def menu():
    taked_data_from_file = False
    v = None
    AR, MA = 0, 0
    AR_coefficients, MA_coefficients = np.ones(AR + 1), np.ones(MA)
    coefficients = np.ones(AR + MA + 2)
    number_of_y = 10
    error_text = ''
    while(True):
        os.system('cls')
        change = show_menu(taked_data_from_file,AR,MA,coefficients,number_of_y, error_text)
        os.system('cls')
        error_text = ""
        try:
            change = int(change)
        except ValueError:
            error_text = "Invalid input. Type 1-6 number"
        if change not in [1,2,3,4,5,6]:
            error_text = "Invalid input. Type 1-6 number"
            continue
        if change == 4 and taked_data_from_file:
            print("You can`t change amount of y if you taked data from file")
        if change == 5 and taked_data_from_file:
            print("You want discard data taked from file?(y/n)")
            change = input()
            if change == 'y':
                print("Discarded")
                taked_data_from_file = False
                change = 4
            elif change == 'n':
                change = 7
            else:
                error_text = "Invalid input"
        if change == 1:
            try:
                data = int(input("New AR amount : "))
            except ValueError:
                error_text = "Invalid input"
                continue
            if data > 100 or data < 0:
                error_text = "Invalid input"
                continue
            success, AR_coefficients = input_AR_coef(data, AR_coefficients)
            if not success:
                error_text = "Invalid input. Changes discarded"
                continue
            AR = data
            coefficients = np.zeros((AR+MA+2,1))
            coefficients = make_coefficients(AR_coefficients, MA_coefficients)            
        if change == 2:
            try:
                data = int(input("New MA amount : "))
            except ValueError:
                error_text = "Invalid input"
                continue
            if data > 100 or data < 0:
                error_text = "Invalid input"
                continue
            success, MA_coefficients = input_MA_coef(data, MA_coefficients)
            if not success:
                error_text = "Invalid input. Changes discarded"
                continue
            MA = data
            coefficients = np.zeros((AR+MA+2,1))
            coefficients = make_coefficients(AR_coefficients, MA_coefficients)  
        if change == 3:
            coefficients = np.zeros((AR+MA+2,1))
            success, coefficients = input_coef(AR, MA, coefficients)
            if not success:
                error_text = "Invalid input. Changes discarded"
                continue
        if change == 4:
            success, number_of_y = input_y_amount(number_of_y)
            if not success:
                error_text = "Invalid input. Changes discarded"
                continue
            if data <= 0:
                error_text = "Invalid input"
                continue
            if data <= max(AR, MA) + 1:
                error_text = "Invalid input. Amount of y can`t be lower that AR + 1 or MA + 1"
                continue
        if change == 5:
            num = number_of_y
            success, dir = input_dir("Input directory to file : ")
            if not success:
                error_text = "Unknown error"
                continue
            success, number_of_y, v = read_var_from_file(dir)
            if not success:
                error_text = number_of_y
                v = None
                number_of_y = num
                continue
            else:
                taked_data_from_file = True
        if change == 6:
            result = math_part.ARMA(AR, MA, coefficients, number_of_y, v)
            return result[0], result[1], coefficients, AR, MA

def results_showing(AR, MA, LSM, RLSM):
    print(  "Result for ARMA(%d,%d):\n" % (AR,MA) +
            "LSM:\n" +
            "S = %f\n" % (LSM.S) +
            "R^2 = %f\n" % (LSM.R2) +
            "IKA = %f\n" % (LSM.IKA) +
            "RLSM:\n" +
            "S = %f\n" % (RLSM.S) +
            "R^2 = %f\n" % (RLSM.R2) +
            "IKA = %f\n" % (RLSM.IKA))

def main():
    y, X, real_coefficients, AR, MA = menu()
    print("Vector y:")
    print(y)
    Y = y[max(AR, MA):]
    LSM, RLSM = results(), results()
    LSM.S, LSM.e = math_part.less_square_method(X, Y, real_coefficients)
    RLSM.S, RLSM.e = math_part.recursive_less_square_method(X, Y, real_coefficients)
    LSM.R2 = math_part.coefficient_of_determination(LSM.S, real_coefficients)
    RLSM.R2 = math_part.coefficient_of_determination(RLSM.S, real_coefficients)
    LSM.IKA = math_part.IKA(LSM.e, AR, MA)
    RLSM.IKA = math_part.IKA(RLSM.e, AR, MA)
    results_showing(AR, MA, LSM, RLSM)

main()