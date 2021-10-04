import methods as mth
import os
#test 4,-3,1,2,-4,6  [-2,0]

os.remove('labsCM\Lab1\Result.txt')
with open('labsCM\Lab1\console.txt', 'w') as file:
    print("Рішення рівняння виду a5*х^5+a4*x^4+a3*x^3+a2*x^2+a1*x+a0")
    coefficients = input("Введіть коефіцієнти у форматі a5,a4,a3,a2,a1,a0 : ").split(',')
    for i in range(0,6):
        coefficients[i]=int(coefficients[i])
    coefficients = coefficients[::-1]
    range = input("Введіть проміжок в форматі [a,b]: ")[1:-1].split(',')
    range_start, range_end = float(range[0]), float(range[1])
    precision = 1E-5
    mth.bisection_method_iterations = 0
    mth.bisection_method_result = mth.bisection_method(range_start, range_end, coefficients, precision, file)
    print('------------------------')
    file.write('------------------------')
    mth.chorde_method_iterations = 0
    mth.chorde_method_result = mth.chorde_method(range_start, range_end, coefficients, precision, file)
    print('------------------------')
    file.write('------------------------')
    mth.newton_method_iterations = 0
    mth.newton_method_result = mth.newton_method(range_start, range_end, coefficients, precision, file)

os.rename('labsCM\Lab1\console.txt','labsCM\Lab1\Result.txt')

