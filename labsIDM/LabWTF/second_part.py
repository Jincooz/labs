from unittest import result
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

def make_coefficients(AR, MA):
    result = np.zeros((len(AR)+len(MA)+1,1))
    for i in range(len(AR)):
        result[i] = AR[i]
    result[len(AR)] = 1
    for i in range(len(MA)):
        result[i+len(AR)+1] = MA[i]
    return result

def take_coefficients(AR, MA):
    file = open("labsIDM\Lab3\lab coefficients.txt", 'r')
    file = file.readlines()
    all_AR = int(file[0])
    AR_list = [float(element) for element in file[1:all_AR + 2]]
    MA_list = [float(element) for element in file[all_AR + 2:]]
    return make_coefficients(AR_list[:AR+1], MA_list[:MA]).T

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
    figure, axis = plt.subplots(1, 3)
    plot_X = []
    plot_y_S = [[],[]]
    plot_y_R2 = [[],[]]
    plot_y_IKA = [[],[]]
    y_amount = 200
    v = math_part.white_noise(y_amount)
    for AR in range(1,4):
        for MA in range(1,4):    
            coefficients = take_coefficients(AR, MA)
            y, X = math_part.ARMA(AR,MA,coefficients, y_amount, v = v)
            Y = y[max(AR, MA):]
            #coefficients = np.delete(coefficients, axis = 1, obj = AR + 1)
            LSM, RLSM = results(), results()
            LSM.S, LSM.e = math_part.less_square_method(X, Y, coefficients)
            RLSM.S, RLSM.e = math_part.recursive_less_square_method(X, Y, coefficients)
            LSM.R2 = math_part.coefficient_of_determination(LSM.S, coefficients)
            RLSM.R2 = math_part.coefficient_of_determination(RLSM.S, coefficients)
            LSM.IKA = math_part.IKA(LSM.e, AR, MA)
            RLSM.IKA = math_part.IKA(RLSM.e, AR, MA)
            plot_X.append("ARMA(%d,%d)" % (AR, MA))
            plot_y_S[0].append(LSM.S)
            plot_y_S[1].append(RLSM.S)
            plot_y_R2[0].append(LSM.R2)
            plot_y_R2[1].append(RLSM.R2)
            plot_y_IKA[0].append(LSM.IKA)
            plot_y_IKA[1].append(RLSM.IKA)
    axis[0].plot(plot_X, plot_y_S[0])
    axis[0].plot(plot_X, plot_y_S[1])
    axis[0].legend(["LSM","RLSM"])
    axis[0].set_title("Sum of squares")
    axis[0].tick_params(axis = 'x', labelrotation = 70)
    axis[1].plot(plot_X, plot_y_R2[0])
    axis[1].plot(plot_X, plot_y_R2[1])
    axis[1].legend(["LSM","RLSM"])
    axis[1].set_title("R squares")
    axis[1].tick_params(axis = 'x', labelrotation = 70)
    axis[2].plot(plot_X, plot_y_IKA[0])
    axis[2].plot(plot_X, plot_y_IKA[1])
    axis[2].legend(["LSM","RLSM"])
    axis[2].set_title("IKA coefficient")
    axis[2].tick_params(axis = 'x', labelrotation = 70)
    plt.show()
            

main()