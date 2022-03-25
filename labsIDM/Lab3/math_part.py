import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def white_noise(N = 1):
    white_noise_vector = np.zeros((N,1))
    for i in range(N):
        white_noise_vector[i] = np.random.normal(0,1,size=None)    
    return white_noise_vector

def ARMA(AR, MA, coefficients, y_amount, v = None):
    if v is None:
        v = white_noise(y_amount)
    y = np.zeros((y_amount,1))
    for i in range(max(AR, MA)):
        y[i] = v[i]
    X = np.zeros((y_amount - max(AR, MA), AR + MA + 2))
    for i in range(max(AR, MA),y_amount):
        X[i-max(AR, MA)][0] = 1
        for j in range(1,AR+1):
            X[i-max(AR, MA)][j] = y[i-j]
        for j in range(AR+1, AR + MA + 2):
            X[i-max(AR, MA)][j] = v[i - j + AR + 1]
        row = np.reshape(X[i-max(AR, MA)],(X.shape[1],1)).T
        y[i] = row @ coefficients.T
    y = y
    X = np.delete(X,axis = 1, obj = AR + 1)
    return y, X

def less_square_method(X, Y, real_coefficients):
    coefficients_predict = np.linalg.inv(X.T @ X) @ X.T @ Y
    error_vector = coefficients_predict-real_coefficients.T
    standard_deviation = np.sum(np.power(error_vector, 2))
    return standard_deviation, error_vector

def recursive_less_square_method(X, Y, real_coefficients, a = 0.0001, b = 1000):
    i = 0
    sigma_past = np.zeros((X.shape[1], 1))
    P_past = b * np.diag(np.ones(X.shape[1]))
    for i in range(X.shape[0]):
        row = np.array([X[i]])
        P_current = P_past - (P_past @ row.T @ row @ P_past)/(1 + row @ P_past @ row.T)
        dt = Y[i].T - row @ sigma_past
        sigma_current = sigma_past + P_current @ row.T * (dt)
        P_past = P_current
        sigma_past = sigma_current
    error_vector = sigma_current-real_coefficients.T
    standard_deviation = np.sum(np.power(error_vector,2))
    return standard_deviation, error_vector

def coefficient_of_determination(RSS, vector_for_TSS):
    TSS = np.sum(np.power(vector_for_TSS-np.mean(vector_for_TSS),2))
    return 1-RSS/TSS

def IKA(e, AR, MA):
    sum = np.sum(np.power(e,2))
    return e.size * np.log(sum) + 2 * (AR + MA + 1)