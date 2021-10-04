import os
#test 4,-3,1,2,-4,6  [-2,0]
def function(сoefecients, x):
    return coeficients[0]+coeficients[1]*x+coeficients[2]*(x**2)+coeficients[3]*(x**3)+coeficients[4]*(x**4)+coeficients[5]*(x**5)

def bisection_method(range_start, range_end, coeficients):
    global bisection_method_iterations
    range_middle = (range_start + range_end) / 2
    if(abs(range_middle - range_start) > POHIBKA):
        bisection_method_iterations += 1
        print("Метод бисекций " + str(bisection_method_iterations) + "-ая итерация c = " + str(range_middle))
        file.write("Метод бисекций " + str(bisection_method_iterations) + "-ая итерация c = " + str(range_middle) + '\n')
        if (function(coeficients, range_middle) >= POHIBKA):
            return bisection_method(range_start,range_middle,coeficients)
        elif (function(coeficients, range_middle) <= -POHIBKA):
            return bisection_method(range_middle,range_end,coeficients)
    else:
        return range_middle

def chorde_method(range_start, range_end, coeficients):
    global chorde_method_iterations
    secant_x = (range_start*function(coeficients, range_end)-range_end*function(coeficients, range_start))/(function(coeficients, range_end)-function(coeficients, range_start))
    if(abs(secant_x - range_start) > POHIBKA):
        chorde_method_iterations += 1
        print("Метод хорд " + str(chorde_method_iterations) + "-ая итерация c = " + str(secant_x))
        file.write("Метод хорд " + str(chorde_method_iterations) + "-ая итерация c = " + str(secant_x) + '\n')
        if (function(coeficients, secant_x) >= POHIBKA):
            return bisection_method(range_start,secant_x,coeficients)
        elif (function(coeficients, secant_x) <= -POHIBKA):
            return bisection_method(secant_x,range_end,coeficients)
    else:
        return secant__x
    

with open('labsCM\Lab1\console.txt', 'w') as file:
    print("Рішення рівняння виду a5*х^5+a4*x^4+a3*x^3+a2*x^2+a1*x+a0")
    coeficients = input("Введіть коефіцієнти у форматі a5,a4,a3,a2,a1,a0 : ").split(',')
    for i in range(0,6):
        coeficients[i]=int(coeficients[i])
    coeficients = coeficients[::-1]
    range = input("Vvedite promizok in format [a,b]: ")[1:-1].split(',')
    range_start, range_end = float(range[0]), float(range[1])
    POHIBKA = 1E-5
    bisection_method_iterations = 0
    bisection_method_result = bisection_method(range_start, range_end, coeficients)
    chorde_method_iterations = 0
    chorde_method_result = chorde_method(range_start, range_end, coeficients)

os.rename('labsCM\Lab1\console.txt','labsCM\Lab1\Result.txt')

