import matplotlib.pyplot as plt

def df(x, y):
    return 3*x - y/x

def f(x):
    return x * x

def RK4(function, y0, h, x0, x_end):
    x = [x0]
    y = [y0]
    for i in range(int((x_end - x0)/h)):
        k1 = h*function(x[i], y[i])
        k2 = h*function(x[i] + h/2, y[i] + k1/2)
        k3 = h*function(x[i] + h/2, y[i] + k2/2)
        k4 = h*function(x[i] + h, y[i] + k3)
        x.append(x[i]+h)
        y.append(y[i]+(k1 + 2 * k2 + 2 * k3 + k4)/6)
    return y

def adams4(function,x0, y0, h, x_end):
    x = x0[:]
    y = y0[:]
    for i in range(3, int((x_end - x0[0])/h)):
        x.append(x[i]+h)
        delta_y = (h/24)*(55*function(x[i], y[i]) - 59*function(x[i-1], y[i-1]) + 37*function(x[i-2], y[i-2]) - 9*function(x[i-3], y[i-3]))
        y.append(y[i] + delta_y)
    return y

x0 = 1
y0 = 1
h = 0.01
x_end = x0 + 1
amount = int((x_end - x0)/h)+1
x_list = [x0+h*i for i in range(amount)]
y_list = [f(x) for x in x_list]
y2_list = RK4(df,y0,h,x0,x_end)
y3_list = adams4(df,x_list[:4],y2_list[:4],h,x_end)
e2 = [abs(y2_list[i]-y_list[i]) for i in range(amount)]
e3 = [abs(y3_list[i]-y_list[i]) for i in range(amount)] 
print(f"x_list\ty\ty_RK4\te_RK4\ty_adams\te_adams")
for i in range(amount):
    print(f"{round(x_list[i],4)}\t{round(y_list[i],4)}\t{round(y2_list[i],4)}\t{round(e2[i],5)}\t{round(y3_list[i],4)}\t{round(e3[i],5)}")
plt.plot(x_list, y_list)
plt.plot(x_list, y2_list)
plt.plot(x_list, y3_list)
plt.legend(["y_real","y_RK4", "y_adams"])
plt.show()
plt.clf()
plt.plot(x_list, e2)
plt.plot(x_list, e3)
plt.legend(["e_RK4","e_adams"])
plt.show()
plt.clf()
h = []
errRK = []
erradams = []
x_end = x0 + 1
for i in range(1,5000):    
    h.append(i * 0.0001)
    amount = int((x_end - x0)/h[i-1])+1
    y_list = [f(x0+h[i-1]*j) for j in range(amount)]
    y2_list = RK4(df,y0,h[i-1],x0,x_end)
    y3_list = adams4(df,x_list[:4],y2_list[:4],h[i-1],x_end)
    e2 = [abs(y2_list[j]-y_list[j]) for j in range(amount)]
    e3 = [abs(y3_list[j]-y_list[j]) for j in range(amount)] 
    errRK.append(max(e2))
    erradams.append(max(e3))
plt.plot(h, errRK)
plt.plot(h, erradams)
plt.legend(["RK4","adams"])
plt.yscale('log')
plt.show()