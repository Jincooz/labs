def function(coefficients, x):
    return coefficients[0] + coefficients[1] * x + coefficients[2] * (x**2) + coefficients[3] * (x**3) \
        + coefficients[4] * (x**4) + coefficients[5] * (x**5)

def function_derivative(coefficients, x):
    return coefficients[1] + 2 * coefficients[2] * x + 3 * coefficients[3] * (x**2) \
        + 4 * coefficients[4] * (x**3) + 5 * coefficients[5] * (x**4)

def function_derivative2(coefficients, x):
    return 2 * coefficients[2] + 2 * 3 * coefficients[3] * x + 3 * 4 * coefficients[4] * (x**2) + 4 * 5 * coefficients[5] * (x**3)

def bisection_method(range_start, range_end, coefficients, precision, file):
    global bisection_method_iterations
    range_middle = (range_start + range_end) / 2
    if(abs(range_middle - range_start) > precision):
        bisection_method_iterations += 1
        print("Метод бисекций " + str(bisection_method_iterations) + "-а ітерація c = " + str(range_middle))
        file.write("Метод бисекций " + str(bisection_method_iterations) + "-а ітерація c = " + str(range_middle) + '\n')
        if (function(coefficients, range_middle) >= precision):
            return bisection_method(range_start,range_middle,coefficients, precision, file)
        elif (function(coefficients, range_middle) <= -precision):
            return bisection_method(range_middle,range_end,coefficients, precision, file)
    else:
        return range_middle

def chorde_method(range_start, range_end, coefficients, precision, file):
    global chorde_method_iterations
    secant_x = (range_start*function(coefficients, range_end)-range_end*function(coefficients, range_start))/(function(coefficients, range_end)-function(coefficients, range_start))
    if(abs(secant_x - range_start) > precision):    
        chorde_method_iterations += 1
        print("Метод хорд " + str(chorde_method_iterations) + "-а ітерація c = " + str(secant_x))
        file.write("Метод хорд " + str(chorde_method_iterations) + "-а ітерація c = " + str(secant_x) + '\n')
        if (function(coefficients, secant_x) >= precision):
            return chorde_method(range_start,secant_x,coefficients, precision, file)
        elif (function(coefficients, secant_x) <= -precision):
            return chorde_method(secant_x,range_end,coefficients, precision, file)
    else:
        return secant_x

def newton_method(range_start, range_end, coefficients, precision, file):
    global newton_method_iterations
    if (function_derivative2(coefficients, range_start)*function(coefficients, range_start) > 0):
        x_prev = range_start
    else:
        x_prev = range_end
    x = x_prev - (function(coefficients,x_prev)/function_derivative(coefficients,x_prev))
    newton_method_iterations += 1
    print("Метод ньютона " + str(newton_method_iterations) + "-а ітерація x = " + str(x))
    file.write("Метод ньютона " + str(newton_method_iterations) + "-а ітерація x = " + str(x) + '\n')
    while(abs(x-x_prev) > precision and abs(function(coefficients,x)) > precision):
    #while(abs(precision-x)<=abs(function(coefficients,x)/min(function_derivative(coefficients,range_start),function_derivative(coefficients,range_end)))):
        newton_method_iterations += 1
        x_prev = x
        x = x_prev - (function(coefficients,x_prev)/function_derivative(coefficients,x_prev))
        print("Метод ньютона " + str(newton_method_iterations) + "-а ітерація x = " + str(x))
        file.write("Метод ньютона " + str(newton_method_iterations) + "-а ітерація x = " + str(x) + '\n')
    return x

def combinate_method(range_start, range_end, coefficients, precision, file):
    global combinate_method_iterations
    if (function_derivative2(coefficients, range_start)*function(coefficients,range_start) > 0):
        x_prev = range_start
    else:
        x_prev = range_end
    x = x_prev - (function(coefficients,x_prev)/function_derivative(coefficients,x_prev))
    secant_x = (range_start*function(coefficients, range_end)-range_end*function(coefficients, range_start))/(function(coefficients, range_end)-function(coefficients, range_start))
    combinate_method_iterations += 1    
    print("Комбінований метод " + str(combinate_method_iterations) + "-а ітерація координата перетину оХ : січною = " + str(secant_x) + " дотичною = " + str(x))
    file.write("Комбінований метод " + str(combinate_method_iterations) + "-а ітерація координата перетину оХ : січною = " + str(secant_x) + " дотичною = " + str(x) + '\n')
    if(abs(x-secant_x)>precision):
        if(function_derivative(coefficients,range_start)*function_derivative2(coefficients,range_start) > 0):
            combinate_method(secant_x, x,coefficients,precision,file)
        else:
            combinate_method(x, secant_x,coefficients,precision,file)
    else:
        print('Корень рівняння ' + str((x+secant_x)/2))

