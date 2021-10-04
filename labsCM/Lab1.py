def function(сoefecients, x):
    return coeficients[0]+coeficients[1]*x+coeficients[2]*(x**2)+coeficients[3]*(x**3)+coeficients[4]*(x**4)+coeficients[5]*(x**5)

def bisection_method(range_start, range_end, coeficients):
    global bisection_method_iterations
    range_middle = (range_start + range_end) / 2
    if(abs(range_middle - range_start) > POHIBKA):
        bisection_method_iterations += 1
        if (function(coeficients, range_middle) >= POHIBKA):
            print("Метод бисекций " + bisection_method_iterations + "-ая итерация c = " +)
            return bisection_method(range_start,range_middle,coeficients)
        elif (function(coeficients, range_middle) <= -POHIBKA):
            return bisection_method(range_middle,range_end,coeficients)
    else:
        return range_middle



with open('con.txt', 'w') as file:
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

